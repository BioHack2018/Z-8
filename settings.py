#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re


#file opening
os.getcwd()
path = input("Please provide a path to genome-containing directory:\n")
os.chdir(path)
    
file_name = input("Provide a file name")

fp = open(file_name, "r")
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
shine_dalgarno = ["TCCTCC"]


for motif in shine_dalgarno:
    sd_positions = [seq.start() for seq in re.finditer(motif, final_genome)]
    
    
#extracting the UPSTREAM AND DOWNSTREAM REGIONS 
region_seq = []

for coord in sd_positions:

    start = coord - 100
    stop = coord + 10
    
    if (start < 0):
        start = 0
    
    if (stop > (len(final_genome)-1)):
        stop = len(final_genome)-1
        
                    
    region_seq.append(final_genome[start:stop])
    
  
 
from header import Region_with_SD

unfiltered_regions = []    
for i in range(len(region_seq)):
    x = Region_with_SD(region_seq[i], sd_positions[i])
    unfiltered_regions.append(x)
    
    unfiltered_regions[2].get_sequence()

 





    
