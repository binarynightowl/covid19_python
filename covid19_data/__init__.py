from covid19_data.JHU import dataByCallerName, dataByCallerNameShort, dataByName, dataByNameShort, jsonByCallerName, \
    jsonByCallerNameShort, jsonByName, jsonByNameShort
from covid19_data import JHU

print("The current number of COVID-19 recoveries in the US according to John Hopkins is: " + JHU.US.recovered)
print("The current number of confirmed COVID-19 cases in Texas according to John Hopkins is: " + JHU.Texas.confirmed)
print("The current number of COVID-19 deaths in California according to John Hopkins is: " + JHU.California.deaths)
print("The current number of worldwide COVID-19 deaths according to John Hopkins is: " + JHU.Total.deaths)
