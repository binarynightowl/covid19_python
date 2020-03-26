![Unit Tests](https://github.com/binarynightowl/covid19_python/workflows/Unit%20Tests/badge.svg)

Gets data for CoronaVirus (COVID-19) using John Hopkins' [ArcGIS application layer]                 (https://services1.arcgis.com/0MSEUqKaxRlEPj5g/ArcGIS/rest/services/ncov_cases/FeatureServer) 
using a query to return a JSON document, so unlike similar packages it does not rely on a datasheet that is might not be up to date, but queries the source database directly. This allows us to get the most up to date information that is currently available, as well enabling us to get any of the data we want without any that is not wanted.
