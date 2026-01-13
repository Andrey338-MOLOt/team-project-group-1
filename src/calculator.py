#!/usr/bin/env python3
"""
Простой консольный калькулятор с поддержкой базовых операций и историей вычислений.
"""

class Calculator:
    def __init__(self):
        """Инициализация калькулятора с пустой историей."""
        self.history = []
        self.current_result = 0
    
    def add(self, a: float, b: float) -> float:
        """Сложение двух чисел."""
        result = a + b
        self._add_to_history(f"{a} + {b}", result)
        return result
    
    def subtract(self, a: float, b: float) -> float:
        """Вычитание двух чисел."""
        result = a - b
        self._add_to_history(f"{a} - {b}", result)
        return result
    
    def multiply(self, a: float, b: float) -> float:
        """Умножение двух чисел."""
        result = a * b
        self._add_to_history(f"{a} * {b}", result)
        return result
    
    def divide(self, a: float, b: float) -> float:
        """Деление двух чисел."""
        if b == 0:
            raise ValueError("Ошибка: деление на ноль!")
        result = a / b
        self._add_to_history(f"{a} / {b}", result)
        return result
    
    def power(self, a: float, b: float) -> float:
        """Возведение в степень."""
        result = a ** b
        self._add_to_history(f"{a} ^ {b}", result)
        return result
    
    def _add_to_history(self, operation: str, result: float):
        """Добавление операции в историю."""
        self.history.append({"operation": operation, "result": result})
        self.current_result = result
    
    def show_history(self) -> str:
        """Отображение истории вычислений."""
        if not self.history:
            return "История пуста."
        
        history_str = "История вычислений:\n"
        for i, entry in enumerate(self.history, 1):
            history_str += f"{i}. {entry['operation']} = {entry['result']}\n"
        return history_str
    
    def clear_history(self):
        """Очистка истории вычислений."""
        self.history = []
        print("История очищена.")

def main():
    """Основная функция калькулятора."""
    calc = Calculator()
    print("Добро пожаловать в калькулятор Акселион!")
    print("Доступные операции: +, -, *, /, ^, history, clear, exit")
    
    while True:
        try:
            command = input("\nВведите команду: ").strip().lower()
            
            if command == 'exit':
                print("Выход из калькулятора.")
                break
            
            elif command == 'history':
                print(calc.show_history())
            
            elif command == 'clear':
                calc.clear_history()
            
            elif command in ['+', '-', '*', '/', '^']:
                try:
                    a = float(input("Введите первое число: "))
                    b = float(input("Введите второе число: "))
                    
                    if command == '+':
                        result = calc.add(a, b)
                    elif command == '-':
                        result = calc.subtract(a, b)
                    elif command == '*':
                        result = calc.multiply(a, b)
                    elif command == '/':
                        result = calc.divide(a, b)
                    elif command == '^':
                        result = calc.power(a, b)
                    
                    print(f"Результат: {result}")
                    
                except ValueError as e:
                    print(f"Ошибка: {e}")
                except Exception as e:
                    print(f"Неизвестная ошибка: {e}")
            
            else:
                print("Неизвестная команда. Используйте: +, -, *, /, ^, history, clear, exit")
                
        except KeyboardInterrupt:
            print("\n\nВыход из калькулятора.")
            break
        except Exception as e:
            print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
