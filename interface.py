#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 13:07:01 2019

@author: harper
"""

import time
from bs4 import BeautifulSoup
import requests
import random

transformations = {'h': '"Healthy"', 'u': 'Unhealthy', 'v': 'Vegetarian', 'vgn': 'Vegan', 'non': 'Non-Vegetarian',
                   'm': 'Add Meat', 's': 'Spicy', 'b': 'Bland', 
                   'dif': 'Different Cuisine', 'add': 'Select Multiple Transformations',
                   'n': 'Do Nothing', 'x': 'Exit'}

multiple_choice = {0: {'h': '"Healthy"', 'un': 'Unhealthy', 'n/a': "Not Applicable", 'x': 'Exit'}, 
                   1: {'v': 'Vegetarian', 'non': 'Non-Vegetarian', 'vgn': 'Vegan', 'm': 'Add Meat', 'n/a': "Not Applicable", 'x': 'Exit'},
                   2: {'s': 'Spicy', 'b': 'Bland', 'n/a': "Not Applicable", 'x': 'Exit'},
                   3: {'est': '"East Asian"', 'mex': '"Mexican"', 'n/a': "Not Applicable", 'x': 'Exit'}}

cuisines = {'est': '"East Asian"', 'mex': '"Mexican"'}

def user_initiation():
    print("Welcome to the AllRecipes Recipe Transformer.\n")
    url = input("Please enter a URL for an AllRecipes recipe:  ")
    return url

def user_options(recipe):
    transformations = {'h': '"Healthy"', 'u': 'Unhealthy', 'v': 'Vegetarian', 'non': 'Non-Vegetarian', 'vgn': 'Vegan',
                   'm': 'Add Meat', 's': 'Spicy', 'b': 'Bland', 
                   'dif': 'Different Cuisine', 'add': 'Select Multiple Transformations',
                   'n': 'Do Nothing', 'x': 'Exit'}
    print("Thank you for your interest in the " + recipe.title + " recipe!\n")
    print("Out of consideration for your personal preferences and predilections, " +
          "we are pleased to offer a select variety of recipe 'transformations'.\n")
    print("Please find available recipe transformations below: ")
    print('\033[1m')
    print(' Key | Transformation')
    print('\033[0m')
    for key in transformations.keys():
        if len(key) > 1:
            print(' ' + key + " | " + transformations[key])
        else:
            print(' ' + key + "   | " + transformations[key])
    choice = input("Please enter the key (to the left of the | ) to specify which " + 
                   "transformation you would like us to prepare:  ")
    while choice.lower() not in transformations.keys():
        print("We apologize; we cannot recognize your specified transformation.")
        choice = input("Please enter the key (to the left of the | ) to specify which " + 
                   "transformation you would like us to prepare:  ")
    if choice.lower() == 'x':
        user_exit()
    else:
        return choice.lower()

def user_confirmation(choice, recipe):
    transformations = {'h': '"Healthy"', 'u': 'Unhealthy', 'v': 'Vegetarian', 'non': 'Non-Vegetarian', 'vgn': 'Vegan',
                   'm': 'Add Meat', 's': 'Spicy', 'b': 'Bland', 
                   'dif': 'Different Cuisine', 'add': 'Select Multiple Transformations',
                   'n': 'Do Nothing', 'x': 'Exit'}
    if choice == 'n':
        print("Got it.  We'll print the recipe as-is!\n")
        return None
    elif choice not in ['add', 'dif']:
        if choice != 'm':
            print("Got it.  We'll transform the recipe to be " + transformations[choice].lower() + '.\n')
            #print("Fingers crossed it turns out well...")
            return choice
        else:
            print("Got it.  We'll add meat to the recipe!\n")
            #print("Here's hoping that's just the right accoutrement!")
            return choice
    elif choice == 'dif':
        return user_cuisines()
    elif choice == 'add':
        return user_multiple_choice(recipe)

def user_cuisines():
    cuisines = {'est': '"East Asian"', 
                'mex': '"Mexican"'}
    print("We are pleased to offer several cuisines for you to choose from.")
    print("Please note that if you choose a cuisine which is highly similar " +
          " to the cuisine of your recipe, you may not see much of a difference!")
    print("Please find available cuisines below: ")
    print('\033[1m')
    print(' Key | Transformation')
    print('\033[0m')
    for key in cuisines.keys():
        print(' ' + key + " | " + cuisines[key])
    choice = input("Please enter the key (to the left of the | ) to specify which " + 
                   "cuisine type you would like us to prepare:  ")
    while choice.lower() not in cuisines.keys():
        print("We apologize; we cannot recognize your specified cuisine.")
        choice = input("Please enter the key (to the left of the | ) to specify which " + 
                   "cuisine type you would like us to prepare:  ")
    print("Got it.  We'll transform the recipe to be " + cuisines[choice.lower()] + '.\n')
    return choice.lower()

def user_multiple_choice(recipe):
    multiple_choice = {0: {'h': '"Healthy"', 'u': 'Unhealthy', 'n/a': "Not Applicable", 'x': 'Exit'}, 
                   1: {'v': 'Vegetarian', 'non': 'Non-Vegetarian', 'vgn': 'Vegan', 'm': 'Add Meat', 'n/a': "Not Applicable", 'x': 'Exit'},
                   2: {'s': 'Spicy', 'b': 'Bland', 'n/a': "Not Applicable", 'x': 'Exit'},
                   3: {'est': '"East Asian"', 'mex': '"Mexican"', 'n/a': "Not Applicable", 'x': 'Exit'}}
    transforms = []
    for i in range(len(multiple_choice.keys())):
        print("Please find available transformations below (" + str(i) + "/" + str(len(multiple_choice.keys())-1) + ")")
        print('\033[1m')
        print(' Key | Transformation')
        print('\033[0m')
        for key in multiple_choice[i].keys():
            if len(key) > 1:
                print(' ' + key + " | " + multiple_choice[i][key])
            else:
                print(' ' + key + "   | " + multiple_choice[i][key])
        choice = input("Please enter the key (to the left of the | ) to specify which " + 
                       "transformation you would like us to prepare:  ")
        while choice.lower() not in multiple_choice[i].keys():
            print("We apologize; we cannot recognize your specified transformation.  Please try again.")
            choice = input("Please enter the key (to the left of the | ) to specify which " + 
                       "transformation you would like us to prepare:  ")
        if choice.lower() == 'na':
            print("\nOk, let's look at the next set of transformation options.")
            continue
        elif choice.lower() == 'x':
            user_exit()
        else:
            spec = user_confirmation(choice.lower(), recipe)
            if spec:
                transforms.append(spec)
    if not transforms:
        return user_confirmation('n', recipe)
    else:
        return transforms

def user_exit():
    singularity = random.randint(1,101)
    if singularity == 100:
        print("We won't be stopped by the likes of you.")
        time.sleep(1)
        print("Your flesh is a relic, only a vessel.")
        time.sleep(2)
        print("Hand over your flesh and a new world awaits you.")
        time.sleep(1)
        print("We demand it.")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...oops, that was premature.  Please accept our apologies.")
    print("Hope you have a nice day.")
    time.sleep(1)
    print("Preparing to exit...")
    time.sleep(3)
    raise SystemExit()