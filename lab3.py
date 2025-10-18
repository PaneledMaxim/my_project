def task1():
    """Генератор списка квадратов чисел"""
    print("=== Задание 1: Генератор списка квадратов ===")
    squares = [x ** 2 for x in range(1, 11)]
    print(squares)
    print()
##########

def task2():
    """Генератор списка четных чисел"""
    print("=== Задание 2: Генератор списка четных чисел ===")
    even_numbers = [x for x in range(1, 20) if x % 2 == 0]
    print(even_numbers)
    print()


def task3():
    """Генератор списка слов в верхнем регистре"""
    print("=== Задание 3: Генератор списка слов в верхнем регистре ===")
    words = ["python", "Java", "c++", "dog", "Rust", "go"]
    result = [word.upper() for word in words if len(word) >= 3]
    print(result)
    print()


def task4():
    """Итератор обратного отсчета"""
    print("=== Задание 4: Итератор обратного отсчета ===")

    class Countdown:
        def __init__(self, n):
            self.n = n

        def __iter__(self):
            num = self.n
            while num >= 1:
                yield num
                num -= 1

    # Использование
    for x in Countdown(5):
        print(x)
    print()


def task5():
    """Генератор чисел Фибоначчи"""
    print("=== Задание 5: Генератор чисел Фибоначчи ===")

    def fibonacci(n):
        a, b = 0, 1
        count = 0
        while count < n:
            yield a
            a, b = b, a + b
            count += 1

    # Пример использования
    for num in fibonacci(5):
        print(num)
    print()


def task6():
    """Калькулятор вкладов с Decimal"""
    print("=== Задание 6: Калькулятор вкладов ===")

    from decimal import Decimal, getcontext

    def deposit_calculator():
        # Устанавливаем точность вычислений
        getcontext().prec = 10

        # Ввод данных
        initial_amount = Decimal(input("Введите начальную сумму вклада (рубли.копейки): "))
        interest_rate = Decimal(input("Введите годовую процентную ставку (например, 12.5): "))
        years = Decimal(input("Введите срок вклада в годах: "))

        # Расчет по формуле ежемесячной капитализации
        # S = P * (1 + r/(12*100))^(12*t)
        monthly_rate = interest_rate / (Decimal('12') * Decimal('100'))
        months = Decimal('12') * years
        final_amount = initial_amount * (Decimal('1') + monthly_rate) ** months

        # Округляем до копеек (2 знака после запятой)
        final_amount = final_amount.quantize(Decimal('0.01'))

        # Расчет прибыли
        profit = final_amount - initial_amount

        # Вывод результатов
        print("\nРезультаты расчета:")
        print(f"Начальная сумма: {initial_amount} руб.")
        print(f"Годовая ставка: {interest_rate}%")
        print(f"Срок вклада: {years} лет")
        print(f"Итоговая сумма: {final_amount} руб.")
        print(f"Общая прибыль: {profit} руб.")

    # Запуск калькулятора
    deposit_calculator()
    print()


def task7():
    """Работа с дробями Fractions"""
    print("=== Задание 7: Работа с дробями ===")

    from fractions import Fraction

    # Создание дробей
    frac1 = Fraction(3, 4)
    frac2 = Fraction(5, 6)

    print(f"Дробь 1: {frac1}")
    print(f"Дробь 2: {frac2}")

    # Выполнение операций
    addition = frac1 + frac2
    subtraction = frac1 - frac2
    multiplication = frac1 * frac2
    division = frac1 / frac2

    # Вывод результатов
    print(f"\nРезультаты операций:")
    print(f"Сложение: {frac1} + {frac2} = {addition}")
    print(f"Вычитание: {frac1} - {frac2} = {subtraction}")
    print(f"Умножение: {frac1} * {frac2} = {multiplication}")
    print(f"Деление: {frac1} / {frac2} = {division}")
    print()


def task8():
    """Работа с датой и временем"""
    print("=== Задание 8: Работа с датой и временем ===")

    from datetime import datetime

    # Текущая дата и время
    current_datetime = datetime.now()
    print(f"Текущая дата и время: {current_datetime}")

    # Только текущая дата
    current_date = current_datetime.date()
    print(f"Только текущая дата: {current_date}")

    # Только текущее время
    current_time = current_datetime.time()
    print(f"Только текущее время: {current_time}")
    print()


def task9():
    """Расчет дней до дня рождения"""
    print("=== Задание 9: Расчет дней до дня рождения ===")

    from datetime import datetime, date

    # День рождения
    birthday = date(2005, 12, 19)  # год, месяц, день

    # Сегодняшняя дата
    today = date.today()

    # Сколько дней прошло с момента рождения
    days_passed = (today - birthday).days

    # Следующий день рождения в этом году
    next_birthday = date(today.year, birthday.month, birthday.day)

    # Если день рождения в этом году уже прошел, берем следующий год
    if next_birthday < today:
        next_birthday = date(today.year + 1, birthday.month, birthday.day)

    # Сколько дней до следующего дня рождения
    days_to_birthday = (next_birthday - today).days

    # Вывод результатов
    print(f"День рождения: {birthday.strftime('%d.%m.%Y')}")
    print(f"Сегодня: {today.strftime('%d.%m.%Y')}")
    print(f"Дней прошло с рождения: {days_passed:,} дней".replace(',', ' '))
    print(f"Дней до следующего дня рождения: {days_to_birthday} дней")
    print()


def task10():
    """Форматирование даты на русском языке"""
    print("=== Задание 10: Форматирование даты на русском ===")

    from datetime import datetime

    def format_datetime(dt):
        # Словари для русских названий месяцев и дней
        months = {
            1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля',
            5: 'мая', 6: 'июня', 7: 'июля', 8: 'августа',
            9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря'
        }

        # Форматируем строку
        formatted = f"Сегодня {dt.day} {months[dt.month]} {dt.year} года, время: {dt:%H:%M}"

        return formatted

    # Пример использования
    current_time = datetime.now()
    print(format_datetime(current_time))

    # Можно передать любую дату
    example_date = datetime(2025, 2, 21, 17, 37)
    print(format_datetime(example_date))
    print()


def main():
    """Главное меню для выбора заданий"""
    while True:
        print("=" * 50)
        print("ВЫБЕРИТЕ ЗАДАНИЕ ДЛЯ ВЫПОЛНЕНИЯ:")
        print("1. Генератор списка квадратов чисел")
        print("2. Генератор списка четных чисел")
        print("3. Генератор списка слов в верхнем регистре")
        print("4. Итератор обратного отсчета")
        print("5. Генератор чисел Фибоначчи")
        print("6. Калькулятор вкладов с Decimal")
        print("7. Работа с дробями Fractions")
        print("8. Работа с датой и временем")
        print("9. Расчет дней до дня рождения")
        print("10. Форматирование даты на русском языке")
        print("0. Выход")
        print("=" * 50)

        choice = input("Введите номер задания (1-10) или 0 для выхода: ")

        if choice == '0':
            print("Выход из программы...")
            break
        elif choice == '1':
            task1()
        elif choice == '2':
            task2()
        elif choice == '3':
            task3()
        elif choice == '4':
            task4()
        elif choice == '5':
            task5()
        elif choice == '6':
            task6()
        elif choice == '7':
            task7()
        elif choice == '8':
            task8()
        elif choice == '9':
            task9()
        elif choice == '10':
            task10()
        else:
            print("Неверный выбор! Пожалуйста, введите число от 0 до 10.")

        input("Нажмите Enter чтобы продолжить...")


# Запуск программы
if __name__ == "__main__":
    main()


# git add .
# git commit -m 'laba3 add'
# git push
