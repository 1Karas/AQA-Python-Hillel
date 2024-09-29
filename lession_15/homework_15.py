import functools

'''Напишіть генератор, який повертає послідовність парних чисел від 0 до N.'''

def even_numbers_up_to_n(n):
    return [i for i in range(0, n+1, 2)]

# Пример использования
n = 10
print(even_numbers_up_to_n(n))

'''Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.'''

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci_generator()
for _ in range(10):
    print(next(fib))

'''Реалізуйте ітератор для зворотного виведення елементів списку.'''

def iteration_list(num_list):
    num_list.reverse()

num_list = [2, 5, 7, 65, 87, 12]
iteration_list(num_list)
print(num_list)

'''Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.'''

class EvenNumbers:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration

        else:
            result = self.current
            self.current += 2
            return result

n = 10
even_iterator = EvenNumbers(n)
for num in even_iterator:
    print(num)


'''Напишіть декоратор, який логує аргументи та результати викликаної функції.'''

def log_function_data(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} вернула {value!r}")
        return value
    return wrapper

@log_function_data
def add(x, y):
    return x + y

result = add(5, 3)


def handle_exceptions(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Возникла ошибка в функции {func.__name__}: {str(e)}")

    return wrapper

@handle_exceptions
def divide(x, y):
    return x / y

result = divide(10, 0)
print(result)
