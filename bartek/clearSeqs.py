import math
from Bio import SeqIO


def _hamming(sequence, TFBS):
    diffs = 0
    for ch1, ch2 in zip(sequence, TFBS):
        if ch1 != ch2:
            diffs += 1
    return diffs


def _calculateHamming(seq, TFBS):
    for x in range(len(seq.get_sequence())):
        if len(seq.get_sequence()[x:x + len(TFBS)]) < len(TFBS):
            return -1
        else:
            distance = _hamming(seq.get_sequence()[x:x + len(TFBS)], TFBS)
            if distance < math.ceil(0.3 * len(TFBS)):
                return distance



def clearSeqs(seqList):
    pureSD = []
    seq_TFBS = list(SeqIO.parse("StreptococcusDB.fasta", "fasta"))
    for seq in seqList:
        for TFBS in seq_TFBS:
            distance = _calculateHamming(seq.get_sequence(), TFBS.seq)
            if distance != -1:
                pureSD.extend(seq.get_position())
                break
    return pureSD