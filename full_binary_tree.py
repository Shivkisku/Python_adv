class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def makeFullBinaryTree(root):
    if root is None:
        return None

    # Recursively process the left and right subtrees
    root.left = makeFullBinaryTree(root.left)
    root.right = makeFullBinaryTree(root.right)

    # Case 1: Node is a leaf node (no children), return the node itself
    if root.left is None and root.right is None:
        return root

    # Case 2: Node has only one child, return the non-empty child
    if root.left is None:
        return root.right
    if root.right is None:
        return root.left

    # Case 3: Node has two children, return the node itself
    return root

def printTree(root):
    if root is None:
        return
    print(root.val)
    printTree(root.left)
    printTree(root.right)

# Example usage:
if __name__ == "__main__":
    # Build the example binary tree
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(6)
    root.right.right.right = TreeNode(7)

    print("Original Binary Tree:")
    printTree(root)

    full_tree_root = makeFullBinaryTree(root)

    print("\nFull Binary Tree:")
    printTree(full_tree_root)
