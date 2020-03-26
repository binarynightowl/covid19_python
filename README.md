# COVID19-Data
![Build Status](https://github.com/binarynightowl/covid19_python/workflows/Build%20Status/badge.svg)
![GitHub issues](https://img.shields.io/github/issues/binarynightowl/covid19_python)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/covid19-data?style=plastic&logo=python) 
![GitHub release (latest by date)](https://img.shields.io/github/v/release/binarynightowl/covid19_python?logo=github&style=plastic)
![PyPI](https://img.shields.io/pypi/v/covid19-data?label=PyPi&logo=PyPi&style=plastic)
![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/binarynightowl/covid19_python?include_prereleases&label=pre-release&logo=github&style=plastic)


Gets data for CoronaVirus (COVID-19) using John Hopkins' [ArcGIS application layer](https://services1.arcgis.com/0MSEUqKaxRlEPj5g/ArcGIS/rest/services/ncov_cases/FeatureServer) using a query to return a JSON document, so unlike similar packages it does not rely on a datasheet that is might not be up to date, but queries the source database directly. This allows us to get the most up to date information that is currently available, as well enabling us to get any of the data we want without any that is not wanted.


## Sources
This project utilizes [John Hopkins University](https://coronavirus.jhu.edu/map.html)'s 
[ArcGIS data layer](https://services1.arcgis.com/0MSEUqKaxRlEPj5g/ArcGIS/rest/services/ncov_cases/FeatureServer) 
to get its data. The data layer pulls data from the following sources:
- [World Health Organization (WHO)](https://www.who.int/)
- [DXY.cn. Pneumonia. 2020.](http://3g.dxy.cn/newh5/view/pneumonia)
- [BNO News](https://bnonews.com/index.php/2020/02/the-latest-coronavirus-cases/)
- [National Health Commission of the People’s Republic of China (NHC)](http://www.nhc.gov.cn/xcs/yqtb/list_gzbd.shtml)
- [China CDC (CCDC)](http://weekly.chinacdc.cn/news/TrackingtheEpidemic.htm)
- [Hong Kong Department of Health](https://www.chp.gov.hk/en/features/102465.html)
- [Macau Government](https://www.ssm.gov.mo/portal/)
- [Taiwan CDC](https://sites.google.com/cdc.gov.tw/2019ncov/taiwan?authuser=0)
- [US CDC](https://www.cdc.gov/coronavirus/2019-ncov/index.html)
- [Government of Canada](https://www.canada.ca/en/public-health/services/diseases/coronavirus.html)
- [Australia Government Department of Health](https://www.health.gov.au/news/coronavirus-update-at-a-glance)
- [European Centre for Disease Prevention and Control (ECDC)](https://www.ecdc.europa.eu/en/geographical-distribution-2019-ncov-cases)
- [Ministry of Health Singapore (MOH)](https://www.moh.gov.sg/covid-19)
- [Italy Ministry of Health](http://www.salute.gov.it/nuovocoronavirus)
