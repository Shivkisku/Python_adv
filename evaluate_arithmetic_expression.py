class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def evaluate_expression(root):
    if root is None:
        return 0
    
    if root.value.isdigit():
        return int(root.value)
    
    left_value = evaluate_expression(root.left)
    right_value = evaluate_expression(root.right)
    
    if root.value == '+':
        return left_value + right_value
    elif root.value == '-':
        return left_value - right_value
    elif root.value == '*':
        return left_value * right_value
    elif root.value == '/':
        return left_value // right_value  # Integer division

# Example usage:
# Construct the binary tree
root = TreeNode("*")
root.left = TreeNode("+")
root.right = TreeNode("+")
root.left.left = TreeNode("3")
root.left.right = TreeNode("2")
root.right.left = TreeNode("4")
root.right.right = TreeNode("5")

result = evaluate_expression(root)
print(result)  # Output: 45
