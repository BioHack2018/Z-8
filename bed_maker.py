#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from header import Gene



def to_bed(all_records):

    fp = open('annotation.bed', "a")
    for i in range(len(all_records)):
        row = "chr1\t" + str(all_records[i].get_start()) + "\t" + str(all_records[i].get_stop()) + "\t" + all_records[i].get_name() + "\n" 
        fp.write(row)
        fp.close()
        
        
def to_fasta(all_records):
    
    fp = open("annotation.fasta", "a")
    for i in range(len(all_records)):
        
        fst_row = ">" + all_records[i].get_name() + "\n"
        snd_row = all_records[i].get_sequence() + "\n"
        
        fp.write(fst_row)
        fp.write(snd_row)
         
    fp.close()

    
