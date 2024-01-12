from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def gen_Passwords():
    password_letters = [random.choice(letters) for _ in range(random.randint(8,10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2,4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2,4))]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_input.get().title()
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Error", message="Please fill out all fields.")
    else:
        result = messagebox.askokcancel(
            title=website, message=f"Email: {email}\nPassword: {password}\nDo you want to save?")
        if result:
            with open(r"Password Manager\data.txt", mode="a") as database:
                toSave = f"{website} | {email} | {password}\n"
                database.write(toSave)
                password_input.delete(0, END)
                website_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
photo = PhotoImage(file=r"Password Manager\logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_input = Entry(width=36)
website_input.grid(row=1, column=1, columnspan=2, sticky="EW")
website_input.focus()
website = website_input

email_input = Entry(width=36)
email_input.grid(row=2, column=1, columnspan=2, sticky="EW")
email_input.insert(0, "johndoe123@gmail.com")
email = email_input

password_input = Entry(width=21)
password_input.grid(row=3, column=1, sticky="EW")
password = password_input

gen_button = Button(text="Generate Password", command=gen_Passwords)
gen_button.grid(row=3, column=2, sticky="EW")

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
