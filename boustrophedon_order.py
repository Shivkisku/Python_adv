class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def boustrophedon_order(root):
    if not root:
        return []

    result = []
    current_level = [root]
    left_to_right = True

    while current_level:
        next_level = []
        current_values = []

        for node in current_level:
            current_values.append(node.value)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

        if left_to_right:
            result.extend(current_values)
        else:
            result.extend(current_values[::-1])

        current_level = next_level
        left_to_right = not left_to_right

    return result

# Example usage:
# Build the example tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

result = boustrophedon_order(root)
print(result)  # Output: [1, 3, 2, 4, 5, 6, 7]
