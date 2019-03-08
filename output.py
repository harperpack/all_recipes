#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 23:15:46 2019

@author: harper
"""

class ingred:
    def __init__(self):
        self.quantity = 0
        self.name = ''
        self.unit = ''
        self.preparation = []
        self.descriptor = []

class Direction:
    def __init__(self):
        self.text = ''
        self.device = ''
        self.actions = []
        self.duration = ''
        self.time_unit = ''
        self.ingredients = []

def print_recipe(ingredients, directions, title, servings, time):
    print