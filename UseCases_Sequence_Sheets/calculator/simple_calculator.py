class SimpleCalculator:
    def __init__(self):
        pass

    def add(self, *args):
        """Return the sum of all arguments."""
        return sum(args)

    def multiply(self, *args):
        """Return the product of all arguments."""
        product = 1
        for num in args:
            product *= num
        return product

    def subtract(self, initial, *args):
        """Return the result of subtracting all arguments from the initial value."""
        return initial - sum(args)

    def divide(self, initial, *args):
        """Return the result of successively dividing the initial value by the arguments."""
        quotient = initial
        for num in args:
            if num == 0:
                return "Error: Division by zero"
            quotient /= num
        return quotient

