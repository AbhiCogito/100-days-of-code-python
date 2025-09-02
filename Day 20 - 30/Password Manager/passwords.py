import os, csv, random, string
import tkinter as tk
from tkinter import ttk

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logo.png")
csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "credentials.csv")
os.system("clear")

# ---------------------------- UI SETUP ------------------------------- #
root = tk.Tk() #Creates the main window
root.title("Password Manager")
root.config(bg="white")
root.geometry("700x700")

#Creating the canvas inside which all the objects will be placed
c = tk.Canvas(root, width=220, height=240, highlightthickness=0)
logo = tk.PhotoImage(file=file_path) #Loading the image
c.create_image(110,120,image=logo)   #Using the image in canvas
c.grid(column=1, row=0, pady= 30) #Placing the canvas itself using the grid method

p_category = tk.Label(text="Category", font=("Calibri", 15, "bold"))
p_category.grid(column=0, row=2)
p_length = tk.Label(text="Password Length", font=("Calibri", 15, "bold"))
p_length.grid(column=0, row=3)

#Adding space between all the rows
for i in range(6):
    root.grid_rowconfigure(i, pad=15)  # 15px extra below row 

# Dropdown (Combobox)
categories = ["Website", "Finance"]
category_var = tk.StringVar()  # stores the selected value
dropdown = ttk.Combobox(root, textvariable=category_var, values=categories, state="readonly")
dropdown.grid(column=1, row=2, padx=10, pady=10)

#Adding a horizontal slider for password length
slider = tk.Scale(
    root,
    from_=7,            # starting value
    to=12,              # ending value
    orient="horizontal",# horizontal orientation
    length=200,         # slider length in pixels
    tickinterval=1      # show tick marks every 1 unit
)
slider.grid(column=1, row=3, sticky='w')

'''
# Password composition frame
composition_frame = tk.Frame(root)
composition_frame.grid(column=1, row=4, pady=5)

tk.Label(composition_frame, text="Letters").grid(row=0, column=0, padx=5)
tk.Entry(composition_frame, width=5).grid(row=1, column=0, padx=5)

tk.Label(composition_frame, text="Numbers").grid(row=0, column=1, padx=5)
tk.Entry(composition_frame, width=5).grid(row=1, column=1, padx=5)

tk.Label(composition_frame, text="Symbols").grid(row=0, column=2, padx=5)
tk.Entry(composition_frame, width=5).grid(row=1, column=2, padx=5)
'''

# ---- Email/Username ----
tk.Label(root, text="Email:").grid(row=5, column=0, padx=5, pady=5, sticky="e") #stick to "east"
email_var = tk.StringVar() #Creates a string variable in tkinter
tk.Entry(root, textvariable=email_var).grid(row=5, column=1, padx=5, pady=5, sticky="w") #stick to "west"

# ---- Password & Generate ----
tk.Label(root, text="Password:").grid(row=6, column=0, padx=5, pady=5, sticky="e")
password_var = tk.StringVar()
tk.Entry(root, textvariable=password_var).grid(row=6, column=1, padx=5, pady=5, sticky="w")

def generate_password():
    length = int(slider.get())

    all_chars = string.ascii_letters + string.digits + string.punctuation

    # Ensure at least one of each type
    new_password_list = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]

    # Fill remaining length
    new_password_list += random.choices(all_chars, k=length - 4)

    # Shuffle
    random.shuffle(new_password_list)
    password_var.set("".join(new_password_list))


def store_data():
    email = email_var.get()
    password = password_var.get()
    category = category_var.get()

    with open(csv_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([category,email, password])
        email_var.set("")
        password_var.set("")
        category_var.set("")

generate_btn = tk.Button(root, text="Generate", command=generate_password)
generate_btn.grid(row=6, column=2, padx=5, pady=5)

# ---- Store Data ----
store_btn = tk.Button(root, text="Store Data", width=20, command=store_data)
store_btn.grid(row=7, column=0, columnspan=3, pady=15)

root.mainloop()