import covid19_data

# example of how to get json by name
# .jsonByName([string of item you want to find, can be any state, country, or total amount (do not use spaces EX: NewYork)])
# object has three useful attributes: .deaths, .cases (.confirmed also works), and .recovered

total = covid19_data.jsonByName("Total")  # create an object for our total data
china = covid19_data.jsonByName("China")
US = covid19_data.jsonByName("US")
new_york = covid19_data.jsonByName("NewYork")
print(total, china, US, new_york)

# example of how to get json by abbreviated name
# .jsonByNameShort([two letter string of item you want to find, can be any state])
# object has three useful attributes: .deaths, .cases (.confirmed also works), and .recovered

texas = covid19_data.jsonByNameShort("TX")  # create an object for our total data
california = covid19_data.jsonByNameShort("CA")
new_york = covid19_data.jsonByNameShort("NY")
print(texas, california, new_york)
