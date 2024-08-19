

def calculate_remainder(dividend, divisor):
    return dividend % divisor

'''
Calculate the remainder of the division of dividend by divisor.

Parameters:
dividend (int): The number to be divided.
divisor (int): The number by which the dividend is divided.

Returns:
int: The remainder of the division.
'''

# Основная часть программы
lst = [(8019, 8), (9907, 9), (2789, 5), (7248, 6), (7128, 5), (19224, 9)]
remainders = [calculate_remainder(dividend, divisor) for dividend, divisor in lst]
for (dividend, divisor), remainder in zip(lst, remainders):
    print(f"The remainder when {dividend} is divided by {divisor} is {remainder}.")

""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1
    results = []
    # Complete the while loop condition.
    while number * multiplier <= 25:
        result = number * multiplier
        results.append(result)
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1
    return results

multiplication_table(5)

"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def avarage(lst):
    if sum(lst) == 0:
        return 0
    return sum(lst) / len(lst)

lst = [1, 2, 3, 4, 5, 6]
print(avarage(lst))

'''Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті'''
def counter(lst):
    """
      Calculate the sum of all even numbers in the given list.

      Parameters:
      lst (list): A list of integers.

      Returns:
      int: The sum of all even numbers in the list.
      """
    return sum([integer for integer in lst if integer % 2 == 0 ])

lst = [54, 33, 5, 8, 23, 65, 88, 44]
print(counter(lst))

"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def long(lst):
    longest = max(lst, key=len)
    return longest

lst_words = ["apple", "banana", "cherry", "blueberry", "kiwi"]
long_word = long(lst_words)
print(long_word)