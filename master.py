#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 19:37:17 2019

@author: harper
"""

from ingredients import load_ingredients, make_ingredient, new_ingredient, rationalize_details
from directions import load_directions, make_direction
from categorize import categorize_ingredient
from builld_recipe import load_recipe, get_title, get_servings, make_recipe, print_recipe
from interface import user_initiation, user_options, user_confirmation
from transform import route_transformations

def launch_recipes():
    url = user_initiation()
    recipe = make_recipe(url)
#    print("Here is the recipe you have selected.")
#    print_recipe(recipe)
    choice = user_options(recipe)
    transformation = user_confirmation(choice, recipe)
    recipe = route_transformations(transformation, recipe)
    recipe.replace_directions()
    print("Here is the transformed recipe!\n")
    print_recipe(recipe)

launch_recipes()