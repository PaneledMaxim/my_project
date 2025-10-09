#1.
# squares = [x**2 for x in range(1, 11)]
# print(squares)
# aaaaaaaa
# 2.
# even_numbers = [x for x in range(1, 20) if x % 2 == 0]
# print(even_numbers)

# 3.
# words = ["python", "Java", "c++", "dog", "Rust", "go"]
# result = [word.upper() for word in words if len(word) >= 3]
# print(result)

# 4.
# class Countdown:
#     def __init__(self, n):
#         self.n = n
#
#     def __iter__(self):
#         num = self.n
#         while num >= 1:
#             yield num
#             num -= 1
#
# # Использование
# for x in Countdown(5):
#     print(x)

# 5.
# def fibonacci(n):
#     a, b = 0, 1
#     count = 0
#     while count < n:
#         yield a
#         a, b = b, a + b
#         count += 1
#
# # Пример использования
# for num in fibonacci(5):
#     print(num)

# 6.
# from decimal import Decimal, getcontext
#
#
# def deposit_calculator():
#     # Устанавливаем точность вычислений
#     getcontext().prec = 10
#
#     # Ввод данных
#     initial_amount = Decimal(input("Введите начальную сумму вклада (рубли.копейки): "))
#     interest_rate = Decimal(input("Введите годовую процентную ставку (например, 12.5): "))
#     years = Decimal(input("Введите срок вклада в годах: "))
#
#     # Расчет по формуле ежемесячной капитализации
#     # S = P * (1 + r/(12*100))^(12*t)
#     monthly_rate = interest_rate / (Decimal('12') * Decimal('100'))
#     months = Decimal('12') * years
#     final_amount = initial_amount * (Decimal('1') + monthly_rate) ** months
#
#     # Округляем до копеек (2 знака после запятой)
#     final_amount = final_amount.quantize(Decimal('0.01'))
#
#     # Расчет прибыли
#     profit = final_amount - initial_amount
#
#     # Вывод результатов
#     print("\nРезультаты расчета:")
#     print(f"Начальная сумма: {initial_amount} руб.")
#     print(f"Годовая ставка: {interest_rate}%")
#     print(f"Срок вклада: {years} лет")
#     print(f"Итоговая сумма: {final_amount} руб.")
#     print(f"Общая прибыль: {profit} руб.")
#
#
# # Запуск калькулятора
# if __name__ == "__main__":
#     deposit_calculator()

# 7.
# from fractions import Fraction
#
# # Создание дробей
# frac1 = Fraction(3, 4)
# frac2 = Fraction(5, 6)
#
# print(f"Дробь 1: {frac1}")
# print(f"Дробь 2: {frac2}")
#
# # Выполнение операций
# addition = frac1 + frac2
# subtraction = frac1 - frac2
# multiplication = frac1 * frac2
# division = frac1 / frac2
#
# # Вывод результатов
# print(f"\nРезультаты операций:")
# print(f"Сложение: {frac1} + {frac2} = {addition}")
# print(f"Вычитание: {frac1} - {frac2} = {subtraction}")
# print(f"Умножение: {frac1} * {frac2} = {multiplication}")
# print(f"Деление: {frac1} / {frac2} = {division}")

# 8.
# from datetime import datetime
#
# # Текущая дата и время
# current_datetime = datetime.now()
# print(f"Текущая дата и время: {current_datetime}")
#
# # Только текущая дата
# current_date = current_datetime.date()
# print(f"Только текущая дата: {current_date}")
#
# # Только текущее время
# current_time = current_datetime.time()
# print(f"Только текущее время: {current_time}")

# 9.
# from datetime import datetime, date
#
# # День рождения
# birthday = date(2005, 12, 9)  # год, месяц, день
#
# # Сегодняшняя дата
# today = date.today()
#
# # Сколько дней прошло с момента рождения
# days_passed = (today - birthday).days
#
# # Следующий день рождения в этом году
# next_birthday = date(today.year, birthday.month, birthday.day)
#
# # Если день рождения в этом году уже прошел, берем следующий год
# if next_birthday < today:
#     next_birthday = date(today.year + 1, birthday.month, birthday.day)
#
# # Сколько дней до следующего дня рождения
# days_to_birthday = (next_birthday - today).days
#
# # Вывод результатов
# print(f"День рождения: {birthday.strftime('%d.%m.%Y')}")
# print(f"Сегодня: {today.strftime('%d.%m.%Y')}")
# print(f"Дней прошло с рождения: {days_passed:,} дней".replace(',', ' '))
# print(f"Дней до следующего дня рождения: {days_to_birthday} дней")

# 10.
# from datetime import datetime
#
#
# def format_datetime(dt):
#     # Словари для русских названий месяцев и дней
#     months = {
#         1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля',
#         5: 'мая', 6: 'июня', 7: 'июля', 8: 'августа',
#         9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря'
#     }
#
#     # Форматируем строку
#     formatted = f"Сегодня {dt.day} {months[dt.month]} {dt.year} года, время: {dt:%H:%M}"
#
#     return formatted
#
#
# # Пример использования
# current_time = datetime.now()
# print(format_datetime(current_time))
#
# # Можно передать любую дату
# example_date = datetime(2025, 9, 26, 5, 30)
# print(format_datetime(example_date))






# git add .
# git commit -m "задание8"
# git push