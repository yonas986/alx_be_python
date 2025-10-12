class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method: does not depend on class or instance state.
        Just takes two numbers and returns their sum.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method: has access to class-level data (cls).
        Prints the class attribute before performing multiplication.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
