import unittest
from stack import Stack

class TestStack(unittest.TestCase):

    def test_push(self):
        stack = Stack()
        stack.push(5)
        self.assertEqual(stack.size(), 1)
        self.assertEqual(stack.peek(), 5)

    def test_pop(self):
        stack = Stack()
        stack.push(3)
        stack.push(4)
        self.assertEqual(stack.pop(), 4)
        self.assertEqual(stack.size(), 1)

    def test_peek(self):
        stack = Stack()
        stack.push(7)
        self.assertEqual(stack.peek(), 7)
        stack.push(8)
        self.assertEqual(stack.peek(), 8)

    def test_size(self):
        stack = Stack()
        self.assertEqual(stack.size(), 0)
        stack.push(1)
        self.assertEqual(stack.size(), 1)

    def test_is_empty(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())
        stack.push(2)
        self.assertFalse(stack.is_empty())

if __name__ == '__main__':
    unittest.main()
