from covid19_data import JHU

# data can now be retrieved by [Organization providing data].[Entity to get data for].[Data that you wish to retrieve]
# for example to get data from John Hopkins University, follow the following examples
print(JHU.US.recovered)
print(JHU.TX.confirmed)
print(JHU.CA.deaths)