import re

fp = open("/home/panda/Pulpit/sequence.fasta", "r")
full_genome = fp.read()
fp.close()

startCodonsWith10rand = re.findall(".{10}TAC", full_genome)
templist = []
for z in startCodonsWith10rand:
    match = re.match("[ACTG]*(TCCTCC|TCCTTC|TCCTC|TCCTT)[ACTG]*", z)
    if match != None:
        templist.append(match.string)
positions = []
for w in templist:
    x = [m.start() for m in re.finditer(w, full_genome)]
    z.extend(x + len(w))
print(set(z))