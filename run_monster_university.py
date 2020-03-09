# here I need to import
from Monster_workshop_class import *
from Teacher_class import *
from Student_class import *
from Monsters_class import *

list_of_students = []
first_name = ''
last_name = ''
student_id = 0
#
while (first_name != 'quit') or (last_name != 'quit'):
    student_id += 1
    first_name = str(input("What is your first name: "))
    last_name = str(input("What is your last name: "))
    skills = str(input("What are your skills: "))

    student1 = Student('Fred', 'Alfredo', 1)
    student2 = Student('sam', 'jones', 2)
    student3 = Student('phil', 'brown', 3)

    list_of_students.append(student1)
    list_of_students.append(student2)
    list_of_students.append(student3)

teacher1 = Teacher('Frank', 'Williams', 1)
teacher2 = Teacher('Sarah', 'Smith', 2)
teacher3 = Teacher('Barry', 'lambert', 3)

print(teacher1.f_name, teacher1.l_name, teacher1.teacher_id)
print(teacher2.f_name, teacher2.l_name, teacher2.teacher_id)
print(teacher3.f_name, teacher3.l_name, teacher3.teacher_id)

student1 = Student('Fred', 'Alfredo', 1)
student2 = Student('sam', 'jones', 2)
student3 = Student('phil', 'brown', 3)

print(student1.f_name, student1.l_name, student1.student_id)
print(student2.f_name, student2.l_name, student2.student_id)
print(student3.f_name, student3.l_name, student3.student_id)

workshop1 = MonsterWorkshop('Scare School', teacher1)
workshop2 = MonsterWorkshop('Spanish', teacher2)
workshop3 = MonsterWorkshop('Child Communications', teacher3)

workshop1.list_of_attendees.append(student1.f_name)
workshop1.list_of_attendees.append(student2.f_name)
workshop1.list_of_attendees.append(student3.f_name)

print(workshop1.list_of_attendees)
#

# attendees = 0
# while True:
#     attendees += 1
#     subject = input('add a workshop to the list: ')
#     if subject == 'quit':
#         break
#


# skills = list_of_students
# list_of_students.append(Student)
# print(len(list_of_students))
# print(first_name)
# print(last_name)
