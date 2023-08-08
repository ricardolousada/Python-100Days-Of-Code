# Created by Ricardo Lousada
"""
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)
"""
# Write
with open("..\..\..\..\..\OneDrive - FUJITSU\Desktop\my_file.txt", mode="w") as file:
    file.write("new text with relative path\n")



"""
# Append
with open("my_file.txt", mode="a") as file:
    file.write("new text2\n")

# create a new file
with open("new_file.txt", mode="w") as file:
    file.write("New text file created")
"""