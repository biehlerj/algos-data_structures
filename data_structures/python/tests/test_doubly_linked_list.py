import sys
import os.path

sys.path.append(os.path.join(os.path.abspath(os.pardir), "linked_list"))

from doubly_linked_list import LinkedList
import unittest


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.list = LinkedList()

    def tearDown(self):
        self.list = None

    def testAppend(self):
        self.list.append("David")

        self.assertTrue(self.list.head.data == "David")
        self.assertTrue(self.list.head.nextNode is None)

    def testAppend2(self):
        self.list.append("David")
        self.list.append("Thomas")

        self.assertTrue(self.list.head.data == "David")

        nextNode = self.list.head.nextNode
        self.assertTrue(nextNode.data == "Thomas")

    def testSearchSuccess(self):
        self.list.append("Jacob")
        self.list.append("Pallymay")
        self.list.append("Rasmus")

        found = self.list.search("Jacob")
        self.assertTrue(found.data == "Jacob")

        found = self.list.search("Pallymay")
        self.assertTrue(found.data == "Pallymay")

        found = self.list.search("Rasmus")
        self.assertTrue(found.data == "Rasmus")

    def testSearchNone(self):
        self.list.append("Jacob")
        self.list.append("Pallymay")

        # make sure regular search works
        found = self.list.search("Jacob")

        self.assertTrue(found.data == "Jacob")

        with self.assertRaises(ValueError):
            self.list.search("Vincent")

    def testDelete(self):
        self.list.append("Jacob")
        self.list.append("Pallymay")
        self.list.append("Rasmus")

        # Deleting the head of the list
        self.list.delete("Jacob")
        self.assertTrue(self.list.head.data == "Pallymay")

        # Deleting the tail of the list
        self.list.delete("Rasmus")
        self.assertTrue(self.list.head.nextNode is None)

    def testBadDelete(self):
        self.list.append("Jacob")
        self.list.append("Pallymay")
        self.list.append("Rasmus")

        with self.assertRaises(ValueError):
            self.list.delete("Sunny")

    def testEmptyListDelete(self):
        with self.assertRaises(ValueError):
            self.list.delete("Sunny")

    def testDeleteNextNode(self):
        '''
        Testing that the nextNode node is correctly assigned after a deletion
        '''
        self.list.append("Jacob")
        self.list.append("Cid")
        self.list.append("Pallymay")
        self.list.append("Rasmus")

        self.list.delete("Pallymay")
        self.list.delete("Cid")

        self.assertTrue(self.list.head.nextNode.data == "Rasmus")

    def testDeletePrev(self):
        '''
        Testing that the previous node is correctly assigned after a deletion
        '''
        self.list.append("Jacob")
        self.list.append("Cid")
        self.list.append("Pallymay")
        self.list.append("Rasmus")

        self.list.delete("Pallymay")
        self.list.delete("Cid")

        nextNodeNode = self.list.head.nextNode
        self.assertTrue(nextNodeNode.prev.data == "Jacob")

    def testSize(self):
        self.list.append("Jacob")
        self.list.append("Cid")
        self.list.append("Pallymay")
        self.list.append("Rasmus")

        size = self.list.size()

        self.assertTrue(size == 4)
