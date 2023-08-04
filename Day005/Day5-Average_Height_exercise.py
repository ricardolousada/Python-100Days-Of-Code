# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 11:31:05 2023

@author: LousadaR
"""
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sum = 0
count = 0
for student_height in student_heights:
    count += 1
    sum += student_height

average = sum/count

print(round(average))
    
