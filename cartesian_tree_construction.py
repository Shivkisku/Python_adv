class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_cartesian_tree(S):
    if not S:
        return None

    # Find the index of the minimum element in the sequence
    min_index = S.index(min(S))

    # Create a TreeNode with the minimum element as the root
    root = TreeNode(S[min_index])

    # Recursively build the left and right subtrees
    root.left = build_cartesian_tree(S[:min_index])
    root.right = build_cartesian_tree(S[min_index + 1:])

    return root

def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.value, end=" ")
        in_order_traversal(root.right)

# Example usage:
sequence = [3, 2, 6, 1, 9]
cartesian_tree = build_cartesian_tree(sequence)
in_order_traversal(cartesian_tree)
