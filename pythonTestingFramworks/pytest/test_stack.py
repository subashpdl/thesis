import pytest
from stack import Stack

def test_push():
    stack = Stack()
    stack.push(5)
    assert stack.size() == 1
    assert stack.peek() == 5

def test_pop():
    stack = Stack()
    stack.push(3)
    stack.push(4)
    assert stack.pop() == 4
    assert stack.size() == 1

def test_peek():
    stack = Stack()
    stack.push(7)
    assert stack.peek() == 7
    stack.push(8)
    assert stack.peek() == 8

def test_size():
    stack = Stack()
    assert stack.size() == 0
    stack.push(1)
    assert stack.size() == 1

def test_is_empty():
    stack = Stack()
    assert stack.is_empty() == True
    stack.push(2)
    assert stack.is_empty() == False

