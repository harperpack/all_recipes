#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 09:14:49 2019

@author: harper
"""

def transform_vegetarian(recipe, vgn=False):
    recipe.transformations.append('Vegetarian')
    for ingredient in recipe.ingredients:
        if 'non-veg' in ingredient.flags:
            recipe, ingredient = transform_ingredient_vegetarian(recipe, ingredient, vgn)
    return recipe

def transform_ingredient_vegetarian(recipe, ingredient, vgn=None, flagged=None):
    unflag = ['non-veg']
    if flagged:
        unflag.append(flagged)
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
            recipe.add_ingredient(ingredient, 'garlic powder')
            recipe.add_ingredient(ingredient, 'paprika')
    elif ingredient.type == 'ham':
        if recipe.meal == 'roast':
            recipe.replace_ingredient(ingredient, new_name='Tofurky ham roast', old_name=ingredient.name, deflag=unflag)
        else:
            # ADD FUNCTION?
            recipe.replace_ingredient(ingredient, 'seitan')
            # ADD FUNCTION?
            recipe.add_ingredient('salt')
    elif ingredient.type == 'bacon':
        recipe.replace_ingredient(ingredient, new_name='vegetarian bacon', old_name='bacon', deflag=unflag)
    elif ingredient.type == 'processed meat':
        # ADD FUNCTION?
        recipe.replace_ingredient(ingredient, 'seitan')
        # ADD FUNCTION?
        recipe.add_ingredient('salt')
    elif ingredient.type == 'poultry':
        if recipe.meal == 'roast':
            recipe.replace_ingredient(ingredient, 'eggplant')
        else:
            recipe.replace_ingredient(ingredient, 'jackfruit')
            # ADD FUNCTION?
            recipe.add_ingredient('brown lentils')
    elif ingredient.type == 'sausage':
        recipe.replace_ingredient(ingredient, new_name='vegetarian sausage', old_name='sausage', deflag=unflag)
    elif ingredient.type == 'shellfish':
        recipe.replace_ingredient(ingredient, 'shiitake mushrooms')
    elif ingredient.type == 'stock':
        if 'stock' in ingredient.name or 'bouillon' in ingredient.name:
            if 'chicken' in ingredient.name:
                recipe.replace_ingredient(ingredient, new_name='vegetable', old_name='chicken', deflag=unflag)
            elif 'beef' in ingredient.name:
                recipe.replace_ingredient(ingredient, new_name='vegetable', old_name='beef', deflag=unflag)
            elif 'shrimp' in ingredient.name:
                recipe.replace_ingredient(ingredient, new_name='vegetable', old_name='shrimp', deflag=unflag)
        elif 'blood' in ingredient.name or 'bone' in ingredient.name:
            # PRESENTLY UNSUPPORTED
            recipe.replace_ingredient(ingredient, 'vegetable bouillon cube')
        else:
            # PRESENTLY UNSUPPORTED
            recipe.replace_ingredient(ingredient, 'agar agar')
    else:
        recipe.replace_ingredient(ingredient, 'tofu')
    return recipe, ingredient

def transform_healthy(recipe):
    recipe.transformations.append('Healthy')
    fruits_or_vegetables = 0
    for ingredient in recipe.ingredients:
        if 'unhealthy' in ingredient.flags:
            print(ingredient.name)
            recipe, ingredient = transform_ingredient_healthy(recipe, ingredient)
            print(ingredient.name)
        if ingredient.type == 'fruit' or ingredient.type == 'vegetable':
            fruits_or_vegetables = True
    if fruits_or_vegetables < 4:
        # ADD FUNCTION
        recipe.add_ingredient('spinach')
    return recipe

def transform_ingredient_healthy(recipe, ingredient):
    unflag = ['unhealthy']
    if ingredient.type in ['pork', 'bacon', 'sausage', 'ham', 'processed meat', 'poultry', 'red meat']:
        if ingredient.type == 'poultry':
            if 'thigh' in ingredient.name:
                recipe.replace_ingredient(ingredient, new_name='breast', old_name='thigh', deflag=unflag)
            elif 'wing' in ingredient.name:
                recipe.replace_ingredient(ingredient, new_name='breast', old_name='wing', deflag=unflag)
            elif 'dark' in ingredient.name:
                recipe.replace_ingredient(ingredient, new_name='white', old_name='dark', deflag=unflag)
        else:
            recipe, ingredient = transform_ingredient_vegetarian(recipe, ingredient, flagged=unflag[0])
    elif ingredient.type == 'bread':
        if 'white' in ingredient.name:
            recipe.replace_ingredient(ingredient, new_name='whole wheat', old_name='white', deflag=unflag)
        else:
            recipe.replace_ingredient(ingredient, new_name='whole grain ' + ingredient.name, old_name=ingredient.name, deflag=unflag)
    elif ingredient.type == 'pasta':
        recipe.replace_ingredient(ingredient, new_name='whole wheat ' + ingredient.name, old_name=ingredient.name, deflag=unflag)
    elif ingredient.type == 'carb':
        recipe.replace_ingredient(ingredient, new_name='brown rice', old_name=ingredient.name, deflag=unflag)
    elif ingredient.type == 'cheese':
        ingredient.quantity /= 2
    elif ingredient.type == 'dairy':
        if 'sour' in ingredient.name:
            recipe.replace_ingredient(ingredient, new_name='light sour', old_name='sour', deflag=unflag)
        elif 'cream' in ingredient.name:
            recipe.replace_ingredient(ingredient, new_name='half and half', old_name=ingredient.name, deflag=unflag)
        elif 'yogurt' in ingredient.name:
            recipe.replace_ingredient(ingredient, new_name='nonfat yogurt', old_name='yogurt', deflag=unflag)
        elif 'yoghurt' in ingredient.name:
            recipe.replace_ingredient(ingredient, new_name='nonfat yogurt', old_name='yoghurt', deflag=unflag)
        elif 'milk' in ingredient.name:
            recipe.replace_ingredient(ingredient, new_name='skim milk', old_name='milk', deflag=unflag)
    elif ingredient.type == 'sugar':
        recipe.replace_ingredient(ingredient, new_name='granulated coconut sugar', old_name=ingredient.name, deflag=unflag)
    elif ingredient.type == 'fat':
        recipe.replace_ingredient(ingredient, 'olive oil')
    elif ingredient.type == 'flour':
        print("Being called")
        recipe.replace_ingredient(ingredient, new_name='whole wheat flour', old_name=ingredient.name, deflag=unflag)
    return recipe, ingredient

def transform_mexican(recipe):
    mex_seasonings = 0
    mex_veg_and_frt = 0
    mex_others = 0
    for ingredient in recipe.ingredients:
        if 'un-mexican' in ingredient.flags:
            recipe, ingredient = transform_ingredient_mexican(recipe, ingredient)
            ingredient.flags.append('mexican')
        if 'mexican' in ingredient.flags:
            if 'seasoning' in ingredient.type:
                mex_seasonings += 1
            elif ingredient.type == 'vegetable':
                mex_veg_and_frt += 1
            elif ingredient.type == 'fruit':
                mex_veg_and_frt += 1
            else:
                mex_others += 1
    if mex_seasonings + mex_veg_and_frt + mex_others < 4:
        recipe.add_ingredient('avocado')
        recipe.add_ingredient('chili powder')
        recipe.add_ingredient('onion powder')
        recipe.add_ingredient('garlic powder')
    return recipe

def transform_ingredient_mexican(recipe, ingredient):
    unflag = ['un-mexican']
    if 'seasoning' in ingredient.type:
        if 'bitter' in ingredient.type:
            recipe.replace_ingredient(ingredient, new_name='azafran', old_name=ingredient.name, deflag=unflag)
        elif 'sweet' in ingredient.type:
            recipe.replace_ingredient(ingredient, new_name='allspice', old_name=ingredient.name, deflag=unflag)
        elif 'savory' in ingredient.type:
            recipe.replace_ingredient(ingredient, new_name='oregano', old_name=ingredient.name, deflag=unflag)
        else:
            recipe.replace_ingredient(ingredient, new_name='cayenne pepper', old_name=ingredient.name, deflag=unflag)
    elif ingredient.type == 'pasta':
        recipe.replace_ingredient(ingredient, new_name='fideo noodle', old_name=ingredient.name, deflag=unflag)
    elif ingredient.type == 'carb':
        recipe.replace_ingredient(ingredient, new_name='red rice', old_name=ingredient.name, deflag=unflag)
    elif ingredient.type == 'cheese':
        recipe.replace_ingredient(ingredient, new_name='cotija cheese', old_name=ingredient.name, deflag=unflag)
    elif ingredient.type == 'dairy':
        recipe.replace_ingredient(ingredient, new_name='sour cream', old_name=ingredient.name, deflag=unflag)
    elif ingredient.type == 'vegetable':
        pass
    elif ingredient.type == 'fruit':
        recipe.replace_ingredient(ingredient, 'avocado')
    elif ingredient.type == 'base':
        if 'powder' in ingredient.name:
            recipe.replace_ingredient(ingredient, new_name='cocoa powder', old_name=ingredient.name, deflag=unflag)
        else:
            recipe.replace_ingredient(ingredient, new_name='mole negro sauce', old_name=ingredient.name, deflag=unflag)
    elif ingredient.type == 'condiment':
        recipe.replace_ingredient(ingredient, new_name='tomatillo salsa', old_name=ingredient.name, deflag=unflag)
    return recipe, ingredient