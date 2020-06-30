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
