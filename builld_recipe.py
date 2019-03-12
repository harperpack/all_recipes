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

common_words = ['the', 'of', 'and', 'for', 'by', 'or', 'that', 'but', 'then',
                'than', 'to', 'them', 'it', 'into', ',', '.', '-', "'", '"', 
                ')', '(', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'all',
                'stew', 'cubes', 'cube', 'roast', 'bouillon', 'can', 'bottle',
                'in', 'our', 'your']

class Recipe():
    def __init__(self):
        self.title = ''
        self.servings = 0
        self.ingredients = []
        self.replaced = []
        self.primary = ''
        self.meal = ''
        self.directions = []
        self.transformations = []
    
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
        print("Swap happenned!")
    
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
            print("Check happened")
        else:
            self.swap(old, sub)
    
    def add_directions(self, name):
        new = new_ingredient(name)
        new = create_metadata(new, self.servings)
    
    def replace_directions(self):
        if self.replaced:
            #names = [ingredient.name for ingredient in self.replaced]
            for direction in self.directions:
                for ingredient in self.replaced:
                    for word in ingredient.specified:
                        if word in direction.text and word not in common_words:
                            direction.text = direction.text.replace(word, ingredient.new.name)
#                    if ' ' in ingredient.name:
#                        pieces = ingredient.name.split(' ')
#                        for piece in pieces:
#                            if piece not in common_words:
##                                print(piece)
##                                print(direction.text)
#                                if piece in direction.text:
#                                    direction.text = direction.text.replace(piece, ingredient.new.name)
#                    elif ingredient.name in direction.text:
#                        direction.text = direction.text.replace(ingredient.name, ingredient.new.name)

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

#url = 'https://www.allrecipes.com/recipe/8130/sour-cream-coffee-cake-iii/'
#
#url2 = 'https://www.allrecipes.com/recipe/8758/white-cheese-chicken-lasagna/'
#
#print(get_title(load_recipe(url2)))
#print(get_servings(load_recipe(url2)))
#dir_list = load_directions(load_recipe(url2))
#for direction in dir_list:
#    step = make_direction(direction)
#    print(step.text)

# NEED TO FIGURE OUT HOW TO GET PRIMARY AND MEAL
def make_recipe(url):
    # instantiate the recipe object
    recipe = Recipe()
    # load the html from All Recipes
    html = load_recipe(url)
    # obtain recipe title
    recipe.title = get_title(html)
#    print(recipe.title)
    # obtain recipe serving size
    recipe.servings = get_servings(html)
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
            recipe.ingredients.append(ingredient)
    # load directions
    directions = load_directions(html)
    # build list of ingredient names to aid in parsing directions
    names = [ingredient.name for ingredient in recipe.ingredients]
    for step in directions:
        # instantiate each direction as direction object
        direction = make_direction(step, names)
        if direction:
            # add direction to recipe
            recipe.directions.append(direction)
    return recipe

def print_recipe(recipe):
    if recipe.transformations:
        title = recipe.transformations[0]
        max_index = len(recipe.transformations) - 1
        if max_index > 0:
            for i in range(1, len(recipe.transformations)):
                title += ', ' + recipe.transformations[i]
        title += ' ' + recipe.title
        print(title)
    else:
        print(recipe.title)
    print("Serves " + str(recipe.servings))
    print('------------------------------------')
    print("INGREDIENTS:")
#    print_ingredients(recipe.ingredients)
    for ingredient in recipe.ingredients:
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
                    output += ' and'
        print(output)
        output = ''
    print("\n")
    print("DIRECTIONS:")
    step_no = 1
    for direction in recipe.directions:
        print("   " + str(step_no) + "] " + direction.text)
        step_no += 1

def print_ingredients(ingredients):
    for ingredient in ingredients:
        print('Name:' + ingredient.name)
        print('Quantity:' + str(ingredient.quantity))
        print('Unit: ' + ingredient.unit)
        print('Descriptors: ' + str(ingredient.descriptors))
        print('Preprocessing: ' + str(ingredient.preprocessing))
        print('Flags: ' + str(ingredient.flags))
        print('Type: ' + str(ingredient.type))

def create_metadata(ingredient, servings):
    pass

def count_cook_verbs(recipe):
   cook_verbs = ['preheat', 'cook', 'broil', 'roast', 'drain', 'bake',
                 'rinse', 'melt', 'stir', 'mix', 'bake', 'simmer', 'season',
                 'sauté', 'poach', 'whisk', 'stew']
   #dictionary of tuples that are the value and want to choose the higher int tuple
   verb_count = {}
   #want to find the a match in title and cook verbs
   if any(verb in recipe.title.lower() for verb in cook_verbs):
       for verb in cook_verbs:
           if verb in recipe.title.lower():
               return verb
   else:
       for direction in recipe.directions:
           time = direction.duration
           if direction.actions and direction.duration and direction.time_unit != 'subjective':
               for action in direction.actions:
                   if action not in verb_count.keys():
                       verb_count[action] = time
                   else:
                       verb_count[action] += time

                   collections.Counter(verb_count)
   print(max(collections.Counter(verb_count), key=collections.Counter(verb_count).get))