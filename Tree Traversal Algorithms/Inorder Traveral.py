class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def inorder_traversal(root):
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right)

# Example 1: Simple Binary Tree
# Structure:    1
#              / \
#             2   3
root1 = TreeNode(1, TreeNode(2), TreeNode(3))

# Example 2: Binary Tree with Multiple Children
# Structure:    1
#              / \
#             2   3
#                / \
#               4   5
root2 = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))

# Example 3: Unbalanced Binary Tree
# Structure: 1
#              \
#               2
#                \
#                 3
root3 = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))

# Example 1: Simple Binary Tree (Same as Preorder Example 1)
print("Inorder Example 1:", inorder_traversal(root1))

# Example 2: Binary Tree with Multiple Children (Same as Preorder Example 2)
print("Inorder Example 2:", inorder_traversal(root2))

# Example 3: Unbalanced Binary Tree (Same as Preorder Example 3)
print("Inorder Example 3:", inorder_traversal(root3))
