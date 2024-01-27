# Tree Traversal

## About
This folder is dedicated to various tree traversal and manipulation algorithms, implemented in Python. Trees are a fundamental data structure in computer science used to represent hierarchical relationships. Traversal is the process of visiting all the nodes of the tree and may be performed in several ways. Additionally, this folder includes algorithms for inserting and deleting nodes in specific types of trees, such as Binary Search Trees (BST) and AVL Trees.

## Algorithms Included

### AVL Insertion
- **File**: `AVL Insertion.py`
- **Description**: AVL trees are self-balancing binary search trees where the difference between heights of left and right subtrees cannot be more than one for all nodes. This script demonstrates how nodes are inserted in such a way that the tree remains balanced.

### BST Deletion
- **File**: `BST Deletion.py`
- **Description**: This algorithm shows how to remove a node from a Binary Search Tree (BST). The process varies depending on the node's children and involves updating parent and child links to maintain the BST properties.

### BST Insertion
- **File**: `BST Insertion.py`
- **Description**: Demonstrates how to insert a new node in a Binary Search Tree (BST). The properties of the BST (left child < parent node, right child > parent node) are preserved during the insertion process.

### Inorder Traversal
- **File**: `Inorder Traveral.py`
- **Description**: Inorder traversal is one of the most common ways to traverse a binary tree. It involves visiting the left subtree, the root node, and then the right subtree recursively. This order of traversal ensures that nodes are visited in their non-decreasing order.

### Level Order Traversal
- **File**: `Level Order Traversal.py`
- **Description**: Level order traversal visits each level of the tree from top to bottom and from left to right. It is also known as breadth-first search (BFS) in the context of trees.

### Postorder Traversal
- **File**: `Postorder Traversal.py`
- **Description**: In postorder traversal, the nodes are recursively visited in the order of left subtree, right subtree, and then the root node. This method is used often in mathematical expressions and to delete a tree.

### Preorder Traversal
- **File**: `Preorder Traversal.py`
- **Description**: Preorder traversal involves visiting the root node first, then recursively visiting the left subtree, and finally the right subtree. This traversal method is used to create a copy of the tree.
