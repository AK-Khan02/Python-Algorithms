class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def bst_insert(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = bst_insert(root.left, value)
    else:
        root.right = bst_insert(root.right, value)
    return root

def inorder_traversal(root):
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right)

# Example 1: Inserting into an Empty Tree
root1 = bst_insert(None, 5)
print("BST Insert Example 1:", inorder_traversal(root1))

# Example 2: Inserting into a Single Node Tree
root2 = bst_insert(TreeNode(2), 1)
bst_insert(root2, 3)
print("BST Insert Example 2:", inorder_traversal(root2))

# Example 3: Inserting into a BST
root3 = TreeNode(4, TreeNode(2), TreeNode(6))
bst_insert(root3, 5)
bst_insert(root3, 3)
bst_insert(root3, 7)
print("BST Insert Example 3:", inorder_traversal(root3))
