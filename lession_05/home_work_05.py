# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

# people_records = [
#   ('John', 'Doe', 28, 'Engineer', 'New York'),
#   ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
#   ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
#   ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
#   ('Michael', 'Brown', 22, 'Student', 'Seattle'),
#   ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
#   ('David', 'Miller', 33, 'Software Developer', 'Austin'),
#   ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
#   ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
#   ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
#   ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
#   ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
#   ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
#   ('Ava', 'White', 42, 'Journalist', 'San Diego'),
#   ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
# ]
# 1 - Add your new record o the beginning of the given list
# my_tuple = ('Ron', 'Lemon', 20, 'Developer', 'Mexico')
# people_records.insert(0, my_tuple)
# print(people_records)

# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# people_records[1], people_records[5] = people_records[5], people_records[1]
# print(people_records)

# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

# a = people_records[6][2]
# b = people_records[10][2]
# c = people_records[13][2]
# if a > 30 and b > 30 and c > 30:
#   print(a, b, c)
# else:
#   print("None")

'''Існує деяка інформація про автомобілі з кольором, роком випуску, об'ємом двигуна, типом автомобіля та ціною.
Маємо критерії пошуку у вигляді кортежу (рік ≥, об'єм двигуна ≥, ціна ≤).
Напишіть код, який допоможе нам отримати автомобілі, які відповідають критеріям пошуку. Автомобілі повинні бути відсортовані за зростанням ціни.
Ми повинні вивести до п'яти (5) перших знайдених елементів'''
car_data = {
  'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
  'Audi': ('black', 2020, 2.0, 'sedan', 55000),
  'BMW': ('white', 2018, 3.0, 'suv', 70000),
  'Lexus': ('gray', 2016, 2.5, 'coupe', 45000),
  'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
  'Honda': ('red', 2017, 1.5, 'sedan', 30000),
  'Ford': ('green', 2019, 2.3, 'suv', 40000),
  'Chevrolet': ('purple', 2020, 1.4, 'hatchback', 22000),
  'Nissan': ('pink', 2018, 1.8, 'sedan', 35000),
  'Volkswagen': ('brown', 2021, 1.4, 'hatchback', 28000),
  'Hyundai': ('gray', 2019, 1.6, 'suv', 32000),
  'Kia': ('white', 2020, 2.0, 'sedan', 28000),
  'Volvo': ('silver', 2017, 1.8, 'suv', 45000),
  'Subaru': ('blue', 2018, 2.5, 'wagon', 35000),
  'Mazda': ('red', 2019, 2.5, 'sedan', 32000),
  'Porsche': ('black', 2017, 3.0, 'coupe', 80000),
  'Jeep': ('green', 2021, 3.0, 'suv', 50000),
  'Chrysler': ('gray', 2016, 2.4, 'sedan', 22000),
  'Dodge': ('yellow', 2020, 3.6, 'suv', 40000),
  'Ferrari': ('red', 2019, 4.0, 'coupe', 500000),
  'Lamborghini': ('orange', 2021, 5.0, 'coupe', 800000),
  'Maserati': ('blue', 2018, 4.7, 'coupe', 100000),
  'Bugatti': ('black', 2020, 8.0, 'coupe', 2000000),
  'McLaren': ('yellow', 2017, 4.0, 'coupe', 700000),
  'Rolls-Royce': ('white', 2019, 6.8, 'sedan', 500000),
  'Bentley': ('gray', 2020, 4.0, 'coupe', 300000),
  'Jaguar': ('red', 2016, 2.0, 'suv', 40000),
  'Land Rover': ('green', 2018, 3.0, 'suv', 60000),
  'Tesla': ('silver', 2020, 0.0, 'sedan', 60000),
  'Acura': ('white', 2017, 2.4, 'suv', 40000),
  'Cadillac': ('black', 2019, 3.6, 'suv', 55000),
  'Infiniti': ('gray', 2018, 2.0, 'sedan', 35000),
  'Lincoln': ('white', 2021, 2.0, 'suv', 50000),
  'GMC': ('blue', 2016, 1.5, 'pickup', 30000),
  'Ram': ('black', 2019, 5.7, 'pickup', 40000),
  'Chevy': ('red', 2017, 2.4, 'pickup', 35000),
  'Dodge Ram': ('white', 2020, 3.6, 'pickup', 45000),
  'Ford F-Series': ('gray', 2021, 3.5, 'pickup', 50000),
  'Nissan Titan': ('silver', 2018, 5.6, 'pickup', 35000)
}
search_criteria = (2017, 1.6, 36000)

car_filter = {key: value for key, value in car_data.items() if value[1] >= 2017 and value[2] >= 1.6 and value[4] <= 36000}

sorted_cars = dict(sorted(car_filter.items(), key=lambda item: item[1][4])[:5])

for key, value in sorted_cars.items():
  year = value[1]
  engine_capacity = value[2]
  price = value[4]
  print(f"Car: {key}, Year: {year}, Engine_capacity: {engine_capacity}, Price: {price}")