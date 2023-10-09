def sort_string_by_frequency(s):
    # Count the frequency of each character in the string
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Sort the string based on character frequencies in decreasing order
    sorted_string = ''.join(sorted(s, key=lambda char: (-char_count[char], char)))
    
    return sorted_string

# Test the function
input_str = "tweet"
result = sort_string_by_frequency(input_str)
print(result)
