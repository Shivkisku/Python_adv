class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]
        node.value = num

    def find_max_xor(self, num):
        node = self.root
        xor = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            complement = 1 - bit  # Find the complement bit
            if complement in node.children:
                xor |= (1 << i)  # Set the bit in XOR result
                node = node.children[complement]
            else:
                node = node.children[bit]
        return xor

def find_max_xor(nums):
    if not nums or len(nums) < 2:
        return 0

    trie = Trie()
    max_xor = float('-inf')

    for num in nums:
        trie.insert(num)
        max_xor = max(max_xor, trie.find_max_xor(num))

    return max_xor

# Example usage:
nums = [3, 10, 5, 25, 2, 8]
result = find_max_xor(nums)
print(result)  # Output: 28
