#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 19:37:17 2019

@author: harper
"""

from ingredients import load_ingredients, make_ingredient, new_ingredient, rationalize_details
from directions import load_directions, make_direction
from categorize import categorize_ingredient
from builld_recipe import Recipe
from interface import user_initiation, user_options, user_confirmation
from transform import route_transformations

def launch_recipes():
    url = user_initiation()
    r = Recipe(url)
#    print("Here is the recipe you have selected.")
#    print_recipe(recipe)
    choice = user_options(r)
    transformation = user_confirmation(choice, r)
    r = route_transformations(transformation, r)
    r.update_directions()
    print("Here is the transformed recipe!\n")
    r.print_recipe()

if __name__ == '__main__':
    launch_recipes()