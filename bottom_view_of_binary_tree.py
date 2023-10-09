class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.hd = 0  # Horizontal distance

def bottomView(root):
    if not root:
        return []

    hd_dict = {}  # Dictionary to store nodes at each horizontal distance
    queue = [(root, 0)]  # (node, horizontal distance)

    while queue:
        node, hd = queue.pop(0)
        hd_dict[hd] = node.val  # Update the dictionary with the latest node at this horizontal distance

        if node.left:
            node.left.hd = hd - 1
            queue.append((node.left, hd - 1))

        if node.right:
            node.right.hd = hd + 1
            queue.append((node.right, hd + 1))

    # Extract the values from the dictionary to get the bottom view
    bottom_view = [hd_dict[hd] for hd in sorted(hd_dict)]
    return bottom_view

# Example usage:
if __name__ == "__main__":
    # Build the example binary tree
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    root.left.left.left = TreeNode(0)
    root.right.right.left = TreeNode(8)

    result = bottomView(root)
    print(result)  # Output: [0, 1, 3, 6, 8, 9]
