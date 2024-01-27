class TreeNode:
    def __init__(self, value=0, left=None, right=None, height=1):
        self.value = value
        self.left = left
        self.right = right
        self.height = height

def get_height(node):
    if not node:
        return 0
    return node.height

def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

def right_rotate(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    return x

def left_rotate(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y

def avl_insert(node, value):
    if not node:
        return TreeNode(value)
    if value < node.value:
        node.left = avl_insert(node.left, value)
    else:
        node.right = avl_insert(node.right, value)

    node.height = 1 + max(get_height(node.left), get_height(node.right))
    balance = get_balance(node)

    # Left Left Case
    if balance > 1 and value < node.left.value:
        return right_rotate(node)

    # Right Right Case
    if balance < -1 and value > node.right.value:
        return left_rotate(node)

    # Left Right Case
    if balance > 1 and value > node.left.value:
        node.left = left_rotate(node.left)
        return right_rotate(node)

    # Right Left Case
    if balance < -1 and value < node.right.value:
        node.right = right_rotate(node.right)
        return left_rotate(node)

    return node

def inorder_traversal(root):
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right)

# Example 1: Right Rotate
root1 = TreeNode(3, TreeNode(2, TreeNode(1)))
root1 = right_rotate(root1)
print("AVL Right Rotate Example:", inorder_traversal(root1))

# Example 2: Left Rotate
root2 = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
root2 = left_rotate(root2)
print("AVL Left Rotate Example:", inorder_traversal(root2))

# Example 3: AVL Insertion
root3 = None
for val in [10, 20, 30, 40, 50, 25]:
    root3 = avl_insert(root3, val)
print("AVL Insert Example:", inorder_traversal(root3))
