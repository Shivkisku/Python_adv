def find_smallest_distance(text, word1, word2):
    words = text.split()
    word1_pos, word2_pos = -1, -1
    min_distance = len(words)  # Initialize with a large value

    for i, word in enumerate(words):
        if word == word1:
            word1_pos = i
        elif word == word2:
            word2_pos = i

        if word1_pos != -1 and word2_pos != -1:
            min_distance = min(min_distance, abs(word1_pos - word2_pos))

    return min_distance

# Example usage:
text_content = "dog cat hello cat dog dog hello cat world"
word1 = "hello"
word2 = "world"
result = find_smallest_distance(text_content, word1, word2)
print(result)  
