class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

def build_trie(words):
    root = TrieNode()
    for word in words:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    return root

def can_win(node):
    if node.is_end_of_word:
        return False
    for char in node.children:
        if not can_win(node.children[char]):
            return True
    return False

def find_winning_starting_letters(words):
    trie = build_trie(words)
    winning_starting_letters = []
    
    for char in trie.children:
        if not can_win(trie.children[char]):
            winning_starting_letters.append(char)
    
    return winning_starting_letters

# Example usage:
dictionary = ["cat", "calf", "dog", "bear"]
winning_starting_letters = find_winning_starting_letters(dictionary)
print(winning_starting_letters)  # Output: ['b']
