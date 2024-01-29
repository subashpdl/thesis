class TypeChecker:
    def __init__(self):
        pass

    def check_ints(self, *args):
        """Check if all arguments are integers."""
        return all(isinstance(arg, int) for arg in args)

    def check_strs(self, *args):
        """Check if all arguments are strings."""
        return all(isinstance(arg, str) for arg in args)

    def check_floats(self, *args):
        """Check if all arguments are floats."""
        return all(isinstance(arg, float) for arg in args)
