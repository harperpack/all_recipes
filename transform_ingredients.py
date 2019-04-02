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
    if vgn:
        unflag.append('non-vgn')
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
        elif 'sauce' in ingredient.name and vgn:
            recipe.replace_ingredient(ingredient, new_name='tamari sauce', old_name=ingredient.name, deflag=unflag)
        elif 'honey' in ingredient.name and vgn:
            recipe.replace_ingredient(ingredient, new_name='agave syrup', old_name=ingredient.name, deflag=unflag)
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
            recipe, ingredient = transform_ingredient_healthy(recipe, ingredient)
        if ingredient.type == 'fruit' or ingredient.type == 'vegetable':
            fruits_or_vegetables += 1
    if fruits_or_vegetables < 4:
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
        if 'bell pepper' in ingredient.name:
            recipe.add_ingredient('jalapeño pepper')
            recipe.add_ingredient('habanero pepper')
    elif ingredient.type == 'fruit':
        recipe.replace_ingredient(ingredient, 'avocado')
    elif ingredient.type == 'base':
        if 'powder' in ingredient.name:
            recipe.replace_ingredient(ingredient, new_name='cocoa powder', old_name=ingredient.name, deflag=unflag)
        else:
            recipe.replace_ingredient(ingredient, new_name='mole negro sauce', old_name=ingredient.name, deflag=unflag)
    elif ingredient.type == 'condiment':
        if 'marinara' in ingredient.name:
            recipe.replace_ingredient(ingredient, new_name='enchilada sauce', old_name=ingredient.name, deflag=unflag)
        else:
            recipe.replace_ingredient(ingredient, new_name='tomatillo salsa', old_name=ingredient.name, deflag=unflag)
    return recipe, ingredient

def transform_eastasian(recipe):
    est_seasonings = 0
    est_veg_and_frt = 0
    est_others = 0
    for ingredient in recipe.ingredients:
        if 'un-eastasian' in ingredient.flags:
            recipe, ingredient = transform_ingredient_eastasian(recipe, ingredient)
            ingredient.flags.append('eastasian')
        if 'eastasian' in ingredient.flags:
            if 'seasoning' in ingredient.type:
                est_seasonings += 1
            elif ingredient.type == 'vegetable':
                est_veg_and_frt += 1
            elif ingredient.type == 'fruit':
                est_veg_and_frt += 1
            else:
                est_others += 1
    if est_seasonings + est_veg_and_frt + est_others < 2:
        recipe.add_ingredient('kimchi')
        recipe.add_ingredient('chili powder')
        recipe.add_ingredient('onion powder')
        recipe.add_ingredient('garlic powder')
    return recipe

def transform_ingredient_eastasian(recipe, ingredient):
    unflag = ['un-eastasian']
    if 'seasoning' in ingredient.type:
        if 'bitter' in ingredient.type:
            recipe.replace_ingredient(ingredient, new_name='cardamom', old_name=ingredient.name, deflag=unflag)
        elif 'sweet' in ingredient.type:
            recipe.replace_ingredient(ingredient, new_name='cloves', old_name=ingredient.name, deflag=unflag)
        elif 'savory' in ingredient.type:
            recipe.replace_ingredient(ingredient, new_name='scallions', old_name=ingredient.name, deflag=unflag)
            recipe.add_ingredient('1.0 egg')
        elif 'spicy' in ingredient.type:
            recipe.replace_ingredient(ingredient, new_name="wasabi", old_name=ingredient.name, deflag=unflag)
        else:
            recipe.replace_ingredient(ingredient, new_name='chinese five spice', old_name=ingredient.name, deflag=unflag)
    elif ingredient.type == 'red_meat':
        recipe.replace_ingredient(ingredient, new_name='wagyu beef', old_name=ingredient.name, deflag=unflag)
    elif ingredient.type == 'pasta':
        recipe.replace_ingredient(ingredient, new_name='rice noodle', old_name=ingredient.name, deflag=unflag)
    elif ingredient.type == 'carb':
        recipe.replace_ingredient(ingredient, new_name='jasmine rice', old_name=ingredient.name, deflag=unflag)
    elif ingredient.type == 'vegetable':
        if 'bell pepper' in ingredient.name:
            recipe.add_ingredient('bok choy') # PROBABLY NEEDS SUPPORT
            recipe.add_ingredient('green wild onions') # PROBABLY NEEDS SUPPORT
        if 'lettuce' in ingredient.name:
            recipe.replace_ingredient(ingredient, new_name='cabbage', old_name=ingredient.name, deflag=unflag)
        else:
            recipe.add_ingredient('green wild onions') # PROBABLY NEEDS SUPPORT
            recipe.add_ingredient('lemongrass') # PROBABLY NEEDS SUPPORT
    elif ingredient.type == 'base':
        if 'powder' in ingredient.name:
            recipe.replace_ingredient(ingredient, new_name='cinnamon powder', old_name=ingredient.name, deflag=unflag)
        else:
            recipe.replace_ingredient(ingredient, new_name='soy sauce', old_name=ingredient.name, deflag=unflag)
    elif ingredient.type == 'refined oils':
        recipe.replace_ingredient(ingredient, new_name='sesame oil', old_name=ingredient.name, deflag=unflag)
    elif ingredient.type == 'condiment':
        if 'marinara' in ingredient.name:
            recipe.replace_ingredient(ingredient, new_name='jalapeño aioli', old_name=ingredient.name, deflag=unflag)
        else:
            recipe.replace_ingredient(ingredient, new_name='kimchi', old_name=ingredient.name, deflag=unflag)
    return recipe, ingredient

