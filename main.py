import tkinter as tk

FONT_NAME = "Ariel"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

canvas = tk.Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = tk.Label(text="Website:", font=(FONT_NAME, 14), bg="white", fg="black")
website_label.grid(column=0, row=1)

website_entry = tk.Entry(width=35, bg="white", fg="black", highlightthickness=0)
website_entry.grid(column=1, row=1, columnspan=2)

username_label = tk.Label(text="Username:", font=(FONT_NAME, 14), bg="white", fg="black")
username_label.grid(column=0, row=2)

username_entry = tk.Entry(width=35, bg="white", fg="black", highlightthickness=0)
username_entry.grid(column=1, row=2, columnspan=2)

password_label = tk.Label(text="Password:", font=(FONT_NAME, 14), bg="white", fg="black")
password_label.grid(column=0, row=3)

password_entry = tk.Entry(width=21, bg="white", fg="black", highlightthickness=0)
password_entry.grid(column=1, row=3)

generate_password_button = tk.Button(text="Generate Password", font=(FONT_NAME), width=10)
generate_password_button.grid(column=2, row=3)

add_button = tk.Button(text="Add", width=36)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()