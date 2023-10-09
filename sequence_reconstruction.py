def reconstruct_sequence(clues):
    n = len(clues)
    sequence = [0] * (n + 1)
    current = 0

    for i in range(n):
        if clues[i] == '+':
            current += 1
        elif clues[i] == '-':
            current -= 1
        sequence[i + 1] = current

    return sequence

# Example usage:
clues = [None, '+', '+', '-', '+']
result = reconstruct_sequence(clues)
print(result)  
