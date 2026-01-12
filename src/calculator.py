"""Calculator module with basic operations and history tracking."""

class History:
    """Stores calculation history."""
    
    def __init__(self):
        self.operations = []
    
    def add(self, operation: str, result: float):
        """Add operation to history."""
        self.operations.append(f"{operation} = {result}")
    
    def clear(self):
        """Clear history."""
        self.operations.clear()
    
    def get_all(self):
        """Get all history entries."""
        return self.operations.copy()


class Calculator:
    """Basic calculator with four operations."""
    
    def __init__(self):
        self.history = History()
    
    def add(self, a: float, b: float) -> float:
        """Add two numbers."""
        result = a + b
        self.history.add(f"{a} + {b}", result)
        return result
    
    def subtract(self, a: float, b: float) -> float:
        """Subtract b from a."""
        result = a - b
        self.history.add(f"{a} - {b}", result)
        return result
    
    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers."""
        result = a * b
        self.history.add(f"{a} * {b}", result)
        return result
    
    def divide(self, a: float, b: float) -> float:
        """Divide a by b."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.history.add(f"{a} / {b}", result)
        return result
    
    def get_history(self):
        """Get calculation history."""
        return self.history.get_all()
    
    def clear_history(self):
        """Clear calculation history."""
        self.history.clear()


if __name__ == "__main__":
    # Пример использования
    calc = Calculator()
    print("Калькулятор запущен!")
    print("2 + 3 =", calc.add(2, 3))
    print("5 - 2 =", calc.subtract(5, 2))
    print("4 * 3 =", calc.multiply(4, 3))
    print("10 / 2 =", calc.divide(10, 2))
    print("История:", calc.get_history())
