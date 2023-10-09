class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def findCousins(root, target):
    if not root:
        return []

    result = []
    queue = [(root, None, 1)]  # (node, parent, level)

    target_parent = None
    target_level = 0

    while queue:
        node, parent, level = queue.pop(0)

        if node.val == target:
            target_parent = parent
            target_level = level

        if node.left:
            queue.append((node.left, node, level + 1))
        if node.right:
            queue.append((node.right, node, level + 1))

    if target_parent is None:
        return []

    for node, parent, level in queue:
        if level == target_level and parent != target_parent:
            result.append(node.val)

    return result

# Example usage:
if __name__ == "__main__":
    # Build the example binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    target_node = 4
    cousins = findCousins(root, target_node)
    print("Cousins of node", target_node, "are:", cousins)
