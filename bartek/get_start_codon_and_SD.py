import re

def get_start_codon_and_SD (genome):
    fp = open(genome, "r")
    full_genome = fp.read()
    fp.close()

    ten_and_start = re.findall(".{10}TAC", full_genome)
    ready_sequences_to_search=[]
    for match in ten_and_start:
        supplement_match = re.match("[ACTG]*(TCCTCC|TCCTTC|TCCTC|TCCTT)[ACTG]*", match)
        if supplement_match != None:
            ready_sequences_to_search.append(supplement_match.string)
    positions = []
    for sequence in ready_sequences_to_search:
        position = [m.start() for m in re.finditer(sequence, full_genome)]
        positions.extend(position)
    positions = set(positions)
    for q in positions:
        #position have to start from codon start
        q = q + 13
    return positions
