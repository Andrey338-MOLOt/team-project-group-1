"""Console interface for calculator."""

from src.calculator import Calculator


def display_menu():
    """Display calculator menu."""
    print("\n" + "="*40)
    print("          КАЛЬКУЛЯТОР")
    print("="*40)
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    print("5. Показать историю")
    print("6. Очистить историю")
    print("0. Выход")
    print("="*40)


def get_number(prompt: str) -> float:
    """Get valid number from user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите число!")


def main():
    """Main calculator interface."""
    calc = Calculator()
    
    while True:
        display_menu()
        choice = input("Выберите операцию (0-6): ")
        
        if choice == "0":
            print("Выход из калькулятора. До свидания!")
            break
        
        elif choice == "1":
            a = get_number("Введите первое число: ")
            b = get_number("Введите второе число: ")
            result = calc.add(a, b)
            print(f"Результат: {a} + {b} = {result}")
        
        elif choice == "2":
            a = get_number("Введите первое число: ")
            b = get_number("Введите второе число: ")
            result = calc.subtract(a, b)
            print(f"Результат: {a} - {b} = {result}")
        
        elif choice == "3":
            a = get_number("Введите первое число: ")
            b = get_number("Введите второе число: ")
            result = calc.multiply(a, b)
            print(f"Результат: {a} * {b} = {result}")
        
        elif choice == "4":
            a = get_number("Введите первое число: ")
            b = get_number("Введите второе число: ")
            try:
                result = calc.divide(a, b)
                print(f"Результат: {a} / {b} = {result}")
            except ValueError as e:
                print(f"Ошибка: {e}")
        
        elif choice == "5":
            history = calc.get_history()
            if history:
                print("\nИстория вычислений:")
                for i, entry in enumerate(history, 1):
                    print(f"{i}. {entry}")
            else:
                print("История пуста.")
        
        elif choice == "6":
            calc.clear_history()
            print("История очищена.")
        
        else:
            print("Неверный выбор. Попробуйте снова.")
        
        input("\nНажмите Enter чтобы продолжить...")


if __name__ == "__main__":
    main()
