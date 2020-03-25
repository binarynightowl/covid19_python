import json
import urllib.request

document = {
}

used_id = {
}


def get_data(url):
    data = json.loads(urllib.request.urlopen(url).read().decode())
    doc = data['features']  # remove headers and return just the data
    return doc


def get_all_data(links_list):
    test_val = 0
    for link in links_list:
        doc = get_data(link)
        for item in doc:
            if 'confirmed' in item['attributes'].keys():
                attributes = item['attributes']
                document.update({'Total': attributes})
                used_id.update()
            elif 'Country_Region' in item['attributes'].keys():
                attributes = item['attributes']
                country = attributes['Country_Region']
                attributes.pop('Country_Region', None)
                document.update({country: attributes})
            elif 'Province_State' in item['attributes'].keys():
                attributes = item['attributes']
                stateprov = attributes['Province_State']
                attributes.pop('Province_State', None)
                document.update({stateprov: attributes})
            else:
                attributes = item['attributes']
                name = "unclassified"
                document.update({name: attributes})

    return document
