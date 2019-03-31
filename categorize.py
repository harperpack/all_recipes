#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 12:35:52 2019

@author: harper
"""

greens = ['arugula', 'spinach', 'bok choy', 'baby bok choy', 'kale', 'lettuce',
          'romaine', 'iceberg', 'collard greens', 'swiss chard', 'watercress',
          'mustard greens']

mushrooms = ['enoki', 'enoki mushrooms', 'shiitake mushrooms', 'portobello mushrooms',
             'chanterelle', 'button mushrooms', 'white button mushrooms', 'truffles',
             'porcini mushrooms', 'king oyster mushrooms']

non_mex_veg = ['asparagus', 'beet', 'bamboo shoots', 'bean sprouts', 'endive',
               'broccoli', 'sprouts', 'brussel sprouts', 'brussels sprouts',
               'celery', 'red cabbage', 'coconut', 'olive',
               'pear', 'bamboo shoot', 'bean sprout', 'grape', 'shallot', 'yam',
               'fennel', 'celeric']

non_mex_cruc = ['artichoke', 'celery', 'asparagus', ]

non_mex_starch = ['water chestnut', 'celeric', 'taro', 'yam']

veg_subs = ['portobello mushroom', 'seitan', 'jackfruit', 'Tofurky', 'vegetarian',
            'veggie', 'eggplant', 'shiitake mushrooms', 'tofu', 'tempeh',
            'textured vegetable protein', 'garden', 'quorn']

veg = ['artichoke', 'asparagus', 'beet', 'bamboo shoots', 'bean sprouts', 'endive',
       'bell pepper', 'broccoli', 'sprouts', 'brussel sprouts', 'brussels sprouts',
       'cabbage', 'carrot', 'cassava', 'cauliflower', 'celery', 'corn', 'cucumber',
       'daikon', 'turnip', 'radish', 'eggplant', 'green beans',
       'string beans', 'string bean', 'peas', 'heart of palm', 'okra', 'olive', 'onion', 
       'parsnip', 'snow pea', 'sugar snap pea', 'pea', 'bamboo shoot', 'bean sprout',
       'snow peas', 'sugar snap peas', 'potato', 'sweet potato', 'taro', 'pumpkin',
       'radicchio', 'rutabaga', 'shallot', 'squash', 'tomato', 'yam', 'zucchini',
       'water chestnut', 'potatoes', 'sweet potatoes']

fruit = ['apple', 'blueberry', 'strawberry', 'blueberries', 'strawberries', 'cherry',
         'citron', 'orange', 'fig', 'raisin', 'grape', 'durian', 'grapefruit',
         'guava', 'jackfruit', 'kiwi', 'melon', 'honeydew', 'lemon', 'lime',
         'kumquat', 'lychee', 'mango', 'nectarine', 'papaya', 'passion fruit',
         'pineapple', 'peach', 'pear', 'pomegranate', 'pomelo', 'tangerine', 
         'plum', 'persimmon', 'quince', 'rhubarb', 'starfruit', 'canteloupe',
         'cranberry']

mex_veg = ['jicama', 'tomatillo', 'squash', 'corn', 'potato', 'potatoes', 
           'pepper', 'tomato']

mex_fruit = ['avocado', 'tamarind', 'prickly pear', 'plantain', 'mango', 
             'papaya']

spicy_vegetables = ['guajillo', 'habanero', 'jalapeño', 'scotch bonnet', 'chili',
                    'savina', 'tabasco', 'serrano', 'peperoncino', 'chipotle']

mex_vegetables = mex_veg + spicy_vegetables

vegetables = greens + veg + mex_vegetables + mushrooms

fruits = fruit + mex_fruit

fruits_and_vegetables = fruits + vegetables

mex_grains = ['corn', 'rice', 'quinoa']

mex_bread = ['tortilla', 'chalupa', 'arepa', 'taco shell', 'taco', 'torta']

sweet_bread = ['donut']

white_bread = ['white bread', 'kaiser roll', 'bagel', 'wedge', 'croissant', 
               'naan','potato bread', 'ciabatta bread', 'hot dog buns', 'bun',
               'hamburger buns']

whole_bread = ['rye bread', 'marbled rye bread', 'pumpernickel', 
               'whole wheat bread']

breads = sweet_bread + white_bread + whole_bread

bread = breads + mex_bread

pasta = ['pasta', 'macaroni', 'spaghetti', 'fusili', 'penne', 'noodle', 
         'bowtie', 'linguine', 'lasagna', 'fideo']

grain = ['white rice', 'brown rice', 'wild rice', 'yellow rice', 'quinoa',
         'farro', 'barley', 'wheat', 'bulgur', 'cous cous', 'pearled barley',
         'bulgur wheat', 'buckwheat', 'oat', 'rye', 'sorghum', 'spelt', 'wheat berries',
         'couscous', 'semolina', 'durum']

grains = grain + pasta + mex_grains

red_meat = ['beef', 'pork', 'lamb', 'veal', 'venison', 'rabbit', 'goat', 
            'mutton', 'boar', 'buffalo', 'ox', 'calf', 'steak', 'tenderloin']

processed_meat = ['sausage', 'ham', 'bacon', 'salami', 'bologna', 'corned',
                  'canned', 'jerky', 'chorizo', 'ground beef', 'canadian bacon']

poultry = ['chicken', 'turkey', 'duck', 'goose', 'fowl', 'quail', 'bird', 
           'partridge', 'ostrich', 'grouse', 'pheasant']

dark_meat = ['thigh', 'wing', 'dark']

fish = ['salmon', 'tuna', 'bass', 'anchovy', 'sardine', 'catfish', 'cod',
        'trout', 'perch', 'roe', 'caviar', 'mahi', 'herring', 'flounder',
        'mackerel', 'swordfish', 'pollock', 'halibut', 'hake', 'bream', 'eel',
        'tilapia', 'snapper', 'char', 'carp', 'sole', 'sturgeon', 'yellowtail',
        'walleye', 'monkfish', 'grouper', 'marlin', 'shark', 'fish']

shellfish = ['shrimp', 'crab', 'lobster', 'clam', 'scallop', 'oyster', 'mussel',
             'crayfish', 'crawfish', 'winkel', 'squid', 'octopus', 'cuttlefish',
             'prawn', 'cockle']

white_meat = poultry + fish + shellfish

meat = white_meat + dark_meat + red_meat + processed_meat

mex_cheese = ['cotija cheese', 'queso fresco', 'manchego cheese', 'queso panela',
              'queso añejo', 'oaxaca cheese', 'panela cheese', 'queso asadero', 
              'asadero cheese']

gen_cheese = ['parmesan cheese', 'mozzarella cheese', 'gorgonzola cheese', 
               'cheese', 'cheddar cheese', 'muenster cheese', 'gouda cheese',
               'blue cheese', 'bleu cheese', 'cream cheese', 'swiss cheese',
               'ricotta cheese', 'goat cheese', 'colby-monterey jack cheese',
               'monterey jack cheese', 'processed cheese', 'emmentaler cheese',
               'colby cheese', 'pepper jack cheese', 'american cheese',
               'cheese wiz', 'colby jack cheese', 'havarti cheese', 'feta cheese',
               'brie', 'brie cheese', 'camembert cheese', 'provolone',
               'pecorino romano cheese', 'raclette cheese']

cheese = gen_cheese + mex_cheese

liquid_dairy = ['yogurt', 'yoghurt', 'milk', 'cream', 'sour cream', 'heavy cream',
                'whipping cream']

dairy = liquid_dairy + cheese

other_animal_protein = ['egg']

animal_proteins = meat + dairy + other_animal_protein

general_seasonings = ['black pepper', 'salt', 'allspice', 'basil', 'cinnamon',
                      'bay leaf', 'onion salt', 'celery salt', 'garlic', 'lime',
                      'lemon', 'oregano', 'cumin', 'garlic powder', 'onion powder',
                      'paprika', 'parsley', 'safflower', 'sassafras', 'tarragon',
                      'vanilla', 'saffron', 'sage', 'lemongrass', 'sea salt',
                      'cinnamon bark', 'ground cinnamon', 'clove', 'bay',
                      'nutmeg', 'thyme', 'coriander', 'chamomile', 'peppercorn',
                      'tamari sauce', 'tamari', ]

mex_seasonings = ['cayenne', 'cayenne powder']

non_mex_bitter = ['dill', 'anise', 'star anise', 'fennel', 'fenugreek', 'licorice',
                  'turmeric']

non_mex_sweet = ['asafoetida', 'mint', 'peppermint']

non_mex_savory = ['caper', 'rosemary', 'ginger', 'chives', 'galangal', 
                  'chimichurri', 'marjoram', 'lavender']

non_mex_spicy = ['cardamom', 'cardamon', 'mustard', 'curry', 'horseradish']

non_mex_seasonings = non_mex_bitter + non_mex_sweet + non_mex_savory + non_mex_spicy

tiny_measures = ['teaspoon','tablespoon','pinch', 'taste', 'soupçon', 'soupcon',
                 'tsp', 'tbsp', 'sprig', 'inch', 'leaf', 'clove']

spicy_seasonings = ['cayenne', 'chile', 'peppercorn', 'horseradish', 'pepper oil',
                    'red pepper', 'curry powder', 'wasabi', 'chili oil', 
                    'chili powder']

seasonings = general_seasonings + non_mex_seasonings + spicy_seasonings

base_ingreds = ['gravy', 'barbecue sauce', 'lemon juice', 'lime juice',
                'cocktail sauce', 'sauce', 'oil', 'vanilla extract', 'tomato paste',
                'steak sauce', 'coffee sauce', 'mint sauce', 'tomato sauce', 
                'wine sauce', 'vinaigrette', 'bread crumbs', 'baking powder',
                'taro powder', 'powdered taro', 'potato flour', 'yeast',
                'active dry yeast', 'vinegar', 'canola oil', 'baking soda',
                'coconut oil', 'palm oil', 'rapeseed oil', 'truffle oil',
                'shortening', 'almond extract', 'rum flavoring', 'brandy flavoring',
                'liquid smoke', 'cocoa powder', 'rolled oats', 'jam', 'preserve',
                'food coloring', 'jelly', 'agar agar', 'panko bread crumbs']

non_mex_condiments = ['mustard', 'catsup', 'ketchup', 'mayonnaise', 'ranch',
                      'thousand island dressing', 'russian dressing', 'bernaisse',
                      'ranch dressing', 'french dressing', 'duck sauce', 'hollandaise']

non_mex_misc = ['mint extract', 'peanut butter', 'almond butter', 'matcha powder']

non_mex_bases = non_mex_condiments + non_mex_misc

mex_base = ['corn starch', 'corn flour', 'guacamole', 'masa']

refined_flours = ['white flour', 'all purpose flour', 'all-purpose flour']

refined_fats = ['vegetable oil', 'margarine']

healthy_sugar = ['coconut sugar', 'agave nectar', 'honey', 'agave syrup', 
                 'molasses']

sugars = ['sugar', 'powdered sugar', 'brown sugar' 'granulated sugar', 'sugar',
          'high fructose corn syrup', 'stevia', "confecioner's sugar", 'sprinkles']

unhealthy_bases = sugars + refined_flours + refined_fats

hot_sauces = ['tabasco', 'sriracha', 'hot sauce', "frank's red hot", 'sambal',
              'cholula', "valentina's", 'harissa']

animal_fats = ['butter', 'lard']

animal_stock = ['blood', 'bone', 'bouillon' 'chicken stock', 'beef stock', 'gelatin', 
                'beef bouillon', 'chicken bouillon', 'shrimp stock']

animal_sauces = ['fish sauce', 'Worcestershire sauce']

addl_animal_prods = ['foie gras', 'honey', 'furikake', 'bonito', 'confit', 'pâté']

animal_bases = animal_fats + animal_stock + animal_sauces + addl_animal_prods

non_vegan = animal_proteins + animal_bases

bases = base_ingreds + non_mex_bases + mex_base + unhealthy_bases + healthy_sugar + hot_sauces + animal_bases

seed = ['chia seeds', 'chia', 'flax seeds', 'flax', 'sunflower seeds', 'pumpkin seeds',
        'hemp seeds', 'sesame seeds', 'caraway seeds', 'poppy seeds', 'pepitas',
        'squash seeds']

nut = ['peanut', 'almond', 'almond slivers', 'walnut', 'pecan', 'pistachio',
       'macademia', 'macademia nuts', 'brazil nut', 'cashew', 'cashews',
       'hazelnut', 'peanut', 'pine nut']

nuts_and_seeds = nut + seed

beans = ['black beans', 'kidney beans', 'navy beans', 'pinto beans', 'lima beans',
         'red beans', 'great northern beans', 'garbanzo beans', 'chickpeas', 
         'fava beans', 'cannellini beans', 'beans']

lentils = ['green lentils', 'red lentils', 'brown lentils', 'yellow lentils',
           'lentils']

legumes = beans + lentils

class ingred:
    def __init__(self):
        self.quantity = 0
        self.name = ''
        self.unit = ''
        self.preprocessing = []
        self.descriptors = []
        self.alternative = ''
        self.type = ''
        self.specified = ''
        self.flags = []
        self.method = []

def in_other(name, category):
    all_types = []
    meat + seasonings + bases + grains + dairy + fruits_and_vegetables
    all_types -= category
    if name in all_types:
        return True
    else:
        return False

def categorize_ingredient(ingredient):
    name = ingredient.name.lower()
    if ingredient.unit in tiny_measures:
        if any(item in name for item in seasonings):
            return categorize_seasoning(ingredient)
        else:
            return categorize_base(ingredient)
    elif any(item in name for item in meat):
        # ensure stock is not seen as meat
        if any(item in name for item in ['broth', 'stock', 'bouillon']):
            return categorize_base(ingredient)
        else:
            # categorize the meat type
            return categorize_meat(ingredient)
    elif any(item in name for item in grains): 
        # categorize the grain type
        return categorize_grain(ingredient)
    elif any(item in name for item in bases):
        return categorize_base(ingredient)
    elif any(item in name for item in dairy):
        # categorize the dairy type
        return categorize_dairy(ingredient)
    elif any(item in name for item in fruits_and_vegetables):
        # categorize the fruits and veggies
        return categorize_fruits_and_vegetables(ingredient)
    elif any(item in name for item in veg_subs):
        return categorize_veg_subs(ingredient)
    else:
        return categorize_other(ingredient)

# how to know what type of ingredient to switch for?
def categorize_seasoning(ingredient):
    name = ingredient.name.lower()
    ingredient.type = 'seasoning'
    if any(item in name for item in spicy_seasonings):
        ingredient.flags.append('spicy')
    if any(item in name for item in non_mex_seasonings):
        ingredient.flags.append('un-mexican')
        if any(item in name for item in non_mex_bitter):
            ingredient.type = 'bitter seasoning'
        elif any(item in name for item in non_mex_sweet):
            ingredient.type == 'sweet seasoning'
        elif any(item in name for item in non_mex_savory):
            ingredient.type == 'savory seasoning'
        else:
            ingredient.type == 'spicy seasoning'
    if any(item in name for item in mex_seasonings):
        ingredient.flags.append('mexican')
    return ingredient

def categorize_meat(ingredient):
    name = ingredient.name.lower()
    ingredient.flags.append('non-veg')
    ingredient.flags.append('unhealthy')
    if 'pork' not in name and any(item in name for item in red_meat):
        ingredient.type = 'red meat'
    elif 'pork' in name:
        ingredient.type = 'pork'
    elif any(item in name for item in ['veggie', 'vegetable', 'vegetarian', 'vegetable-based', 'garden', 'mock']):
        ingredient.type = 'analogue'
        ingredient.flags.append('veg')
    elif any(item in name for item in processed_meat):
        if 'bacon' in name:
            ingredient.type = 'bacon'
        elif 'sausage' in name:
            ingredient.type = 'sausage'
        elif 'ham' in name:
            # CHECK IF WHOLE HAM?
            ingredient.type = 'ham'
        else:
            ingredient.type = 'processed meat'
    elif any(item in name for item in fish):
        ingredient.type = 'fish'
        ingredient.flags.remove('unhealthy')
    elif any(item in name for item in shellfish):
        ingredient.type = 'shellfish'
        ingredient.flags.remove('unhealthy')
    elif any(item in name for item in poultry):
        ingredient.type = 'poultry'
        if not any(item in name for item in dark_meat):
            ingredient.flags.remove('unhealthy')
    return ingredient

def categorize_grain(ingredient):
    name = ingredient.name.lower()
    # check if bread
    if any(item in name for item in bread):
        ingredient.type = 'bread'
        # check if white bread:
        if name in white_bread:
            # white breads are made from refined grains which are ostensibly unhealthy
            ingredient.flags.append('unhealthy')
        elif any(item in name for item in mex_bread):
            ingredient.flags.append('mexican')
    elif any(item in name for item in pasta):
        ingredient.type = 'pasta'
        # pasta shall not be mexican, unless it is fideo
        if 'fideo' not in name:
            ingredient.flags.append('un-mexican')
        if 'wheat' not in name or 'spinach' not in name:
            # standard pasta is effectively a refined grain
            ingredient.flags.append('unhealthy')
    else:
        ingredient.type = 'carb'
        # check if carb is non-mexican; presumed otherwise to be healthy and veg
        if not any(item in name for item in mex_grains):
            ingredient.flags.append('un-mexican')
    return ingredient

def categorize_dairy(ingredient):
    name = ingredient.name.lower()
    ingredient.flags.append('non-vgn')
    if 'skim' not in name:
        # presume full-fat dairy is unhealthy
        ingredient.flags.append('unhealthy')
    if any(item in name for item in cheese):
        ingredient.type = 'cheese'
        if not any(item in name for item in mex_cheese):
            ingredient.flags.append('un-mexican')
    else:
        ingredient.type = 'dairy'
        if 'sour' not in name:
            # presume non-solid dairy outside of sour cream is non-mexican
            ingredient.flags.append('un-mexican')
    return ingredient

def categorize_fruits_and_vegetables(ingredient):
    name = ingredient.name.lower()
    if any(item in name for item in vegetables):
        ingredient.type = 'vegetable'
        if any(item in name for item in non_mex_veg):
            ingredient.flags.append('un-mexican')
        if any(item in name for item in mex_vegetables):
            if 'un-mexican' not in ingredient.flags:
                ingredient.flags.append('mexican')
        if any(item in name for item in veg_subs):
            ingredient.flags.append('veg')
    else:
        ingredient.type = 'fruit'
        if not any(item in name for item in mex_fruit):
            ingredient.flags.append('un-mexican')
        elif any(item in name for item in mex_fruit):
            if 'un-mexican' not in ingredient.flags:
                ingredient.flags.append('mexican')
        elif any(item in name for item in veg_subs):
            ingredient.flags.append('veg')
    return ingredient

def categorize_base(ingredient):
    name = ingredient.name.lower()
    if any(item in name for item in animal_bases):
        ingredient.flags.append('non-vgn')
        if any(item in name for item in animal_fats):
            ingredient.type = 'fat'
        elif any(item in name for item in animal_stock):
            ingredient.type = 'stock'
            ingredient.flags.append('non-veg')
        elif any(item in name for item in animal_sauces):
            ingredient.type = 'sauce'
        else:
            ingredient.type = 'base'
            if any(item in name for item in ['vegetable', 'veggie']):
                ingredient.flags.append('veg')
    elif any(item in name for item in unhealthy_bases):
        ingredient.flags.append('unhealthy')
        if any(item in name for item in sugars):
            ingredient.type = 'sugar'
        elif any(item in name for item in refined_fats):
            ingredient.type = 'fat'
        else:
            ingredient.type = 'flour'
    elif any(item in name for item in hot_sauces):
        ingredient.flags.append('spicy')
        ingredient.type = 'sauce'
    else:
        ingredient.type = 'base'
        if any(item in name for item in non_mex_bases):
            ingredient.flags.append('un-mexican')
            if any(item in name for item in non_mex_condiments):
                ingredient.type = 'condiment'
        elif any(item in name for item in mex_base):
            ingredient.flags.append('mexican')
        elif any(item in name for item in healthy_sugar):
            ingredient.type = 'sugar'
        elif 'sauce' in name:
            ingredient.type = 'sauce'
    return ingredient

def categorize_other(ingredient):
    name = ingredient.name.lower()
    if any(item in name for item in nuts_and_seeds):
        if name in nut:
            ingredient.type = 'nuts'
        else:
            ingredient.type = 'seeds'
    elif any(item in name for item in legumes):
        if any(item in name for item in beans):
            ingredient.type = 'beans'
        else:
            ingredient.type = 'lentils'
            ingredient.flags.append('un-mexican')
    else:
        ingredient.type = 'other'
    return ingredient

def categorize_veg_subs(ingredient):
    ingredient.type = 'meatswap'
    ingredient.flags.append('veg')
    return ingredient