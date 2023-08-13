# Created by Ricardo Lousada
#File not found
"""
try:
    file = open("a_file_text.txt")
    a_dict = {"key":"value"}
    print(a_dict["key"])
except FileNotFoundError:
    file = open("a_file_text.txt","w")
    file.write("Something")
except KeyError as error_message:
    print(f"the key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    raise TypeError("This error that i made up")
"""

#Key error
#a_dict = {"key": "value"}
#value = a_dict{"non_existing key"}

#Index error
#fruit_list = ["Apple","Banana","Pear"]
#fruit = fruit_list[3]

# Type Error
#text = "abc"
#print(text + 5)

height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise  ValueError("Human height should not be over 3 met4ers")
bmi = weight / (height * height)
print(bmi)