from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
import random

Base = declarative_base()

# Ассоциативная таблица для связи студентов и курсов
enrollment_table = Table('enrollment', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    courses = relationship('Course', secondary=enrollment_table, back_populates="students")

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    students = relationship('Student', secondary=enrollment_table, back_populates="courses")

# Настройка базы данных
engine = create_engine('sqlite:///students.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def add_student(name, age):
    student = Student(name=name, age=age)
    session.add(student)
    session.commit()
    return student

def add_course(title):
    course = Course(title=title)
    session.add(course)
    session.commit()
    return course

def enroll_student(student_id, course_id):
    student = session.get(Student, student_id)
    course = session.get(Course, course_id)
    if student and course:
        course.students.append(student)
        session.commit()

# Создание курсов и студентов
courses = [add_course(f"Course {i}") for i in range(5)]
students = [add_student(f"Student {i}", 20 + i) for i in range(20)]

# Рандомное распределение студентов по курсам
for student in students:
    chosen_course = random.choice(courses)
    enroll_student(student.id, chosen_course.id)

def get_students_by_course(course_id):
    course = session.get(Course, course_id)
    return [student.name for student in course.students] if course else []

def get_courses_by_student(student_id):
    student = session.get(Student, student_id)
    return [course.title for course in student.courses] if student else []

def update_student(student_id, **kwargs):
    student = session.get(Student, student_id)
    if student:
        for key, value in kwargs.items():
            setattr(student, key, value)
        session.commit()

def delete_student(student_id):
    student = session.get(Student, student_id)
    if student:
        session.delete(student)
        session.commit()

# Использование запросов для проверки функциональности
print(get_students_by_course(1))
print(get_courses_by_student(1))

update_student(1, name="Updated Student 1")
delete_student(20)
