# COVID19-Data
![Build Status](https://github.com/binarynightowl/covid19_python/workflows/Build%20Status/badge.svg)
<img alt="GitHub issues" src="https://img.shields.io/github/issues/binarynightowl/covid19_python">
<img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/covid19-data?logo=python">
<img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/binarynightowl/covid19_python?logo=github">
<img alt="PyPI" src="https://img.shields.io/pypi/v/covid19-data?label=PyPi&logo=PyPi">
<img alt="GitHub release (latest by date including pre-releases)" src="https://img.shields.io/github/v/release/binarynightowl/covid19_python?include_prereleases&label=pre-release&logo=github">
![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/binarynightowl/covid19_python?include_prereleases&label=pre-release&logo=github&style=plastic)

## Overview
covid19-data is a powerful and easy to use Python client for getting COVID-19 data (*see sources below
for more information on how data is obtained*)
* Uses a fast method of getting data
    * Does not rely on scraping sites, parsing files, or getting (old) data from a repository, so you do not depend on the 
    repository being updated to get up to date data
* Very fast and responsive
    * The client only gets the data once, and parses it into a search friendly format in the backend, so once the data is 
    loaded ( *~* 1 second ), data for the World or any Country/State can be retrieved instantly
* User friendly and simple to implement into your application
* Very flexible and will return the data in multiple forms (*read documentation section for more info*)
    * Can return a object with the data as attributes
    * Can return a JSON document


## Installing
covid19-data can be installed with [pip](https://pypi.org/project/covid19-data/):
```
$ pip install covid19-data
```
Alternatively, you can grab the latest source code from [GitHub](https://github.com/binarynightowl/covid19_python):
```
$ git clone git://github.com/binarynightowl/covid19_python
$ python setup.py install
```


## Documentation

#### Sources
This project utilizes [John Hopkins University](https://coronavirus.jhu.edu/map.html)'s 
[ArcGIS data layer](https://services1.arcgis.com/0MSEUqKaxRlEPj5g/ArcGIS/rest/services/ncov_cases/FeatureServer) 
to get its data. Please follow their terms of service and licensing when using their data in your application. The data layer 
pulls data from the 
following sources:
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
