class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_mirror(root1, root2):
    # Base case: If both roots are None, they are mirrors
    if not root1 and not root2:
        return True
    
    # If one of the roots is None or their values are not equal, they are not mirrors
    if not root1 or not root2 or root1.val != root2.val:
        return False
    
    # Recursively check if the left subtree of the first tree is a mirror of the right subtree of the second tree,
    # and if the right subtree of the first tree is a mirror of the left subtree of the second tree.
    return is_mirror(root1.left, root2.right) and is_mirror(root1.right, root2.left)

def is_symmetric(root):
    # Check if the tree is a mirror of itself (symmetric)
    return is_mirror(root, root)

# Example usage:
# Construct a binary tree
#        1
#       / \
#      2   2
#     / \ / \
#    3  4 4  3
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

result = is_symmetric(root)
print(result)  # Output: True
