class Calculator:
    def __init__(self):
        self.__result = 0  # Private attribute to store the result

    def add(self, value):
        """Method to add a value to the result."""
        if isinstance(value, (int, float)):  # Ensure value is a number
            self.__result += value
        else:
            raise ValueError("The value must be an integer or float.")

    def subtract(self, value):
        """Method to subtract a value from the result."""
        if isinstance(value, (int, float)):  # Ensure value is a number
            self.__result -= value
        else:
            raise ValueError("The value must be an integer or float.")

    def get_result(self):
        """Method to get the current result."""
        return self.__result

# Create an instance of the Calculator class
calc = Calculator()

# Perform operations
calc.add(10)
print("After addition of 10:", calc.get_result())

calc.subtract(4)
print("After subtraction of 4:", calc.get_result())
