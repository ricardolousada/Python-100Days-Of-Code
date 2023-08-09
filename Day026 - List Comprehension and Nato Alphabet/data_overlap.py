with open("file1.txt") as file:
    list1=(file.readlines())
#print(list1)
#print(type(list1))

list1_numbers = [int(n) for n in list1]
#print(list1_numbers)

with open("file2.txt") as file:
    list2=(file.readlines())
#print(list2)
#print(type(list2))

list2_numbers = [int(n) for n in list2]
#print(list2_numbers)

result = [n for n in list1_numbers if n in list2_numbers]

# Write your code above 👆

print(result)
