
def read_data_from_file(filename):
    with open(filename) as f:
        data = f.readlines()
    for i in range(len(data)):
        data[i] = data[i].strip()  # remove whitespace
    return data


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


def det_median_string(dna, k):
    median_string = ''
    min_hd_sum = k*len(dna)
    for line_index, line in enumerate(dna):
        for i in range(len(line)-k+1):
            pattern = line[i:i+k]
            hd_sum = sum([hd(pattern, cl) for i, cl in enumerate(dna) if i != line_index])
            # unnecessary expensive list creation
            if hd_sum < min_hd_sum:
                min_hd_sum = hd_sum
                median_string = pattern
    return median_string


data = read_data_from_file('median_data.txt')
print(det_median_string(data, 3))