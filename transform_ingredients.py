#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 09:14:49 2019

@author: harper
"""

def transform_vegetarian(recipe):
    for ingredient in recipe.ingredients:
        if 'non-veg' in ingredient.flags:
            recipe, ingredient = transform_ingredient_vegetarian(recipe, ingredient)
    return recipe

def transform_ingredient_vegetarian(ingredient, recipe):
    if ingredient.type == 'red meat':
        if recipe.meal == 'roast' or recipe.meal == 'stew':
            # ADD FUNCTION?
            recipe.replace_ingredient(ingredient, 'portobello mushroom')
            # ADD FUNCTION?
            recipe.add_ingredient('black beans')
        else:
            # ADD FUNCTION?
            recipe.replace_ingredient(ingredient, 'seitan')
            # ADD FUNCTION?
            recipe.add_ingredient('tamari sauce')
    elif ingredient.type == 'pork':
        if recipe.meal == 'stew':
            # ADD FUNCTION?
            recipe.replace_ingredient(ingredient, 'jackfruit')
        else:
            # ADD FUNCTION?
            recipe.replace_ingredient(ingredient, 'seitan')
            # ADD FUNCTION?
            recipe.add_ingredient(ingredient, 'TBD SPICE')
    elif ingredient.type == 'ham':
        if recipe.meal == 'roast':
            ingredient.name = ingredient.name.replace('ham', 'Tofurky ham roast')
        else:
            # ADD FUNCTION?
            recipe.replace_ingredient(ingredient, 'seitan')
            # ADD FUNCTION?
            recipe.add_ingredient('salt')
    elif ingredient.type == 'bacon':
        ingredient.name = ingredient.name.replace('bacon', 'vegetarian bacon')
    elif ingredient.type == 'processed meat':
        # ADD FUNCTION?
        recipe.replace_ingredient(ingredient, 'seitan')
        # ADD FUNCTION?
        recipe.add_ingredient('salt')
    elif ingredient.type == 'poultry':
        if recipe.meal == 'roast':
            # ADD FUNCTION?
            recipe.replace_ingredient(ingredient, 'eggplant')
        else:
            # ADD FUNCTION?
            recipe.replace_ingredient(ingredient, 'jackfruit')
            # ADD FUNCTION?
            recipe.add_ingredient('brown lentils')
    elif ingredient.type == 'sausage':
        # ADD FUNCTION?
        recipe.replace_ingredient(ingredient, 'vegetarian sausage')
    elif ingredient.type == 'shellfish':
        # ADD FUNCTION?
        recipe.replace_ingredient(ingredient, 'shiitake mushrooms')
    elif ingredient.type == 'broth':
        if 'chicken' in ingredient.name:
            ingredient.name = ingredient.name.replace('chicken', 'vegetable')
        elif 'beef' in ingredient.name:
            ingredient.name = ingredient.name.replace('beef', 'vegetable')
    else:
        # ADD FUNCTION?
        recipe.replace_ingredient(ingredient, 'extra-firm tofu')
    return recipe, ingredient

def transform_mexican(recipe):
    