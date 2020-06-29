from covid19_data import JHU

# data can now be retrieved by [Organization providing data].[Entity to get data for].[Data that you wish to retrieve]
# for example to get data from John Hopkins University, follow the following examples

print("The current number of COVID-19 recoveries in the US according to John Hopkins is: " + str(JHU.US.recovered))
print("The current number of confirmed COVID-19 cases in Texas according to John Hopkins is: " + str(JHU.Texas.confirmed))
print("The current number of COVID-19 deaths in California according to John Hopkins is: " + str(JHU.California.deaths))
print("The current number of worldwide COVID-19 deaths according to John Hopkins is: " + str(JHU.Total.deaths))
print("The current number of COVID-19 deaths in China according to John Hopkins is: " + str(JHU.China.deaths))
print("The current number of COVID-19 deaths in China according to John Hopkins is: " + str(JHU.UnitedKingdom.deaths))