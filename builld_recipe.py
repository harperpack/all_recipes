#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 00:39:52 2019

@author: harper
"""

from ingredients import load_ingredients, make_ingredient, new_ingredient, rationalize_details
from directions import load_directions, make_direction
from categorize import categorize_ingredient

from bs4 import BeautifulSoup
import requests
import spacy
import collections
from spacy.lang.en import English
import en_core_web_sm

common_words = ['the', 'of', 'and', 'for', 'by', 'or', 'that', 'but', 'then',
                'than', 'to', 'them', 'it', 'into', ',', '.', '-', "'", '"',
                ')', '(', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'all',
                'stew', 'cubes', 'cube', 'roast', 'bouillon', 'can', 'bottle',
                'in', 'our', 'your']

class Recipe():
    def __init__(self, url):
        self.title = ''
        self.servings = 0
        self.ingredients = []
        self.replaced = []
        self.primary = ''
        self.meal = ''
        self.directions = []
        self.transformations = []

        if url != '':
            # load the html from All Recipes
            html = load_recipe(url)
            # obtain recipe title
            self.title = get_title(html)
            # obtain recipe serving size
            self.servings = get_servings(html)
        #    print(recipe.servings)
            # load ingrediets
            ingredients = load_ingredients(html)
            for item in ingredients:
                # instatiate each ingredient as ingredient object
                ingredient = make_ingredient(item)
                if ingredient:
        #            print(ingredient.name)
                    # NEED TO DEFINE CATEGORIZE INGREDIENT
                    ingredient = categorize_ingredient(ingredient)
        #            print(ingredient.type)
                    # add ingredient to recipe
                    self.ingredients.append(ingredient)
            # load directions
            directions = load_directions(html)
            # build list of ingredient names to aid in parsing directions
            names = [ingredient.name for ingredient in self.ingredients]
            for step in directions:
                # instantiate each direction as direction object
                direction = make_direction(step, names)
                if direction:
                    # add direction to self
                    self.directions.append(direction)
            self.make_main_cook()
            self.make_tool_list()



    def print_recipe(self):
        if self.transformations:
            title = self.transformations[0]
            max_index = len(self.transformations) - 1
            if max_index > 0:
                for i in range(1, len(self.transformations)):
                    title += ', ' + self.transformations[i]
            title += ' ' + self.title
            print(title)
        else:
            print(self.title)
        print("Serves " + str(self.servings))
        print('------------------------------------')
        print("INGREDIENTS:")
    #    print_ingredients(recipe.ingredients)
        for ingredient in self.ingredients:
            if ingredient.unit.strip() in ['cup','teaspoon','tablespoon','ounce','pound','clove', 'stalk', 'pinch']:
                output = "   " + str(ingredient.quantity).strip() + ' ' + ingredient.unit.strip()
            else:
                if ingredient.unit == 'discrete':
                    output = "   " + str(ingredient.quantity).strip()
                else:
                    output = "   " + str(ingredient.quantity).strip() + ' ' + ingredient.name.strip()
            if ingredient.descriptors:
                output += ' ' + ingredient.descriptors[0].strip()
                max_index = len(ingredient.descriptors) - 1
                if max_index > 0:
                    output += ','
                    for i in range(1, len(ingredient.descriptors)):
                        output += ' ' + ingredient.descriptors[i].strip()
                        if i < max_index:
                            output += ','
            if ingredient.name not in output:
                output += ' ' + ingredient.name.strip()
            if ingredient.preprocessing:
                output += ','
                max_index = len(ingredient.preprocessing) - 1
                for step in ingredient.preprocessing:
                    i = ingredient.preprocessing.index(step)
                    output += ' ' + step.strip()
                    if i < max_index:
                        output += 'and'
            print(output)
            output = ''
        print("\n")
        print("DIRECTIONS:")
        step_no = 1
        for direction in self.directions:
            print("   " + str(step_no) + "] " + direction.text)
            step_no += 1
        print('------------------------------------')
        print("And here is our representation, partly:")
        print("Primary cooking method: " + str(self.main_cook))
        self.print_ingredients()


    def print_ingredients(self):
        for ingredient in self.ingredients:
            print('Name:' + ingredient.name)
            print('Quantity:' + str(ingredient.quantity))
            print('Unit: ' + ingredient.unit)
            print('Descriptors: ' + str(ingredient.descriptors))
            print('Preprocessing: ' + str(ingredient.preprocessing))

    def check_duplicates(self, old, potential_duplicate):
        sure_dup = None
        for ingredient in self.ingredients:
            if ingredient.name == potential_duplicate.name:
                sure_dup = ingredient
        if sure_dup:
            for ingredient in self.replaced:
                if ingredient.name == old.name:
                    return None
            return sure_dup
        else:
            return None

    def swap(self, old, new):
        indx = self.ingredients.index(old)
        self.ingredients.pop(indx)
        self.ingredients.insert(indx, new)
        self.replaced.append(old)

    def identify_words_for_replacement(self, old, new):
        uniques = []
        if ' ' in old.name:
            old_words = old.name.split(' ')
        else:
            old_words = old.name
        if ' ' in new.name:
            new_words = new.name.split(' ')
        else:
            new_words = new.name
        if isinstance(old_words, list):
            for word in old_words:
                if word not in new_words:
                    uniques.append(word)
        else:
            if old_words not in new_words:
                uniques.append(old_words)
        old.specified = uniques
    
    def revert_to_old(self, devolve):
        # FOR UNDOING A TRANSFORMATION
        sub = new_ingredient(devolve.old.name, devolve.old.quantity, devolve.old.unit, devolve.old.preprocessing, devolve.old.descriptors)
        sub.type = devolve.old.type
        sub.old = devolve
        devolve.new = sub
        self.identify_words_for_replacement(devolve, sub)
        self.swap(devolve, sub)

    def replace_ingredient(self, old, new_name, old_name=None, deflag=None):
        # IF NOT OLD_NAME, IT'S A NEW INGREDIENT
        if not old_name:
            sub = new_ingredient(new_name, old.quantity, old.unit, old.preprocessing, old.descriptors)
            sub = categorize_ingredient(sub)
            sub.old = old
            old.new = sub
            sub = rationalize_details(sub, self.servings)
        # ASSUME THE INGREDIENT IN THIS CASE IS ALL BUT IDENTICAL - E.G., VEGETABLE BROTH FOR BEEF BROTH
        else:
            updated = old.name.replace(old_name, new_name)
            sub = new_ingredient(updated, old.quantity, old.unit, old.preprocessing, old.descriptors)
            sub.type = old.type
            sub.flags = [flag for flag in old.flags if flag not in deflag]
            sub.old = old
            old.new = sub
        self.identify_words_for_replacement(old, sub)
        check = self.check_duplicates(old, sub)
        if check:
            # NEED TO MAKE FUNCTION
            check.more(sub)
        else:
            self.swap(old, sub)

    def add_ingredient(self, name):
        new = new_ingredient(name)
        new = categorize_ingredient(new)
        self.set_quantity(new)
        self.ingredients.append(new)
        self.add_to_directions(new)
        #similars = self.find_similar(new)

    def set_quantity(self, ingredient):
        if 'seasoning' in ingredient.type:
            ingredient.quantity = float(int(self.servings) / 3)
            ingredient.unit = 'teaspoon'
        elif 'bean' in ingredient.name:
            ingredient.quantity = float(int(self.servings) / 4)
            ingredient.unit = '(15 ounce) cans'
            ingredient.preprocessing = ['drained', 'rinsed']
        elif 'lentil' in ingredient.name:
            ingredient.quantity = float(int(self.servings) / 4)
            ingredient.unit = 'cup'
            ingredient.descriptors = ['dry']
            ingredient.preprocessing = ['soaked overnight']
        elif 'avocado' in ingredient.name:
            ingredient.quantity = float(int(self.servings) / 2)
            ingredient.unit = 'discrete'
            ingredient.descriptors = ['fresh']
            ingredient.preprocessing = ['peeled', 'pitted', 'diced']
        elif 'spinach' in ingredient.name:
            ingredient.quantity = float(int(self.servings)) * 2
            ingredient.unit = 'ounce'
            ingredient.descriptors = ['fresh']
            ingredient.preprocessing = ['rinsed', 'dried', 'torn into bite-size pieces']
            ingredient.type = 'vegetable'
        elif ingredient.type == 'vegetable':
            ingredient.quantity = float(int(self.servings) / 4)
            ingredient.unit = 'cup'
            ingredient.descriptors = ['fresh']
            ingredient.preprocessing = ['washed', 'diced']

    def add_to_directions(self, ingredient):
        tag = ingredient.type
        names = [i.name for i in self.ingredients if i.type == tag]
        if not names:
            self.ingredients.remove(ingredient)
        for direction in self.directions:
            if any(name in direction.text for name in names):
                for name in names:
                    if name in direction.text:
                        direction.text = direction.text.replace(name, ingredient.name + ' and ' + name)
                        break

    def replace_directions(self):
        if self.replaced:
            #names = [ingredient.name for ingredient in self.replaced]
            for direction in self.directions:
                for ingredient in self.replaced:
                    for word in ingredient.specified:
                        if word in direction.text and word not in common_words:
                            direction.text = direction.text.replace(word, ingredient.new.name)

    def make_main_cook(self):
        cook_verbs = ['bake','shir','boil','fried','saut','grill','roast','baste','blanch','poach','scald','simmer','steam','stew','temper','caramelize']

        #want to find the a match in title and cook verbs
        for i in cook_verbs:
            if self.title.lower().find(i) != -1:
                return i

        maxDuration = 0
        cookAction = 'unknown'
        subj_time = .001
        for direction in self.directions:
            if direction.actions:
                if direction.duration:
                    newDuration = toMinute(direction.duration,direction.time_unit)
                else:
                    newDuration = subj_time
                    subj_time = subj_time + .001
                if newDuration > maxDuration:
                    for action in direction.actions:
                        if action.lower() in cook_verbs:
                            cookAction = action.lower()
                            maxDuration = newDuration
        self.main_cook = cookAction
        return

    def make_tool_list(self):
        tools = set()
        for direction in self.directions:
            if direction.device != '':
                tools.add(direction.device)
        self.tool_list = list(tools)
        return

def toMinute(q,u):
    if u.lower()[0:6]=='minute':
        return q[1]
    elif u.lower()[0:4]=='hour':
        return q[1] * 60
    elif u.lower()[0:6]=='second':
        return q[1] / 60
    return 0


def load_recipe(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "lxml")
    return soup

def get_title(soup):
    results = soup.find_all('title')
    for i in results:
        if len(i.contents) > 0:
            title = i.contents[0]
            title = title.split(" Recipe")
            return title[0]

def get_servings(soup):
    results = soup.find('meta', id="metaRecipeServings")
    servings = results.get("content", '')
    return servings
