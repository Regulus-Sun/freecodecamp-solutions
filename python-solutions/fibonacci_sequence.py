def fibonacci_sequence_og(start_sequence, length):
    if length == 0:
        return []

    if length == 1:
        return [start_sequence[0]]  # return as an array

    seq = start_sequence[:2]
    
    while len(seq) < length:
        seq.append(seq[-1] + seq[-2])

    return seq

# Optimal
def fibonacci_sequence(start_sequence, length):
    if length == 0:
        return []

    seq = start_sequence[:length]  # slicing the initial sequence based on length, removes the need for the separate length == 1 condition
    while len(seq) < length:
        seq.append(seq[-1] + seq[-2])

    return seq
