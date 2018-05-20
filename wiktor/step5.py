from Bio.Seq import Seq
from Bio import SeqIO

kodon_start = "TAC"
kodon_stop1 = "ATT"
kodon_stop2 = "ATC"
kodon_stop3 = "ACT"


def funkcja(lista, genome):
    list_of_genes=[]
    for i in lista:
        for j in range(2):
            starting_position=i+j
            gene_start=genome.find(kodon_start,starting_position)
            gene_end1=genome.find(kodon_stop1,gene_start)
            gene_end2=genome.find(kodon_stop2,gene_start)
            gene_end3=genome.find(kodon_stop3,gene_start)
            print("start",gene_start)
            print("konce",gene_end1,gene_end2,gene_end3)
            gene_end=min(n for n in [gene_end1,gene_end2,gene_end3] if n>0)
            print("poczatek genu: ",gene_start,"koniec genu: ",gene_end)
            list_of_genes.append(genome[gene_start:gene_end+3])

    list_of_genes = [x for x in list_of_genes if len(x) >= 60]
    return list_of_genes
