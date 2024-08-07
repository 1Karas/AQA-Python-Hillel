# '''Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True, інакше - False. Строку отримати за допомогою функції input()'''
#
# propose_string = input('Enter symbol ')
# unic_counter = sum([1 for char in propose_string if propose_string.count(char) == 1])
# if unic_counter > 10:
#     print(True)
# else:
#     print(False)
#
# '''Напишіть цикл, який буде вимагати від користувача ввести слово,
# в якому є літера "h" (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".'''
# is_correct = False
#
# while not is_correct:
#   provided_word = input("Enter symbol ").islower()
#   if propose_string.find('h') != -1:
#     is_correct = True
#

# '''Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
#  Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг,
#  які присутні в lst1. Данні в лісті можуть бути будь якими'''
#
# lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
# disired_list: list = [item for item in lst1 if isinstance(item, str)]
# print(disired_list)

# '''Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті'''
# lst = [54, 33, 5, 8, 23, 65, 88, 44]
# result = sum([integer for integer in lst if integer % 2 == 0 ])
# print(result)