def transform_nonveg(recipe):
    nonveg_flag = False
    recipe.transformations.append('Non-vegetarian')
    for ingredient in recipe.ingredients:
        if ingredient.old:
            if 'non-veg' in ingredient.old.flags:
                recipe.revert_to_old(ingredient)
        if 'veg' in ingredient.flags:
            recipe, ingredient = transform_ingredient_nonveg(recipe, ingredient)
            nonveg_flag = True
    if not nonveg_flag:
        recipe.add_ingredient('bacon')
    return recipe

def transform_ingredient_nonveg(recipe, ingredient):
    unflag = ['veg']
    if ingredient.type == 'base':
        if 'vegetable' in ingredient.name:
            recipe.replace_ingredient(ingredient, new_name='beef', old_name='vegetable', deflag=unflag)
        elif 'veggie' in ingredient.name:
            recipe.replace_ingredient(ingredient, new_name='beef', old_name='veggie', deflag=unflag)
    elif ingredient.type == 'analogue':
        if 'burger' in ingredient.name:
            recipe.replace_ingredient(ingredient, new_name='beef hamburger patties', old_name=ingredient.name, deflag=unflag)
        elif 'bacon' in ingredient.name:
            recipe.replace_ingredient(ingredient, new_name='bacon', old_name=ingredient.name, deflag=unflag)
        else:
            recipe.replace_ingredient(ingredient, new_name='andouille sausage', old_name=ingredient.name, deflag=unflag)
    elif ingredient.type == 'meatswap':
        if 'ofurky' in ingredient.name:
            if 'turkey' in ingredient.name:
                recipe.replace_ingredient(ingredient, new_name='roast turkey', old_name=ingredient.name, deflag=unflag)
            elif 'ham' in ingredient.name:
                recipe.replace_ingredient(ingredient, new_name='roast ham', old_name=ingredient.name, deflag=unflag)
        elif 'tofu' in ingredient.name:
            recipe.replace_ingredient(ingredient, new_name='white meat chicken', old_name=ingredient.name, deflag=unflag)
        elif any(sub in ingredient.name for sub in ['seitan', 'tempeh', 'textured vegetable protein', 'quorn']):
            recipe.replace_ingredient(ingredient, 'beef')
    elif ingredient.type == 'fruit':
        if 'jackfruit' in ingredient.name:
            recipe.replace_ingredient(ingredient, 'pork')
    elif ingredient.type == 'vegetable':
        other_meat = False
        for ingred in recipe.ingredients:
            if ingred.type in ['red meat', 'pork', 'bacon', 'sausage', 'ham', 'processed meat', 'fish', 'shellfish', 'poultry']:
                other_meat = True
                break
        if not other_meat:
            if 'take' in ingredient.name:
                recipe.replace_ingredient(ingredient, 'shrimp')
            elif 'plant' in ingredient.name:
                recipe.replace_ingredient(ingredient, new_name='white meat chicken', old_name=ingredient.name, deflag=unflag)
            elif 'mushroom' in ingredient.name:
                recipe.replace_ingredient(ingredient, 'beef')
    return recipe, ingredient

