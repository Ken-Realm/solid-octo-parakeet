import random, os

guardians = 999

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
with open("generated.txt", "w") as results:
    for list in all:
        results.write(str(count) + ": " + ", ".join(list) + "\n")
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