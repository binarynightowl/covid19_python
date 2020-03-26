from .get_data import get_all_data


class Items:
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
    data = get_all_data([total_url, countries_url, states_url])

    def __init__(self, s):
        self.URLS = self.states_url
        self.fullJSON = self.data
        self.caller = s


class Item(Items):
    def rtrn_item_json(self, name=None):
        json = self.fullJSON[self.caller]
        self.json = json

    def rtrn_dat(self):
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
