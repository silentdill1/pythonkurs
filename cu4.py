import numpy as np
from cu3 import frequent_words
import time
import matplotlib.pyplot as plt

SYM_TO_NUM = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
NUM_TO_SYM = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}


def pattern_to_number(pattern):
    if len(pattern) == 0:
        return 0
    else:
        symbol = pattern[-1]
        prefix = pattern[:-1]
        return 4*pattern_to_number(prefix)+SYM_TO_NUM[symbol]


def number_to_pattern(index, k):
    if k == 1:
        return NUM_TO_SYM[index]
    else:
        pref_ind = index // 4
        r = index % 4
        symb = NUM_TO_SYM[r]
        pref_pattern = number_to_pattern(pref_ind, k-1)
        return pref_pattern+symb


def computing_frequencies(text, k):
    frequency_array = np.zeros(4**k)
    for start_index in range(len(text)-k+1):
        k_mer = text[start_index:start_index+k]
        index = pattern_to_number(k_mer)
        frequency_array[index] += 1
    return frequency_array


def faster_frequent_words(text, k):
    frequency_array = computing_frequencies(text, k)
    max_number = max(frequency_array)
    frequent_k_mers = []
    for i in range(len(frequency_array)):
        if frequency_array[i] == max_number:
            pattern = number_to_pattern(i, k)
            frequent_k_mers.append(pattern)
    return frequent_k_mers


def long_string(a):
    base_string = 'ACGTTGCATGTCGCATGATGCATGATTTCCCATTATATATTCGTAGTCTGATCTGATCG'
    return base_string*a


li = []
li2 = []
'''
for a in range(1, 15):
    start = time.time()
    print(frequent_words(4, 0, long_string(a)))
    end = time.time()
    li.append(end-start)
'''
for a in range(1, 200):
    start = time.time()
    faster_frequent_words(long_string(a), 4)
    end = time.time()
    li2.append(end-start)
# plt.plot(range(1, 15), li)
plt.plot(range(1, 200), li2)
plt.show()