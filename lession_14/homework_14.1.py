'''Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи для площі та периметру.
Властивості по типу “довжина сторони” й т.д. повинні бути приватними, та ініціалізуватись через конструктор.
Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.'''

from abc import ABC, abstractmethod

class Figure(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(Figure):
    def __init__(self, length):
        self.__length = length

    def square(self):
        return self.__length ** 2

    def perimeter(self):
        return 4 * self.__length


class Rectangle(Figure):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def square(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)


class EquilateralTriangle(Figure):
    def __init__(self, side):
        self.__side = side

    def square(self):
        return (self.__side ** 2 * (3 ** 0.5)) / 4

    def perimeter(self):
        return 3 * self.__side


figures = [
    Square(5),
    Rectangle(4, 6),
    EquilateralTriangle(3)
]

for figure in figures:
    print(f"Площа: {figure.square()}, Периметр: {figure.perimeter()}")







