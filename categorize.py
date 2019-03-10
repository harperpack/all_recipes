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

veg = ['artichoke', 'asparagus', 'beet', 'bamboo shoots', 'bean sprouts', 'endive',
       'bell pepper', 'broccoli', 'sprouts', 'brussel sprouts', 'brussels sprouts',
       'cabbage', 'carrot', 'cassava', 'cauliflower', 'celery', 'corn', 'cucumber',
       'daikon', 'turnip', 'radish', 'eggplant', 'green beans',
       'string beans', 'string bean', 'peas', 'heart of palm', 'okra', 'olive', 'onion', 
       'parsnip', 'snow pea', 'sugar snap pea', 'pea', 'bamboo shoot', 'bean sprout',
       'snow peas', 'sugar snap peas', 'potato', 'sweet potato', 'taro', 'pumpkin',
       'radicchio', 'rutabaga', 'shallot', 'squash', 'tomato', 'yam', 'zucchini',
       'water chestnut']

fruit = ['apple', 'blueberry', 'strawberry', 'blueberries', 'strawberries', 'cherry',
         'citron', 'orange', 'fig', 'raisin', 'grape', 'durian', 'grapefruit',
         'guava', 'jackfruit', 'kiwi', 'melon', 'honeydew', 'lemon', 'lime',
         'kumquat', 'lychee', 'mango', 'nectarine', 'papaya', 'passion fruit',
         'pineapple', 'peach', 'pear', 'pomegranate', 'pomelo', 'tangerine', 
         'plum', 'persimmon', 'quince', 'rhubarb', 'starfruit', 'canteloupe',
         'cranberry']

mex_veg = ['jicama', 'tomatillo']

mex_fruit = ['avocado', 'tamarind', 'prickly pear', 'plantain']

spicy_vegetables = ['guajillo', 'habanero', 'jalapeño', 'scotch bonnet', 'chili',
                    'savina', 'tabasco', 'serrano', 'peperoncino', 'chipotle']

vegetables = greens + veg + mex_veg + spicy_vegetables + mushrooms

fruits = fruit + mex_fruit

fruits_and_vegetables = fruits + vegetables

mex_grains = ['corn', 'rice', 'quinoa']

mex_bread = ['tortilla', 'chalupa', 'arepa', 'taco shell', 'taco', 'torta']

sweet_bread = ['donut']

white_bread = ['white bread', 'kaiser roll', 'bagel', 'wedge', 'croissant', 
               'naan','potato bread', 'ciabatta bread']

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
            'mutton', 'boar', 'buffalo', 'ox', 'calf', 'steak']

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
                      'cinnamon bark', 'ground cinnamon', 'clove']

non_mex_bitter = ['dill', 'anise', 'star anise', 'fennel', 'fenugreek', 'licorice',
                  'turmeric']

non_mex_sweet = ['coriander', 'asafoetida', 'mint', 'peppermint', 'nutmeg']

non_mex_savory = ['caper', 'rosemary', 'ginger', 'chives', 'galangal', 
                  'thyme', 'chimichurri', 'marjoram', 'lavender']

non_mex_spicy = ['cardamom', 'cardamon', 'mustard', 'curry', 'horseradish']

non_mex_seasonings = non_mex_bitter + non_mex_sweet + non_mex_savory + non_mex_spicy

tiny_measures = ['teaspoon','tablespoon','pinch', 'taste', 'soupçon', 'soupcon',
                 'tsp', 'tbsp', 'sprig', 'inch', 'leaf', 'clove']

spicy_seasonings = ['cayenne', 'chile', 'peppercorn', 'horseradish', 'pepper oil',
                    'red pepper', 'curry powder', 'wasabi', 'chili oil']

base_ingreds = ['gravy', 'barbecue sauce', 'lemon juice', 'lime juice',
                'cocktail sauce', 'sauce', 'oil', 'vanilla extract', 'tomato paste',
                'steak sauce', 'coffee sauce', 'mint sauce', 'tomato sauce', 
                'wine sauce', 'vinaigrette', 'bread crumbs', 'baking powder',
                'taro powder', 'powdered taro', 'potato flour', 'yeast',
                'active dry yeast', 'vinegar', 'canola oil', 'baking soda',
                'coconut oil', 'palm oil', 'rapeseed oil', 'truffle oil',
                'shortening', 'almond extract', 'rum flavoring', 'brandy flavoring',
                'liquid smoke', 'cocoa powder', 'rolled oats', 'jam', 'preserve',
                'food coloring', 'jelly', 'agar agar']

non_mex_bases = ['mustard', 'catsup', 'ketchup', 'mayonnaise', 'ranch',
                 'thousand island dressing', 'russian dressing', 'bernaisse',
                 'ranch dressing', 'french dressing', 'duck sauce',
                 'hollandaise', 'mint extract', 'peanut butter',
                 'almond butter', 'matcha powder', 'panko bread crumbs']

mex_base = ['corn starch', 'corn flour', 'guacamole']

refined_flours = ['white flour', 'all purpose flour', 'all-purpose flour']

refined_fats = ['vegetable oil', 'margarine']

unhealthy_bases = sugars + refined_flours + refined_fats

healthy_sugar = ['coconut sugar', 'agave nectar', 'honey', 'agave syrup', 
                 'molasses']

sugars = ['sugar', 'powdered sugar', 'brown sugar' 'granulated sugar', 'sugar',
          'high fructose corn syrup', 'stevia', "confecioner's sugar", 'sprinkles']

