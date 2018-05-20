#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re

from Bio.Seq import Seq

import test

fp = open("sequence.fasta", "r")
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

from wiktor import step5
dane = step5.trojki(test.zaqw('sequence.fasta'), final_genome)

headers = []

for i in range(len(dane)):
    headers.append(">Seq " + str(i) + '\n')

fp = open('wygranko.fasta', 'a')


for i in range(len(dane)):
    fp.write(headers[i] + dane[i] + "\n")
fp.close()

seq = Seq(final_genome)
seq = seq.reverse_complement()

dane = step5.trojki(test.zaqw('sequence.fasta'), seq)

headers = []

for i in range(len(dane)):
    headers.append(">Seq Reverse " + str(i) + '\n')

fp = open('wygrankoReverse.fasta', 'a')


for i in range(len(dane)):
    fp.write(headers[i] + dane[i] + "\n")
fp.close()



