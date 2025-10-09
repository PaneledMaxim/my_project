#1.
# squares = [x**2 for x in range(1, 11)]
# print(squares)

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

7.