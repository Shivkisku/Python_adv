def minJumps(arr):
    n = len(arr)
    if n <= 1:
        return 0

    jumps = [float('inf')] * n
    jumps[0] = 0

    for i in range(1, n):
        for j in range(i):
            if j + arr[j] >= i:
                jumps[i] = min(jumps[i], jumps[j] + 1)
                break

    return jumps[-1]

# Example usage:
if __name__ == "__main__":
    arr = [6, 2, 4, 0, 5, 1, 1, 4, 2, 9]
    result = minJumps(arr)
    print(result)  # Output: 2
