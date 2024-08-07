# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
# def multiplication_table(number):
#     # Initialize the appropriate variable
#     multiplier = 1
#
#     # Complete the while loop condition.
#     while number * multiplier <= 25:
#         result = number * multiplier
#         print(str(number) + "x" + str(multiplier) + "=" + str(result))
#
#         # Increment the appropriate variable
#         multiplier += 1
#
# multiplication_table(6)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
# def sum_int(a, b):
#     return a + b
# c = sum_int(5, 6)
# print(c)


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

# def avarage(lst):
#     if sum(lst) == 0:
#         return 0
#     return sum(lst) / len(lst)
#
# lst = [1, 2, 3, 4, 5, 6]
# print(avarage(lst))
# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

# def revers(s):
#     return s[::-1]
#
# origin_string = "Hello World!"
# revers_string = revers(origin_string)
# print(revers_string)


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

# def long(lst):
#     longest = max(lst, key=len)
#     return longest
#
# lst = ["apple", "banana", "cherry", "blueberry", "kiwi"]
# lo = long(lst)
# print(lo)


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
# def find_substring(str1, str2):
#
#     return str1.find(str2)
#
# str1 = "Hello, world!"
# str2 = "world"
# print(find_substring(str1, str2)) # поверне 7
#
# str1 = "The quick brown fox jumps over the lazy dog"
# str2 = "cat"
# print(find_substring(str1, str2)) # поверне -1


"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

# task 7
'''Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?'''

# def area(black_sea_s, azov_sea_s ):
#     """
#        Returns the sum of two arguments.
#
#        Parameters:
#        black_sea_s (int, float): The area of the Black Sea.
#        azov_sea_s (int, float): The area of the Azov Sea.
#
#        Returns:
#        int, float: The total area of both seas.
#        """
#     return black_sea_s + azov_sea_s
# print(area(436402, 37800))


# task 8
# '''Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті'''
# def counter(lst):
#     """
#       Calculate the sum of all even numbers in the given list.
#
#       Parameters:
#       lst (list): A list of integers.
#
#       Returns:
#       int: The sum of all even numbers in the list.
#       """
#     return sum([integer for integer in lst if integer % 2 == 0 ])
#
# lst = [54, 33, 5, 8, 23, 65, 88, 44]
# print(counter(lst))

# task 9
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""

# def remainder(dividend,divisor):
#     return dividend % divisor
#     """
#     Calculate the remainder of the division of dividend by divisor.
#
#     Parameters:
#     dividend (int): The number to be divided.
#     divisor (int): The number by which the dividend is divided.
#
#     Returns:
#     int: The remainder of the division.
#     """
#
# lst = [(8019, 8), (9907,9), (2789,5), (7248, 6), (7128, 5), (19224, 9)]
# remaind = [remainder(dividend, divisor) for dividend,divisor in lst ]
# for (dividend, divisor), remainder in zip(lst, remaind):
#     print(f"The remainder when {dividend} is divided by {divisor} is {remainder}.")

# task 10
# '''Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True, інакше - False. Строку отримати за допомогою функції input()'''

# def unique(propose_string):
#     """
#     Calculate the number of unique characters in the string.
#
#     Parameters:
#     propose_string (str): The input string.
#
#     Returns:
#     int: The number of unique characters in the string.
#     """
#     return  sum([1 for char in propose_string if propose_string.count(char) == 1])
# propose_string = input('Enter symbol ')
# if len(propose_string ) > 10:
#     print(True)
# else:
#     print(False)