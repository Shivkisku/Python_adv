def smallestStringWithKMoves(s, k):
    n = len(s)
    smallest = s

    for i in range(k):
        # Check if we can find a smaller character by cyclically rotating the string
        for j in range(1, n):
            rotated = s[j:] + s[:j]
            if rotated < smallest:
                smallest = rotated

        # If no smaller character can be found, we are done
        if s == smallest:
            break

        # Update the string with the smallest found so far
        s = smallest

    return smallest

# Example usage:
if __name__ == "__main__":
    s = "daily"
    k = 1
    result = smallestStringWithKMoves(s, k)
    print(result)  # Output: "ailyd"
