def group_anagrams(words):
    anagrams = {}
    
    for word in words:
        sorted_word = ''.join(sorted(word))
        
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    
    result = list(anagrams.values())
    return result

# Example usage:
input_array = ['eat', 'ate', 'apt', 'pat', 'tea', 'now']
result = group_anagrams(input_array)
print(result)
