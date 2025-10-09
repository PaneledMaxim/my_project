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

6.
