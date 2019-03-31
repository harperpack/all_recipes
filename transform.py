#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 14:07:04 2019

@author: harper
"""

from transform_ingredients import transform_vegetarian, transform_healthy, transform_mexican, transform_eastasian, transform_nonveg, transform_unhealthy

def route_transformations(selection, recipe):
    if selection:
#        if isinstance(selection, list):
#            recipe = transform_multiple(selection, recipe)
        if isinstance(selection, str):
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
#            elif selection == 'm':
#                recipe = transform_meatier(recipe)
#            elif selection == 'a':
#                recipe = transform_cost(recipe)
#            elif selection == 'e':
#                recipe = transform_cost(recipe, more = True)
#            elif selection == 'b':
#                recipe = transform_spice(recipe)
#            elif selection == 's':
#                recipe = transform_spice(recipe, more = True)
    return recipe