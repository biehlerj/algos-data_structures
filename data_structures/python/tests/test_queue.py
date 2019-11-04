#!/usr/bin/python3
import unittest

from data_structures.python.queue import Queue


class TestQueue(unittest.TestCase):
    """Tests for Queues"""

    @classmethod
    def setUpClass(cls) -> None:
        print('\n\n.............................')
        print('..... Testing Functions .....')
        print('...... For Queue Class ......')
        print('.............................\n\n')

    def setUp(self) -> None:
        """Initializes a new instance of a Queue"""
        self.queue = Queue(4)

    def tearDown(self):
        self.queue = None

    def test_enqueue(self):
        correct = [1]
        self.queue.enqueue(1)
        self.assertEqual(correct, self.queue.__repr__())

    def test_dequeue(self):
        correct = [1, 2]
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.queue.dequeue()
        self.assertEqual(correct, self.queue.__repr__())

    def test_overflow_queue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.queue.enqueue(4)
        with self.assertRaises(IndexError):
            self.queue.enqueue(5)

    def test_bad_dequeue(self):
        with self.assertRaises(IndexError):
            self.queue.dequeue()


if __name__ == '__main__':
    unittest.main()
