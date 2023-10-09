class TernarySearchTree:
    def __init__(self):
        self.root = None

    class Node:
        def __init__(self, char):
            self.char = char
            self.left = None
            self.middle = None
            self.right = None
            self.is_end_of_word = False

    def insert(self, word):
        self.root = self._insert_recursively(self.root, word, 0)

    def _insert_recursively(self, node, word, index):
        if not node:
            node = self.Node(word[index])

        if word[index] < node.char:
            node.left = self._insert_recursively(node.left, word, index)
        elif word[index] > node.char:
            node.right = self._insert_recursively(node.right, word, index)
        else:
            if index < len(word) - 1:
                node.middle = self._insert_recursively(node.middle, word, index + 1)
            else:
                node.is_end_of_word = True

        return node

    def search(self, word):
        return self._search_recursively(self.root, word, 0)

    def _search_recursively(self, node, word, index):
        if not node:
            return False

        if word[index] < node.char:
            return self._search_recursively(node.left, word, index)
        elif word[index] > node.char:
            return self._search_recursively(node.right, word, index)
        else:
            if index == len(word) - 1:
                return node.is_end_of_word
            return self._search_recursively(node.middle, word, index + 1)

# Example usage:
if __name__ == "__main__":
    tst = TernarySearchTree()
    words = ["code", "cob", "be", "ax", "war", "we"]

    for word in words:
        tst.insert(word)

    search_words = ["code", "cob", "war", "bat"]
    for word in search_words:
        if tst.search(word):
            print(f"'{word}' found in the Ternary Search Tree.")
        else:
            print(f"'{word}' not found in the Ternary Search Tree.")
