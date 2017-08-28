# Python Pretest for Code Fellows 401 Course

### How to use this Module:

First import the module
`from school import School()`

To create a school
`myschool = School()`
You now have a school with students and teachers. The school randomly creates a "High", "Middle" or "Elementary" school. The total number of students at the school are chosen from a random number between 100-600.

### Use the following commands to get information about the school:

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

List all students with a gpa between two given parameter
`myschool.gpa_below(94, 101)`

List teachers in order of the average gpa performance of their students
`myschool.teacher_performance()`
