def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("The lengths of the two strands must be equal.")
    strands = zip(strand_a, strand_b)
    return sum(a != b for a, b in strands)
    