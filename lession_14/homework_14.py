'''Завдання 1

Створіть клас Employee, який має атрибути name та salary. Далі створіть два класи, Manager та Developer, які успадковуються від Employee.
Клас Manager повинен мати додатковий атрибут department, а клас Developer - атрибут programming_language.

Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer. Цей клас представляє керівника з команди розробників.
Клас TeamLead повинен мати всі атрибути як Manager (ім'я, зарплата, відділ), а також атрибут team_size, який вказує на кількість розробників у команді,
якою керує керівник.

Напишіть тест, який перевіряє наявність атрибутів з Manager та Developer у класі TeamLead'''

import pytest
class Employee:

    def __init__(self, name,  salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name,  salary, department):
        super().__init__(name, salary)
        self.department = department

class Developer(Employee):
    def __init__(self,name, salary, programming_language):
        super().__init__( name, salary)
        self.programming_language = programming_language

class TeamLead:
    def __init__(self, name, salary, department, programming_language):
        self.employee = Employee(name, salary)
        self.manager = Manager(name, salary, department)
        self.developer = Developer(name, salary, programming_language)


def test_teamlead_attributes():
    name = "John Snow"
    salary = 100000
    department = "Engineering"
    programming_language = "Python"

    team_lead = TeamLead(name, salary, department, programming_language)

    assert team_lead.manager.department == department, "Атрибут department должен быть корректным"
    assert team_lead.developer.programming_language == programming_language, "Атрибут programming_language должен быть корректным"


