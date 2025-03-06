import pyinputplus as pyip
breadCost = {'wheat': 1, 'white': 1, 'sourdough': 1.5}
proteinCost = {'chicken': 2, 'turkey': 2, 'ham': 2, 'tofu': 2}
cheeseCost = {'cheddar': 1, 'Swiss': 1, 'mozzarella': 1}
condimentCost = {'mayo': 0.5, 'mustard': 0.5, 'lettuce': 0.5, 'tomato': 0.5}
breadType = pyip.inputMenu(['wheat', 'white', 'sourdough'])
proteinType = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'])
cheese = pyip.inputYesNo(prompt='Do you want cheese?')
if cheese == 'yes':
    cheeseType = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'])
mayo = pyip.inputYesNo(prompt='Do you want mayo?')
mustard = pyip.inputYesNo(prompt='Do you want mustard?')
lettuce = pyip.inputYesNo(prompt='Do you want lettuce?')
tomato = pyip.inputYesNo(prompt='Do you want tomato?')
numSandwiches = pyip.inputInt(prompt='How many sandwiches do you want?', min=1)

print(f'You ordered {numSandwiches} {proteinType} sandwich(es) on {breadType} bread with {"mayo," if mayo == "yes" else ""} {"mustard," if mustard == "yes" else ""} {"lettuce," if lettuce == "yes" else ""} {"tomato." if tomato == "yes" else ""}')

totalCost = numSandwiches * (breadCost[breadType] + proteinCost[proteinType])
if cheese == 'yes':
    totalCost += numSandwiches * cheeseCost[cheeseType]
if mayo == 'yes':
    totalCost += numSandwiches * condimentCost['mayo']
if mustard == 'yes':
    totalCost += numSandwiches * condimentCost['mustard']
if lettuce == 'yes':
    totalCost += numSandwiches * condimentCost['lettuce']
if tomato == 'yes':
    totalCost += numSandwiches * condimentCost['tomato']
print(f'Total cost: ${totalCost}')