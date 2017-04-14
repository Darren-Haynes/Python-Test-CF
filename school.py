
"""
This module creates a school. The school is given a name plus students and
teachers that are members of that school.

Note the python Faker Module is used for generating fake info for the school
and its teachers and students.

Designed for Python 3 and Python 2 compatability
"""

from random import choice
from random import randint
from faker import Faker


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
        self.student_num = randint(100, 601)
        self.students = self.__get_students()
        students_per_grade = self.__grades_for_creating_teachers()
        self.teachers = self.__get_teachers()

    def __get_students(self):
        """Use Student() class to create a random number of students"""
        students = {}
        for _ in range(1, self.student_num + 1):
            student = self.__no_duplicate_students(students)
            students[student.name] = student.get_data(self.school_type)
        return students

    def __no_duplicate_students(self, students):
        """ Recursive function that tests if student already exists in
            'student' dictionary. If so then that student is not returned and
            a new one created. This is to stop a duplicate student name
            overriding an existing entry in dictionary 'students'. Such an
            override reduces the number of students in 'students' and this
            creates a disparity between the 'self.num_of_students' and actual
            num of students in 'students' dictionary."""
        student = Student()
        if student.name in students:
            return self.__no_duplicate_students(students)
        else:
            return student

    def __get_teachers(self):
        """Use Teachers() class to create 1 teacher for every 10 students in
           each grade"""

        teacher_grade = self.__grades_for_creating_teachers()
        teachers = {}
        # Create 1 teacher for every 10 students of each grade
        for grade in teacher_grade:
            num_of_teachers = teacher_grade[grade] // 10 + 1
            for _ in range(1, num_of_teachers + 1):
                teacher = Teacher()
                teachers[teacher.name] = {'grade': grade}
        return teachers

    def __grades_for_creating_teachers(self):
        """Before actually creating teachers for students, we need to count
           how many students are in each grade. Each teacher teaches a
           specific grade, so we need these numbers"""

        # key is the grade, value is how many students for each grade
        count = {}
        for value in self.students.values():
            k = value['grade']
            count[k] = count.get(value['grade'], 0) + 1
        return count
