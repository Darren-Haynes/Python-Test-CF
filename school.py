"""
This module creates a school. The school is given a name plus students and
teachers that are members of that school.

Note the python Faker Module is used for generating fake info for the school
and its teachers and students.

Designed for Python 3 and Legacy Python compatability
"""

from numpy import mean
import pickle
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


class School(object):
    """Create a School consisting of School name, school type, school size,
       teachers and students. All this data is stored in a dictionary.
    """

    def __init__(self):
        """Instatiate school type, name and size to get things rolling.
           'self.school' is a dict that contains all the data for the school.
        """

        self.school_name = self._create_school_name()
        self.school_size = choice(['small', 'medium', 'large'])
        self.school = {self.school_name: self._create_teachers()}
        self.teachers = self._teachers_names()
        self.students = self._students_names()
        self.teachers_info = self._teachers_info()
        self.students_info = self._students_info()

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
        for grade in self.grade_ranges:
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

    def __str__(self):
        return(str(self.school))


class High_School(School):
    """Create High School. Mainly adding GPA score data and methods."""

    grade_ranges = [9, 10, 11, 12]

    def __init__(self):
        self.school_type = "High"
        School.__init__(self)
        self.students_gpa = self._get_gpa()

    def _get_gpa(self):
        """Elementary and Middle schools don't have gpa scores, so 'None' is
           returned. For high school a dict is returned student:gpa."""

        gpas = {}
        for student in self.students_info:
            gpa = self.students_info[student]['gpa']
            gpas[student] = gpa

        return gpas

    def gpa_above(self, score):
        """Get the name of students and their GPA if GPA higher than 'score'
           parameter. Return False if no GPA higher than 'score'. Return None
           for Elementary and middle schools."""

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

    def teacher_performance(self):
        """Print teachers in order of average gpa score of all their students.
           students gpa scores."""

        averages = {}
        for teacher in self.teachers:
            # get inner dictionary of a teachers students
            a_teachers_students = self.teachers_info.get(
                teacher).get('Students')

            gpas = [x['gpa'] for x in a_teachers_students.values()]
            average = mean(gpas)
            averages[teacher] = average

        teacher_sort = sorted(averages.items(), key=lambda x: x[1],
                              reverse=True)

        for results in teacher_sort:
            print("{0}: {1:.1f}".format(*results))


class Middle_School(School):
    """Create Middle school. Almost identical to Elementary school except for
       'grade_ranges'. Unlike High school, Middle or Elementary schools do not
       have data and methods regarding GPA scores."""

    grade_ranges = [6, 7, 8]

    def __init__(self):
        self.school_type = "Middle"
        School.__init__(self)


class Elementary_School(School):
    """Create Elementary school. Almost identical to middle school except for
       'grade_ranges'. Unlike High school, Middle or Elementary schools do not
       have data and methods regarding GPA scores."""

    grade_ranges = ['K', 1, 2, 3, 4, 5]

    def __init__(self):
        self.school_type = "Elementary"
        School.__init__(self)


class Create_School(object):
    """Create a school!"""
    schools = [High_School(), Middle_School(), Elementary_School()]

    def __init__(self, type_of_school=False):
        if not type_of_school:
            self.school = choice(self.schools)
        elif type_of_school == "High":
            self.school = High_School()
        elif type_of_school == "Middle":
            self.school = Middle_School()
        elif type_of_school == "Elementary":
            self.school = Elementary_School()
        else:
            print("Type of school not recognized")

    def save(self, fname):
        with open(fname, 'wb') as f:
            pickle.dump(Create_School().school, f)

    @staticmethod
    def open(fname):
        with open(fname, 'rb') as f:
            return(pickle.load(f))

