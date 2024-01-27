class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def bst_delete(root, value):
    if root is None:
        return root
    if value < root.value:
        root.left = bst_delete(root.left, value)
    elif value > root.value:
        root.right = bst_delete(root.right, value)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp_val = find_min_value(root.right)
        root.value = temp_val
        root.right = bst_delete(root.right, temp_val)
    return root

def find_min_value(node):
    current = node
    while current.left is not None:
        current = current.left
    return current.value

def inorder_traversal(root):
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right)

# Example 1: Deleting Leaf Node
root1 = TreeNode(2, TreeNode(1), TreeNode(3))
bst_delete(root1, 3)
print("BST Delete Example 1:", inorder_traversal(root1))

# Example 2: Deleting Node with One Child
root2 = TreeNode(2, TreeNode(1), TreeNode(3))
bst_delete(root2, 1)
print("BST Delete Example 2:", inorder_traversal(root2))

# Example 3: Deleting Node with Two Children
root3 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6, TreeNode(5), TreeNode(7)))
bst_delete(root3, 4)
print("BST Delete Example 3:", inorder_traversal(root3))
