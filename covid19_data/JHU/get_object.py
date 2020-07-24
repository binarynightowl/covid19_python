from .get_data import get_all_data, get_data_from_api
from ..dict_as_attribute import DictAsObj as DictToObj


class Items:
    states = {}
    countries = {}
    total = {}
    data = get_data_from_api()

    for entity in data:
        if 'Countries' == entity:
            countries.update(data[entity])
        elif 'States' == entity:
            states.update(data[entity])
        elif 'TOTAL' == entity:
            total.update(data[entity])

    data = {}
    data.update(countries)
    data.update(states)
    data.update({'Total'.upper(): total})

    def __init__(self, s):
        self.fullJSON = self.data
        self.caller = s


class Item(Items):
    def rtrn_item_json(self, name=None):
        self.json = self.fullJSON[self.caller]

    def rtrn_data(self):
        self.rtrn_item_json()
        self._confirmed()
        self._deaths()
        self._recovered()

    def _confirmed(self):
        self.confirmed = self.json['Confirmed']
        self.cases = self.confirmed

    def _deaths(self):
        self.deaths = self.json['Deaths']

    def _recovered(self):
        self.recovered = self.json['Recovered']
