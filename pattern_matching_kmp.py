def compute_prefix(pattern):
    m = len(pattern)
    prefix = [0] * m
    j = 0

    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = prefix[j - 1]

        if pattern[i] == pattern[j]:
            j += 1

        prefix[i] = j

    return prefix

def find_pattern_indices(text, pattern):
    if not text or not pattern:
        return []

    n = len(text)
    m = len(pattern)
    prefix = compute_prefix(pattern)
    indices = []

    j = 0
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = prefix[j - 1]

        if text[i] == pattern[j]:
            j += 1

        if j == m:
            indices.append(i - m + 1)
            j = prefix[j - 1]

    return indices

# Example usage:
text = "abracadabra"
pattern = "abr"
result = find_pattern_indices(text, pattern)
print(result)  # Output: [0, 7]
