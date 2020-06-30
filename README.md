# COVID19-Data
![Build Status](https://github.com/binarynightowl/covid19_python/workflows/Build%20Status/badge.svg)
<img alt="GitHub issues" src="https://img.shields.io/github/issues/binarynightowl/covid19_python">
<img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/covid19-data?logo=python">
<img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/binarynightowl/covid19_python?logo=github">
<img alt="PyPI" src="https://img.shields.io/pypi/v/covid19-data?label=PyPi&logo=PyPi">
<img alt="GitHub release (latest by date including pre-releases)" src="https://img.shields.io/github/v/release/binarynightowl/covid19_python?include_prereleases&label=pre-release&logo=github">

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
    * Can return data as a "Class Style Object" with attributes (*only requires one line of code, and is super easy to
     read!*)
    * Can return an object with the data as attributes
    * Can return a JSON document
* Super simplistic and lightweight and does not rely on any external python packages


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


# Documentation

## Usage
There are multiple ways of getting data with covid19-data
1. Object/parameter style retrieval
    * Gets the data by calling the class of the desired information source and the statistics for any location. *As of now, only John Hopkins University
     (__JHU__) is
     supported but in
     a future release, multiple sources will be supported*.
      ```python
      from covid19_data import JHU
    
      # Format: <Data Source>.<Location>.<Statistic>
      # For example to get data from John Hopkins University, review the following example:
      # JHU.China.deaths
        
      print("The number of COVID-19 recoveries in the US: " + str(JHU.US.recovered))
      print("The number of confirmed COVID-19 cases in Texas: " + str(JHU.Texas.confirmed))
      print("The number of COVID-19 deaths in California: " + str(JHU.California.deaths))
      print("The number of worldwide COVID-19 deaths: " + str(JHU.Total.deaths))
      print("The number of COVID-19 deaths in China: " + str(JHU.China.deaths))
      print("The number of COVID-19 deaths in UK: " + str(JHU.UnitedKingdom.deaths))
        ```
        Sample Output:
        ```
        The number of COVID-19 recoveries in the US : 685164
        The number of confirmed COVID-19 cases in Texas : 150851
        The number of COVID-19 deaths in California : 5935
        The number of worldwide COVID-19 deaths : 502947
        The number of COVID-19 deaths in China : 4641
        The number of COVID-19 recoveries in the United Kingdom : 1364
        ```
      
2. As an object with attributes of COVID data
    * Get the data by name (*note: spacing and capitalization do not matter, EX: `total = covid19_data.dataByName("New 
    York")`, 
    `total = covid19_data.dataByName("newyork")`, and `total = covid19_data.dataByName("NEW YORK")` are all interchangable*)
        ```python
        import covid19_data
    
        # example of how to get data by name
        # .dataByName([string of item to find: any state, country, or total amount (spacing and capitalization do not matter)])
        # object has three useful attributes: .deaths, .cases (.confirmed also works), and .recovered
        
        total = covid19_data.dataByName("Total")    # create an object for our total data
        china = covid19_data.dataByName("China")
        US = covid19_data.dataByName("US")
        new_york = covid19_data.dataByName("NewYork")
        print(total.deaths, china.recovered, US.cases)
        ```
        Sample Output:
        ```
        22184 74181 69246
        ```
    * Get the data by abbreviation (*note: spacing and capitalization do not matter, EX: `total = covid19_data.dataByName("New 
    York")`, 
    `total = covid19_data.dataByName("newyork")`, and `total = covid19_data.dataByName("NEW YORK")` are all interchangable*)
        ```python
        import covid19_data        
        
        # example of how to get data by abbreviated name
        # .dataByNameShort([two letter string of item you want to find, can be any state])
        # object has three useful attributes: .deaths, .cases (.confirmed also works), and .recovered
        
        texas = covid19_data.dataByNameShort("TX")    # create an object for our total data
        california = covid19_data.dataByNameShort("CA")
        new_york = covid19_data.dataByNameShort("NY")
        print(texas.cases, california.deaths, new_york.cases)
        ```
        Sample Output:
        ```
        1353 67 33033
        ```
3. As a JSON document 
    * Get the json by name (*note: spacing and capitalization do not matter, EX: `total = covid19_data.dataByName("New 
    York")`, 
    `total = covid19_data.dataByName("newyork")`, and `total = covid19_data.dataByName("NEW YORK")` are all interchangable*)
        ```python
        import covid19_data
        
        # example of how to get json by name
        # .jsonByName([string of item you want to find, can be any state, country, or total amount (spacing and capitalization do not matter)])
        # object has three useful attributes: .deaths, .cases (.confirmed also works), and .recovered
        
        total = covid19_data.jsonByName("Total")    # create an object for our total data
        china = covid19_data.jsonByName("China")
        US = covid19_data.jsonByName("US")
        new_york = covid19_data.jsonByName("NewYork")
        print(total, china, US, new_york)
        ```
        Sample Output::
        ```
        {'Confirmed': 492603, 'Deaths': 22184, 'Recovered': 119918}
        {'Confirmed': 81782, 'Deaths': 3291, 'Recovered': 74181, 'Active': 4310}
        {'Confirmed': 69246, 'Deaths': 1046, 'Recovered': 619, 'Active': 0}
        {'Confirmed': 33033, 'Deaths': 366, 'Recovered': 0, 'Active': 0}
        ```
    * Get the json by abbreviation (*note: spacing and capitalization do not matter, EX: `total = covid19_data.dataByName("New 
    York")`, 
    `total = covid19_data.dataByName("newyork")`, and `total = covid19_data.dataByName("NEW YORK")` are all interchangable*)
        ```python
        import covid19_data
        
        # example of how to get json by abbreviated name
        # .jsonByNameShort([two letter string of item you want to find, can be any state])
        # object has three useful attributes: .deaths, .cases (.confirmed also works), and .recovered
        
        texas = covid19_data.jsonByNameShort("TX")    # create an object for our total data
        california = covid19_data.jsonByNameShort("CA")
        new_york = covid19_data.jsonByNameShort("NY")
        print(texas, california, new_york)
        ```
        Sample Output::
        ```
        {'Confirmed': 1353, 'Deaths': 17, 'Recovered': 0, 'Active': 0}
        {'Confirmed': 3172, 'Deaths': 67, 'Recovered': 0, 'Active': 0}
        {'Confirmed': 33033, 'Deaths': 366, 'Recovered': 0, 'Active': 0}
        ```
  
#### Sources
This package utilizes [John Hopkins University's](https://coronavirus.jhu.edu/map.html) [ArcGIS data layer](https://services1.arcgis.com/0MSEUqKaxRlEPj5g/ArcGIS/rest/services/ncov_cases/FeatureServer) 
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
