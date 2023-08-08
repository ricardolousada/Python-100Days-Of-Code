#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

#open the file with the list of names
with open("C:\\Users\\LOUSADAR\\OneDrive - FUJITSU\\Documents\\Pessoal\\Learning\\Python100DaysOfCode\\Python-100Days-Of-Code\\Day024 - Files, Directories and Paths\\\Mail Merge Project Start\Input\\Names\invited_names.txt") as file:
    list_of_names = file.readlines()

#print(list_of_names)

# clean the list of names
for i in range(len(list_of_names)):
    list_of_names[i] = list_of_names[i].replace("\n","")
    #print(new_name)

#print(list_of_names)

#open the leter and put a sentence/each line in a list
with open("C:\\Users\\LOUSADAR\\OneDrive - FUJITSU\\Documents\\Pessoal\\Learning\\Python100DaysOfCode\\Python-100Days-Of-Code\\Day024 - Files, Directories and Paths\\\Mail Merge Project Start\Input\\Letters\starting_letter.txt") as file:
    lines_of_letter = file.readlines()

#print(lines_of_letter)

#create a string with the letter contents expect for the first line:
letter_string =""
for line in range(1,len(lines_of_letter)):
    letter_string += lines_of_letter[line]
#print(letter_string)

#creat a file for each name in the list
for name in list_of_names:
    filename = name
    first_line = f"Dear {name},"
    final_string_letter = first_line + "\n" + letter_string
    with open(f"C:\\Users\\LOUSADAR\\OneDrive - FUJITSU\\Documents\\Pessoal\\Learning\\Python100DaysOfCode\\Python-100Days-Of-Code\\Day024 - Files, Directories and Paths\\\Mail Merge Project Start\Output\\ReadyToSend\{filename}.txt", mode="w") as file:
        file.write(final_string_letter)