import random
from tkinter import *
from tkinter import messagebox
from random import randint, choice, sample
import pyperclip
import pandas as pd
import json

# CONSTANTS
FONT = ("Arial", 10, "bold")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pw_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pw_letters = [choice(letters) for _ in range(randint(8, 10))]
    pw_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    pw_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = pw_letters + pw_symbols + pw_numbers
    password = ''.join(sample(password_list, len(password_list)))

    pw_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = user_entry.get()
    password = pw_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if website == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        with open("data.json", "w") as data_txt:
            json.dump(new_data, data_txt, indent=4)
            website_entry.delete(0, END)
            pw_entry.delete(0, END)
            website_entry.focus()


# ---------------------------- SHOW/HIDE PASSWORD ------------------------------- #
def show_password():
    if pw_var.get() == 1:
        pw_entry.config(show='')
    else:
        pw_entry.config(show='*')


# ---------------------------- RETRIEVE PASSWORD ------------------------------- #
def search():
    website = website_entry.get()
    if website == "":
        messagebox.showinfo(title="", message="Please type a website name.")
    else:
        data = pd.read_csv("data.txt", header=None)
        print(data[0])


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=60, pady=70)

# variable
pw_var = IntVar(value=0)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=0, columnspan=3)

# Labels
website_label = Label(text="Website:", font=FONT)
website_label.grid(row=1, column=0, pady=5)

user_label = Label(text="Email/Username:", font=FONT)
user_label.grid(row=2, column=0, pady=5)

pw_label = Label(text="Password:", font=FONT)
pw_label.grid(row=3, column=0, pady=5)

# Entries
website_entry = Entry(width=25, font=FONT)
website_entry.grid(row=1, column=1, sticky="w", pady=5, padx=5)
website_entry.focus()

user_entry = Entry(width=50, font=FONT)
user_entry.grid(row=2, column=1, columnspan=2, sticky="w", pady=5, padx=5)
user_entry.insert(0, "eirol1221@gmail.com")

pw_entry = Entry(width=25, font=FONT, show='*')
pw_entry.grid(row=3, column=1, sticky="w", pady=5, padx=5)

# buttons
generate_pw = Button(text="Generate Password", font=FONT, command=pw_generator)
generate_pw.grid(row=3, column=2, sticky="e", pady=5, padx=5)

add_button = Button(text="Add", font=FONT, command=save)
add_button.grid(row=5, column=1, columnspan=2, sticky="ew", pady=5, padx=5)

search_button = Button(text="Search", font=FONT, width=16, bg="blue")
search_button.grid(row=1, column=2, sticky='e', pady=5, padx=5)

# checkbutton
show_pw_button = Checkbutton(text="Show password", variable=pw_var, onvalue=1, offvalue=0, command=show_password)
show_pw_button.grid(row=4, column=1, sticky='w')

window.mainloop()