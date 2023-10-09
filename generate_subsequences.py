def generate_subsequences(s):
    def backtrack(index, current_subsequence):
        if index == len(s):
            subsequences.append(current_subsequence)
            return

        # Include the current character in the subsequence
        backtrack(index + 1, current_subsequence + s[index])

        # Exclude the current character from the subsequence
        backtrack(index + 1, current_subsequence)

    subsequences = []
    backtrack(0, "")
    return subsequences

# Example usage:
input_string = "xyz"
subsequences = generate_subsequences(input_string)
print(subsequences)
