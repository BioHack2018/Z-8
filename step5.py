from Bio.Seq import Seq
from Bio import SeqIO

kodon_start = "AUG"
kodon_stop1 = "UAG"
kodon_stop2 = "UAA"
kodon_stop3 = "UGA"
sequence="xxxxxxAUGxxxxxxxxxxUAGxxxxxxxxUAAxxxxxxUGAxxxxxxxAUGxxxUGAxxxxxxxxxxxxxUAGxxxxxxxxxxAUGxxxxxxUAAxxxxxxxxxxxxUAGxxxxxxxxxxxxxxxxxxAUGxxxxxxxxxxxxxxxUGAxxxx"

list_of_sd_positions=[1,29,55,100];

def funkcja(list):
    list_of_genes=[]
    for i in list:
        starting_position=i
        gene_start=sequence.find(kodon_start,starting_position)
        gene_end1=sequence.find(kodon_stop1,gene_start)
        gene_end2=sequence.find(kodon_stop2,gene_start)
        gene_end3=sequence.find(kodon_stop3,gene_start)
        print("start",gene_start)
        print("konce",gene_end1,gene_end2,gene_end3)
        gene_end=min(n for n in [gene_end1,gene_end2,gene_end3] if n>0)
        print("poczatek genu: ",gene_start,"koniec genu: ",gene_end)
        list_of_genes.append(sequence[gene_start:gene_end+3])

    print(list_of_genes)

funkcja(list_of_sd_positions)