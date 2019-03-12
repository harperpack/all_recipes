#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 01:22:43 2019

@author: harper
"""

import spacy
from spacy.lang.en import English
import en_core_web_sm

from bs4 import BeautifulSoup
import requests

from ingredients import ingred, convert_to_float, new_ingredient

nlp = en_core_web_sm.load()

class Direction:
    def __init__(self):
        self.text = ''
        self.device = ''
        self.actions = []
        self.duration = ()
        self.time_unit = ''
        self.ingredients = []

def load_directions(soup):
#    resp = requests.get(url_string)
#    soup = BeautifulSoup(resp.text, "lxml")
    results = soup.find_all('span', class_='recipe-directions__list--item')
    r_list = []
    for i in results:
        if len(i.contents) > 0:
            for f in range(len(i.contents)):
                if i.contents[f]:
                    steps = i.contents[f].split(". ")
                    for step in steps:
                        if "." in step:
                            step = step.rstrip()
                        else:
                            step += "."
                        r_list.append(step)
    return r_list

# NEED TO MAKE USE OF INGREDIENT LIST TO BETTER CAPTURE INGREDIENTS IN DIRECTIONS

def make_direction(step, names):
    cook_verbs = ['preheat', 'cook', 'broil', 'roast', 'drain', 'bake',
                  'rinse', 'melt', 'stir', 'mix', 'bake', 'simmer', 'season',
                  'sauté', 'poach', 'whisk', 'stew', 'grill']
    measure_words = ['cup','teaspoon','tablespoon','ounce','pound','clove', 'stalk', 'pinch']
    time_words = ['second', 'minute', 'hour', 'seconds', 'minutes', 'hours']
    cook_nouns = ['oven', 'saucepan', 'pot', 'dish', 'cooker', 'bowl', 'pan',
                  'stove', 'cups']
    cn_qualifiers = ['baking', 'mixing', 'slow']
    agglomerations = ['mixture', 'sauce', 'contents', 'marinade', 'mix', 'bowl']
    direction = Direction()
    direction.text = step
    doc = nlp(direction.text)
    # tokenize each instructions step
    tokens = list(doc)
    for token in tokens:
        j = tokens.index(token)
        if tokens[j].is_punct:
            continue
        # if the token is a cooking action, store it as such
        if tokens[j].text.lower() in cook_verbs:
            direction.actions.append(tokens[j].text)
        elif tokens[j].tag_ == 'VB' and tokens[j].lemma_ == 'heat':
            direction.actions.append(tokens[j].text)
        elif tokens[j].lemma_ == 'boil' or tokens[j].lemma_ == 'boiling':
            direction.actions.append(tokens[j].text)
        # numbers may pertain to time or quantities, both of which we want
        elif j < len(tokens) and tokens[j].tag_ == 'CD' or tokens[j].tag_ == 'LS':
            # often we see "X to Y time_units"
            if tokens[j+1].text == 'to':
                direction.time_unit = tokens[j+3].lemma_
                direction.duration = (int(tokens[j].text),int(tokens[j+2].text))
#                dur = tokens[j].text + ' to ' + tokens[j+2].text
#                direction.duration = dur
                del tokens[j:j+4]
            # may also see "X time_units"
            elif tokens[j+1].lemma_ in time_words:
                direction.time_unit = tokens[j+1].lemma_
                direction.duration = (int(tokens[j].text), int(tokens[j].text))
                del tokens[j:j+2]
            # may also refer to ingredient quantities - e.g., 'X units of...'
            elif tokens[j+1].lemma_ in measure_words:
                # if j is followed by measure, it's likely a quantity
                quantity = convert_to_float(tokens[j].text)
                unit = tokens[j+1].lemma_
                # check if form of 'X units ingredient'
                if tokens[j+2].tag_ == 'NN' or tokens[j+2].tag_ == 'NNP':
                    # check if ingredient has multi-part name (e.g., Parm cheese)
                    if j+3 < len(tokens) and tokens[j+3].tag_ == 'NN':
                        name = tokens[j+2].text + ' ' + tokens[j+3].text
                        item = new_ingredient(name, quantity, unit)
                        del tokens[j:j+4]
                    else:
                        name = tokens[j+2].text
                        item = new_ingredient(name, quantity, unit)
                        del tokens[j:j+3]
                # check if form of 'X units OF ingredient'
                elif tokens[j+2].tag_ == 'IN' and tokens[j+3].tag_ == 'NN' or tokens[j+3].tag_ == 'NNP':
                    # check if ingredient has multi-part name (e.g., Parm cheese)
                    if j+4 < len(tokens) and tokens[j+4].tag_ == 'NN':
                        name = tokens[j+3].text + ' ' + tokens[j+4].text
                        item = new_ingredient(name, quantity, unit)
                        del tokens[j:j+5]
                    else:
                        name = tokens[j+3].text
                        item = new_ingredient(name, quantity, unit)
                        del tokens[j:j+4]
                    direction.ingredients.append(item)
            elif tokens[j+1].text == 'of':
                jth = 0
                quantity = convert_to_float(tokens[j].text)
                if tokens[j+2].text == 'the':
                    if tokens[j+3].lemma_ in agglomerations:
                        if tokens[j+4].lemma_ in agglomerations:
                            name = tokens[j+3].text + ' ' + tokens[j+4].text
                            jth = 5
                        else:
                            name = tokens[j+3].text
                            jth = 4
                        item = new_ingredient(name, quantity, 'ratio')
                        item.type = 'combination'
                        del tokens[j:j+jth]
                    elif tokens[j+4].lemma_ in agglomerations:
                        if tokens[j+5].lemma_ in agglomerations:
                            name = tokens[j+4].text + ' ' + tokens[j+5].text
                            jth = 6
                        else:
                            name = tokens[j+4].text
                            jth = 5
                        item = new_ingredient(name, quantity, 'ratio')
                        item.type = 'combination'
                        del tokens[j:j+jth]
                    elif any(name in tokens[j+3].lemma_ for name in names):
                        if any(name in tokens[j+4].lemma_ for name in names):
                            name = tokens[j+3].text + ' ' + tokens[j+4].text
                            jth = 5
                        else:
                            name = tokens[j+3].text
                            jth = 4
                        item = new_ingredient(name, quantity, 'ratio')
                        del tokens[j:j+jth]
            elif tokens[j+1].tag_ == 'CD' or tokens[j+1].tag_ == 'LS':
                combined = convert_to_float(tokens[j].text)
                combined += convert_to_float(tokens[j+1].text)
                if tokens[j+2].lemma_ in time_words:
                    direction.duration = (int(combined), int(combined))
                    direction.time_unit = tokens[j+2].text
                    del tokens[j:j+3]
        # check if token is a cooking implement
        elif tokens[j].text in cook_nouns:
            # check if it has a multi-part name (e.g., 'slow cooker')
            if j > 0 and tokens[j-1].text in cn_qualifiers:
                name = tokens[j-1].text + ' ' + tokens[j].text
                direction.device = name
            else:
                direction.device = tokens[j].text
        elif tokens[j].text == 'until':
            if not direction.duration:
                check = [x.text for x in tokens[j+1:]]
                if not any(word in time_words for word in check):
                    until_dur = tokens[j].text
                    for word in tokens[j+1:]:
                        if word.is_punct:
                            break
                        until_dur += ' ' + word.text
                    direction.duration = until_dur
                    direction.time_unit = 'subjective'
    return direction

#load_directions('https://www.allrecipes.com/recipe/8758/white-cheese-chicken-lasagna/')