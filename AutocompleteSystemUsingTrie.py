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

def find_words_with_prefix(trie, prefix):
    node = trie
    for char in prefix:
        if char in node.children:
            node = node.children[char]
        else:
            return []
    
    def dfs(node, current_word):
        results = []
        if node.is_end_of_word:
            results.append(current_word)
        
        for char, child_node in node.children.items():
            results.extend(dfs(child_node, current_word + char))
        
        return results
    
    return dfs(node, prefix)

def autocomplete(words, query):
    trie = build_trie(words)
    return find_words_with_prefix(trie, query)

# Test the autocomplete function
words = ['dog', 'deer', 'deal']
query = 'de'
results = autocomplete(words, query)
print(results)  # Output: ['deer', 'deal']