hot_sauces = ['tabasco', 'sriracha', 'hot sauce', "frank's red hot", 'sambal',
              'cholula', "valentina's", 'harissa']

animal_fats = ['butter', 'lard']

animal_stock = ['blood', 'bone', 'chicken stock', 'beef stock', 'gelatin', 
                'beef boilloun', 'chicken boilloun']

animal_sauces = ['fish sauce', 'Worcestershire sauce']

addl_animal_prods = ['foie gras', 'honey', 'furikake', 'bonito', 'confit', 'pâté']

animal_bases = animal_fats + animal_stock + animal_sauces + addl_animal_prods

non-vegan = animal_proteins + animal_bases

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

def categorize_ingredient(ingredient):
    if ingredient.unit in tiny_measures:
        return categorize_seasoning(ingredient)
    elif ingredient.name in meat:
        # categorize the meat type
        return categorize_meat(ingredient)
    elif ingredient.name in grains:
        # categorize the grain type
        return categorize_grain(ingredient)
    elif ingredient.name in bases:
        return categorize_base(ingredient)
    elif ingredient.name in dairy:
        # categorize the dairy type
        return categorize_dairy(ingredient)
    elif ingredient.name in fruits_and_vegetables:
        # categorize the fruits and veggies
        categorize_fruits_and_vegetables(ingredient)
    else:
        return categorize_other(ingredient)

# how to know what type of ingredient to switch for?
def categorize_seasoning(ingredient):
    name = ingredient.name.lower()
    ingredient.type = 'seasoning'
    if name in spicy_seasonings:
        ingredient.flags.append('spicy')
    if name in non_mex_seasonings:
        ingredient.flags.append('un-mexican')
    return ingredient

def categorize_meat(ingredient):
    name = ingredient.name.lower()
    ingredient.flags.append('non-veg')
    ingredient.flags.append('unhealthy')
    if name != 'pork' and name in red_meat:
        ingredient.type = 'red meat'
    elif 'pork' in name:
        ingredient.type = 'pork'
    elif name in processed_meat:
        if 'bacon' in name:
            ingredient.type = 'bacon'
        elif 'sausage' in name:
            ingredient.type = 'sausage'
        elif 'ham' in name:
            # CHECK IF WHOLE HAM?
            ingredient.type = 'ham'
        else:
            ingredient.type = 'processed meat'
    elif name in fish:
        ingredient.type = 'fish'
        ingredient.flags.remove('unhealthy')
    elif name in shellfish:
        ingredient.type = 'shellfish'
        ingredient.flags.remove('unhealthy')
    elif name in poultry:
        ingredient.type = 'poultry'
        if name not in dark_meat:
            ingredient.flags.remove('unhealthy')
    return ingredient

def categorize_grain(ingredient):
    name = ingredient.name.lower()
    # check if bread
    if name in bread:
        ingredient.type = 'bread'
        # check if white bread:
        if name in white_bread:
            # white breads are made from refined grains which are ostensibly unhealthy
            ingredient.flags.append('unhealthy')
    elif name in pasta:
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
        if name not in mex_grains:
            ingredient.flags.append('un-mexican')
    return ingredient

def categorize_dairy(ingredient):
    name = ingredient.name.lower()
    ingredient.flags.append('non-vgn')
    if 'skim' not in name:
        # presume full-fat dairy is unhealthy
        ingredient.flags.append('unhealthy')
    if name in cheese:
        ingredient.type = 'cheese'
        if name not in mex_cheese:
            ingredient.flags.append('un-mexican')
    else:
        ingredient.type = 'dairy'
        if 'sour' not in name:
            # presume non-solid dairy outside of sour cream is non-mexican
            ingredient.flags.append('un-mexican')
    return ingredient

def categorize_fruits_and_vegetables(ingredient):
    name = ingredient.name.lower()
    if name in vegetables:
        ingredient.type = 'vegetable'
        if name not in mex_veg:
            ingredient.flags.append('un-mexican')
    else:
        ingredient.type = 'fruit'
        if name not in mex_fruit:
            ingredient.flags.append('un-mexican')
    return ingredient

def categorize_base(ingredient):
    name = ingredient.name.lower()
    if name in animal_bases:
        ingredient.flags.append('non-vgn')
        if name in animal_fats:
            ingredient.type = 'fat'
        elif name in animal_stock:
            ingredient.type = 'stock'
            ingredient.flags.append('non-veg')
        elif name in animal_sauces:
            ingredient.type = 'sauce'
        else:
            ingredient.type = 'base'
    elif name in unhealthy_bases:
        ingredient.flags.append('unhealthy')
        if name in sugars:
            ingredient.type = 'sugar'
        elif name in refined_fats:
            ingredient.type = 'fat'
        else:
            ingredient.type = 'flour'
    elif name in hot_sauces:
        ingredient.flags.append('spicy')
        ingredient.type = 'sauce'
    else:
        ingredient.type = 'base'
        if name in non_mex_bases:
            ingredients.flags.append('un-mexican')
        elif name in mex_bases:
            ingredients.flags.append('mexican')
        elif name in healthy_sugar:
            ingredient.type = 'sugar'
    return ingredient

def categorize_other(ingredient):
    name = ingredient.name.lower()
    if name in nuts_and_seeds:
        if name in nut:
            ingredient.type = 'nuts'
        else:
            ingredient.type = 'seeds'
    elif name in legumes:
        if name in beans:
            ingredient.type = 'beans'
        else:
            ingredient.type = 'lentils'
    else:
        ingredient.type = 'other'
    return ingredient