def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("The lengths of the two strands must be equal.")
    hamming_distance = 0
    for base in range(len(strand_a)):
        if strand_a[base] != strand_b[base]:
            hamming_distance += 1
    return hamming_distance   

