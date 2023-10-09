class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

def find_LCA(root, p, q):
    def find_path(node, target):
        path = []
        while node:
            path.append(node)
            if node == target:
                break
            node = node.parent
        return path
    
    path_p = find_path(root, p)
    path_q = find_path(root, q)
    
    # Find the LCA by comparing the paths from root to p and q
    LCA = None
    for node_p, node_q in zip(path_p, path_q):
        if node_p == node_q:
            LCA = node_p
        else:
            break
    
    return LCA

# Example usage:
# Construct a binary tree and set parent pointers
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.parent = root
root.right.parent = root
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.left.parent = root.left
root.left.right.parent = root.left
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.left.right.left.parent = root.left.right
root.left.right.right.parent = root.left.right

p = root.left
q = root.left.right.right

LCA = find_LCA(root, p, q)
if LCA:
    print("Lowest Common Ancestor:", LCA.val)
else:
    print("No common ancestor found")
