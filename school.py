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

    def __init__(self):
        Person.__init__(self)


class School(object):
    """Create school name and teachers and students for the school"""

    def __init__(self):
        fake = Faker()
        school_types = ['Elementary', 'High', 'Middle']
        self.school_type = choice(school_types)
        self.school_name = fake.street_name() + " " + self.school_type

        # Create dict of random number of students
        self.students = {}
        self.num_of_students = randint(100, 601)
        for _ in range(0, self.num_of_students):
            student = Student()
            self.students[student.name] = 'data TBA'

        # Create dict of teachers
        self.teachers = {}
        # Create 1 teacher for every 10 students
        self.num_of_teachers = self.num_of_students // 10 + 1
        for _ in range(0, self.num_of_teachers + 1):
            teacher = Teacher()
            self.teachers[teacher.name] = 'data TBA'


# For initial testing
print(' ')
school = School()
print(school.school_name)
print(school.num_of_students)
print(school.students)
print(school.teachers)
print('\n')
