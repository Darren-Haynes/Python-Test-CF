# Python Pretest for Code Fellows 401 Course

### How to Create, Save and Open a School

First import the module
`from school import Create_School`

To create a school
`myschool = Create_School()`
You now have a school with students and teachers. The school randomly creates a
"High", "Middle" or "Elementary" school, and randomly creates the size of the
school: 'small', 'medium' or 'large'. The size of the school determines how
many teachers teach per grade; each teacher is randomly assigned 7-10 students.
Other information about the school can be accessed as outlined in the
methods/attributes section below.

If you prefer to choose which school to create, then pass the type of school as
a parameter when creating it
`myschool = Create_School('High')` or
`myschool = Create_School('Middle')` or
`myschool = Create_School('Elementary')`

To save the school as a pickle file
`myschool.save('name-of-file-to-save-to')`

To open saved school into a variable
`myschool = Create_School().open('saved-file')`

### Use the following methods/attributes to get information about the school:

Dict containing all data about school
`myschool.school`

School name
`myschool.school_name`

Type of school
`myschool.school_type`

Num of students at school
`myschool.student_num`

List of students names at the school
`myschool.students`

List of teachers names at the school
`myschool.teachers`

Dict of teacher plus their info (name, students, age, etc)
`myschool.teachers_info`

Dict of students plus their info (name, students, age, etc)
`myschool.students_info`

List all students with a gpa above given parameter
`myschool.gpa_above(80)`

List all students with a gpa below given parameter
`myschool.gpa_below(70)`

List all students with a gpa between two given parameters
`myschool.gpa_below(94, 101)`

List teachers in order of the average gpa performance of their students
`myschool.teacher_performance()`
