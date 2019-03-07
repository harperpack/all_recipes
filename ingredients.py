#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 00:48:41 2019

@author: harper
"""
#url_test = 'https://www.allrecipes.com/recipe/257306/easy-skinless-fried-chicken-thighs/'
#url_test = 'https://www.allrecipes.com/recipe/162894/black-pepper-goat-curry/'
#url_test = 'https://www.allrecipes.com/recipe/234621/rusty-chicken-thighs/
#url_test = 'https://www.allrecipes.com/recipe/140897/mimis-smoked-salmon-chowder/'

from bs4 import BeautifulSoup
import requests
import spacy

#url_test = 'https://www.allrecipes.com/recipe/8130/sour-cream-coffee-cake-iii/'
#url_test = 'https://www.allrecipes.com/recipe/8149/flourless-chocolate-cake-i/'

url_test = 'https://www.allrecipes.com/recipe/234621/rusty-chicken-thighs/'

class ingred:
    def __init__(self):
        self.quantity = 0
        self.name = ''
        self.unit = ''
        self.preprocessing = []
        self.descriptors = []
        self.alternative = ''
        self.type = ''
        self.method = []

def convert_to_float(frac_str):
    try:
        return float(frac_str)
    except ValueError:
        try:
            num, denom = frac_str.split('/')
        except ValueError:
            return None
        try:
            leading, num = num.split(' ')
        except ValueError:
            return float(num) / float(denom)        
        if float(leading) < 0:
            sign_mult = -1
        else:
            sign_mult = 1
        return float(leading) + sign_mult * (float(num) / float(denom))

def is_bad(tok):
    if tok.pos_ in ['ADJ','PUNCT'] or tok.tag_ in ['CC','VBN']:
        return True
    for i in tok.ancestors:
        if is_bad(i):
            return True
    return False

def load_ingredients(soup):
#    resp = requests.get(url_string)
#    soup = BeautifulSoup(resp.text, "lxml")
    results = soup.find_all('span', class_='recipe-ingred_txt')
    r_list = []
    for i in results:
        if len(i.contents) > 0:
            if i.contents[0] != 'Add all ingredients to list':
                r_list.append(str(i.contents[0]))
    return r_list

def make_ingredient(i):
    measure_words = ['cup','teaspoon','tablespoon','ounce','pound','clove', 'stalk']
    adj_exclude = ['sour','garlic']
    avoid_list = []
    nlp = spacy.load('en_core_web_sm')
    info_struct = ingred()
    doc = nlp(i)
    tokens = list(doc)
    if len(tokens) < 2:
        return None
    if tokens[0].text.lower() == 'a':
        del tokens[0:1]
    if tokens[0].tag_ == 'CD' or tokens[0].tag_ == 'LS':
        if tokens[1].tag_ == 'CD' or tokens[1].tag_ == 'LS':
            q1 = convert_to_float(str(tokens[0]))
            q2 = convert_to_float(str(tokens[1]))
            info_struct.quantity = q1 + q2
            del tokens[0:2]
        else:
            info_struct.quantity = convert_to_float(str(tokens[0]))
            del tokens[0:1]
        if tokens[0].lemma_ in measure_words:
            info_struct.unit = tokens[0].lemma_
            del tokens[0:1]
        else:
            info_struct.unit = 'discrete'
        if tokens[0].text == '(':
            end_paren_ix = 1
            while tokens[end_paren_ix].text != ')':
                end_paren_ix += 1
            info_struct.unit = "".join(j.text+' ' for j in tokens[0:end_paren_ix+2] if j.pos_ != 'PUNCT').strip()
            del tokens[0:end_paren_ix+2]
    #deal with the 'or' case
    for j in range(0,len(tokens)-1):
        if tokens[j].text == 'or':
            info_struct.alternative = ''.join(k.text+' ' for k in tokens[j+1:]).strip()
            del tokens[j:]
            break
    newdoc = nlp("".join(j.text_with_ws for j in tokens))
    chunk_list = list(newdoc.noun_chunks)
    if len(chunk_list) > 0:
        for j in chunk_list[0].root.children:
            if j.tag_ == 'VBN':
                info_struct.preprocessing.append(''.join(w.text_with_ws for w in j.subtree if w.pos_ not in ['NOUN','PUNCT']))
                for k in j.subtree:
                    if k.pos_!='NOUN':
                        avoid_list.append(k.text)
            elif j.pos_ == 'ADJ':
                if j.text not in adj_exclude:
                    info_struct.descriptors.append(''.join(w.text_with_ws for w in j.subtree if w.pos_ not in ['PUNCT']))
                    for k in j.subtree:
                        avoid_list.append(k.text)
        info_struct.name = ''.join(w.text + ' ' for w in chunk_list[0].root.subtree if w.text not in avoid_list and w.pos_ != 'PUNCT').strip()
    else:
        for j in newdoc:
            if j.tag_ == 'VBN':
                info_struct.preprocessing.append(''.join(w.text_with_ws for w in j.subtree if w.pos_ not in ['NOUN','PUNCT']))
                for k in j.subtree:
                    if k.pos_!='NOUN':
                        avoid_list.append(k.text)
        info_struct.name = ''.join(w.text + ' ' for w in newdoc if w.text not in avoid_list and w.pos_ != 'PUNCT')
    return info_struct

#tests = load_ingredients(url_test)
#ingredients = []
#for test in tests:
#    result = make_ingredient(test)
#    if result:
#        ingredients.append(result)
#        print(result.name)