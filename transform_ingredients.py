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

def transform_ingredient_vegetarian(recipe, ingredient):
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

def transform_healthy(recipe):
    fruits_or_vegetables = False
    for ingredient in recipe.ingredients:
        if 'unhealthy' in ingredient.flags:
            recipe, ingredient = transform_ingredient_healthy(recipe, ingredient)
            if ingredient.type == 'fruit' or ingredient.type == 'vegetable':
                fruits_or_vegetables = True
    if not fruits_or_vegetables:
        recipe.add_ingredient('spinach')
    return recipe

def transform_ingredient_healthy(recipe, ingredient):
    if ingredient.type in ['pork', 'bacon', 'sausage', 'ham', 'processed meat', 'poultry', 'red meat']:
        if ingredient.type == 'poultry':
            if 'thigh' in ingredient.name:
                ingredient.name = ingredient.name.replace('thigh', 'breast')
            elif 'wing' in ingredient.name:
                ingredient.name = ingredient.name.replace('wing', 'breast')
            elif 'dark' in ingredient.name:
                ingredient.name = ingredient.name.replace('dark', 'white')
        else:
            recipe, ingredient = transform_ingredient_vegtarian(recipe, ingredient)
    elif ingredient.type == 'bread':
        ingredient.name = ingredient.name.replace('white', 'whole wheat')
    elif ingredient.type == 'pasta':
        name = ingredient.name
        ingredient.name = ingredient.name.replace(name, 'whole wheat ' + name)
    elif ingredient.type == 'carb':
        name = ingredient.name
        ingredient.name = ingredient.name.replace(name, 'brown rice')
    elif ingredient.type == 'cheese':
        # ADD FUNCTION?
        recipe.replace_ingredient(ingredient, 'cheese')
    elif ingredient.type == 'dairy':
        # ADD FUNCTION?
        recipe.replace_ingredient(ingredient, 'dairy')
    return recipe, ingredient

def transform_mexican(recipe):
    for ingredient in recipe.ingredients:
        if 'un-mexican' in ingredient.flags:
            recipe, ingredient = transform_ingredient_vegetarian(recipe, ingredient)
    return recipe