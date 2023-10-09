def make_palindrome(s):
    def is_palindrome(string):
        return string == string[::-1]

    # Find the longest palindromic prefix
    for i in range(len(s)):
        if is_palindrome(s[:i]):
            suffix = s[i:]
            return s + suffix[::-1]

# Example usage:
input_string_1 = "race"
result_1 = make_palindrome(input_string_1)
print(result_1)  

input_string_2 = "google"
result_2 = make_palindrome(input_string_2)
print(result_2)  
