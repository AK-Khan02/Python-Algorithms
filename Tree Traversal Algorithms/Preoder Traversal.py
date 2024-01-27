class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def preorder_traversal(root):
    if root is None:
        return []
    return [root.value] + preorder_traversal(root.left) + preorder_traversal(root.right)

# Example 1: Simple Binary Tree
# Structure:    1
#              / \
#             2   3
root1 = TreeNode(1, TreeNode(2), TreeNode(3))
print("Preorder Example 1:", preorder_traversal(root1))

# Example 2: Binary Tree with Multiple Children
# Structure:    1
#              / \
#             2   3
#                / \
#               4   5
root2 = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
print("Preorder Example 2:", preorder_traversal(root2))

# Example 3: Unbalanced Binary Tree
# Structure: 1
#              \
#               2
#                \
#                 3
root3 = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
print("Preorder Example 3:", preorder_traversal(root3))
