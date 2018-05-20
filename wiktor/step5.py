
from Bio.Seq import Seq

from Bio import SeqIO

kodon_start = "TAC"

kodon_stop1 = "ATT"

kodon_stop2 = "ATC"

kodon_stop3 = "ACT"

list_of_sd_positions = [1, 29, 55, 100];


def trojki(lista,genome):
    list_of_genes = []

    for j in lista:

        starting_position = j

        gene_start = genome.find(kodon_start, starting_position)

        temp_start = gene_start + 3

        while (True):

            codon = genome[temp_start: temp_start + 3]

            if codon == kodon_stop1 or codon == kodon_stop2 or codon == kodon_stop3:

                list_of_genes.append(genome[gene_start:temp_start + 3])

                break

            else:

                temp_start += 3

    return [x for x in list_of_genes if len(x) >= 60]

    # n=3

    # list_of_ends=[]

    # list_of_ends.append([sequence[i:i + n] for i in range(gene_start, len(sequence), n)])

    # print (list_of_ends)
