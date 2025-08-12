import tkinter as tk

FG_COLOR = "skyblue"
BG_COLOR = "pink"
FONT_STYLE = ("Calibri", 30, "bold")

#To create a window
root = tk.Tk()
root.geometry("500x500")

#To display text using Labels
title = tk.Label(root, text="Calculator", fg=FG_COLOR, bg=BG_COLOR, font=FONT_STYLE)
title.pack(padx=10, pady=10)
result = tk.Label(root, text="0", fg=FG_COLOR, bg=BG_COLOR, font=FONT_STYLE)
result.pack(padx=10, pady=10)

#To enter single line of text
my_entry_1 = tk.Entry(root, bg=FG_COLOR)
my_entry_1.pack(padx=10, pady=10)
my_entry_2 = tk.Entry(root)
my_entry_2.pack()

#To input multiple lines of text
# t = tk.Text(root, height=2, width=30, fg=FG_COLOR, bg="white")
# t.pack(padx=10, pady=10)

#Functions for mathematical operations
def append_numbers(num):
    focused_widget = root.focus_get() #To find the currently focused widget (Entry box)
    if isinstance(focused_widget, tk.Entry):
        focused_widget.insert(tk.END, str(num))

def add():
    print("add")
    res = int(my_entry_1.get()) + int(my_entry_2.get())
    result.config(text=res)

def minus():
    print("---")
    res = int(my_entry_1.get()) - int(my_entry_2.get())
    result.config(text=res)

def multiply():
    print("***")
    res = int(my_entry_1.get()) * int(my_entry_2.get())
    result.config(text=res)

def divide():
    print("///")
    res = int(my_entry_1.get()) / int(my_entry_2.get())
    result.config(text=res)

#Using a Button frame
buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

# Operators row 0
tk.Button(buttonframe, text="+", font=FONT_STYLE, command=add).grid(column=0, row=0, sticky="nsew")
tk.Button(buttonframe, text="-", font=FONT_STYLE, command=minus).grid(column=1, row=0, sticky="nsew")

# Operators row 1
tk.Button(buttonframe, text="*", font=FONT_STYLE, command=multiply).grid(column=0, row=1, sticky="nsew")
tk.Button(buttonframe, text="/", font=FONT_STYLE, command=divide).grid(column=1, row=1, sticky="nsew")

# Numbers starting from row 2
# Lambda used too pass arguments to a function that’s triggered by a widget (like a button), 
# because Tkinter’s command= option normally only works with function names that take no arguments.
tk.Button(buttonframe, text="7", font=FONT_STYLE, command=lambda: append_numbers(7)).grid(column=0, row=2, sticky="nsew")
tk.Button(buttonframe, text="8", font=FONT_STYLE, command=lambda: append_numbers(8)).grid(column=1, row=2, sticky="nsew")
tk.Button(buttonframe, text="9", font=FONT_STYLE, command=lambda: append_numbers(9)).grid(column=2, row=2, sticky="nsew")

tk.Button(buttonframe, text="4", font=FONT_STYLE, command=lambda: append_numbers(4)).grid(column=0, row=3, sticky="nsew")
tk.Button(buttonframe, text="5", font=FONT_STYLE, command=lambda: append_numbers(5)).grid(column=1, row=3, sticky="nsew")
tk.Button(buttonframe, text="6", font=FONT_STYLE, command=lambda: append_numbers(6)).grid(column=2, row=3, sticky="nsew")

tk.Button(buttonframe, text="1", font=FONT_STYLE, command=lambda: append_numbers(1)).grid(column=0, row=4, sticky="nsew")
tk.Button(buttonframe, text="2", font=FONT_STYLE, command=lambda: append_numbers(2)).grid(column=1, row=4, sticky="nsew")
tk.Button(buttonframe, text="3", font=FONT_STYLE, command=lambda: append_numbers(3)).grid(column=2, row=4, sticky="nsew")

# Zero at the bottom
tk.Button(buttonframe, text="0", font=FONT_STYLE, command=lambda: append_numbers(0)).grid(column=0, row=5, columnspan=3, sticky="nsew")



buttonframe.pack(fill="x", expand=True)

root.mainloop()