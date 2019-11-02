from data_structures.python.stack import Stack
import unittest


class TestStack(unittest.TestCase):
    """Testing for Stack instances"""

    @classmethod
    def setUpClass(cls) -> None:
        print('\n\n.............................')
        print('..... Testing Functions .....')
        print('...... For Stack Class ......')
        print('.............................\n\n')

    def setUp(self) -> None:
        """Initializes a new instance of a Stack"""
        self.stack = Stack(4)

    def tearDown(self):
        self.list = None

    def test_push(self):
        self.stack.push(1)
        expected = [1]
        actual = self.stack.__repr__()
        self.assertEqual(expected, actual)

    def test_push_overflow(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.push(4)
        with self.assertRaises(IndexError):
            self.stack.push(5)

    def test_peak(self):
        self.stack.push(1)
        expected = 1
        actual = self.stack.peak()
        self.assertEqual(expected, actual)

    def test_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.push(4)
        expected = 4
        actual = self.stack.pop()
        self.assertEqual(expected, actual)

    def test_bad_pop(self):
        expected = None
        actual = self.stack.pop()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
