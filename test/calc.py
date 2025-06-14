import math

class Calculator:

    @staticmethod
    def add(a, b):
        Calculator._validate_numbers(a, b)
        return a + b

    @staticmethod
    def subtract(a, b):
        Calculator._validate_numbers(a, b)
        return a - b

    @staticmethod
    def multiply(a, b):
        Calculator._validate_numbers(a, b)
        return a * b

    @staticmethod
    def divide(a, b):
        Calculator._validate_numbers(a, b)
        if b == 0:
            raise TypeError("Division by zero is not allowed")
        return a / b

    @staticmethod
    def power(a, b):
        Calculator._validate_numbers(a, b)
        return math.pow(a, b)

    @staticmethod
    def sqrt(a):
        Calculator._validate_number(a)
        if a < 0:
            raise TypeError("Cannot take square root of negative number")
        return math.sqrt(a)

    @staticmethod
    def log10(a):
        Calculator._validate_number(a)
        if a <= 0:
            raise TypeError("Logarithm undefined for zero or negative numbers")
        return math.log10(a)

    @staticmethod
    def _validate_numbers(*args):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError("Parameters must be numbers")

    @staticmethod
    def _validate_number(arg):
        if not isinstance(arg, (int, float)):
            raise TypeError("Parameter must be a number")