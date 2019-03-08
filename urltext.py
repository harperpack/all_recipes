#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 12:26:52 2019

@author: harper
"""

import json
import spacy
from collections import Counter
from spacy.lang.en import English
import en_core_web_sm

from bs4 import BeautifulSoup
import requests
import re

nlp = en_core_web_sm.load()

from bs4 import BeautifulSoup
import requests

vowels = ['a', 'e', 'i', 'o', 'u']

measure_words = ['cup','teaspoon','tablespoon','ounce','pound','clove', 'stalk', 'pinch']

cook_verbs = ['preheat', 'cook', 'broil', 'roast', 'drain', 'bake',
              'rinse', 'melt', 'stir', 'mix', 'bake', 'simmer', 'season',
              'sauté', 'poach', 'whisk']

time_words = ['second', 'minute', 'hour', 'seconds', 'minutes', 'hours']

cook_nouns = ['oven', 'saucepan', 'pot', 'dish', 'cooker', 'bowl', 'pan',
              'stove', 'cups']

cn_qualifiers = ['baking', 'mixing', 'slow']

class ingred:
    def __init__(self):
        self.quantity = 0
        self.name = ''
        self.unit = ''
        self.preparation = []
        self.descriptor = []

class Direction:
    def __init__(self):
        self.text = ''
        self.device = ''
        self.actions = []
        self.duration = ''
        self.time_unit = ''
        self.ingredients = []
        
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

resp = requests.get('https://www.allrecipes.com/recipe/8758/white-cheese-chicken-lasagna/')

soup = BeautifulSoup(resp.text, "lxml")

results = soup.find_all('span', class_='recipe-directions__list--item')
r_list = []
directions = []
for i in results:
    if len(i.contents) > 0:
        for f in range(len(i.contents)):
            steps = i.contents[f].split(". ")
            for step in steps:
                newstep = Direction()
                if "." in step:
                    newstep.text = step.rstrip()
                else:
                    newstep.text = step + "."
                directions.append(newstep)

#for i in range(len(directions)):
#    if i == 3:
#        print(len(directions[i].text))
#        for char in directions[i].text:
#            print(char)
#    print(directions[i].text)

for i in range(len(directions)):
    doc = nlp(directions[i].text)
    # tokenize each instructions step
    tokens = list(doc)
#    print(tokens)
#    delPrev = False
    for token in tokens:
#        if delPrev:
##            print("Deleting: " + tokens[j].text)
#            del tokens[j]
#            delPrev = False
#        print(token)
        j = tokens.index(token)
        if tokens[j].is_punct:
#            delPrev = True
            continue
        # if the token is a cooking action, store it as such
        if tokens[j].text.lower() in cook_verbs:
            directions[i].actions.append(tokens[j].text)
        elif tokens[j].tag_ == 'VB' and tokens[j].lemma_ == 'heat':
            directions[i].actions.append(tokens[j].text)
        elif tokens[j].lemma_ == 'boil' or tokens[j].lemma_ == 'boiling':
            directions[i].actions.append(tokens[j].text)
            # so categorized, we have no further use for this token
#            del tokens[j]
        # numbers may pertain to time or quantities, both of which we want
        elif j < len(tokens) and tokens[j].tag_ == 'CD' or tokens[j].tag_ == 'LS':
            # often we see "X to Y time_units"
            if tokens[j+1].text == 'to':
                directions[i].time_unit = tokens[j+3].lemma_
                dur = tokens[j].text + ' to ' + tokens[j+2].text
                directions[i].duration = dur
                del tokens[j:j+4]
            # may also see "X time_units"
            elif tokens[j+1].lemma_ in time_words:
                directions[i].time_unit = tokens[j+1].lemma_
                directions[i].duration = tokens[j].text
                del tokens[j:j+2]
            # may also refer to ingredient quantities - e.g., 'X units of...'
            elif tokens[j+1].lemma_ in measure_words:
                item = ingred()
                # if j is followed by measure, it's likely a quantity
                item.quantity = convert_to_float(tokens[j].text)
                item.unit = tokens[j+1].lemma_
                # check if form of 'X units ingredient'
                if tokens[j+2].tag_ == 'NN' or tokens[j+2].tag_ == 'NNP':
                    # check if ingredient has multi-part name (e.g., Parm cheese)
                    if j+3 < len(tokens) and tokens[j+3].tag_ == 'NN':
                        name = tokens[j+2].text + ' ' + tokens[j+3].text
                        item.name = name
                        del tokens[j:j+4]
                    else:
                        item.name = tokens[j+2].text
                        del tokens[j:j+3]
                # check if form of 'X units OF ingredient'
                elif tokens[j+2].tag_ == 'IN' and tokens[j+3].tag_ == 'NN' or tokens[j+3].tag_ == 'NNP':
                    # check if ingredient has multi-part name (e.g., Parm cheese)
                    if j+4 < len(tokens) and tokens[j+4].tag_ == 'NN':
                        name = tokens[j+3].text + ' ' + tokens[j+4].text
                        item.name = name
                        del tokens[j:j+5]
                    else:
                        item.name = tokens[j+3].text
                        del tokens[j:j+4]
                directions[i].ingredients.append(item)
        # check if token is a cooking implement
        elif tokens[j].text in cook_nouns:
            # check if it has a multi-part name (e.g., 'slow cooker')
            if j > 0 and tokens[j-1].text in cn_qualifiers:
                name = tokens[j-1].text + ' ' + tokens[j].text
                directions[i].device = name
#                del tokens[j-1:j+1]
            else:
                directions[i].device = tokens[j].text
#                del tokens[j]
        elif tokens[j].text == 'until':
            if not directions[i].duration:
                check = [x.text for x in tokens[j+1:]]
                if not any(word in time_words for word in check):
                    until_dur = tokens[j].text
                    for word in tokens[j+1:]:
                        if word.is_punct:
                            break
                        until_dur += ' ' + word.text
                    directions[i].duration = until_dur
                    directions[i].time_unit = 'subjective'
#    break

for direction in directions:
    print("Here is the direction:")
    print(direction.text)
    if direction.device:
        print("Here is the device used:")
        print(direction.device)
    if direction.actions:
        print("Here are the actions taken:")
        print(direction.actions)
    if direction.duration:
        print("Here is the duration of actions:")
        print(direction.duration)
    if direction.time_unit:
        print("Here is the unit of duration:")
        print(direction.time_unit)
#    if direction.ingredients:
#        print("Here are the ingredients:")
#        for ingredient in direction.ingredients:
#            print('Name: '+ ingredient.name)
#            print('Quantity: ' + str(ingredient.quantity))
#            print('Unit: ' + ingredient.unit)