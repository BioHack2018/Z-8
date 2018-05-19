from Bio import SeqIO


def clearSeqs(seqList):
    seq_records = list(SeqIO.parse("StreptococcusDB.fasta", "fasta"))
    
clearSeqs(["xxxxx", "xxxxx"])
