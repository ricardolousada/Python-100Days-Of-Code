# Created by Ricardo Lousada
from tkinter import *

# create the window
window = Tk()
window.title("Mile to KM Converter")
#window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


def button_clicked():
    """responds when the button is click does the conversion math and updates de label"""
    miles = float(my_input.get())
    # Converts miles to Km's
    km = round(miles * 1.609)
    km_calculated_label.config(text=str(km))


# create the input text

my_input = Entry(width=7)
my_input.grid(column=1, row=0)
# my_input.config(padx=20,pady=20)

# Creates the labels

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
#miles_label.config(padx=20, pady=20)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)
#is_equal_label.config(padx=20, pady=20)

km_calculated_label = Label(text="0")
km_calculated_label.grid(column=1, row=1)
#km_calculated_label.config(padx=20, pady=20)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)
#km_label.config(padx=20, pady=20)

# Creates the button

my_button = Button(text="Calculate", command=button_clicked)
my_button.grid(column=1, row=2)
#my_button.config(padx=20, pady=20)

window.mainloop()
