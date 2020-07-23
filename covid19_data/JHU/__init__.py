from .get_data import get_all_data
from .get_object import Item, Items
from covid19_data.dict_as_attribute import DictAsObj as DictToObj
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
    'DC': 'DistrictOfColumbia',
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
    "UnitedKingdom",
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
    "AntiguaAndBarbuda",
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
    "BosniaAndHerzegovina",
    "Botswana",
    "Brunei",
    "Bulgaria",
    "BurkinaFaso",
    "Burma",
    "Burundi",
    "CaboVerde",
    "Cambodia",
    "Cameroon",
    "CentralAfricanRepublic",
    "Chad",
    "Comoros",
    "CongoBrazzaville",
    "CongoKinshasa",
    "CostaRica",
    "CotedIvoire",
    "Croatia",
    "Cuba",
    "Cyprus",
    "Czechia",
    "DiamondPrincess",
    "Djibouti",
    "Dominica",
    "DominicanRepublic",
    "Ecuador",
    "Egypt",
    "ElSalvador",
    "EquatorialGuinea",
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
    "GuineaBissau",
    "Guyana",
    "Haiti",
    "HolySee",
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
    "KoreaSouth",
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
    "MsZaandam",
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
    "NewZealand",
    "Nicaragua",
    "Niger",
    "Nigeria",
    "NorthMacedonia",
    "Oman",
    "Panama",
    "PapuaNewGuinea",
    "Paraguay",
    "Philippines",
    "Poland",
    "Portugal",
    "Qatar",
    "Romania",
    "Rwanda",
    "SaintKittsAndNevis",
    "SaintLucia",
    "SaintVincentAndTheGrenadines",
    "SanMarino",
    "SaoTomeAndPrincipe",
    "SaudiArabia",
    "Senegal",
    "Serbia",
    "Seychelles",
    "SierraLeone",
    "Singapore",
    "Slovakia",
    "Slovenia",
    "Somalia",
    "SouthAfrica",
    "SouthSudan",
    "SriLanka",
    "Sudan",
    "Suriname",
    "Syria",
    "Taiwan",
    "Tajikistan",
    "Tanzania",
    "Thailand",
    "TimorLeste",
    "Togo",
    "TrinidadAndTobago",
    "Tunisia",
    "Turkey",
    "Uganda",
    "UnitedArabEmirates",
    "Uruguay",
    "Uzbekistan",
    "Venezuela",
    "Vietnam",
    "WestBankAndGaza",
    "WesternSahara",
    "Yemen",
    "Zambia",
    "Zimbabwe"
]

remove_space = re.compile(r'\s+')

