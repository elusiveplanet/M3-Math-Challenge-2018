#EtaP.Mainfile
#Written by: Alexis Renderos

data = open('EtaPData.txt', 'r')
stateData = open('StateData.txt', 'r')

useableRatio = 0.75

nutritionIndex = 0.0

countryPopulation = 326023584.0

insecurePopulationRatio = 0.0

grains = 0.0
fish = 0.0
roots = 0.0
oilseed = 0.0
milk = 0.0
fruits = 0.0
meat = 0.0

wasteProductionConstantOne = 0.5
wasteProductionConstantTwo = 0.3
wasteProductionConstantThr = 0.2

dietaryNeedsPerYear = 0.15695 # something something kilograms

stateRatios = []

for line in stateData:
	stateRatios.append(line.split())

i = 0
k = 0

while i < len(stateRatios):
	#this grabs the current line
	print(str(i + 1) + " " + stateRatios[i][0])
	i += 1