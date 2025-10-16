# 1. Декоратор логирования
def logger(func):
    def wrapper(*args, **kwargs):
        # Перед вызовом функции
        print(f"Вызов функции {func.__name__} с аргументами {args} и {kwargs}")

        # Выполнение функции
        result = func(*args, **kwargs)

        # После выполнения функции
        print(f"Функция {func.__name__} вернула {result}")
        return result

    return wrapper


# Применение декоратора к функциям
@logger
def add(a, b):
    """Возвращает сумму двух чисел"""
    return a + b


@logger
def divide(a, b):
    """Возвращает результат деления"""
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a / b


@logger
def greet(name):
    """Выводит приветствие"""
    return f"Привет, {name}!"


# 2. Декоратор доступа
def require_role(allowed_roles):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            # Проверка роли пользователя
            if user.get('role') in allowed_roles:
                return func(user, *args, **kwargs)
            else:
                print(f"Доступ запрещён пользователю {user['name']}")
                return None

        return wrapper

    return decorator


# Пример использования декоратора доступа
@require_role(["admin"])
def delete_database(user):
    print(f"База данных удалена пользователем {user['name']}")
    return "Успешно удалено"


@require_role(["admin", "manager"])
def edit_settings(user):
    print(f"Настройки изменены пользователем {user['name']}")
    return "Настройки обновлены"


@require_role(["user", "admin", "manager"])
def view_data(user):
    print(f"Данные просмотрены пользователем {user['name']}")
    return "Данные показаны"


# Тестирование
if __name__ == "__main__":
    print("=== Тестирование декоратора логирования ===")

    # Тестирование функций с логированием
    print("\n1. Тестирование add():")
    result1 = add(5, 3)
    print(f"Результат: {result1}")

    print("\n2. Тестирование divide():")
    result2 = divide(10, 2)
    print(f"Результат: {result2}")

    print("\n3. Тестирование divide() с делением на ноль:")
    result3 = divide(10, 0)
    print(f"Результат: {result3}")

    print("\n4. Тестирование greet():")
    result4 = greet("Анна")
    print(f"Результат: {result4}")

    print("\n" + "=" * 50)
    print("=== Тестирование декоратора доступа ===")

    # Создание пользователей с разными ролями
    users = [
        {"name": "Алексей", "role": "admin"},
        {"name": "Мария", "role": "manager"},
        {"name": "Иван", "role": "user"},
        {"name": "Петр", "role": "guest"}
    ]

    # Тестирование доступа для разных пользователей
    for user in users:
        print(f"\n--- Тестирование для пользователя: {user['name']} (роль: {user['role']}) ---")

        print("Попытка удалить базу данных:")
        delete_database(user)

        print("Попытка изменить настройки:")
        edit_settings(user)

        print("Попытка просмотреть данные:")
        view_data(user)