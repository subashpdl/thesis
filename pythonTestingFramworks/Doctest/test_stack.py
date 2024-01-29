def test_stack():
    """
    Test the Stack implementation.

    >>> stack = Stack()
    >>> stack.is_empty()
    True
    >>> stack.push(1)
    >>> stack.push(2)
    >>> stack.peek()
    2
    >>> stack.pop()
    2
    >>> stack.size()
    1
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()
