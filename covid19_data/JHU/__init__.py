from .get_data import get_all_data
from .get_object import Item, Items
from covid19_data.dict_as_attribute import DictAsObj as DictToOjb
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
    item.rtrn_data()
    return item


def dataByCallerNameShort():
    s = str(inspect.stack()[1][4]).split()[0][2:]
    item = Item(states[s])
    item.rtrn_data()
    return item


def dataByName(name):
    name = re.sub(remove_space, '', name).upper()
    item = Item(name)
    item.rtrn_data()
    return item


def dataByNameShort(name):
    name = re.sub(remove_space, '', name).upper()
    item = Item(states[name].upper())
    item.rtrn_data()
    return item


def jsonByCallerName():
    s = str(inspect.stack()[1][4]).split()[0][2:]
    item = Item(s)
    item.rtrn_data()
    return item.json


def jsonByCallerNameShort():
    s = str(inspect.stack()[1][4]).split()[0][2:]
    item = Item(states[s])
    item.rtrn_data()
    return item.json


def jsonByName(name):
    name = re.sub(remove_space, '', name).upper()
    item = Item(name)
    item.rtrn_data()
    return item.json


def jsonByNameShort(name):
    name = re.sub(remove_space, '', name).upper()
    item = Item(states[name].upper())
    item.rtrn_data()
    return item.json


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

US_obj = dataByName("US")
us_dict = {
    "deaths": US_obj.deaths, "cases": US_obj.cases, "recovered": US_obj.recovered, "confirmed": US_obj.cases
}

total_obj = dataByName("Total")
total_dict = {
    "deaths": total_obj.deaths, "cases": total_obj.cases, "recovered": total_obj.recovered, "confirmed": total_obj.cases
}

for state in states:
    name = states[state]
    obj = dataByName(name)
    data_dict = {"deaths": obj.deaths,
                 "cases": obj.cases, "recovered": obj.recovered, "confirmed": obj.cases}
    globals()[name] = DictToOjb(data_dict)

US = DictToOjb(us_dict)
Total = DictToOjb(total_dict)
