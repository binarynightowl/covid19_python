import json
import urllib.request
import re

document = {
}


def get_data(url):
    req_headers = {'User-Agent': 'COVID19-Data'}
    req = urllib.request.Request(url, None, req_headers)
    data = json.loads(urllib.request.urlopen(req).read().decode())
    doc = data['features']
    return doc


def get_all_data(links_list):
    remove_space = re.compile('[^a-zA-Z]')
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


def get_data_from_api():
    req_headers = {'User-Agent': 'COVID19-Data'}
    req = urllib.request.Request('https://api.bnry.host/covid19-data', None, req_headers)
    data = json.loads(urllib.request.urlopen(req).read().decode())
    return data
