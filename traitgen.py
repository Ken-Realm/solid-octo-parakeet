import random, os

guardians = 12000

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

#all.sort()

count = 1
final = {}
ranks = {}
level = {}
hud = {}
skin = {}
weapons = {}

if os.path.exists("./generated.txt"):
  os.remove("./generated.txt")

with open("./generated.txt", "w+") as results:
    for item in all:
        line = ", ".join(item)
        if line not in final:
            final[line] = True
            results.write(str(count) + ": " + line + "\n")
            count += 1

            if item[0] in ranks:
                ranks[item[0]] +=1
            else:
                ranks[item[0]] = 1

            if item[1] in skin:
                skin[item[1]] += 1
            else:
                skin[item[1]] = 1

            if item[2] in level:
                level[item[2]] += 1
            else:
                level[item[2]] = 1

            if item[3] in hud:
                hud[item[3]] += 1
            else:
                hud[item[3]] = 1

            if item[4] in weapons:
                weapons[item[4]] += 1
            else:
                weapons[item[4]] = 1
    
    for key in sorted(ranks.keys()):
        ranks[key] = ranks[key]/100
    for key in sorted(skin.keys()):
        skin[key] = skin[key]/100
    for key in sorted(level.keys()):
        level[key] = level[key]/100
    for key in sorted(hud.keys()):
        hud[key] = hud[key]/100
    for key in sorted(weapons.keys()):
        weapons[key] = weapons[key]/100

    results.seek(0,0)
    content=results.read()
    results.seek(0,0)
    results.write(str(ranks).rstrip('\r\n') + '\n')
    results.write(str(skin).rstrip('\r\n') + '\n')
    results.write(str(level).rstrip('\r\n') + '\n')
    results.write(str(hud).rstrip('\r\n') + '\n')
    results.write(str(weapons).rstrip('\r\n') + '\n' + content)

print(count)



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