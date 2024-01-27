from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def level_order_traversal(root):
    if not root:
        return []
    queue, result = deque([root]), []
    while queue:
        level_size = len(queue)
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result

# Example 1: Simple Binary Tree
root1 = TreeNode(1, TreeNode(2), TreeNode(3))
print("Level-Order Example 1:", level_order_traversal(root1))

# Example 2: Complete Binary Tree
root2 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
print("Level-Order Example 2:", level_order_traversal(root2))

# Example 3: Unbalanced Binary Tree
root3 = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(6))), TreeNode(3, None, TreeNode(5)))
print("Level-Order Example 3:", level_order_traversal(root3))
