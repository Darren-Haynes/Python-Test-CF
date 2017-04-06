"""
This module creates a school. The school is given a name plus students and
teachers that are members of that school.

Note the python Faker Module is used for generating fake info for the school
and its teachers and students.

Designed for Python 3 and Python 2 compatability
"""

from faker import Faker
from random import choice
from random import randint


class Person(object):
    """Top level hierarchy for subclasses Teacher() and Student()."""

    def __init__(self):
        fake = Faker()
        first = fake.first_name()
        last = fake.last_name()
        self.name = first + " " + last


class Teacher(Person):
    """Create teachers for the school"""

    def __init__(self):
        Person.__init__(self)


class Student(Person):
    """Create students for the school"""

    e_grades = ['K', 1, 2, 3, 4, 5]
    m_grades = [6, 7, 8]
    h_grades = [9, 10, 11, 12]

    def __init__(self):
        Person.__init__(self)

    def get_data(self, school_type):
        data = {}
        grade = self.get_grade(school_type)
        data['grade'] = grade
        data['gpa'] = self.get_gpa(school_type)
        return data

    def get_grade(self, school_type):
        """Assign a grade to each student"""

        if school_type == 'Elementary':
            return choice(self.e_grades)
        elif school_type == 'Middle':
            return choice(self.m_grades)
        else:
            return choice(self.h_grades)

    def get_gpa(self, school_type):
        """Assign gpa to high school students only. Middle and Elementary
           School students are given a gpa value of 'NA'"""

        if school_type == 'High':
            return randint(50, 101)
        else:
            return 'NA'


class School(object):
    """Create school name and teachers and students for the school"""

    def __init__(self):
        fake = Faker()
        school_types = ['Elementary', 'High', 'Middle']
        self.school_type = choice(school_types)
        self.school_name = fake.street_name() + " " + self.school_type

        # Create dict of random number of students
        self.students = {}
        self.student_num = randint(100, 601)
        for _ in range(0, self.student_num):
            student = Student()
            self.students[student.name] = student.get_data(self.school_type)

        # Create dict of teachers
        self.teachers = {}
        # Create 1 teacher for every 10 students
        self.num_of_teachers = self.student_num // 10 + 1
        for _ in range(0, self.num_of_teachers + 1):
            teacher = Teacher()
            self.teachers[teacher.name] = 'data TBA'
