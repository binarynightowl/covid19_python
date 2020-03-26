import json
import urllib.request
import re

document = {
}


def get_data(url):
    data = json.loads(urllib.request.urlopen(url).read().decode())
    doc = data['features']  # remove headers and return just the data
    return doc


def get_all_data(links_list):
    remove_space = re.compile(r'\s+')
    for link in links_list:
        doc = get_data(link)
        for item in doc:
            if 'Country_Region' in item['attributes'].keys():
                attributes = item['attributes']
                country = re.sub(remove_space, '', attributes['Country_Region']).upper()
                attributes.pop('Country_Region', None)
                document.update({country: attributes})
            elif 'Province_State' in item['attributes'].keys():
                attributes = item['attributes']
                stateprov = re.sub(remove_space, '', attributes['Province_State']).upper()
                attributes.pop('Province_State', None)
                document.update({stateprov: attributes})
            else:
                attributes = item['attributes']
                name = "Total".upper()
                document.update({name: attributes})

    return document
