import os, csv, random, string, json
import tkinter as tk
from tkinter import ttk, messagebox

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logo.png")
json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "credentials.json")
os.system("clear")

# ---------------------------- UI SETUP ------------------------------- #
root = tk.Tk() #Creates the main window
root.title("Password Manager")
root.config(bg="white")
root.geometry("700x700")

#Creating the canvas within which all the objects will be placed
c = tk.Canvas(root, width=220, height=240, highlightthickness=1, bg="cyan")
logo = tk.PhotoImage(file=file_path) #Loading the image
c.create_image(110,120,image=logo)   #Using the image in canvas
c.grid(column=1, row=0, pady= 30) #Placing the canvas itself using the grid method

p_category = tk.Label(text="Category", font=("Calibri", 15, "bold"))
p_category.grid(column=0, row=2)
p_length = tk.Label(text="Password Length", font=("Calibri", 15, "bold"))
p_length.grid(column=0, row=4)

#Adding space between all the rows
for i in range(6):
    root.grid_rowconfigure(i, pad=15)  # 15px extra below row 

# Dropdown (Combobox)
categories = ["Website", "Finance"]
category_var = tk.StringVar()  #Creating a string variable within tkinter to store the selected dropdown option
#Dropdown takes values from <categories> and the selected option is stored in <category_var>
dropdown = ttk.Combobox(root, values=categories, textvariable=category_var, state="readonly")
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
slider.grid(column=1, row=4, sticky='w')

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
tk.Label(root, text="Website").grid(row=3, column=0, padx=5, pady=5, sticky="e") #stick to "east"
web_var = tk.StringVar() #Tkinter string variable to store user's input
tk.Entry(root, textvariable=web_var).grid(row=3, column=1, padx=5, pady=5, sticky="w") #stick to "west"

tk.Label(root, text="Email:").grid(row=5, column=0, padx=5, pady=5, sticky="e") #stick to "east"
email_var = tk.StringVar() #Tkinter string variable to store user's input
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

    # Fill remaining length by selecting k items
    new_password_list += random.choices(all_chars, k=length - 4)

    # Shuffle
    random.shuffle(new_password_list)
    password_var.set("".join(new_password_list))


def store_data():
    email = email_var.get()
    password = password_var.get()
    category = category_var.get()
    website = web_var.get()

    #Defining the structure of data for storing
    json_dict = {website: {
                    "Category" : category,
                    "Email"    : email,
                    "Password" : password
    }}

    if email == "" or password == "" or category == "":
        messagebox.showinfo(message="Category, Email & Password can't be empty.")
    else:
        save = messagebox.askokcancel(title=category, message=f"Confirm for saving: \n \
                                                                Email: {email} \n Password: {password}")
        if save:
            try:
                with open(json_path, "r") as file:
                    #Load the JSON data for reading
                    json_data = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                # if file doesn’t exist or is empty → start with empty dict
                json_data = {}

            # update existing data
            json_data.update(json_dict)

            # write back to file
            with open(json_path, "w") as file:
                json.dump(json_data, file, indent=4)
            email_var.set("")
            password_var.set("")
            category_var.set("")
            web_var.set("")

def search_data():
    website = web_var.get().strip().lower()

    if website == "":
        messagebox.showinfo(message="Website can't be empty.")
        return #To exit the loop as no point continuing
    else:
        try:
            with open(json_path, "r") as file:
                reader = json.load(file)
                for site, details in reader.items():
                    if site.lower() == website:
                        category = details.get("Category", "")
                        email = details.get("Email", "")
                        password = details.get("Password", "")
                        messagebox.showinfo(title=site, message=f"Category: {category}\n \
                                                                Email: {email}\n \
                                                                Password: {password}  ")
                        
                        return
        except (FileNotFoundError, json.JSONDecodeError):
            messagebox.showinfo(message="No data file exists. Save some passwords before sarching!!")


generate_btn = tk.Button(root, text="Generate", command=generate_password)
generate_btn.grid(row=6, column=2, padx=5, pady=5)

search_btn = tk.Button(root, text="Search Data", width=20, command=search_data)
search_btn.grid(row=3, column=2, columnspan=2, padx=5, pady=5)

# ---- Store Data ----
store_btn = tk.Button(root, text="Store Data", width=20, command=store_data)
store_btn.grid(row=7, column=0, columnspan=3, pady=15)

root.mainloop()