from student import Student
import flask
studets = []
with open('resources/mapping.csv','r') as src:
    data = src.read().splitlines()
    for row in data:
        elements = row.split(',')
        studets.append(Student(elements[0],elements[1],list(elements[2:])))


sa = []
for student in studets:sa.append(f"{student.get_roll_no()},{student.get_name()},{student.get_gmeet_names()}")


for ele in sa:print(ele) 