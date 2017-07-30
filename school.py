"""
This module creates a school. The school is given a name plus students and
teachers that are members of that school.

Note the python Faker Module is used for generating fake info for the school
and its teachers and students.

Designed for Python 3 and Legacy Python compatability
"""

from random import choice, randint
from faker import Faker

FAKE = Faker()


class Person(object):
    """Top level hierarchy for subclasses Teacher() and Student()."""

    @staticmethod
    def fake_name():
        """Create a fake persons name"""

        return(FAKE.first_name() + " " + FAKE.last_name())


class Student(Person):

    """Create Students. """

    def __init__(self, grade):
        """Create students name, grade and info. """
        self.name = self.fake_name()
        self.grade = grade
        self.student_info = self._student_info()

    def _student_info(self):
        """Create dictionary that contains students age and gpa.
        """
        info = {}
        info['age'] = self.student_age()
        info['gpa'] = self.gpa()
        info['grade'] = self.grade

        return info

    def gpa(self):
        """Create gpa for grades 9 and above. No gpa for grades below 9.
        """
        if self.grade == 'K':
            return None
        if self.grade < 9:
            return None
        else:
            return randint(51, 100)

    def student_age(self):
        """Assign student an age based on their school grade.
        """
        grade_age = randint(5, 6)
        if self.grade == 'K':
            return grade_age
        else:
            return self.grade + grade_age


class Teacher(Person):

    """Create a Teacher. """

    def __init__(self, school_size, grade):
        """Instantiatie teachers name, grade, size of school taught in.
           Plus other info
        """
        self.name = self.fake_name()
        self.school_size = school_size
        self.grade = grade
        self.teacher_info = self._teacher_info()

    def _teacher_info(self):
        """Create dictionary containing teacher's teaching grade, age and
           students.
        """
        info = {}
        info['Grade'] = self.grade
        info['Age'] = randint(21, 65)
        info['Students'] = self._create_students()

        return info

    def _create_students(self):
        """Create 7 - 10 students per teacher.
        """
        students_per_teacher = randint(7, 10)
        students = {}
        for _ in range(students_per_teacher):
            student = Student(self.grade)
            students[student.name] = student.student_info

        return students


class School (object):

    """Create a School consisting of School name, school type, school size,
       teachers and students. All this data is stored in a dictionary.
    """
    _grade_ranges = {'High':       [9, 10, 11, 12]}
    # _grade_ranges = {'Elementary': ['K', 1, 2, 3, 4, 5],
                     # 'Middle':     [6, 7, 8],
                     # 'High':       [9, 10, 11, 12]}

    def __init__(self):
        """Instatiate school type, name and size to get things rolling.
           'self.school' is a dict that contains all the data for the school.
        """

        self.school_type = choice(list(self._grade_ranges))
        self.school_name = self._create_school_name()
        self.school_size = choice(['small', 'medium', 'large'])
        self.school = {self.school_name: self._create_teachers()}
        self.teachers = self._teachers_names()
        self.students = self._students_names()
        self.teachers_info = self._teachers_info()
        self.students_info = self._students_info()
        self.students_gpa = self._get_gpa()

    def _teachers_info(self):
        """Returns dict of all teachers and their info.
        """
        return self.school[self.school_name]

    def _students_info(self):
        """Returns dict of all students and their info.
        """
        data = {}
        for teacher in self.teachers:
            students = self.teachers_info[teacher]['Students']
            data.update(students)

        return data

    def _teachers_names(self):
        """Return list of teachers names
        """
        return list(self.school[self.school_name])

    def _students_names(self):
        """ Return list of students names
        """
        students = []
        for teacher in self.teachers:
            students.extend(list(self.school[self.school_name]
                                            [teacher]['Students']))

        return students

    def _create_school_name(self):
        """Create fake name for the school.
        """

        name = FAKE.street_name() + " " + self.school_type \
            + " School"
        return(name)

    def _create_teachers(self):
        """Create teachers for each grade of the school.
        """

        teachers = {}
        for grade in self._grade_ranges[self.school_type]:
            for _ in range(self._teachers_per_grade()):
                teacher = Teacher(self.school_size, grade)
                teachers[teacher.name] = teacher.teacher_info

        return(teachers)

    def _teachers_per_grade(self):
        """Create a controlled random number of teachers per grade based on
           the size of the school (small, medium or large).
        """
        if self.school_size == 'small':
            min_teacher = 3
            max_teacher = 5
        elif self.school_size == 'medium':
            min_teacher = 6
            max_teacher = 8
        else:
            min_teacher = 9
            max_teacher = 12

        upper = randint(min_teacher, max_teacher)
        return upper

    def _get_gpa(self):
        """Elementary and Middle schools don't have gpa scores, so 'None' is
           returned. For high school a dict is returned student:gpa
        """
        gpas = {}
        if self.school_type == "Elementary" or self.school_type == "Middle":
            return None
        else:
            for student in self.students_info:
                gpa = self.students_info[student]['gpa']
                gpas[student] = gpa

        return gpas

    def gpa_above(self, score):
        """Get the name of students and their GPA, if GPA higher than 'score'
           parameter. Return
        """

        # Middle and elementary schools have no gpa. Return None
        if not self.students_gpa:
            print("Gpa's not available for {} schools.".format(
                                                    self.school_type))
            return None

        # If no gpa above 'score' parameter then return False
        if len([self.students_gpa[gpa] for gpa in self.students_gpa]) == 0:
            print("No student has a GPA over {}.".format(score))
            return False
        # Return students names and their gpa if above 'score' parameter
        else:
            return {student: gpa for student, gpa in self.students_gpa.items()
                    if gpa > score}

    def __str__(self):
        return(str(self.school))