Australia = DictToObj({})
Austria = DictToObj({})
Canada = DictToObj({})
China = DictToObj({})
Denmark = DictToObj({})
Finland = DictToObj({})
France = DictToObj({})
Germany = DictToObj({})
Iceland = DictToObj({})
Ireland = DictToObj({})
Italy = DictToObj({})
Netherlands = DictToObj({})
Norway = DictToObj({})
Russia = DictToObj({})
Sweden = DictToObj({})
Switzerland = DictToObj({})
UnitedKingdom = DictToObj({})
Spain = DictToObj({})
Mexico = DictToObj({})
Chile = DictToObj({})
Brazil = DictToObj({})
Peru = DictToObj({})
Colombia = DictToObj({})
Japan = DictToObj({})
Ukraine = DictToObj({})
India = DictToObj({})
Pakistan = DictToObj({})
Afghanistan = DictToObj({})
Albania = DictToObj({})
Algeria = DictToObj({})
Andorra = DictToObj({})
Angola = DictToObj({})
AntiguaAndBarbuda = DictToObj({})
Argentina = DictToObj({})
Armenia = DictToObj({})
Azerbaijan = DictToObj({})
Bahamas = DictToObj({})
Bahrain = DictToObj({})
Bangladesh = DictToObj({})
Barbados = DictToObj({})
Belarus = DictToObj({})
Belgium = DictToObj({})
Belize = DictToObj({})
Benin = DictToObj({})
Bhutan = DictToObj({})
Bolivia = DictToObj({})
BosniaAndHerzegovina = DictToObj({})
Botswana = DictToObj({})
Brunei = DictToObj({})
Bulgaria = DictToObj({})
BurkinaFaso = DictToObj({})
Burma = DictToObj({})
Burundi = DictToObj({})
CaboVerde = DictToObj({})
Cambodia = DictToObj({})
Cameroon = DictToObj({})
CentralAfricanRepublic = DictToObj({})
Chad = DictToObj({})
Comoros = DictToObj({})
CongoBrazzaville = DictToObj({})
CongoKinshasa = DictToObj({})
CostaRica = DictToObj({})
CotedIvoire = DictToObj({})
Croatia = DictToObj({})
Cuba = DictToObj({})
Cyprus = DictToObj({})
Czechia = DictToObj({})
DiamondPrincess = DictToObj({})
Djibouti = DictToObj({})
Dominica = DictToObj({})
DominicanRepublic = DictToObj({})
Ecuador = DictToObj({})
Egypt = DictToObj({})
ElSalvador = DictToObj({})
EquatorialGuinea = DictToObj({})
Eritrea = DictToObj({})
Estonia = DictToObj({})
Eswatini = DictToObj({})
Ethiopia = DictToObj({})
Fiji = DictToObj({})
Gabon = DictToObj({})
Gambia = DictToObj({})
Ghana = DictToObj({})
Greece = DictToObj({})
Grenada = DictToObj({})
Guatemala = DictToObj({})
Guinea = DictToObj({})
GuineaBissau = DictToObj({})
Guyana = DictToObj({})
Haiti = DictToObj({})
HolySee = DictToObj({})
Honduras = DictToObj({})
Hungary = DictToObj({})
Indonesia = DictToObj({})
Iran = DictToObj({})
Iraq = DictToObj({})
Israel = DictToObj({})
Jamaica = DictToObj({})
Jordan = DictToObj({})
Kazakhstan = DictToObj({})
Kenya = DictToObj({})
KoreaSouth = DictToObj({})
Kosovo = DictToObj({})
Kuwait = DictToObj({})
Kyrgyzstan = DictToObj({})
Laos = DictToObj({})
Latvia = DictToObj({})
Lebanon = DictToObj({})
Lesotho = DictToObj({})
Liberia = DictToObj({})
Libya = DictToObj({})
Liechtenstein = DictToObj({})
Lithuania = DictToObj({})
Luxembourg = DictToObj({})
MSZaandam = DictToObj({})
Madagascar = DictToObj({})
Malawi = DictToObj({})
Malaysia = DictToObj({})
Maldives = DictToObj({})
Mali = DictToObj({})
Malta = DictToObj({})
Mauritania = DictToObj({})
Mauritius = DictToObj({})
Moldova = DictToObj({})
Monaco = DictToObj({})
Mongolia = DictToObj({})
Montenegro = DictToObj({})
Morocco = DictToObj({})
Mozambique = DictToObj({})
Namibia = DictToObj({})
Nepal = DictToObj({})
NewZealand = DictToObj({})
Nicaragua = DictToObj({})
Niger = DictToObj({})
Nigeria = DictToObj({})
NorthMacedonia = DictToObj({})
Oman = DictToObj({})
Panama = DictToObj({})
PapuaNewGuinea = DictToObj({})
Paraguay = DictToObj({})
Philippines = DictToObj({})
Poland = DictToObj({})
Portugal = DictToObj({})
Qatar = DictToObj({})
Romania = DictToObj({})
Rwanda = DictToObj({})
SaintKittsAndNevis = DictToObj({})
SaintLucia = DictToObj({})
SaintVincentAndTheGrenadines = DictToObj({})
SanMarino = DictToObj({})
SaoTomeAndPrincipe = DictToObj({})
SaudiArabia = DictToObj({})
Senegal = DictToObj({})
Serbia = DictToObj({})
Seychelles = DictToObj({})
SierraLeone = DictToObj({})
Singapore = DictToObj({})
Slovakia = DictToObj({})
Slovenia = DictToObj({})
Somalia = DictToObj({})
SouthAfrica = DictToObj({})
SouthSudan = DictToObj({})
SriLanka = DictToObj({})
Sudan = DictToObj({})
Suriname = DictToObj({})
Syria = DictToObj({})
Taiwan = DictToObj({})
Tajikistan = DictToObj({})
Tanzania = DictToObj({})
Thailand = DictToObj({})
TimorLeste = DictToObj({})
Togo = DictToObj({})
TrinidadAndTobago = DictToObj({})
Tunisia = DictToObj({})
Turkey = DictToObj({})
Uganda = DictToObj({})
UnitedArabEmirates = DictToObj({})
Uruguay = DictToObj({})
Uzbekistan = DictToObj({})
Venezuela = DictToObj({})
Vietnam = DictToObj({})
WestBankAndGaza = DictToObj({})
WesternSahara = DictToObj({})
Yemen = DictToObj({})
Zambia = DictToObj({})
Zimbabwe = DictToObj({})

