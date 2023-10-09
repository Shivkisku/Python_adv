class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(root):
    def check_height(node):
        if not node:
            return 0
        
        left_height = check_height(node.left)
        if left_height == -1:
            return -1
        
        right_height = check_height(node.right)
        if right_height == -1:
            return -1
        
        if abs(left_height - right_height) > 1:
            return -1
        
        return 1 + max(left_height, right_height)

    return check_height(root) != -1

# Example usage:
# Construct a height-balanced binary tree
#        1
#       / \
#      2   2
#     / \ / \
#    3  4 4  3
balanced_root = TreeNode(1)
balanced_root.left = TreeNode(2)
balanced_root.right = TreeNode(2)
balanced_root.left.left = TreeNode(3)
balanced_root.left.right = TreeNode(4)
balanced_root.right.left = TreeNode(4)
balanced_root.right.right = TreeNode(3)

# Construct an unbalanced binary tree
#        1
#       / \
#      2   2
#     / \
#    3   3
unbalanced_root = TreeNode(1)
unbalanced_root.left = TreeNode(2)
unbalanced_root.right = TreeNode(2)
unbalanced_root.left.left = TreeNode(3)
unbalanced_root.left.right = TreeNode(3)

balanced_result = is_balanced(balanced_root)
unbalanced_result = is_balanced(unbalanced_root)

print("Is the balanced tree height-balanced?", balanced_result)  # Output: True
print("Is the unbalanced tree height-balanced?", unbalanced_result)  # Output: False
