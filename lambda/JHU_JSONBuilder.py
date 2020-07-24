import json
import urllib.request
import re
from threading import Thread
import os

doc = {}


def get_data(url):
    return json.loads(
        urllib.request.urlopen(urllib.request.Request(url, None, {'User-Agent': os.environ['useragent']})).read().decode())[
        'features']


def get_state(
        link='https://services1.arcgis.com/0MSEUqKaxRlEPj5g/ArcGIS/rest/services/ncov_cases/FeatureServer/1/query?where=Count'
             'ry_Region=%27US%27&outFields=Province_State,confirmed,deaths,recovered,%20active&resultRecordCount=200&f=pjson'):
    document = {'States': {}
                }
    for item in get_data(link):
        if 'Province_State' in item['attributes'].keys():
            stateprov = re.sub(re.compile('[^a-zA-Z]'), '', item['attributes']['Province_State'])
            del item['attributes']['Province_State']
            document['States'].update({stateprov.upper(): item['attributes']})
        else:
            pass
    doc.update(document)


def get_country(
        link='https://services1.arcgis.com/0MSEUqKaxRlEPj5g/ArcGIS/rest/services/ncov_cases/FeatureServer/2/query?where=1%3D1'
             '&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&resultT'
             'ype=none&distance=0.0&units=esriSRUnit_Meter&returnGeodetic=false&outFields=+Country_Region%2C+confirmed%2C+dea'
             'ths%2C+recovered%2C+active&returnGeometry=false&featureEncoding=esriDefault&multipatchOption=xyFootprint&maxAll'
             'owableOffset=&geometryPrecision=&outSR=&datumTransformation=&applyVCSProjection=false&returnIdsOnly=false&retur'
             'nUniqueIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&returnQueryGeometry=false&returnDistinctValue'
             's=false&cacheHint=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&having=&resultOffset=&resultR'
             'ecordCount=&returnZ=false&returnM=false&returnExceededLimitFeatures=true&quantizationParameters=&sqlFormat=none'
             '&f=pjson&token='):
    document = {'Countries': {},
                }
    for item in get_data(link):
        if 'Country_Region' in item['attributes'].keys():
            country = re.sub(re.compile('[^a-zA-Z]'), '', item['attributes']['Country_Region'])
            del item['attributes']['Country_Region']
            document['Countries'].update({country.upper(): item['attributes']})
        else:
            pass
    doc.update(document)


def get_total(
        link='https://services1.arcgis.com/0MSEUqKaxRlEPj5g/ArcGIS/rest/services/Coronavirus_2019_nCoV_Cases/FeatureServer/1/'
             'query?where=1%3D1&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelI'
             'ntersects&resultType=none&distance=0.0&units=esriSRUnit_Meter&returnGeodetic=false&outFields=&returnGeometry=tr'
             'ue&featureEncoding=esriDefault&multipatchOption=xyFootprint&maxAllowableOffset=&geometryPrecision=&outSR=&datum'
             'Transformation=&applyVCSProjection=false&returnIdsOnly=false&returnUniqueIdsOnly=false&returnCountOnly=false&re'
             'turnExtentOnly=false&returnQueryGeometry=false&returnDistinctValues=false&cacheHint=false&orderByFields=&groupB'
             'yFieldsForStatistics=&outStatistics=%5B%7B%22statisticType%22%3A%22sum%22%2C%22onStatisticField%22%3A%22Confirm'
             'ed%22%2C%22outStatisticFieldName%22%3A%22Confirmed%22%7D%2C%7B%22statisticType%22%3A%22sum%22%2C%22onStatisticF'
             'ield%22%3A%22Deaths%22%2C%22outStatisticFieldName%22%3A%22Deaths%22%7D%2C%7B%22statisticType%22%3A%22sum%22%2C%'
             '22onStatisticField%22%3A%22Recovered%22%2C%22outStatisticFieldName%22%3A%22Recovered%22%7D%5D&having=&resultOff'
             'set=&resultRecordCount=&returnZ=false&returnM=false&returnExceededLimitFeatures=true&quantizationParameters=&sq'
             'lFormat=none&f=pjson&token='):
    document = {}
    for item in get_data(link):
        if 'Country_Region' not in item['attributes'].keys() and 'Province_State' not in item['attributes'].keys():
            document.update({'TOTAL': item['attributes']})
        else:
            pass
    doc.update(document)


def lambda_handler(event, context):
    t1 = Thread(target=get_state)
    t2 = Thread(target=get_country)
    t3 = Thread(target=get_total)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    return doc
