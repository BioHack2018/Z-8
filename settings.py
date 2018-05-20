#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import test


#file opening
os.getcwd()
#path = input("Please provide a path to genome-containing directory:\n")
#os.chdir(path)
    
#file_name = input("Provide a file name")


fp = open("/home/panda/Pulpit/sequence.fasta", "r")
full_genome = fp.read()
fp.close()


end = full_genome.find("\n")

#extracting a header and trimming a file

if (full_genome[1] == ""):
    
    start = 2
    
else:
    start = 1
    
    
    
header = full_genome[start:end]
full_genome = full_genome[end+1:]


#removing blank characters
final_genome = ""
for nucleotide in full_genome:
    
    if (nucleotide == "\n"):
        continue
    
    else:
        final_genome = final_genome + nucleotide


del full_genome

#looking for
shine_dalgarno = ["TCCTCC", "TCCTTC", "TCCTC", "TCCTT"]


for motif in shine_dalgarno:
    sd_positions = [seq.start() for seq in re.finditer(motif, final_genome)]
    



from wiktor import step5

print(len(step5.funkcja(test.zaqw('/home/panda/Pulpit/sequence.fasta'), final_genome)))