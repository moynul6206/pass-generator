import random
import string
from tkinter import Tk, Label, Button, Checkbutton, IntVar, Entry

def generate_password():
    # Get the user's selected options
    include_upper = upper_var.get()
    include_lower = lower_var.get()
    include_number = number_var.get()
    include_symbol = symbol_var.get()
    length = length_entry.get()
    
    # Define the character sets based on the selected options
    characters = ""
    if include_upper:
        characters += string.ascii_uppercase
    if include_lower:
        characters += string.ascii_lowercase
    if include_number:
        characters += string.digits
    if include_symbol:
        characters += string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(int(length)))
    
    # Display the generated password in a popup
    popup = Tk()
    popup.title("Generated Password")
    popup.geometry("300x100")
    label = Label(popup, text="Generated Password:")
    label.pack()
    password_label = Label(popup, text=password)
    password_label.pack()
    ok_button = Button(popup, text="OK", command=popup.destroy)
    ok_button.pack()
    popup.mainloop()

# Create the GUI for selecting options
root = Tk()
root.title("Password Generator")
root.geometry("300x200")

upper_var = IntVar()
lower_var = IntVar()
number_var = IntVar()
symbol_var = IntVar()

upper_check = Checkbutton(root, text="Include Alpha Upper (A-Z)", variable=upper_var)
upper_check.pack()
lower_check = Checkbutton(root, text="Include Alpha Lower (a-z)", variable=lower_var)
lower_check.pack()
number_check = Checkbutton(root, text="Include Number (0-9)", variable=number_var)
number_check.pack()
symbol_check = Checkbutton(root, text="Include Symbol", variable=symbol_var)
symbol_check.pack()

length_label = Label(root, text="Length:")
length_label.pack()
length_entry = Entry(root)
length_entry.pack()

generate_button = Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

root.mainloop()