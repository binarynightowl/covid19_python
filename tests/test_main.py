import covid19_data
from covid19_data.JHU import get_data

total_url = 'https://services1.arcgis.com/0MSEUqKaxRlEPj5g/ArcGIS/rest/services/Coronavirus_2019_nCoV_Cases' \
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
countries_url = 'https://services1.arcgis.com/0MSEUqKaxRlEPj5g/ArcGIS/rest/services/ncov_cases/FeatureServer/2/query?where=1' \
                '%3D1&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects' \
                '&resultType=none&distance=0.0&units=esriSRUnit_Meter&returnGeodetic=false&outFields=+Country_Region%2C' \
                '+confirmed%2C+deaths%2C+recovered%2C+active&returnGeometry=false&featureEncoding=esriDefault' \
                '&multipatchOption=xyFootprint&maxAllowableOffset=&geometryPrecision=&outSR=&datumTransformation' \
                '=&applyVCSProjection=false&returnIdsOnly=false&returnUniqueIdsOnly=false&returnCountOnly=false' \
                '&returnExtentOnly=false&returnQueryGeometry=false&returnDistinctValues=false&cacheHint=false&orderByFields' \
                '=&groupByFieldsForStatistics=&outStatistics=&having=&resultOffset=&resultRecordCount=&returnZ=false&returnM' \
                '=false&returnExceededLimitFeatures=true&quantizationParameters=&sqlFormat=none&f=pjson&token= '
states_url = 'https://services1.arcgis.com/0MSEUqKaxRlEPj5g/ArcGIS/rest/servi' \
             'ces/ncov_cases/FeatureServer/1/query?where' \
             '=Country_Region=%27US%27&outFields=Province_State,confirmed,deaths,recovered,' \
             '%20active&resultRecordCount=200&f=pjson'


def test_dataByName():
    Texas = covid19_data.dataByName("TeXaS")
    Total = covid19_data.dataByName("tOtAl")
    China = covid19_data.dataByName("ChInA")
    data = get_data.get_all_data([total_url, countries_url, states_url])
    assert Total.deaths == data['Total'.upper()]['Deaths']
    assert Texas.deaths == data['Texas'.upper()]['Deaths']
    assert China.deaths == data['China'.upper()]['Deaths']


def test_dataByNameShort():
    Texas = covid19_data.dataByNameShort("Tx")
    California = covid19_data.dataByNameShort("CA")
    NewYork = covid19_data.dataByNameShort("nY")
    data = get_data.get_all_data([total_url, countries_url, states_url])
    assert California.deaths == data['California'.upper()]['Deaths']
    assert Texas.deaths == data['Texas'.upper()]['Deaths']
    assert NewYork.deaths == data['NewYork'.upper()]['Deaths']


def test_jsonByName():
    Texas = covid19_data.jsonByName("TeXaS")
    Total = covid19_data.jsonByName("tOtAl")
    China = covid19_data.jsonByName("ChInA")
    data = get_data.get_all_data([total_url, countries_url, states_url])
    assert Total == data['Total'.upper()]
    assert Texas == data['Texas'.upper()]
    assert China == data['China'.upper()]


def test_jsonByNameShort():
    Texas = covid19_data.jsonByNameShort("Tx")
    California = covid19_data.jsonByNameShort("CA")
    NewYork = covid19_data.jsonByNameShort("nY")
    data = get_data.get_all_data([total_url, countries_url, states_url])
    assert California == data['California'.upper()]
    assert Texas == data['Texas'.upper()]
    assert NewYork == data['NewYork'.upper()]


def test_dataByName_spaces():
    NewYork1 = covid19_data.dataByName("new york")
    NewYork2 = covid19_data.dataByName("New York")
    NewYork3 = covid19_data.dataByName("NEWYORK")
    data = get_data.get_all_data([total_url, countries_url, states_url])
    assert NewYork1.deaths == data['NewYork'.upper()]['Deaths']
    assert NewYork2.deaths == data['NewYork'.upper()]['Deaths']
    assert NewYork3.deaths == data['NewYork'.upper()]['Deaths']


def test_jsonByName_spaces():
    NewYork1 = covid19_data.jsonByName("new york")
    NewYork2 = covid19_data.jsonByName("New York")
    NewYork3 = covid19_data.jsonByName("NEWYORK")
    data = get_data.get_all_data([total_url, countries_url, states_url])
    assert NewYork1 == data['NewYork'.upper()]
    assert NewYork2 == data['NewYork'.upper()]
    assert NewYork3 == data['NewYork'.upper()]
