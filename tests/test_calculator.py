#!/usr/bin/env python3
"""
Тесты для калькулятора Акселион.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculator import Calculator

def test_calculator_initialization():
    """Тест инициализации калькулятора."""
    calc = Calculator()
    assert len(calc.history) == 0
    assert calc.current_result == 0
    print("✓ test_calculator_initialization passed")

def test_addition():
    """Тест операции сложения."""
    calc = Calculator()
    result = calc.add(5, 3)
    assert result == 8
    assert len(calc.history) == 1
    assert calc.history[0]['operation'] == "5.0 + 3.0"
    print("✓ test_addition passed")

def test_subtraction():
    """Тест операции вычитания."""
    calc = Calculator()
    result = calc.subtract(10, 4)
    assert result == 6
    assert calc.history[0]['operation'] == "10.0 - 4.0"
    print("✓ test_subtraction passed")

def test_multiplication():
    """Тест операции умножения."""
    calc = Calculator()
    result = calc.multiply(7, 6)
    assert result == 42
    assert calc.history[0]['operation'] == "7.0 * 6.0"
    print("✓ test_multiplication passed")

def test_division():
    """Тест операции деления."""
    calc = Calculator()
    result = calc.divide(15, 3)
    assert result == 5
    assert calc.history[0]['operation'] == "15.0 / 3.0"
    print("✓ test_division passed")

def test_division_by_zero():
    """Тест деления на ноль."""
    calc = Calculator()
    try:
        calc.divide(10, 0)
        assert False, "Должно было возникнуть исключение ValueError"
    except ValueError as e:
        assert str(e) == "Ошибка: деление на ноль!"
        print("✓ test_division_by_zero passed")

def test_power():
    """Тест возведения в степень."""
    calc = Calculator()
    result = calc.power(2, 3)
    assert result == 8
    assert calc.history[0]['operation'] == "2.0 ^ 3.0"
    print("✓ test_power passed")

def test_history():
    """Тест работы с историей."""
    calc = Calculator()
    
    # Добавляем несколько операций
    calc.add(1, 2)
    calc.subtract(5, 3)
    
    assert len(calc.history) == 2
    assert calc.history[0]['operation'] == "1.0 + 2.0"
    assert calc.history[0]['result'] == 3
    assert calc.history[1]['operation'] == "5.0 - 3.0"
    assert calc.history[1]['result'] == 2
    
    # Проверяем отображение истории
    history_text = calc.show_history()
    assert "История вычислений:" in history_text
    assert "1.0 + 2.0 = 3.0" in history_text
    assert "5.0 - 3.0 = 2.0" in history_text
    
    # Очищаем историю
    calc.clear_history()
    assert len(calc.history) == 0
    assert calc.show_history() == "История пуста."
    
    print("✓ test_history passed")

def test_clear_history():
    """Тест очистки истории."""
    calc = Calculator()
    calc.add(10, 20)
    calc.subtract(50, 30)
    
    assert len(calc.history) == 2
    
    calc.clear_history()
    assert len(calc.history) == 0
    assert calc.current_result == 20  # Последний результат должен сохраниться
    
    print("✓ test_clear_history passed")

def run_all_tests():
    """Запуск всех тестов."""
    print("Запуск тестов калькулятора Акселион...")
    print("=" * 50)
    
    test_calculator_initialization()
    test_addition()
    test_subtraction()
    test_multiplication()
    test_division()
    test_division_by_zero()
    test_power()
    test_history()
    test_clear_history()
    
    print("=" * 50)
    print("Все тесты успешно пройдены! ✓")

if __name__ == "__main__":
    run_all_tests()