Alaska = DictToObj({})
Alabama = DictToObj({})
Arkansas = DictToObj({})
AmericanSamoa = DictToObj({})
Arizona = DictToObj({})
California = DictToObj({})
Colorado = DictToObj({})
Connecticut = DictToObj({})
DistrictOfColumbia = DictToObj({})
Delaware = DictToObj({})
Florida = DictToObj({})
Georgia = DictToObj({})
Guam = DictToObj({})
Hawaii = DictToObj({})
Iowa = DictToObj({})
Idaho = DictToObj({})
Illinois = DictToObj({})
Indiana = DictToObj({})
Kansas = DictToObj({})
Kentucky = DictToObj({})
Louisiana = DictToObj({})
Massachusetts = DictToObj({})
Maryland = DictToObj({})
Maine = DictToObj({})
Michigan = DictToObj({})
Minnesota = DictToObj({})
Missouri = DictToObj({})
NorthernMarianaIslands = DictToObj({})
Mississippi = DictToObj({})
Montana = DictToObj({})
NorthCarolina = DictToObj({})
NorthDakota = DictToObj({})
Nebraska = DictToObj({})
NewHampshire = DictToObj({})
NewJersey = DictToObj({})
NewMexico = DictToObj({})
Nevada = DictToObj({})
NewYork = DictToObj({})
Ohio = DictToObj({})
Oklahoma = DictToObj({})
Oregon = DictToObj({})
Pennsylvania = DictToObj({})
PuertoRico = DictToObj({})
RhodeIsland = DictToObj({})
SouthCarolina = DictToObj({})
SouthDakota = DictToObj({})
Tennessee = DictToObj({})
Texas = DictToObj({})
Utah = DictToObj({})
Virginia = DictToObj({})
VirginIslands = DictToObj({})
Vermont = DictToObj({})
Washington = DictToObj({})
Wisconsin = DictToObj({})
WestVirginia = DictToObj({})
Wyoming = DictToObj({})


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


def dataByName(_name):
    _name = re.sub(remove_space, '', _name).upper()
    item = Item(_name)
    item.rtrn_data()
    return item


def dataByNameShort(_name):
    _name = re.sub(remove_space, '', _name).upper()
    item = Item(states[_name].upper())
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


def jsonByName(_name):
    _name = re.sub(remove_space, '', _name).upper()
    item = Item(_name)
    item.rtrn_data()
    return item.json


def jsonByNameShort(_name):
    _name = re.sub(remove_space, '', _name).upper()
    item = Item(states[_name].upper())
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
    globals()[name] = DictToObj(data_dict)

for country in countries:
    name = country
    obj = dataByName(name)
    data_dict = {"deaths": obj.deaths,
                 "cases": obj.cases, "recovered": obj.recovered, "confirmed": obj.cases}
    globals()[re.sub(remove_space, '', name)] = DictToObj(data_dict)

US = DictToObj(us_dict)
Total = DictToObj(total_dict)
