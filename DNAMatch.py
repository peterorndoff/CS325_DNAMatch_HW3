# Name: Peter Orndoff
# Course: CS325
# Assignment: #3
# Description: Top/Down Dynamic Programming Approaches applied to DNA sequence identification.


def dna_match_bottomup(DNA1, DNA2):
    dna1_size = len(DNA1)  # Size of Array 1
    dna2_size = len(DNA2)  # Size of Array 2
    array = [[0 for i in range(dna2_size + 1)] for i in range(dna1_size + 1)]  # Creates array.

    for i in range(dna1_size + 1):  # For loop to iterate through first sequence
        for j in range(dna2_size + 1):  # For loop to iterate through second sequence

            if i == 0 or j == 0:  # Checks if either iterator is at the first index, if so, set array value to 0 at that position.
                array[i][j] = 0  # Sets array positioning value equal to 0

            elif DNA1[i - 1] == DNA2[
                j - 1]:  # Checks if sequence position in both indexes are equal, if so, update array.
                array[i][j] = array[i - 1][j - 1] + 1

            else:
                array[i][j] = max(array[i - 1][j],
                                  array[i][j - 1])  # Otherwise, take the max value of either side of array.

    return array[dna1_size][dna2_size]  # Return the bottom right value of the array.


def dna_match_topdown(DNA1, DNA2):
    dna1_len = len(DNA1)  # Size of Array 1
    dna2_len = len(DNA2)  # Size of Array 2

    array = [[0 for i in range(len(DNA2) + 1)] for i in range(len(DNA1) + 1)]  # Creates array.

    return dna_match_topdown_helper(DNA1, dna1_len, dna2_len, array)


def dna_match_topdown_helper(DNA1, DNA1_len, DNA2, DNA2_len, array):
    if DNA1_len < 0 or DNA2_len < 0:
        array[DNA1_len][DNA2_len] = 0

    elif DNA1[DNA1_len - 1] == DNA2[DNA2_len]:
        array[DNA1_len][DNA2_len] = array[DNA1_len - 1][DNA2_len - 1] + 1

    else:
        array[DNA1_len][DNA2_len] = max(array[DNA2_len - 1])

    for i in range(DNA1_len + 1):  # For loop to iterate through first sequence
        for j in range(DNA2_len + 1):  # For loop to iterate through second sequence

            if i == 0 or j == 0:  # Checks if either iterator is at the first index, if so, set array value to 0 at that position.
                array[i][j] = 0

            elif DNA1[i - 1] == DNA2[
                j - 1]:  # Checks if sequence position in both indexes are equal, if so, update array.
                array[i][j] = array[i - 1][j - 1] + 1

            else:
                array[i][j] = max(array[i - 1][j],
                                  array[i][j - 1])  # Otherwise, take the max value of either side of array.

    return array[DNA1_len][DNA2_len]  # Return the bottom right value of the array.
