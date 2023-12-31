# Created by Ricardo Lousada
from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500,height=300)
window.config(padx=20,pady=20)

def button_clicked():
    new_text = my_input.get()
    my_label.config(text=new_text)

# Label

my_label = Label(text="I'm a Label",font=("Arial",24,"bold"))
my_label.config(text="New new label")
#my_label.pack()
#my_label.place(x=100,y=200)
my_label.grid(column=0,row=0)
#my_label["text"] = "New label"
my_label.config(padx=20,pady=20)


# Entry - input

my_input = Entry(width=10)
#my_input.pack()
my_input.grid(column=3,row=3)


# Buttons

my_button = Button(text="Click me",command=button_clicked)
#my_button.pack()
my_button.grid(column=1,row=1)
my_button2 = Button(text="Click Me",command=button_clicked)
my_button2.grid(column=2,row=0)

"""
#Text
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END)) #gets the text at line one
print(text.get("2.0",END)) #gets the text at line two
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
"""

window.mainloop()

