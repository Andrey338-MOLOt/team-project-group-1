"""Tests for calculator module."""

import pytest
from src.calculator import Calculator, History


class TestHistory:
    """Test History class."""
    
    def test_init(self):
        """Test History initialization."""
        history = History()
        assert history.operations == []
    
    def test_add(self):
        """Test adding operations to history."""
        history = History()
        history.add("2 + 2", 4)
        assert history.operations == ["2 + 2 = 4"]
        history.add("3 * 3", 9)
        assert len(history.operations) == 2
    
    def test_clear(self):
        """Test clearing history."""
        history = History()
        history.add("1 + 1", 2)
        history.clear()
        assert history.operations == []
    
    def test_get_all(self):
        """Test getting all history entries."""
        history = History()
        history.add("5 - 2", 3)
        history.add("4 / 2", 2)
        result = history.get_all()
        assert result == ["5 - 2 = 3", "4 / 2 = 2"]
        # Проверяем что возвращается копия
        assert result is not history.operations


class TestCalculator:
    """Test Calculator class."""
    
    def setup_method(self):
        """Setup before each test."""
        self.calc = Calculator()
    
    def test_add(self):
        """Test addition."""
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(-1, 1) == 0
        assert self.calc.add(0, 0) == 0
    
    def test_subtract(self):
        """Test subtraction."""
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(0, 5) == -5
        assert self.calc.subtract(10, 10) == 0
    
    def test_multiply(self):
        """Test multiplication."""
        assert self.calc.multiply(2, 3) == 6
        assert self.calc.multiply(-2, 3) == -6
        assert self.calc.multiply(0, 5) == 0
    
    def test_divide(self):
        """Test division."""
        assert self.calc.divide(10, 2) == 5
        assert self.calc.divide(5, 2) == 2.5
        assert self.calc.divide(0, 5) == 0
    
    def test_divide_by_zero(self):
        """Test division by zero error."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(5, 0)
    
    def test_history_tracking(self):
        """Test that operations are tracked in history."""
        self.calc.add(2, 3)
        self.calc.multiply(4, 5)
        history = self.calc.get_history()
        assert len(history) == 2
        assert "2 + 3 = 5" in history[0]
        assert "4 * 5 = 20" in history[1]
    
    def test_clear_history(self):
        """Test clearing calculator history."""
        self.calc.add(1, 1)
        self.calc.clear_history()
        assert self.calc.get_history() == []


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
