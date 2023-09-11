from datetime import datetime, timedelta
from random import randint, choice
from faker import Faker

from database.models import Student, Group, Course, Teacher, Rate
from database.db import session

fake = Faker('uk-UA')

NUM_STUDENTS = 30
NUM_TEACHERS = 5
NUM_RATES = 15
groups = ['КТРСм', 'АКТАКиТ', 'CИ']
courses = ['Українська мова', 'Математика', 'Біологія', 'Історія України', 'Англійська мова']

def create_groups():
    for group in groups:
        session.add(Group(name=group))
    session.commit()

def create_students():
    for i in range(NUM_STUDENTS):
        student = Student(fullname=fake.name(), group_id=randint(1, 3))
        session.add(student)
    session.commit()

def create_courses():
    for course in courses:
        course_obj = Course(name=course)
        course_obj.teacher_id = randint(1, NUM_TEACHERS)
        session.add(course_obj)
    session.commit()

def create_teachers():
    for i in range(NUM_TEACHERS):
        teacher = Teacher(fullname=fake.name())
        session.add(teacher)
    session.commit()

def create_rates():
    start_date = datetime.strptime('2022-09-01', '%Y-%m-%d')
    finish_date = datetime.strptime('2023-05-31', '%Y-%m-%d')

    def get_list_date(start_date, finish_date):
        result = []
        current_day = start_date
        while current_day < finish_date:
            if current_day.isoweekday() < 6:
                result.append(current_day)
            current_day += timedelta(1)
        return result
    
    list_date = get_list_date(start_date, finish_date)

    for i in range(NUM_RATES):
        rate = Rate(rate=randint(1, 12), student_id=randint(1, NUM_STUDENTS), course_id=randint(1, len(courses)), created_at=choice(list_date))
        session.add(rate)
    session.commit()

if __name__ == '__main__':
    create_groups()
    create_students()
    create_teachers()
    create_courses()
    create_rates()
