#!/usr/bin/python3
import unittest

from data_structures.python.binary_tree import BinaryTree


class TestBinaryTree(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('\n\n.............................')
        print('..... Testing Functions .....')
        print('...... For Binary Tree Class ......')
        print('.............................\n\n')

    def setUp(self):
        self.tree = BinaryTree()

    def tearDown(self):
        self.tree = None

    # def test_binary_tree_node(self):
    #     expected =


if __name__ == '__main__':
    unittest.main()
