from sqlalchemy import func, desc, select

from database.db import session
from database.models import Teacher, Student, Course, Rate, Group

def select_1():
    q = session.query(Student.fullname, func.round(func.avg(Rate.rate), 2).label('avg'))\
        .select_from(Rate)\
        .join(Student)\
        .group_by(Student.id)\
        .order_by(desc('avg'))\
        .all()
    return q

def select_2(course_id):
    q = session.query(Student.fullname, Course.name, func.round(func.avg(Rate.rate), 2).label('avg'))\
        .select_from(Rate)\
        .join(Student)\
        .join(Course)\
        .filter(Course.id == course_id)\
        .group_by(Student.id, Course.name)\
        .order_by(desc('avg'))\
        .limit(1).all()
    return q

def select_3(course_id):
    q = session.query(Group.name, func.round(func.avg(Rate.rate), 2).label('avg'),  Course.name)\
        .select_from(Rate)\
        .join(Course)\
        .join(Student)\
        .join(Group)\
        .filter(Course.id == course_id)\
        .group_by(Group.name, Course.name)\
        .all()
    return q

def select_4():
    q = session.query(func.round(func.avg(Rate.rate), 2).label('avg'))\
        .select_from(Rate)\
        .all()
    return q

def select_5(teacher_id):
    q = session.query(Teacher.fullname, Course.name)\
        .select_from(Course)\
        .join(Teacher)\
        .filter(Teacher.id == teacher_id)\
        .all()
    return q

def select_6(group_id):
    q = session.query(Group.name, Student.fullname)\
        .select_from(Student)\
        .join(Group)\
        .filter(Group.id == group_id)\
        .all()
    return q

def select_7(group_id, course_id):
    q = session.query(Student.fullname, Group.name, Course.name, Rate.rate)\
        .select_from(Rate)\
        .join(Student)\
        .join(Course)\
        .join(Group)\
        .filter(Group.id == group_id, Course.id == course_id)\
        .order_by(Course.name)\
        .all()
    return q

def select_8(teacher_id):
    q = session.query(Teacher.fullname, Course.name, func.round(func.avg(Rate.rate), 2).label('avg'))\
        .select_from(Rate)\
        .join(Course)\
        .join(Teacher)\
        .filter(Teacher.id == teacher_id)\
        .group_by(Teacher.fullname, Course.name)\
        .all()
    return q

def select_9(student_id):
    q = session.query(Course.name)\
        .select_from(Rate)\
        .join(Student)\
        .join(Course)\
        .filter(Student.id == student_id)\
        .all()
    return q

def select_10(student_id, teacher_id):
    q = session.query(Course.name)\
        .select_from(Rate)\
        .join(Student)\
        .join(Course)\
        .join(Teacher)\
        .filter(Student.id == student_id, Teacher.id == teacher_id)\
        .group_by(Course.name)\
        .all()

    return q
if __name__ == '__main__':
    # print(select_1())
    # print(select_2(1))
    # print(select_3(4))
    # print(select_4())
    # print(select_5(3))
    # print(select_6(2))
    # print(select_7(1, 4))
    # print(select_8(2))
    # print(select_9(7))
    print(select_10(1, 2))

    