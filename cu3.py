import numpy as np
import time
import matplotlib.pyplot as plt


def hd(k_mer, text):
    k = len(k_mer)
    h_dis = k
    for i in range(len(text)):
        n_hd = k
        for j, letter in enumerate(text[i:i+k]):
            if letter == k_mer[j]:
                n_hd -= 1
        if n_hd < h_dis:
            h_dis = n_hd
    return h_dis


def frequent_words(k, d, text):
    k_mers = {}
    for i in range(len(text)-k+1):
        current_k_mer = text[i:i+k]
        k_mers[current_k_mer] = -1
        for j in range(len(text)-k):
            if hd(current_k_mer, text[j:j+k]) <= d:
                k_mers[current_k_mer] += 1
    max_num = max(k_mers.values())
    # max(k_mers.items(), key=(lambda v: v[1]))[1]
    most_freq = {}
    for key, value in k_mers.items():
        if value == max_num:
            most_freq[key] = value
    return most_freq


def long_string(a):
    base_string = 'ACGTTGCATGTCGCATGATGCATGATTTCCCATTATATATTCGTAGTCTGATCTGATCG'
    return base_string*a


def neighbors(string, d):
    print(string)
    if d == 0:
        return [string]
    if len(string) == 1:
        return ['A', 'C', 'G', 'T']
    else:
        neighbors_list = []
        for i in range(len(string)):
            for neighbor in neighbors(string[i+1:], d-1):
                neighbors_list.extend([string[:i]+'A'+neighbor, string[:i]+'G'+neighbor, string[:i]+'T'+neighbor,
                                       string[:i]+'C'+neighbor])
        return neighbors_list


'''
li = []
for a in range(1, 15):
    start = time.time()
    print(frequent_words(4, 1, long_string(a)))
    end = time.time()
    li.append(end-start)
plt.plot(range(1, 15), li)
plt.show()
'''
if __name__ == "__main__":
    print(neighbors('AGT', 2))

