import numpy as np

SYM_TO_NUM = {'A': 0, 'C': 1, 'G': 2, 'T': 3}


def string_matrix_to_profile(string_matrix):
    string_length = len(string_matrix[0])
    number_of_strings = len(string_matrix)
    profile_matrix = np.zeros((string_length, 4))
    for position in range(string_length):
        frequencies_for_position = np.zeros(4)
        for string in string_matrix:
            letter_index = SYM_TO_NUM[string[position]]
            frequencies_for_position[letter_index] += 1/number_of_strings
        profile_matrix[position] = frequencies_for_position
    return profile_matrix


def string_matrix_to_profile_wpc(string_matrix):
    string_length = len(string_matrix[0])
    number_of_strings = len(string_matrix)
    profile_matrix = np.zeros((string_length, 4))
    for position in range(string_length):
        counts_for_position = np.array([1, 1, 1, 1])
        for string in string_matrix:
            letter_index = SYM_TO_NUM[string[position]]
            counts_for_position[letter_index] += 1
        profile_matrix[position] = counts_for_position/(number_of_strings+1)
    return profile_matrix


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


def read_data_from_file(filename):
    with open(filename) as f:
        data = f.readlines()
    for i in range(len(data)):
        data[i] = data[i].strip()  # remove whitespace
    return data


def greedy_motif_search(dna, k):
    initial_motifs = []
    for line in dna:
        initial_motifs.append(line[:k])
    initial_profile = string_matrix_to_profile(initial_motifs)
    best_motifs = []
    is_first = True
    for line in dna:
        if is_first:
            best_motifs.append(det_pmp_k_mer(line, initial_profile))
            is_first = False
        else:
            current_profile = string_matrix_to_profile(best_motifs)
            best_motifs.append(det_pmp_k_mer(line, current_profile))
    return best_motifs


def greedy_motif_search_wpc(dna, k):
    initial_motifs = []
    for line in dna:
        initial_motifs.append(line[:k])
    initial_profile = string_matrix_to_profile_wpc(initial_motifs)
    best_motifs = []
    is_first = True
    for line in dna:
        if is_first:
            best_motifs.append(det_pmp_k_mer(line, initial_profile))
            is_first = False
        else:
            current_profile = string_matrix_to_profile_wpc(best_motifs)
            best_motifs.append(det_pmp_k_mer(line, current_profile))
    return best_motifs


data = read_data_from_file('greedy_data.txt')
print(greedy_motif_search_wpc(data, 3))

