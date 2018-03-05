#EtaP.Mainfile
#Written by: Alexis Renderos

foodData = open('EtaPData.txt', 'r')
stateData = open('StateData.txt', 'r')


# INPUTS GO HERE

# 13 is Illinois
# 43 is Texas
targetState = 43

useablePercentage = 75 # 0.001

# Target year can only be 2013
targetYear = 2013


# TEST DATA
# Year 2013


# ACTUAL VARIABLES GO HERE

eta_f = 0.0

useableRatio = useablePercentage / 100.0

nutritionIndex = 0.0

countryPopulation = 316200000.0

insecurePopulationRatio = 0.0

wasteConstantGrains = 22.74 / 100.0
wasteConstantRoots = 17.08 / 100.0
wasteConstantOilseed = 3.31 / 100.0
wasteConstantFruitVeg = 18.54 / 100.0
wasteConstantMeat = 9.58 / 100.0
wasteConstantFishSea = 24.71 / 100.0
wasteConstantMilk = 12.91 / 100.0

grains = 0.0
fish = 0.0
roots = 0.0
oilseed = 0.0
milk = 0.0
fruitveg = 0.0
meat = 0.0

wasteProductionConstantOne = 0.5
wasteProductionConstantTwo = 0.3
wasteProductionConstantThr = 0.2

dietaryNeedsPerYear = 0.15695 # something something kilograms

foodProduction = []
stateRatios = []

for line in foodData:
	foodProduction.append(line.split())

for line in stateData:
	stateRatios.append(line.split())

i = 0
k = 0

while i < len(stateRatios):
	if ((i + 1) == targetState):
		insecurePopulationRatio = (float(''.join(stateRatios[i])) / float(100.0))
		print(insecurePopulationRatio)
	i += 1

grains = float(''.join(foodProduction[0]))
fish = float(''.join(foodProduction[1]))
roots = float(''.join(foodProduction[2]))
oilseed = float(''.join(foodProduction[3]))
milk = float(''.join(foodProduction[4]))
fruitveg = float(''.join(foodProduction[5]))
meat = float(''.join(foodProduction[6]))

#print(grains)
#print(fish)
#print(roots)
#print(oilseed)
#print(milk)
#print(fruitveg)
#print(meat)

nutritionIndex = (wasteProductionConstantOne * ((wasteConstantGrains * grains) + (wasteConstantRoots * roots) + (wasteConstantFruitVeg * fruitveg)))
nutritionIndex += (wasteProductionConstantTwo * (wasteConstantOilseed * oilseed))
nutritionIndex += (wasteProductionConstantThr * ((wasteConstantMilk * milk) + (wasteConstantMeat * meat) + (wasteConstantFishSea * fish)))
#print((wasteProductionConstantOne * (grains + roots + fruitveg)))
#print((wasteProductionConstantTwo * (oilseed)))
#print((wasteProductionConstantThr * (milk + meat + fish)))
#print(nutritionIndex)
# we mult by 1000 to get eta in kgs
eta_f = ((useableRatio * (nutritionIndex/countryPopulation)) / (insecurePopulationRatio)) * 1000.0

print(eta_f)

print(((eta_f - dietaryNeedsPerYear) > 0))

print(eta_f / dietaryNeedsPerYear)