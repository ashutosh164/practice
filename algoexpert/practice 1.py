array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]


def myfun(array,sequence):
    i = 0
    j = 0
    while i < len(array) and j < len(sequence):
        if array[i] == sequence[j]:
            i += 1
        j += 1
    return i == len(sequence)


myfun(array,sequence)








