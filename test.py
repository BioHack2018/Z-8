import re

def zaqw (genome):
    fp = open(genome, "r")
    full_genome = fp.read()
    fp.close()

    x = re.findall(".{10}TAC", full_genome)
    b=[]
    for z in x:
        v = re.match("[ACTG]*(TCCTCC|TCCTTC|TCCTC|TCCTT)[ACTG]*", z)
        if v != None:
            b.append(v.string)
    z = []
    for w in b:
        x = [m.start() for m in re.finditer(w, full_genome)]
        z.extend(x)
    z = set(z)
    for q in z:
        q = q + 13
    return z
