import random, os
from typing import Hashable

guardians = 60000

slot = []
rarity = []
for filename in os.listdir("./traits"):
    with open(os.path.join("./traits", filename), 'r') as f:
        lines = f.readlines()
        traits = []
        odds = []
        for line in lines:
            line = line.split(",")
            if (line[0] == ''):
                traits.append(str(line[1]))
                odds.append(float(line[2].strip()))
        slot.append(traits)
        rarity.append(odds)


items = []
for x in range(len(slot)):
    items.append(random.choices(slot[x],rarity[x],k=guardians))

all = []
for x in range(guardians):
    each = []
    for y in items:
        each.append(y[x])
    all.append(each)

all.sort()

count = 1
final = {}
with open("generated.txt", "w") as results:
    for item in all:
        line = ", ".join(item)
        if line not in final:
            final[line] = True
            results.write(str(count) + ": " + line + "\n")
            count += 1

# Open the file
# Read each trait category into an array
# create an array of traits for each category
# create a matching array of probabilities for each trait
# determine number to generate
# iterate over category array
# generate total traits by slot 
# combine traits by index into single array
# sort by trait
# print to file