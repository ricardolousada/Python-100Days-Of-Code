# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 09:53:46 2023

@author: LousadaR
"""

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

def calculate_grade(number):
    if (number >= 91) and (number <= 100):
        grade = "Outstanding"
    elif (number >= 81) and (number <= 90):
        grade = "Exceeds Expectations"
    elif (number >= 71) and (number <= 90):
        grade = "Acceptable"
    else:
        grade = "Fail"
    
    return grade
    


#TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    student_grades[key] = calculate_grade(student_scores[key])

    

# 🚨 Don't change the code below 👇
print(student_grades)