def word_sense_disambiguation(sentence, word_meanings):
    words = sentence.split()
    disambiguated_sentence = []

    for word in words:
        if word in word_meanings:
            # Find the most likely sense based on context (for simplicity, just use the first meaning)
            likely_sense = word_meanings[word][0]
            disambiguated_sentence.append(f"{word}({likely_sense})")
        else:
            # If the word is not in the meanings dictionary, keep it as is
            disambiguated_sentence.append(word)

    return " ".join(disambiguated_sentence)

# Example usage:
word_meanings = {
    "bank": ["place to deposit money", "land beside a river or lake"],
    "money": ["currency", "wealth"],
    # Add more word meanings as needed
}

sentence = "I went to get money from the bank"
result = word_sense_disambiguation(sentence, word_meanings)
print(result)
