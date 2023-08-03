# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 10:18:00 2023

@author: LousadaR
"""

# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
column = int(position[0]) #maps with row
row = int(position[1])
if row == 1:
    row1[column-1] = "X"
elif row == 2:
    row2[column-1] = "X"
else:
    row3[column-1] = "X"
    
# Solution Implementation

#selected_row = map[column-1]
#selected_row[row-1] = "X"
# or map[row-1][column-1] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")