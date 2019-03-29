#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 12:28:55 2019

@author: harper
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 00:48:41 2019

@author: harper
"""

from bs4 import BeautifulSoup
import requests
import spacy

url_test = 'https://www.allrecipes.com/recipe/8149/flourless-chocolate-cake-i/'

measure_words = ['cup','teaspoon','tablespoon','ounce','pound','clove', 'stalk', 'pinch']
descriptor_words = ['whole', 'ground', 'fresh']
prep_words = ['thaw', 'grate']
numerals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

class ingred:
    def __init__(self):
        self.quantity = 0
        self.name = ''
        self.unit = ''
        self.preparation = []
        self.descriptor = []

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

resp = requests.get(url_test)

soup = BeautifulSoup(resp.text, "lxml")

results = soup.find_all('span', class_='recipe-ingred_txt')
r_list = []
for i in results:
    if len(i.contents) > 0:
        if i.contents[0] != 'Add all ingredients to list':
            r_list.append(str(i.contents[0]))

all_info = []

nlp = spacy.load('en_core_web_sm')
for i in r_list:
    info_struct = ingred()
    doc = nlp(i)
    tokens = list(doc)
    #print(tokens)
    if len(tokens) < 2:
        continue
    if tokens[0].tag_ == 'CD' or tokens[0].tag_ == 'LS':
        if tokens[1].tag_ == 'CD' or tokens[1].tag_ == 'LS':
            q1 = convert_to_float(str(tokens[0]))
            q2 = convert_to_float(str(tokens[1]))
            info_struct.quantity = q1 + q2
            #print('Deleting: ' + tokens[0].text + ' ' + tokens[1].text)
            del tokens[0:2]
        else:
            info_struct.quantity = convert_to_float(str(tokens[0]))
            #print('Deleting: ' + tokens[0].text)
            del tokens[0:1]
        if tokens[0].lemma_ in measure_words:
            info_struct.unit = tokens[0].lemma_
            #print('Deleting: ' + tokens[0].text)
            del tokens[0:1]
        else:
            info_struct.unit = 'discrete'
        to_remove = []
        for j in range(0, len(tokens)):
            if tokens[j].tag_ == 'VBN':
                to_remove.append(j)
                if str(tokens[j]) in descriptor_words:
                    info_struct.descriptor.append(str(tokens[j]))
                else:
                    info_struct.preparation.append(str(tokens[j]))
            elif tokens[j].pos_ == 'PUNCT':
                to_remove.append(j)
        for j in sorted(to_remove, reverse=True):
            del tokens[j]
        newdoc = nlp("".join(str(j)+' ' for j in tokens))
        chunk_list = list(newdoc.noun_chunks)
        chunk = 0
        indx = 0
        if len(chunk_list) > 0:
            print((chunk_list[0][0].text))
            if chunk_list[0][0].text in descriptor_words:
                info_struct.descriptor.append(chunk_list[0][0].text)
                indx = 1
            elif chunk_list[0][0].text in prep_words:
                info_struct.preparation.append(chunk_list[0][0].text)
                indx = 1
            elif any(char in numerals for char in chunk_list[0][0].text):
                info_struct.unit = str(chunk_list[0])
                chunk = 1
            info_struct.name = str(chunk_list[chunk][indx:])
    all_info.append(info_struct)
    #for chunk in doc.noun_chunks:
    #    print(chunk.text, chunk.root.text, chunk.root.dep_, chunk.root.head.text)
for i in all_info:
    print('Name: '+ i.name)
    print('Quantity: ' + str(i.quantity))
    print('Unit: ' + i.unit)
    if len(i.preparation) > 0:
        print('List of preparation steps: ')
        for j in i.preparation:
            print('    ' + j)
    print(' ')