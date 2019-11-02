import sys
import os.path
from data_structures.python.doubly_linked_list import LinkedList
import unittest

sys.path.append(os.path.join(os.path.abspath(os.pardir), "linked_list"))


class TestLinkedList(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('\n\n.............................')
        print('..... Testing Functions .....')
        print('...... For Stack Class ......')
        print('.............................\n\n')

    def setUp(self):
        self.list = LinkedList()

    def tearDown(self):
        self.list = None

    def test_append(self):
        self.list.append("David")

        self.assertTrue(self.list.head.data == "David")
        self.assertTrue(self.list.head.next_node is None)

    def test_append2(self):
        self.list.append("David")
        self.list.append("Thomas")

        self.assertTrue(self.list.head.data == "David")

        next_node = self.list.head.next_node
        self.assertTrue(next_node.data == "Thomas")

    def test_search_success(self):
        self.list.append("Jacob")
        self.list.append("Pallymay")
        self.list.append("Rasmus")

        found = self.list.search("Jacob")
        self.assertTrue(found.data == "Jacob")

        found = self.list.search("Pallymay")
        self.assertTrue(found.data == "Pallymay")

        found = self.list.search("Rasmus")
        self.assertTrue(found.data == "Rasmus")

    def test_search_None(self):
        self.list.append("Jacob")
        self.list.append("Pallymay")

        # make sure regular search works
        found = self.list.search("Jacob")

        self.assertTrue(found.data == "Jacob")

        with self.assertRaises(ValueError):
            self.list.search("Vincent")

    def test_delete(self):
        self.list.append("Jacob")
        self.list.append("Pallymay")
        self.list.append("Rasmus")

        # Deleting the head of the list
        self.list.delete("Jacob")
        self.assertTrue(self.list.head.data == "Pallymay")

        # Deleting the tail of the list
        self.list.delete("Rasmus")
        self.assertTrue(self.list.head.next_node is None)

    def test_bad_delete(self):
        self.list.append("Jacob")
        self.list.append("Pallymay")
        self.list.append("Rasmus")

        with self.assertRaises(ValueError):
            self.list.delete("Sunny")

    def test_empty_list_delete(self):
        with self.assertRaises(ValueError):
            self.list.delete("Sunny")

    def test_delete_next_node(self):
        """
        Testing that the next_node is correctly assigned after a deletion
        """
        self.list.append("Jacob")
        self.list.append("Cid")
        self.list.append("Pallymay")
        self.list.append("Rasmus")

        self.list.delete("Pallymay")
        self.list.delete("Cid")

        self.assertTrue(self.list.head.next_node.data == "Rasmus")

    def test_delete_prev(self):
        """
        Testing that the previous node is correctly assigned after a deletion
        """
        self.list.append("Jacob")
        self.list.append("Cid")
        self.list.append("Pallymay")
        self.list.append("Rasmus")

        self.list.delete("Pallymay")
        self.list.delete("Cid")

        next_node_node = self.list.head.next_node
        self.assertTrue(next_node_node.prev.data == "Jacob")

    def test_size(self):
        self.list.append("Jacob")
        self.list.append("Cid")
        self.list.append("Pallymay")
        self.list.append("Rasmus")

        size = self.list.size()

        self.assertTrue(size == 4)
