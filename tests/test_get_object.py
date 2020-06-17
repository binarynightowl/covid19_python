from covid19_data.JHU import get_object
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


def test_Items():
    name = 'Texas'
    object = get_object.Item(name)
    assert object.data == get_data.get_all_data([total_url, countries_url, states_url])
    assert object.fullJSON == get_data.get_all_data([total_url, countries_url, states_url])
    assert name == object.caller


def test_Item():
    total = 'Total'.upper()
    state = 'Texas'.upper()
    country = 'US'.upper()

    data = get_data.get_all_data([total_url, countries_url, states_url])

    Total = get_object.Item(total)
    Total.rtrn_data()
    State = get_object.Item(state)
    State.rtrn_data()
    Country = get_object.Item(country)
    Country.rtrn_data()

    assert Total.deaths == data[total]['Deaths']
    assert State.deaths == data[state]['Deaths']
    assert Country.deaths == data[country]['Deaths']
