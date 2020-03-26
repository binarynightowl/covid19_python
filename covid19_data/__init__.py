from .get_data import get_all_data
from .get_object import Item, Items
import inspect
import re
states = {
    'AK': 'Alaska',
    'AL': 'Alabama',
    'AR': 'Arkansas',
    'AS': 'AmericanSamoa',
    'AZ': 'Arizona',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DC': 'DistrictofColumbia',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'GU': 'Guam',
    'HI': 'Hawaii',
    'IA': 'Iowa',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'MA': 'Massachusetts',
    'MD': 'Maryland',
    'ME': 'Maine',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
    'MP': 'NorthernMarianaIslands',
    'MS': 'Mississippi',
    'MT': 'Montana',
    'NA': 'National',
    'NC': 'NorthCarolina',
    'ND': 'NorthDakota',
    'NE': 'Nebraska',
    'NH': 'NewHampshire',
    'NJ': 'NewJersey',
    'NM': 'NewMexico',
    'NV': 'Nevada',
    'NY': 'NewYork',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'PR': 'PuertoRico',
    'RI': 'RhodeIsland',
    'SC': 'SouthCarolina',
    'SD': 'SouthDakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VA': 'Virginia',
    'VI': 'VirginIslands',
    'VT': 'Vermont',
    'WA': 'Washington',
    'WI': 'Wisconsin',
    'WV': 'WestVirginia',
    'WY': 'Wyoming'
}
remove_space = re.compile(r'\s+')

def dataByCallerName():
    s = str(inspect.stack()[1][4]).split()[0][2:]
    item = Item(s)
    item.rtrn_dat()
    return item


def dataByCallerNameShort():
    s = str(inspect.stack()[1][4]).split()[0][2:]
    item = Item(states[s])
    item.rtrn_dat()
    return item


def dataByName(name):
    name = re.sub(remove_space, '', name).upper()
    item = Item(name)
    item.rtrn_dat()
    return item


def dataByNameShort(name):
    name = re.sub(remove_space, '', name).upper()
    item = Item(states[name].upper())
    item.rtrn_dat()
    return item


def jsonByCallerName():
    s = str(inspect.stack()[1][4]).split()[0][2:]
    item = Item(s)
    item.rtrn_dat()
    return item.json


def jsonByCallerNameShort():
    s = str(inspect.stack()[1][4]).split()[0][2:]
    item = Item(states[s])
    item.rtrn_dat()
    return item.json


def jsonByName(name):
    name = re.sub(remove_space, '', name).upper()
    item = Item(name)
    item.rtrn_dat()
    return item.json


def jsonByNameShort(name):
    name = re.sub(remove_space, '', name).upper()
    item = Item(states[name].upper())
    item.rtrn_dat()
    return item.json
