"""
This module creates a school. The school is given a name plus students and
teachers that are members of that school.

Note the python Faker Module is used for generating fake info for the school
and its teachers and students.

Designed for Python 3 and Legacy Python compatability
"""

from random import choice, randint
from faker import Faker
from numpy import mean

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
    _grade_ranges = {'Elementary': ['K', 1, 2, 3, 4, 5],
                     'Middle':     [6, 7, 8],
                     'High':       [9, 10, 11, 12]}

    def __init__(self):
        """Instatiate school type, name and size to get things rolling.
           'self.school' is a dict that contains all the data for the school.
        """

uchool_type = choice(list(self._grade_ranges))
uchool_name = self._create_school_name()
uchool_size = choice(['small', 'medium', 'large'])
uchool = {self.school_name: self._create_teachers()}
ueachers = self._teachers_names()
utudents = self._students_names()
ueachers_info = self._teachers_info()
utudents_info = self._students_info()
utudents_gpa = self._get_gpa()
u
uers_info(self):
uurns dict of all teachers and their info.
u
u self.school[self.school_name]
u
unts_info(self):
uurns dict of all students and their info.
u
u {}
uacher in self.teachers:
uudents = self.teachers_info[teacher]['Students']
uta.update(students)
u
u data
u
uers_names(self):
uurn list of teachers names
u
u list(self.school[self.school_name])
u
unts_names(self):
uturn list of students names
u
uts = []
uacher in self.teachers:
uudents.extend(list(self.school[self.school_name]
u                              [teacher]['Students']))
u
u students
u
ue_school_name(self):
uate fake name for the school.
u
u
u FAKE.street_name() + " " + self.school_type \
u" School"
u(name)
u
ue_teachers(self):
uate teachers for each grade of the school.
u
u
urs = {}
uade in self._grade_ranges[self.school_type]:
ur _ in range(self._teachers_per_grade()):
u  teacher = Teacher(self.school_size, grade)
u  teachers[teacher.name] = teacher.teacher_info
u
u(teachers)
u
uers_per_grade(self):
uate a controlled random number of teachers per grade based on
u size of the school (small, medium or large).
u
uf.school_size == 'small':
un_teacher = 3
ux_teacher = 5
uelf.school_size == 'medium':
un_teacher = 6
ux_teacher = 8
u
            min_teacher = 9
            max_teacher = 12

        upper = randint(min_teacher, max_teacher)
        return upper

    def _has_gpa(self):
        """ Only High School students have GPA scores. Return true if school is
            a high school, otherwise False."""

        if self.school_type == "Elementary" or self.school_type == "Middle":
            print("Gpa's not available for {} schools.".format(
                                                    self.school_type))
            return False
        else:
            return True

    def _get_gpa(self):
        """Elementary and Middle schools don't have gpa scores, so 'None' is
           returned. For high school a dict is returned student:gpa."""

        if not self._has_gpa:
            return None
        else:
            gpas = {}
            for student in self.students_info:
                gpa = self.students_info[student]['gpa']
                gpas[student] = gpa

        return gpas

    def gpa_above(self, score):
        """Get the name of students and their GPA if GPA higher than 'score'
           parameter. Return False if no GPA higher than 'score'. Return None
           for Elementary and middle schools."""

        # Middle and elementary schools have no gpa. Return None
        if not self._has_gpa():
            return None

        # If no gpa above 'score' parameter then return False
        gpas = any(gpa > score for gpa in list(self.students_gpa.values()))
        if not gpas:
            print("No student has a GPA over {}.".format(score))
            return False
        # Return students names and their gpa if above 'score' parameter
        else:
            return {student: gpa for student, gpa in self.students_gpa.items()
                    if gpa > score}

    def gpa_below(self, score):
        """Get the name of students and their GPA if GPA less than 'score'
           parameter. Return False if no GPA less than 'score'. Return None
           for Elementary and middle schools."""

        # Middle and elementary schools have no gpa. Return None
        if not self._has_gpa():
            return None

        # If no gpa below 'score' parameter then return False
        gpas = any(gpa < score for gpa in list(self.students_gpa.values()))
        if not gpas:
            print("No student has a GPA below {}.".format(score))
            return False
        # Return students names and their gpa if below 'score' parameter
        else:
            return {student: gpa for student, gpa in self.students_gpa.items()
                    if gpa < score}

    def gpa_between(self, gpa_min, gpa_max):
        """Get the name of students and their GPA if GPA between 'gpa_min' and
           'gpa_max' parameters. Return False if no GPA between this range.
           Return None for Elementary and middle schools."""

        # Middle and elementary schools have no gpa. Return None
        if not self._has_gpa():
            return None

        # If no gpa below 'score' parameter then return False
        gpas = any(gpa > gpa_min and gpa < gpa_max for gpa in list(
                                                self.students_gpa.values()))
        if not gpas:
            print("No student has a GPA between {} and {}.".format(
                                                            gpa_min, gpa_max))
            return False
        # Return students names and their gpa if below 'score' parameter
        else:
            return {student: gpa for student, gpa in self.students_gpa.items()
                    if gpa > gpa_min and gpa < gpa_max}

    def teacher_gpa_averages(self):
        """Print teachers in order of average gpa score of all their students.
           students scores."""

        if not self._has_gpa():
            return None

        averages = {}
        for teacher in self.teachers:
            # get inner dictionary of a teachers students
            a_teachers_students = self.teachers_info.get(teacher).get(
                'Students')

            gpas = [student['gpa'] for student in a_teachers_students.values()]
            average = mean(gpas)
            averages[teacher] = round(average, 2)

        return averages

    def teacher_performance(self):
        """Print teachers in order of average gpa score (highest first) of all
           their students gpa scores."""

        if not self._has_gpa():
            return None

        averages = self.teacher_gpa_averages()
        teacher_sort = sorted(averages.items(), key=lambda x: x[1],
                              reverse=True)

        for results in teacher_sort:
            print("{0}: {1:.1f}".format(*results))

    # def teacher_performance_below(self):
        # """

    def __str__(self):
        return(str(self.school))
