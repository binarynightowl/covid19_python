from covid19_data.JHU import get_data
import json, urllib.request

test_url = 'https://services1.arcgis.com/0MSEUqKaxRlEPj5g/ArcGIS/rest/services/Coronavirus_2019_nCoV_Cases' \
           '/FeatureServer/1/query?where=1%3D1&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR' \
           '=&spatialRel=esriSpatialRelIntersects&resultType=none&distance=0.0&units=esriSRUnit_Meter&returnGeodetic' \
           '=false&outFields=&returnGeometry=true&featureEncoding=esriDefault&multipatchOption=xyFootprint' \
           '&maxAllowableOffset=&geometryPrecision=&outSR=&datumTransformation=&applyVCSProjection=false&returnIdsOnly' \
           '=false&returnUniqueIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&returnQueryGeometry=false' \
           '&returnDistinctValues=false&cacheHint=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=%5B%7B' \
           '%22statisticType%22%3A%22sum%22%2C%22onStatisticField%22%3A%22Confirmed%22%2C%22outStatisticFieldName%22%3A' \
           '%22Confirmed%22%7D%2C%7B%22statisticType%22%3A%22sum%22%2C%22onStatisticField%22%3A%22Deaths%22%2C' \
           '%22outStatisticFieldName%22%3A%22Deaths%22%7D%2C%7B%22statisticType%22%3A%22sum%22%2C%22onStatisticField%22' \
           '%3A%22Recovered%22%2C%22outStatisticFieldName%22%3A%22Recovered%22%7D%5D&having=&resultOffset' \
           '=&resultRecordCount=&returnZ=false&returnM=false&returnExceededLimitFeatures=true&quantizationParameters' \
           '=&sqlFormat=none&f=pjson&token='


def test_get_data():
    data = get_data.get_data(test_url)[0]['attributes']['Confirmed']
    test_data = json.loads(urllib.request.urlopen(test_url).read().decode())['features'][0]['attributes']['Confirmed']
    assert data == test_data


def test_get_all_data():
    data = get_data.get_all_data([test_url])['Total'.upper()]['Confirmed']
    test_data = json.loads(urllib.request.urlopen(test_url).read().decode())['features'][0]['attributes']['Confirmed']
    assert data == test_data  # test comment
