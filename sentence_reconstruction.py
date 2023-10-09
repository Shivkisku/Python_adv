def word_break(s, word_dict):
    def backtrack(start):
        if start == len(s):
            return [[]]

        valid_sentences = []
        for word in word_dict:
            if s.startswith(word, start):
                next_start = start + len(word)
                next_sentences = backtrack(next_start)
                for sentence in next_sentences:
                    valid_sentences.append([word] + sentence)
        
        return valid_sentences
    
    valid_sentences = backtrack(0)
    
    if not valid_sentences:
        return None
    
    # Flatten the list of lists into a single list
    result = [''.join(sentence) for sentence in valid_sentences[0]]
    
    return result

# Example usage:
word_dict_1 = {'quick', 'brown', 'the', 'fox'}
s_1 = 'thequickbrownfox'
print(word_break(s_1, word_dict_1))  # Output: ['the', 'quick', 'brown', 'fox']

word_dict_2 = {'bed', 'bath', 'bedbath', 'and', 'beyond'}
s_2 = 'bedbathandbeyond'
print(word_break(s_2, word_dict_2))  # Output: ['bed', 'bath', 'and', 'beyond'] (or ['bedbath', 'and', 'beyond'])
