class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_floor_ceiling(root, target):
    floor = None
    ceiling = None

    current = root

    while current is not None:
        if current.value == target:
            return current.value, current.value
        elif current.value < target:
            floor = current.value
            current = current.right
        else:
            ceiling = current.value
            current = current.left

    return floor, ceiling

# Example usage:
# Create a binary search tree
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.left = TreeNode(12)
root.right.right = TreeNode(18)

target = 8
floor, ceiling = find_floor_ceiling(root, target)
print("Floor:", floor)  # Output: Floor: 7
print("Ceiling:", ceiling)  # Output: Ceiling: 10
