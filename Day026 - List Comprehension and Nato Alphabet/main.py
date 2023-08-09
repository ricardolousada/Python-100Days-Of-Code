# Created by Ricardo Lousada
import random
import pandas as pd
"""
numbers = [1,2,3]
new_numbers = [n+1 for n in numbers]

name = "Ricardo"
new_letters = [letter for letter in name]
print(new_letters)

my_range = range(1,5)
my_new_list = [n*2 for n in my_range]
print(my_new_list)

names = ["Alex","Beth","Caroline","Dave", "Eleanor","Freddie"]
new_names = [name for name in names if len(name) < 5]
print(new_names)
new_names_cap = [name.upper() for name in names if len(name) > 5 ]
print(new_names_cap)
"""

#Dictionary Comprehension
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()}
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}
names = ["Alex","Beth","Caroline","Dave", "Eleanor","Freddie"]
students_scores = {student:random.randint(1,100) for student in names}
print(students_scores)

passed_students = {student:score for (student,score) in students_scores.items() if score > 60}
#print(passed_students)

#Pandas Iteration
student_data = {
    "student": ["Angela","James","Lily"],
    "score": [56,76,98]
}
student_data_frame = pd.DataFrame(student_data)
#print(student_data_frame)

for (key,value) in student_data_frame.items():
    #print(value)
    pass

# This is the way to loop trough the rows
for (index,row) in student_data_frame.iterrows():
    #print(index)
    #print(row) # a pandas series
    #print(row.student)
    #print(row.score)
    if row.student == "Angela":
        print(row.score)
