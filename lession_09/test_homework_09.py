
import unittest
from .homework_09 import calculate_remainder, multiplication_table, avarage, counter, long


class MyTest(unittest.TestCase):

    def test_positive_calculate_remainder_case(self):
        result = calculate_remainder(8019, 8)
        self.assertEqual(result, 3, "Ожидаемый остаток от деления 8019 на 8 должен быть 3")

    def test_negative_calculate_remainder_case(self):
        result = calculate_remainder(10, 5)
        self.assertEqual(result, 1, "Ожидаемый остаток от деления 10 на 5 должен быть 0")


class MyTestMultiplicationTable(unittest.TestCase):

    def test_positive_multiplication_table_case(self):
        result = multiplication_table(5)
        expected = [5, 10, 15, 20, 25]  # Ожидаемые результаты для таблицы умножения на 5
        self.assertEqual(result, expected) # Сравнение результата с ожидаемым списком

    def test_negative_multiplication_table_case(self):
        result = multiplication_table(6)
        expected = []
        self.assertEqual(result, expected)


class MyTestAvarage(unittest.TestCase):

    def test_positive_avarage_case(self):
        lst: int = [1, 2, 3, 4, 5, 6] # Позитивный тест: среднее арифметическое чисел 1, 2, 3, 4, 5, 6 должно быть равно 3.5
        expected = 3.5
        result = avarage(lst)
        self.assertEqual(result, expected)


    def test_negative_avarage_case(self):
        lst: int = [1, 2, 3, 4, 5, 6] # Негативный тест: среднее арифметическое чисел 1, 2, 3, 4, 5, 6  равно 3
        expected = 3
        result = avarage(lst)
        self.assertEqual(result, expected)

    def test_negative_avarage_case(self):
        lst: str = ['1', '2', '3', '4', '5', '6'] # Негативный тест: список состоит из строк
        expected = 3.5
        result = avarage(lst)
        self.assertEqual(result, expected)


class MyTestCounter(unittest.TestCase):

    def test_positive_counter(self):
        lst = [54, 33, 5, 8, 23, 65, 88, 44] # Позитивный тест: сумма всех парных чисел равно 194
        expected = 194
        result = counter(lst)
        self.assertEqual(result, expected)


    def test_negative_counter(self):
        lst = [54, 33, 5, 8, 23, 65, 88, 44, 48] # Негативный тест: сумма всех парных чисел завно 242
        expected = 194
        result = counter(lst)
        self.assertEqual(result, expected)


class MyTestLong(unittest.TestCase):

    def test_positive_long(self):
        lst_words = ["apple", "banana", "cherry", "blueberry", "kiwi"]
        expected = "blueberry"  # Ожидаемое самое длинное слово

        result = long(lst_words)
        self.assertEqual(result, expected)

    def test_negative_case_empty_list(self):
        # Негативный тест: проверяем, что функция возвращает None для пустого списка
        result = long([])
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