def transform_unhealthy(recipe):
    unhealthiness = 0
    recipe.transformations.append('Unhealthy')
    for ingredient in recipe.ingredients:
        recipe, ingredient = transform_ingredient_unhealthy(recipe, ingredient)
        if 'unhealthy' in ingredient.flags:
            unhealthiness += 1
    if unhealthiness < 5:
        recipe.add_ingredient('cigarettes')
    return recipe

def transform_ingredient_unhealthy(recipe, ingredient):
    unflag = []
    if ingredient.type == 'poultry':
        if 'breast' in ingredient.name:
            recipe.replace_ingredient(ingredient, new_name='thigh', old_name='breast', deflag=unflag)
        elif 'white' in ingredient.name:
            recipe.replace_ingredient(ingredient, new_name='dark', old_name='white', deflag=unflag)
    elif ingredient.type == 'analogue':
        recipe.replace_ingredient(ingredient, 'spam')
    elif ingredient.type == 'meatswap':
        recipe.replace_ingredient(ingredient, 'spam')
    elif ingredient.type == 'cheese':
        ingredient.quantity *= 2
    elif ingredient.type == 'dairy':
        recipe.replace_ingredient(ingredient, new_name='heavy cream', old_name=ingredient.name, deflag=unflag)
    elif ingredient.type == 'bread':
        recipe.replace_ingredient(ingredient, new_name='Wonder bread', old_name=ingredient.name, deflag=unflag)
    elif ingredient.type == 'sugar':
        ingredient.quantity *= 2
    elif ingredient.type == 'fat':
        recipe.replace_ingredient(ingredient, new_name='partially hydrogenated vegetable oil', old_name=ingredient.name, deflag=unflag)
    elif ingredient.type == 'flour':
        if 'whole' in ingredient.name or 'wheat' in ingredient.name:
            recipe.replace_ingredient(ingredient, new_name='refined white flour', old_name=ingredient.name, deflag=unflag)
    elif ingredient.type == 'pasta':
        if 'whole' in ingredient.name:
            recipe.replace_ingredient(ingredient, new_name='white', old_name='whole', deflag=unflag)
    elif ingredient.type == 'carb':
        recipe.replace_ingredient(ingredient, new_name='white rice', old_name=ingredient.name, deflag=unflag)
    return recipe, ingredient

def transform_spicy(recipe):
    recipe.add_ingredient('habanero')
    recipe.add_ingredient('cayenne powder')

def transform_bland(recipe):
    for ingredient in recipe.ingredients:
        recipe, ingredient = transform_ingredient_bland(recipe, ingredient)
    return recipe

def transform_ingredient_bland(recipe, ingredient):
    unflag = ['spicy']
    if 'spicy' in ingredient.flags:
        if 'seasoning' in ingredient.type:
            ingredient.quantity /= 4
            recipe.replace_ingredient(ingredient, new_name='white flour', old_name=ingredient.name, deflag=unflag)
        elif 'base' in ingredient.type:
            ingredient.quantity /= 4
            recipe.replace_ingredient(ingredient, new_name='ketchup', old_name=ingredient.name, deflag=unflag)
        elif ingredient.type == 'vegetable':
            recipe.replace_ingredient(ingredient, new_name='iceberg lettuce', old_name=ingredient.name, deflag=unflag)
    elif 'seasoning' in ingredient.type:
        ingredient.quantity /= 4
    return recipe, ingredient

def transform_multiple(selections, recipe):
    for selection in selections:
        if selection == 'h':
            recipe = transform_healthy(recipe)
        elif selection == 'v':
            recipe = transform_vegetarian(recipe)
        elif selection == 'vgn':
            recipe = transform_vegetarian(recipe, vgn = True)
        elif selection == 'mex':
            recipe = transform_mexican(recipe)
        elif selection == 'est':
            recipe = transform_eastasian(recipe)
        elif selection == 'non':
            recipe = transform_nonveg(recipe)
        elif selection == 'u':
            recipe = transform_unhealthy(recipe)
    return recipe

def transform_meatier(recipe):
    meat = False
    for ingredient in recipe.ingredients:
        if ingredient.type == 'meat':
            ingredient.quantity *= 1.5
            meat = True
    if not meat:
        recipe.add_ingredient('bacon')
    return recipe