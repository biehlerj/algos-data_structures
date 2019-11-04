#!/usr/bin/python3

"""
TODO:
Create a binary tree that can do the following:
1) Create a new node
2) Insert to the left
3) Insert to the right
4) Delete the entire binary tree
5) Check if a node is a leaf
6) Check if a node is a root
7) Pre-order traversal
8) In-order traversal
9) Post-order traversal
10) Tree height
11) Node depth
12) Size of the tree
13) Count of leaves in the tree
14) Count of nodes with at least 1 child in the tree
15) Measure the balance factor of the tree
16) Check if the binary tree is full
17) Check if the binary tree is perfect
18) Find the sibling of a node
19) Find the uncle of a node

Finished:
None
"""


class Node:
    def __init__(self, n):
        self.n = n
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
