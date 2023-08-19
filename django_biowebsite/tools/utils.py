import random

def count_words(seq, word_size):
    """Count subsequences in a sequence of a given length"""
    d = {}
    for i in range(len(seq) - word_size + 1):
        subseq = seq[i:i+word_size]        
        if subseq not in d:
            d[subseq] = {'count': 0, 'percentage': 0}
        d[subseq]['count'] += 1
    
    total = sum(x['count'] for x in d.values())
    for subseq in d:
        d[subseq]['percentage'] = d[subseq]['count'] / total * 100

    return d

def reverse(seq):
    """Return the reverse sequence"""
    return seq[::-1]

def complement(seq):
    """Return the complementary sequence"""
    d = {
        'A': 'T',
        'C': 'G',
        'G': 'C',
        'T': 'A'
    }
    return "".join([d.get(nt, 'N') for nt in seq])

def reverse_complement(seq):
    """Return the reverse complement sequence"""
    return complement(reverse(seq))

def translate(seq):
    """Translates a DNA coding sequence into a protein sequence"""
    gencode = {
        'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M', 'ACA': 'T',
        'ACC': 'T', 'ACG': 'T', 'ACT': 'T', 'AAC': 'N', 'AAT': 'N',
        'AAA': 'K', 'AAG': 'K', 'AGC': 'S', 'AGT': 'S', 'AGA': 'R',
        'AGG': 'R', 'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P', 'CAC': 'H',
        'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGA': 'R', 'CGC': 'R',
        'CGG': 'R', 'CGT': 'R', 'GTA': 'V', 'GTC': 'V', 'GTG': 'V',
        'GTT': 'V', 'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E', 'GGA': 'G',
        'GGC': 'G', 'GGG': 'G', 'GGT': 'G', 'TCA': 'S', 'TCC': 'S',
        'TCG': 'S', 'TCT': 'S', 'TTC': 'F', 'TTT': 'F', 'TTA': 'L',
        'TTG': 'L', 'TAC': 'Y', 'TAT': 'Y', 'TAA': '*', 'TAG': '*',
        'TGC': 'C', 'TGT': 'C', 'TGA': '*', 'TGG': 'W'
    }
    protein = [gencode.get(seq[i:i+3], "") for i in range(0, len(seq)-2, 3)]
    return "".join(protein)

def random_dna(length, a_freq, c_freq, g_freq, t_freq):
    """Generate a random DNA sequence of the specified length and nucleotide frequencies"""
    nucleotides = []
    nucleotides.extend(['A'] * int(a_freq * length))
    nucleotides.extend(['C'] * int(c_freq * length))
    nucleotides.extend(['G'] * int(g_freq * length))
    nucleotides.extend(['T'] * int(t_freq * length))
    random.shuffle(nucleotides)

    return "".join(nucleotides)
