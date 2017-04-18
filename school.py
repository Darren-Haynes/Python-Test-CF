
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

FAKE = Faker()


class Person(object):
    """Top level hierarchy for subclasses Teacher() and Student()."""

    def create_name(self):
        """Create a fake persons name"""
        first = FAKE.first_name()
        last = FAKE.last_name()
        return first + " " + last


class Teacher(Person):
    """Create teachers for the school"""

    def create_teachers(self, students):
        """Create 1 teacher for every 10 students in each grade"""

        teacher_grade = self.__grades_for_creating_teachers(students)
        teachers = {}
        # Create 1 teacher for every 10 students of each grade
        for grade in teacher_grade:
            num_of_teachers = teacher_grade[grade] // 10 + 1
            for _ in range(1, num_of_teachers + 1):
                teacher = Teacher()
                teachers[teacher.create_name()] = {'grade': grade}
        return teachers

    def __grades_for_creating_teachers(self, students):
        """Before actually creating teachers for students, we need to count
           how many students are in each grade. Each teacher teaches a
           specific grade, so we need these numbers"""

        # key is the grade, value is how many students for each grade
        count = {}
        for value in students.values():
            k = value['grade']
            count[k] = count.get(value['grade'], 0) + 1
        return count


class Student(Person):
    """Create students for the school"""

    def create_students(self, grade_range):
        """Use Student() class to create a random number of students"""
        students = {}
        student_num = randint(100, 601)
        for _ in range(1, student_num + 1):
            student = self.__no_duplicate_students(students)
            name = student.create_name()
            grade = self.create_grade(grade_range)
            gpa = self.create_gpa(grade_range)
            students[name] = {'grade': grade, 'gpa': gpa}
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
        if student.create_name() in students:
            return self.__no_duplicate_students(students)
        else:
            return student

    def create_grade(self, grade_range):
        """ Returns random grade to assign to student"""
        return (choice(grade_range))

    def create_gpa(self, grade_range):
        """Assign gpa to high school students only. Middle and Elementary
           School students are given a gpa value of None"""

        if 9 in grade_range:  # if 9 in grade range then its a high school
            return randint(50, 101)
        else:
            return None


class School(object):
    """Create school name, teachers and students for the school"""

    grade_ranges = {'Elementary': ['K', 1, 2, 3, 4, 5],
                    'Middle': [6, 7, 8],
                    'High': [9, 10, 11, 12]}

    def __init__(self):
        self.school_type = choice(list(self.grade_ranges))
        self.grade_range = self.grade_ranges[self.school_type]
        self.school_name = FAKE.street_name() + " " + self.school_type

        # create student instance to mint more instances of itself
        __student_instance = Student()
        self.students = __student_instance.create_students(self.grade_range)
        self.students_by_grade = self.get_students_by_grade()

        # create teacher instance to mint more instances of itself
        __teacher_instance = Teacher()
        self.teachers = __teacher_instance.create_teachers(self.students)

    def get_students_by_grade(self, grade_default=None):
        """Get a dict of students by their grades. If no keyword arg is given
           then a list of students is created for every grade in the school.
           The keyword argument accepts a single grade and produces a list
           of students just for that grade."""
        by_grade = {}
        if grade_default is None:
            for grade in self.grade_range:
                names = self.student_names_by_grade(grade)
                by_grade[grade] = names
            return by_grade

        else:
            return self.student_names_by_grade(grade_default)

    def student_names_by_grade(self, grade):
        names = []
        for name in self.students:
            g = self.students[name]['grade']
            if g == grade:
                names.append(name)
        return names
