class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def merge_trees(root1, root2):
    if not root1:
        return root2
    if not root2:
        return root1
    
    # Create a new node with the sum of values from root1 and root2
    new_root = TreeNode(root1.val + root2.val)
    
    # Recursively merge left and right subtrees
    new_root.left = merge_trees(root1.left, root2.left)
    new_root.right = merge_trees(root1.right, root2.right)
    
    return new_root

# Helper function to print the tree (for visualization)
def print_tree(root):
    if not root:
        return
    print(root.val)
    print_tree(root.left)
    print_tree(root.right)

# Example usage:
# Create two binary trees
tree1 = TreeNode(1)
tree1.left = TreeNode(3)
tree1.right = TreeNode(2)
tree1.left.left = TreeNode(5)

tree2 = TreeNode(2)
tree2.left = TreeNode(1)
tree2.right = TreeNode(3)
tree2.left.right = TreeNode(4)
tree2.right.right = TreeNode(7)

# Merge the trees
merged_tree = merge_trees(tree1, tree2)

# Print the merged tree (for visualization)
print_tree(merged_tree)
