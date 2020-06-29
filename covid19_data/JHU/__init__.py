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
countries = [
    "Australia",
    "Austria",
    "Canada",
    "China",
    "Denmark",
    "Finland",
    "France",
    "Germany",
    "Iceland",
    "Ireland",
    "Italy",
    "Netherlands",
    "Norway",
    "Russia",
    "Sweden",
    "Switzerland",
    "United Kingdom",
    "US",
    "Spain",
    "Mexico",
    "Chile",
    "Brazil",
    "Peru",
    "Colombia",
    "Japan",
    "Ukraine",
    "India",
    "Pakistan",
    "Afghanistan",
    "Albania",
    "Algeria",
    "Andorra",
    "Angola",
    "Antigua and Barbuda",
    "Argentina",
    "Armenia",
    "Azerbaijan",
    "Bahamas",
    "Bahrain",
    "Bangladesh",
    "Barbados",
    "Belarus",
    "Belgium",
    "Belize",
    "Benin",
    "Bhutan",
    "Bolivia",
    "Bosnia and Herzegovina",
    "Botswana",
    "Brunei",
    "Bulgaria",
    "Burkina Faso",
    "Burma",
    "Burundi",
    "Cabo Verde",
    "Cambodia",
    "Cameroon",
    "Central African Republic",
    "Chad",
    "Comoros",
    "Congo (Brazzaville)",
    "Congo (Kinshasa)",
    "Costa Rica",
    "Cote d'Ivoire",
    "Croatia",
    "Cuba",
    "Cyprus",
    "Czechia",
    "Diamond Princess",
    "Djibouti",
    "Dominica",
    "Dominican Republic",
    "Ecuador",
    "Egypt",
    "El Salvador",
    "Equatorial Guinea",
    "Eritrea",
    "Estonia",
    "Eswatini",
    "Ethiopia",
    "Fiji",
    "Gabon",
    "Gambia",
    "Georgia",
    "Ghana",
    "Greece",
    "Grenada",
    "Guatemala",
    "Guinea",
    "Guinea-Bissau",
    "Guyana",
    "Haiti",
    "Holy See",
    "Honduras",
    "Hungary",
    "Indonesia",
    "Iran",
    "Iraq",
    "Israel",
    "Jamaica",
    "Jordan",
    "Kazakhstan",
    "Kenya",
    "Korea, South",
    "Kosovo",
    "Kuwait",
    "Kyrgyzstan",
    "Laos",
    "Latvia",
    "Lebanon",
    "Lesotho",
    "Liberia",
    "Libya",
    "Liechtenstein",
    "Lithuania",
    "Luxembourg",
    "MS Zaandam",
    "Madagascar",
    "Malawi",
    "Malaysia",
    "Maldives",
    "Mali",
    "Malta",
    "Mauritania",
    "Mauritius",
    "Moldova",
    "Monaco",
    "Mongolia",
    "Montenegro",
    "Morocco",
    "Mozambique",
    "Namibia",
    "Nepal",
    "New Zealand",
    "Nicaragua",
    "Niger",
    "Nigeria",
    "North Macedonia",
    "Oman",
    "Panama",
    "Papua New Guinea",
    "Paraguay",
    "Philippines",
    "Poland",
    "Portugal",
    "Qatar",
    "Romania",
    "Rwanda",
    "Saint Kitts and Nevis",
    "Saint Lucia",
    "Saint Vincent and the Grenadines",
    "San Marino",
    "Sao Tome and Principe",
    "Saudi Arabia",
    "Senegal",
    "Serbia",
    "Seychelles",
    "Sierra Leone",
    "Singapore",
    "Slovakia",
    "Slovenia",
    "Somalia",
    "South Africa",
    "South Sudan",
    "Sri Lanka",
    "Sudan",
    "Suriname",
    "Syria",
    "Taiwan*",
    "Tajikistan",
    "Tanzania",
    "Thailand",
    "Timor-Leste",
    "Togo",
    "Trinidad and Tobago",
    "Tunisia",
    "Turkey",
    "Uganda",
    "United Arab Emirates",
    "Uruguay",
    "Uzbekistan",
    "Venezuela",
    "Vietnam",
    "West Bank and Gaza",
    "Western Sahara",
    "Yemen",
    "Zambia",
    "Zimbabwe"
]

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

for country in countries:
    name = country
    obj = dataByName(name)
    data_dict = {"deaths": obj.deaths,
                 "cases": obj.cases, "recovered": obj.recovered, "confirmed": obj.cases}
    globals()[re.sub(remove_space, '', name)] = DictToOjb(data_dict)

US = DictToOjb(us_dict)
Total = DictToOjb(total_dict)
