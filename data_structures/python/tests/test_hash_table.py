#!/usr/bin/python3
import unittest

from data_structures.python.hash_table import HashTable


class TestHashTable(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('\n\n.............................')
        print('..... Testing Functions .....')
        print('...... For Stack Class ......')
        print('.............................\n\n')

    def setUp(self) -> None:
        """Initializes a new instance of a Stack"""
        self.hash_table = HashTable(50)

    def tearDown(self):
        self.hash_table = None

    def test_hash(self):
        self.assertEqual(self.hash_table.hash("hello"), self.hash_table.hash("hello"))
        self.assertTrue(self.hash_table.hash("hello") < self.hash_table.capacity)

    def test_insert(self):
        self.assertEqual(self.hash_table.size, 0)
        self.hash_table.insert("test_key", "test_value")
        self.assertEqual(self.hash_table.size, 1)
        self.assertEqual(self.hash_table.buckets[self.hash_table.hash("test_key")].value, "test_value")

    def test_find(self):
        self.assertEqual(self.hash_table.size, 0)
        value = "hello"
        self.hash_table.insert("key1", value)
        self.assertEqual(value, self.hash_table.find("key1"))
        expected_value = ["this", "is", "a", "list"]
        self.hash_table.insert("key2", expected_value)
        self.assertEqual(expected_value, self.hash_table.find("key2"))

    def test_remove(self):
        self.assertEqual(self.hash_table.size, 0)
        expected = "test object"
        self.hash_table.insert("key1", expected)
        self.assertEqual(1, self.hash_table.size)
        self.assertEqual(expected, self.hash_table.remove("key1"))
        self.assertEqual(0, self.hash_table.size)
        self.assertEqual(None, self.hash_table.remove("some random key"))

    def test_capacity(self):
        for i in range(0, 1000):
            self.assertEqual(i, self.hash_table.size)
            self.hash_table.insert("key" + str(i), "value")
        self.assertEqual(self.hash_table.size, 1000)
        for i in range(0, 1000):
            self.assertEqual(1000 - i, self.hash_table.size)
            self.assertEqual(self.hash_table.find("key" + str(i)), self.hash_table.remove("key" + str(i)))

    def test_state(self):
        self.assertEqual(self.hash_table.size, 0)
        self.hash_table.insert("A", 5)
        self.assertEqual(self.hash_table.size, 1)
        self.hash_table.insert("B", 10)
        self.assertEqual(self.hash_table.size, 2)
        self.hash_table.insert("Ball", "hello")
        self.assertEqual(self.hash_table.size, 3)

        self.assertEqual(5, self.hash_table.remove("A"))
        self.assertEqual(self.hash_table.size, 2)
        self.assertEqual(None, self.hash_table.remove("A"))
        self.assertEqual(self.hash_table.size, 2)
        self.assertEqual(None, self.hash_table.remove("A"))
        self.assertEqual(self.hash_table.size, 2)

    def test_find_None(self):
        self.hash_table.insert("key1", "hello")
        self.assertEqual(None, self.hash_table.find("key2"))

    def test_remove_None(self):
        self.assertEqual(None, self.hash_table.remove("key1"))


if __name__ == '__main__':
    unittest.main()
