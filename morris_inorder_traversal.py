class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def morris_inorder_traversal(root):
    result = []
    current = root

    while current:
        if not current.left:
            result.append(current.val)
            current = current.right
        else:
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right

            if not predecessor.right:
                predecessor.right = current
                current = current.left
            else:
                predecessor.right = None
                result.append(current.val)
                current = current.right

    return result

# Example usage:
# Construct a binary tree
#        1
#       / \
#      2   3
#     / \
#    4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

result = morris_inorder_traversal(root)
print(result)  # Output: [4, 2, 5, 1, 3]
