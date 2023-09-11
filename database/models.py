from sqlalchemy import  Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, declarative_base



Base = declarative_base()

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    fullname = Column(String, nullable=False, unique=True)

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    fullname = Column(String, nullable=False, unique=True)
    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship('Group', backref='students')    


class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    teacher = relationship('Teacher', backref='courses')


class Rate(Base):
    __tablename__ = 'rates'
    id = Column(Integer, primary_key=True)
    rate = Column(Integer)
    student_id = Column(Integer, ForeignKey('students.id'))
    course_id = Column(Integer, ForeignKey('courses.id'))
    created_at = Column(DateTime)
    student = relationship('Student', backref='rates')
    course = relationship('Course', backref='rates')
    
