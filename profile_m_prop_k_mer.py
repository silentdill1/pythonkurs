import pandas as pd

SYM_TO_NUM = {'A': 0, 'C': 1, 'G': 2, 'T': 3}


def det_pmp_k_mer(text, profile):
    k = len(profile)
    highest_score = 0
    pmp_kmer = ''
    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        pattern_score = 0
        for j, letter in enumerate(pattern):
            pattern_score += profile[j][SYM_TO_NUM[letter]]
        if pattern_score > highest_score:
            highest_score = pattern_score
            pmp_kmer = pattern
    return pmp_kmer


profile = pd.read_csv('data_pmpk.txt', sep=' ', header=None).as_matrix().T
print(det_pmp_k_mer('ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT', profile))



