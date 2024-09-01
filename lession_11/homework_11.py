class Student:
    def __init__(self, first_name, last_name, age, average_score):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_score = average_score

    def get_info(self):
        return f'Hello, my name is {self.first_name} {self.last_name} I am {self.age} years old and my average score is {self.average_score}'

    def change_average_score(self, new_average_score):
        self.average_score = new_average_score
        return self.average_score

student1 = Student('Jon', 'Smit', 20, 90)
print(student1.first_name)  # Выводит: Jon
print(student1.average_score)  # Выводит: 90

# Метод change_average_score обновляет значение average_score, но не возвращает ничего (возвращает None)
print(student1.change_average_score(50))  # Выводит: None

# Теперь average_score обновлено, и hello метод будет использовать новое значение average_score
print(student1.get_info())  # Выводит: Hello, my name is Jon and my average score is 50