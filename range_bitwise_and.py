def rangeBitwiseAnd(M, N):
    shift = 0
    while M < N:
        M >>= 1
        N >>= 1
        shift += 1
    return M << shift

# Example usage:
if __name__ == "__main__":
    M = 5
    N = 7
    result = rangeBitwiseAnd(M, N)
    print(result)  # Output: 4
