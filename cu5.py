import numpy as np

SYM_TO_NUM = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
NUM_TO_SYM = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}


def hd(k_mer, text):
    k = len(k_mer)
    h_dis = k
    for i in range(len(text)-k+1):
        n_hd = k
        for j, letter in enumerate(text[i:i+k]):
            if letter == k_mer[j]:
                n_hd -= 1
        if n_hd < h_dis:
            h_dis = n_hd
    return h_dis


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


def profile_to_consensus_string(profile):
    string_length = len(profile[0])
    consensus_string = ''
    for position in range(string_length):
        max_index = max(enumerate(profile.T[position]), key=(lambda v: v[1]))[0]
        consensus_string += NUM_TO_SYM[max_index]
    return consensus_string


def read_data_from_file(filename):
    with open(filename) as f:
        data = f.readlines()
    for i in range(len(data)):
        data[i] = data[i].strip()  # remove whitespace
    return data


def motif_enumeration(dna, k, d):
    patterns = set()
    for current_line_index, line in enumerate(dna):
        for i in range(len(line)-k+1):
            pattern = line[i:i+k]
            is_motif = True
            for line_index in range(len(dna)):
                if line_index != current_line_index:
                    current_line = dna[line_index]
                    if hd(pattern, current_line) > d:
                        is_motif = False
                        break
            if is_motif:
                patterns.add(pattern)
    return patterns