class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def print_level_order(root):
    if not root:
        return

    queue = [root]

    while queue:
        current_node = queue.pop(0)
        print(current_node.value, end=' ')

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

# Example usage:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

print_level_order(root)  # Output: 1 2 3 4 5
