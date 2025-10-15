#

#A population can be modeled by the following:
#future population = (current population)*(1+r)^(time in years) 
#Have the user enter the current population, the rate of growth as a decimal and the number of DAYS.
#Calculate the expected future population

#Enter the population: 25000000
#Enter the rate of growth in percent: 2.1
#Enter the number of days: 12
#There will be 25017087 people after 12 days

currentpop = input("enter the current population")
rate = input("enter the rate of growth in percent")
days = input("enter the number of days")

currentpop = int(currentpop)
rate = float(rate)
days = int(days)

rate = rate/100 
years = days/365

futurepopulation = (currentpop)*(1+rate)**years
print(f"the future population is {futurepopulation}")