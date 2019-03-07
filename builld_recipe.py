#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 00:39:52 2019

@author: harper
"""

from ingredients import load_ingredients, make_ingredient
from directions import load_directions, make_direction

from bs4 import BeautifulSoup
import requests
import spacy

class Recipe():
    def __init__(self):
        self.title = ''
        self.servings = 0
        self.ingredients = []
        self.primary = ''
        self.meal = ''
        self.directions = []

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
    for step in directions:
        # instantiate each direction as direction object
        direction = make_direction(step)
        if direction:
            # add direction to recipe
            recipe.directions.append(direction)
    return recipe