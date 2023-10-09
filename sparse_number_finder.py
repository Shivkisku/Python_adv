def find_sparse_number(N):
    binary_representation = bin(N)[2:]
    result = 0
    prev_bit = 0

    for bit in binary_representation:
        if bit == '1' and prev_bit == 1:
            result += 1
            result <<= 1
            prev_bit = 0
        else:
            result <<= 1
            prev_bit = int(bit)

    # Handle the case where the last bit is 1
    if prev_bit == 1:
        result += 1

    return result

# Example usage:
N = 22
sparse_num = find_sparse_number(N)
print(sparse_num)  
