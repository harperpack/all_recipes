#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 14:07:04 2019

@author: harper
"""

from transform_ingredients import transform_vegetarian, transform_healthy, transform_mexican

#import math
#import spacy
#nlp = spacy.load('en_core_web_sm')
#
# h   | "Healthy"
# v   | Vegetarian
# vgn | Vegan
# m   | Add Meat
# s   | Spicy
# b   | Bland
# a   | Affordable
# e   | Expensive
# +   | More Servings
# -   | Fewer Servings
# dif | Different Cuisine
# add | Select Multiple Transformations
# n   | Do Nothing
# x   | Exit
# usa | "American"
# ita | "Italian"
# ind | "Indian"
# mex | "Mexican"
#[h, v, s, a, 4, ita]


#def can_round(x):
#    return math.ceil(x*4)/4
#
#red_meat = ['beef', 'pork', 'lamb', 'veal', 'venison', 'rabbit', 'goat', 
#            'mutton', 'boar', 'buffalo', 'ox', 'calf', 'steak', 'ground beef']
#processed_meat = ['sausage', 'ham', 'bacon', 'salami', 'bologna', 'corned',
#                  'canned', 'jerky', 'chorizo']
#poultry = ['chicken', 'turkey', 'duck', 'goose', 'fowl', 'quail', 'bird', 
#           'partridge', 'ostrich', 'grouse', 'pheasant']
#dark_meat = ['thigh', 'wing']
#fish = ['salmon', 'tuna', 'bass', 'anchovy', 'sardine', 'catfish', 'cod',
#        'trout', 'perch', 'roe', 'caviar', 'mahi', 'herring', 'flounder',
#        'mackerel', 'swordfish', 'pollock', 'halibut', 'hake', 'bream', 'eel',
#        'tilapia', 'snapper', 'char', 'carp', 'sole', 'sturgeon', 'yellowtail',
#        'walleye', 'monkfish', 'grouper', 'marlin', 'shark']
#shellfish = ['shrimp', 'crab', 'lobster', 'clam', 'scallop', 'oyster', 'mussel',
#             'crayfish', 'crawfish', 'winkel', 'squid', 'octopus', 'cuttlefish',
#             'prawn', 'cockle']
#white_meat = poultry + fish + shellfish
#meat = white_meat + dark_meat + red_meat + processed_meat
#mex_cheese = ['cotija cheese', 'queso fresco', 'manchego cheese', 'queso panela',
#              'queso añejo', 'oaxaca cheese', 'panela cheese', 'queso asadero', 
#              'asadero cheese']
#gen_cheese = ['parmesan cheese', 'mozzarella cheese', 'gorgonzola cheese', 
#               'cheese', 'cheddar cheese', 'muenster cheese', 'gouda cheese',
#               'blue cheese', 'bleu cheese', 'cream cheese', 'swiss cheese',
#               'ricotta cheese', 'goat cheese', 'colby-monterey jack cheese',
#               'monterey jack cheese', 'processed cheese', 'emmentaler cheese',
#               'colby cheese', 'pepper jack cheese', 'american cheese',
#               'cheese wiz', 'colby jack cheese', 'havarti cheese', 'feta cheese',
#               'brie', 'brie cheese', 'camembert cheese', 'provolone',
#               'pecorino romano cheese', 'raclette cheese']
#cheese = gen_cheese + mex_cheese
#liquid_dairy = ['yogurt', 'yoghurt', 'milk', 'cream']
#dairy = liquid_dairy + cheese
#other_animal_protein = ['egg']
#animal_proteins = meat + dairy + other_animal_protein
#animal_fats = ['butter', 'lard']
#animal_bases = ['blood', 'bone', 'gelatin', 'foie gras', 'honey', 'fish sauce',
#                'Worcestershire sauce', 'furikake', 'bonito', 'confit', 'pâté',
#                'chicken stock', 'beef stock']
#non-vegan = animal_proteins + animal_fats + animal_bases

#def categorize_veg(recipe, vgn=False):
#    for ingredient in recipe.ingredients:
#        doc = nlp(ingredient.name.lower())
#        tokens = list(doc)
#        if not vgn:
#            if any(word in tokens for word in meat):
#                ingredient.veg = 'meat'
#        elif vgn:
#            if any(word in tokens for word in non-vegan):
#                if any(word in tokens for word in meat):
#                    ingredient.veg = 'meat'
#                elif any(word in tokens for word in dairy):
#                    ingredient.veg = 'dairy'
#                elif any(word in tokens for word in other_animal_protein):
#                    ingredient.veg = 'egg'
#                elif any(word in tokens for word in animal_fats):
#                    ingredient.veg = 'fat'
#                elif any(word in tokens for word in animal_bases):
#                    ingredient.veg = 'base'
#    return recipe

#class Direction:
#    def __init__(self):
#        self.text = ''
#        self.tools = '' # CHANGE TO TOOL
#        self.actions = []
#        self.duration = ''
#        self.time_unit = ''
#        self.ingredients = []

#def categorize_vegetarian(recipe, h=False):
#   for ingredient in recipe.ingredients:
#       # look for meat ingredients
#       if ingredient.name.lower() in meat:
#           # beef or beef-similar meats (not pork) will be handled the same
#           if ingredient.name.lower() == 'beef' or ingredient.name.lower() in red_meat and ingredient.name.lower() != 'pork':
#               # stew and roast have same transformation
#               if recipe.primary_cooking_method == 'stew' or recipe.primary_cooking_method == 'roast':
#                   # portobello good sub for beef et al in stews and roasts
#                   ingredient.name = 'portobello mushroom'
#                   # determine right amount of portobellos to use in substitution
#                   if ingredient.unit == 'ounce':
#                       quantity = ingredient.quantity / 16
#                   elif ingredient.unit == 'pound':
#                       quantity = ingredient.quantity
#                   elif ingredient.unit == 'gram':
#                       quantity = ingredient.quantity / 450
#                   ingredient.quantity = int(5 * quantity)
#                   ingredient.unit = 'discrete'
#                   # add beans for protein
#                   need_beans = True
#                   cook_beans = False
#                   # check if beans already in recipe
#                   for item in recipe.ingredients:
#                       if "bean" in item.name or "beans" in item.name:
#                           item.quantity += can_round(quantity)
#                           need_beans = False
#                   if add_beans:
#                       new_beans = ingred()
#                       new_beans.name = "black beans"
#                       new_beans.quantity = can_round(quantity)
#                       new_beans.unit = "15 ounce can"
#                       recipe.ingredients.append(new_beans)
#                       need_beans = False
#                       bean_instruct = Direction()
#                       bean_instruct.text = "Drain and rinse the beans with cold water in a colander."
#                       bean_instruct.tools = ['colander']
#                       bean_instruct.ingredients.append(new_beans)
#                       bean_instruct.actions = ['Drain', 'rinse']
#                       for direction in recipe.directions:
#                           if cook_beans:
#                               break
#                           else:
#                               if "stir" in direction.actions and direction.ingredients and direction.ingredients[0].type == 'vegetable':
#                                   # add beans
#                                   direction.text.replace(direction.ingredients[0].name, "beans, " + direction.ingreients[0].name)
#                                   cook_beans = True
#                   new_add = ingred()
#                   new_add
#                   
#                   
#           elif primary_cooking_method == 'stirfry':
#               ingredient.name == 'seitan with tameli???'
#       elif ingredient.name == 'pork' | 'pulled pork':
#           if primary_cooking_method == 'stew':
#               ingredient.name == 'chanterelle':
#       elif ingredient.name == 'pork loin' | 'pork chop':
#           if primary_cooking_method == 'stew':
#               ingredient.name == 'seitan'
#           elif primary_cooking_method == 'roast':
#               if ingredient.name == 'ham':
#                   ingredient.name == 'tofurky'
#       elif ingredient.name == 'chicken'
#           if primary_cooking_method == 'roast | bake':
#               ingredient.name == 'eggplant'
#       elif ingredient.name == 'bacon':
#           ingredient.name == 'eggplant'
#       elif ingredient.name == 'sausage':
#           ingredient.name == 'vegan sausage'

#hot_sauces = ['tabasco', 'sriracha', 'hot sauce', "frank's red hot", 'sambal',
#              'cholula', "valentina's", 'harissa']
#spicy_vegetables = ['guajillo', 'habanero', 'jalapeño', 'scotch bonnet', 'chili',
#                    'savina', 'tabasco', 'serrano', 'peperoncino', 'chipotle']
#spicy_seasonings = ['cayenne', 'chile', 'peppercorn', 'horseradish', 'pepper oil',
#                    'red pepper', 'curry powder', 'wasabi', 'chili oil']

#def categorize_spice(recipe, spicier=False):
#    for ingredient in recipe.ingredients:
#        doc = nlp(ingredient.name.lower())
#        tokens = list(doc)

def route_transformations(selection, recipe):
    if selection:
        if isinstance(selection, list):
            recipe = transform_multiple(selection, recipe)
        elif isinstance(selection, str):
            if selection == 'h':
                recipe = transform_healthy(recipe)
            elif selection == 'v':
                recipe = transform_vegetarian(recipe)
            elif selection == 'vgn':
                recipe = transform_vegetarian(recipe, vgn = True)
            elif selection == 'mex':
                recipe = transform_mexican(recipe)
#            elif selection == 'a':
#                recipe = transform_cost(recipe)
#            elif selection == 'e':
#                recipe = transform_cost(recipe, more = True)
#            elif selection == 'b':
#                recipe = transform_spice(recipe)
#            elif selection == 's':
#                recipe = transform_spice(recipe, more = True)
        elif isinstance(selection, float):
            recipe = transform_scale(recipe, selection)
    return recipe

def transform_scale(recipe, scale):
    for ingredient in recipe.ingredients:
        ingredient.quantity *= scale
    for direction in recipe.directions:
        tokens = None
        if direction.ingredients:
            for ingredient in direction.ingredients:
                if ingredient.quantity < 1 and 'each' not in direction.text:
                    if not tokens:
                        doc = nlp(direction.text)
                        tokens = list(doc)
                    j = tokens.index(amount)
                    if tokens[j+1] == 'of' and tokens[j+2] == 'the':
                        continue
                    ingredient.quantity *= scale
    return recipe

def transform_multiple(selections, recipe):
    pass