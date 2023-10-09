def shortest_substring_with_characters(s, char_set):
    char_count = {}  # Dictionary to store the count of characters in the set
    missing_chars = len(char_set)  # Number of characters to find

    left, right = 0, 0  # Pointers for the sliding window
    min_length = float('inf')  # Initialize minimum length with positive infinity
    min_substring = ""

    while right < len(s):
        if s[right] in char_set:
            if s[right] in char_count:
                char_count[s[right]] += 1
            else:
                char_count[s[right]] = 1

            # If we find a new unique character from the set, decrement the missing_chars count
            if char_count[s[right]] == 1:
                missing_chars -= 1

        while missing_chars == 0:
            # Update the minimum length and substring if we have a shorter valid substring
            if right - left + 1 < min_length:
                min_length = right - left + 1
                min_substring = s[left:right + 1]

            # Move the left pointer to the right to find a smaller substring
            if s[left] in char_set:
                char_count[s[left]] -= 1

                # If we remove a character from the set, increment the missing_chars count
                if char_count[s[left]] == 0:
                    missing_chars += 1

            left += 1

        right += 1

    return min_substring if min_substring else None

# Example usage:
s = "figehaeci"
char_set = {'a', 'e', 'i'}
result = shortest_substring_with_characters(s, char_set)
print(result)  # Output: "aeci"
