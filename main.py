import tkinter as tk
import pyperclip
import json
from tkinter import messagebox
from random import choice, randint, shuffle

LETTERS = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]
SYMBOLS = ["!", "#", "$", "&", "(", ")", "*", "%", "@", ".", "/", "¡", "+", "_"]
NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = [choice(LETTERS) for _ in range(randint(8, 10))]
    symbols = [choice(SYMBOLS) for _ in range(randint(2, 4))]
    numbers = [choice(NUMBERS) for _ in range(randint(2, 4))]

    password_list = letters + symbols + numbers
    shuffle(password_list)
    password = "".join(password_list)
    
    password_entry.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": username,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open(file="data.json", mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open(file="data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open(file="data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, last="end")
            password_entry.delete(0, last="end")

    website_entry.focus()


# ---------------------------- FIND PASSWWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open(file="data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    else:
        if website in data:
            username = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Username: {username}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message="No details for the website exist")
    finally:
        website_entry.delete(0, last='end')


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=35, bg="white")

canvas = tk.Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = tk.Label(text="Website:", bg="white", fg="black")
website_label.grid(column=0, row=1)

website_entry = tk.Entry(width=28, bg="white", fg="black", highlightthickness=0, insertbackground="black")
website_entry.grid(column=1, row=1)
website_entry.focus()

search_website_button = tk.Button(width=7, text="Search", highlightbackground="white", command=find_password)
search_website_button.grid(column=2, row=1)

username_label = tk.Label(text="Email/Username:", bg="white", fg="black")
username_label.grid(column=0, row=2)

username_entry = tk.Entry(width=38, bg="white", fg="black", highlightthickness=0, insertbackground="black")
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(index="end", string="example@example.com")

password_label = tk.Label(text="Password:", bg="white", fg="black")
password_label.grid(column=0, row=3)

password_entry = tk.Entry(width=28, bg="white", fg="black", highlightthickness=0, insertbackground="black", show="*")
password_entry.grid(column=1, row=3)

generate_password_button = tk.Button(text="Generate", width=7, highlightbackground="white", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = tk.Button(text="Add", width=36, highlightbackground="white", command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
