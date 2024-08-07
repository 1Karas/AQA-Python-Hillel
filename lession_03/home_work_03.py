# import re
#
# alice_in_wonderland = (
#     '"Would you tell me, please, which way I ought to go from here?"\n'
#     '"That depends a good deal on where you want to get to," said the Cat.\n'
#     '"I don\'t much care where ——" said Alice.\n'
#     '"Then it doesn\'t matter which way you go," said the Cat.\n'
#     '"—— so long as I get somewhere," Alice added as an explanation.\n'
#     '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
#
# )
# # Task 02: Знайти всі одинарні лапки у тексті
# single_quotes = re.findall(r"'", alice_in_wonderland)
#
# # Task 02: Відобразити всі знайдені одинарні лапки
# print("Знайдені одинарні лапки:", single_quotes)
#
# # Task 03: Вивести змінну на друк
# print(alice_in_wonderland)


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
# black_sea_s = 436402
# azov_sea_s = 37800
# total_area = black_sea_s + azov_sea_s
# print(f"Загальна площа Чорного та Азовського морів {total_area}")


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_sum = 375291
first_second_storage = 250449
second_third_storage = 222950

third_storage = total_sum - first_second_storage
second_storage = first_second_storage - third_storage
first_second = total_sum - (second_storage + third_storage)

print(f"Кількість товару на третьому складі {third_storage}")
print(f"Кількість товару на другому складі {second_storage}")
print(f"Кількість товару на першому складі {first_second}")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
# sum_on_month = 1179
# quantity_months = 18
# computer_cost = sum_on_month * quantity_months
# print(f"Вартість комп'ютера {computer_cost}")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
# a, b = 8019, 8
# a1, b1 = 9907, 9
# a2, b2 = 2789, 5
# a3, b3 = 7248, 6
# a4, b4 = 7128, 5
# a5, b5 = 19224, 9
#
# result = a % b
# result1 = a1 % b1
# result2 = a2 % b2
# result3 = a3 % b3
# result4 = a4 % b4
# result5 = a5 % b5
#
# print(f"Остачу від діленя чисел a, b: {result}")
# print(f"Остачу від діленя чисел a1, b1: {result1}")
# print(f"Остачу від діленя чисел a2, b2: {result2}")
# print(f"Остачу від діленя чисел a3, b3: {result3}")
# print(f"Остачу від діленя чисел a4, b4: {result4}")
# print(f"Остачу від діленя чисел a5, b5: {result5}")


# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
# big_pizza_count = 4
# middle_pizza_count = 2
# juice_count = 4
# cake_count = 1
# water_count = 3
# price_big_pizza = 274
# price_middle_pizza = 218
# price_juice = 35
# price_cake = 350
# price_water = 21
#
# total_sum_big_pizza = big_pizza_count * price_big_pizza
# total_sum_middle_pizza = middle_pizza_count * price_middle_pizza
# total_sum_juice_count = juice_count * price_juice
# total_sum_water_count = water_count * price_water
# money = total_sum_big_pizza + total_sum_middle_pizza + total_sum_juice_count + total_sum_water_count + price_cake
# print(f"Кількість грошей {money} грн")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
# photo = 232
# photo_on_the_page = 8
# total_page = photo / photo_on_the_page
# print(f"Кількість сторінок для усіх фото {total_page}")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

# distance = 1600
# gasoline_consumption = 9
# tank_capacity = 48
#
# count_liters = (distance / 100) * gasoline_consumption
# number_of_refills = count_liters / tank_capacity
#
# print(f"Кількість бензину {count_liters}")
# print(f"Кількість заправок {number_of_refills}")




