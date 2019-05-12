"""
assembles linear genome on the basis of perfect reads of equal length
"""

import numpy as np


def read_data_from_file(filename):
    with open(filename) as f:
        data = f.readlines()
    for i in range(len(data)):
        data[i] = data[i].strip()  # remove whitespace
    return data


'''
LETTER_TO_NUMBER = {'A' : 1, 'T': 2, 'G': 3, 'C': 4}


def fragment_to_number_code(fragment):
    """
    :param fragment: String, genome read
    :return: int, translated read
    """
    code = ''
    for letter in fragment:
        code += LETTER_TO_NUMBER[letter]
    return int(code)
'''

data = read_data_from_file('data_genom_ass.txt')  # list of Strings representing genome reads
numberOfReads = len(data)
maxNumberOfNodes = 2 * numberOfReads
length = None  # length of reads


# determining adjacency matrix
adjacencyMatrix = np.zeros((maxNumberOfNodes, maxNumberOfNodes))
numberOfConnections = np.zeros((maxNumberOfNodes, 2))  # outgoing (1) and ingoing (0) connections per node
nodeToIndex = {}
numberOfNodes = 0

firstFragment = True
currentIndex = 0

for read in data:
    if firstFragment:
        length = len(read)
        firstFragment = False
    elif len(read) != length:
        Exception('reads must all be of same length')
    node1 = read[0:length - 1]
    node2 = read[1:length]
    if node1 in nodeToIndex:
        index1 = nodeToIndex[node1]
    else:
        index1 = currentIndex
        nodeToIndex[node1] = currentIndex
        currentIndex += 1
    if node2 in nodeToIndex:
        index2 = nodeToIndex[node2]
    else:
        index2 = currentIndex
        nodeToIndex[node2] = currentIndex
        currentIndex += 1
    numberOfConnections[index1][1] += 1
    numberOfConnections[index2][0] += 1
    adjacencyMatrix[index1][index2] += 1

adjacencyMatrix = adjacencyMatrix[0:currentIndex + 1, 0:currentIndex + 1]  # removing unused matrix elements


# TODO: check if eulerian graph

# determining start / end node
startIndex = None
endIndex = None
for index in nodeToIndex.values():
    if numberOfConnections[index][0] == 0 and numberOfConnections[index][1] != 0:
        if isinstance(startIndex, int):
            Exception('found two starting nodes')
        else:
            startIndex = index
    if numberOfConnections[index][0] != 0 and numberOfConnections[index][1] == 0:
        if isinstance(endIndex, int):
            Exception('found two end nodes')
        else:
            endIndex = index
if endIndex is None or startIndex is None:
    Exception('couldn\'t find end or start index')


# finding eulerian path
remainingConnections = numberOfReads
remainingOutgoingConnections = adjacencyMatrix.T[1]
jigsawPath = []  # list of lists containing index for input into assembled path (0) and list with read indices in order (1)
assembledPath = []  # list of read indices representing path for linear genome
currentIndex = None  # index of node at end of current path
pathIndex = None  # index of current path fragment in jigsawPath
inputIndex = None  # index for input of current path fragment into assembled path
firstIteration = True  # is first created path fragment


def def_indices():
    """
    assigns values to indices for current path fragments (see definition above)
    """
    global inputIndex
    global pathIndex
    global firstIteration
    global currentIndex
    global remainingConnections
    if firstIteration:
        pathIndex = 0
        inputIndex = -1
        currentIndex = startIndex
    else:
        pathIndex += 1
        a_path_length = len(assembledPath)
        for i in range(a_path_length):  # finding last unused node on path
            read_ap_index = a_path_length - i-1  # read index in assembled path
            read_a_index = assembledPath[read_ap_index]  # read index in adjacency matrix
            if remainingOutgoingConnections[read_a_index] != 0:
                inputIndex = read_ap_index
                for j, entry in enumerate(adjacencyMatrix[read_a_index]):
                    if entry != 0:
                        adjacencyMatrix[read_a_index][j] -= 1
                        remainingOutgoingConnections[read_a_index] -= 1
                        remainingConnections -= 1
                        currentIndex = j


def end_reached(current_index):
    global firstIteration
    if firstIteration:
        if currentIndex == endIndex:
            firstIteration = False
            return True
        else:
            return False
    else:
        if current_index == assembledPath[inputIndex]:
            return True
        else:
            return False


while remainingConnections != 0:
    def_indices()
    jigsawPath.append([inputIndex, []])
    while True:
        jigsawPath[pathIndex][1].append(currentIndex)
        if end_reached(currentIndex):
            if jigsawPath[pathIndex][0] == -1:
                for read_index in jigsawPath[pathIndex][1]:
                    assembledPath.append(read_index)
            else:
                assembledPath.insert(jigsawPath[pathIndex][0], jigsawPath[pathIndex][1])
            break
        for i, entry in enumerate(adjacencyMatrix[currentIndex]):
            if entry != 0:
                adjacencyMatrix[currentIndex][i] -= 1
                remainingOutgoingConnections[currentIndex] -= 1
                remainingConnections -= 1
                currentIndex = i
                continue


# reconstructing genome string based on path
print(assembledPath)

indexToNode = {}
for key, value in nodeToIndex.items():
    indexToNode[value] = key

genome = ''
isFirstRead = True

for read_index in assembledPath:
    if isFirstRead:
        genome += indexToNode[read_index]
        isFirstRead = False
    else:
        genome += indexToNode[read_index][-1]

print(genome)
'''
length = False  # read length
numberOfReads = len(data)
firstFragment = True
nodesRepr = np.zeros(numberOfReads)  # arrays (start and end node) of translated String reads (according to dictionary LETTER_TO_NUMBER)

for i in range(numberOfReads):
    fragment = data[i]
    if firstFragment:
        length = len(fragment)
    elif len(fragment) != length:
        Exception('reads must all be of same length')
    node1 = fragment[0:length-1]
    node2 = fragment[1:length]
    nodesRepr[i] = np.array([node1, node2])

adjacencyMatrix = np.array((numberOfReads, numberOfReads))
checkedCombinations = np.array((numberOfReads, numberOfReads))

for i in range(numberOfReads):
    current_nodes = nodesRepr[i]
    for j in range(numberOfReads):
        if i == j:
            continue
        else:
            if checkedCombinations[i][j] != 1:
                c_nodes = nodesRepr[j]  # read to be compared with
                if current_nodes[1] == c_nodes[0]:
                    adjacencyMatrix[i][j] = 1
                checkedCombinations[i][j] = 1
            if checkedCombinations[j][i] != 1:
                c_nodes = nodesRepr[j]  # read to be compared with
                if current_nodes[0] == c_nodes[1]:
                    adjacencyMatrix[j][i] = 1
                checkedCombinations[j][i] = 1
'''




