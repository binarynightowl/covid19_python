import covid19_data

# example of how to get data by name
# .dataByName([string of item you want to find, can be any state, country, or total amount (do not use spaces EX: NewYork)])
# object has three useful attributes: .deaths, .cases (.confirmed also works), and .recovered

total = covid19_data.dataByName("Total")  # create an object for our total data
china = covid19_data.dataByName("China")
US = covid19_data.dataByName("US")
new_york = covid19_data.dataByName("NewYork")
print(total.deaths, china.recovered, US.cases)

# example of how to get data by abbreviated name
# .dataByNameShort([two letter string of item you want to find, can be any state])
# object has three useful attributes: .deaths, .cases (.confirmed also works), and .recovered

texas = covid19_data.dataByNameShort("TX")  # create an object for our total data
california = covid19_data.dataByNameShort("CA")
new_york = covid19_data.dataByNameShort("NY")
print(texas.cases, california.deaths, new_york.cases)
