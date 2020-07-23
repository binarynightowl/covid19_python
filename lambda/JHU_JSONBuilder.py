import json
import urllib.request
import re


def get_data(url):
    return json.loads(
        urllib.request.urlopen(urllib.request.Request(url, None, {'User-Agent': 'COVID19-Data'})).read().decode())['features']


def get_all_data(links_list):
    document = {'Countries': {},
                'States': {}
                }
    for link in links_list:
        for item in get_data(link):
            if 'Country_Region' in item['attributes'].keys():
                country = re.sub(re.compile('[^a-zA-Z]'), '', item['attributes']['Country_Region'])
                item['attributes'].pop('Country_Region', None)
                document['Countries'].update({country.upper(): item['attributes']})
            elif 'Province_State' in item['attributes'].keys():
                stateprov = re.sub(re.compile('[^a-zA-Z]'), '', item['attributes']['Province_State'])
                item['attributes'].pop('Province_State', None)
                document['States'].update({stateprov.upper(): item['attributes']})
            else:
                document.update({'TOTAL': item['attributes']})

    return document


def lambda_handler(event, context):
    return get_all_data([
        'https://services1.arcgis.com/0MSEUqKaxRlEPj5g/ArcGIS/rest/services/Coronavirus_2019_nCoV_Cases/FeatureServer/1'
        '/query?where=1%3D1&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRel'
        'Intersects&resultType=none&distance=0.0&units=esriSRUnit_Meter&returnGeodetic=false&outFields=&returnGeometry='
        'true&featureEncoding=esriDefault&multipatchOption=xyFootprint&maxAllowableOffset=&geometryPrecision=&outSR='
        '&datumTransformation=&applyVCSProjection=false&returnIdsOnly=false&returnUniqueIdsOnly=false&returnCountOnly='
        'false&returnExtentOnly=false&returnQueryGeometry=false&returnDistinctValues=false&cacheHint=false&orderByFields='
        '&groupByFieldsForStatistics=&outStatistics=%5B%7B%22statisticType%22%3A%22sum%22%2C%22onStatisticField%22%3A%'
        '22Confirmed%22%2C%22outStatisticFieldName%22%3A%22Confirmed%22%7D%2C%7B%22statisticType%22%3A%22sum%22%2C%'
        '22onStatisticField%22%3A%22Deaths%22%2C%22outStatisticFieldName%22%3A%22Deaths%22%7D%2C%7B%22statisticType%'
        '22%3A%22sum%22%2C%22onStatisticField%22%3A%22Recovered%22%2C%22outStatisticFieldName%22%3A%22Recovered%22%7D%'
        '5D&having=&resultOffset=&resultRecordCount=&returnZ=false&returnM=false&returnExceededLimitFeatures='
        'true&quantizationParameters=&sqlFormat=none&f=pjson&token=',
        'https://services1.arcgis.com/0MSEUqKaxRlEPj5g/ArcGIS/rest/services/ncov_cases/FeatureServer/2/query?where=1%3D1'
        '&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&resultT'
        'ype=none&distance=0.0&units=esriSRUnit_Meter&returnGeodetic=false&outFields=+Country_Region%2C+confirmed%2C+dea'
        'ths%2C+recovered%2C+active&returnGeometry=false&featureEncoding=esriDefault&multipatchOption=xyFootprint&maxAll'
        'owableOffset=&geometryPrecision=&outSR=&datumTransformation=&applyVCSProjection=false&returnIdsOnly=false&retur'
        'nUniqueIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&returnQueryGeometry=false&returnDistinctValue'
        's=false&cacheHint=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&having=&resultOffset=&resultR'
        'ecordCount=&returnZ=false&returnM=false&returnExceededLimitFeatures=true&quantizationParameters=&sqlFormat=none'
        '&f=pjson&token= ',
        'https://services1.arcgis.com/0MSEUqKaxRlEPj5g/ArcGIS/rest/services/ncov_cases/FeatureServer/1/query?where'
        '=Country_Region=%27US%27&outFields=Province_State,confirmed,deaths,recovered,%20active&resultRecordCount=200&f'
        '=pjson'
    ])
