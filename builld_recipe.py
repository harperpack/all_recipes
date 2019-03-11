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

class Recipe():
    def __init__(self):
        self.title = ''
        self.servings = 0
        self.ingredients = []
        self.replaced = []
        self.primary = ''
        self.meal = ''
        self.directions = []
    
    def check_duplicates(self, potential_duplicate):
        for ingredient in self.ingredients:
            if ingredient.name == potential_duplicate.name:
                return ingredient
        return None
    
    def swap(self, old, new):
        indx = self.ingredients.index(old)
        self.ingredients[indx] = new
        self.replaced.append(old)
    
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
        check = self.check_duplicates(sub)
        if check:
            # NEED TO MAKE FUNCTION
            check.more(sub.quantity, sub.unit)
        else:
            self.swap(old, sub)
    
    def update_directions(self):
        if self.replaced:
            #names = [ingredient.name for ingredient in self.replaced]
            for direction in self.directions:
                if direction.ingredients:
                    for ingredient in self.replaced:
                        if ingredient.name in direction.text:
                            direction.text.replace(ingredient.name, ingredient.new.name)
    

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
    # obtain recipe serving size
    recipe.servings = get_servings(html)
    # load ingrediets
    ingredients = load_ingredients(html)
    for item in ingredients:
        # instatiate each ingredient as ingredient object
        ingredient = make_ingredient(item)
        if ingredient:
            # NEED TO DEFINE CATEGORIZE INGREDIENT
            ingredient = categorize_ingredient(ingredient)
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
    print("Here is the transformed recipe!\n\n")
    print(recipe.title)
    print("Serves " + str(recipe.servings))
    print('------------------------------------')
    print("INGREDIENTS:")
    for ingredient in recipe.ingredients:
        if ingredient.unit != 'discrete':
            output = "   " + str(ingredient.quantity) + ' ' + ingredient.unit + ' of'
        else:
            output = "   " + str(ingredient.quantity)
        if ingredient.descriptors:
            max_index = len(ingredient.descriptors) - 1
            for descriptor in ingredient.descriptors:
                i = ingredient.descriptors.index(descriptor)
                output += ' ' + descriptor
                if i < max_index:
                    output += ','
        output += ' ' + ingredient.name
        if ingredient.preprocessing:
            output += ','
            max_index = len(ingredient.preprocessing)
            for step in ingredient.preprocessing:
                i = ingredient.preprocessing.index(step)
                output += ' ' + step
                if i < max_index:
                    output += 'and'
        print(output)
    print("\n\n")
    print("DIRECTIONS:")
    step_no = 1
    for direction in recipe.directions:
        print("   " + str(step_no) + "] " + direction.text)