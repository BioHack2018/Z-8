from Bio.Seq import Seq
from Bio import SeqIO

kodon_start = "AUG"
kodon_stop1 = "UAG"
kodon_stop2 = "UAA"
kodon_stop3 = "UGA"
sequence="xxxxxxAUGxxxxxxxxxxUAGxxxxxxxxUAAxxxxxxUGAxxxxxxxAUGxxxUGAxxxxxxxxxxxxxUAGxxxxxxxxxxAUGxxxxxxUAAxxxxxxxxxxxxUAGxxxxxxxxxxxxxxxxxxAUGxxxxxxxxxxxxxxxUGAxxxx"

list_of_sd_positions=[1,29,55,100];

def trojki(list):
    list_of_genes=[]
    for j in list:
        starting_position=j
        gene_start = sequence.find(kodon_start, starting_position)
        temp_start = gene_start+3
        while (True):
            codon = sequence[temp_start: temp_start+3]
            if codon == kodon_stop1 or codon == kodon_stop2 or codon == kodon_stop3:
                list_of_genes.append(sequence[gene_start:temp_start+3])
                break
            else:
                temp_start += 3
    print (list_of_genes)
    return (list_of_genes)

    #n=3
    #list_of_ends=[]
    #list_of_ends.append([sequence[i:i + n] for i in range(gene_start, len(sequence), n)])
    #print (list_of_ends)


trojki(list_of_sd_positions)