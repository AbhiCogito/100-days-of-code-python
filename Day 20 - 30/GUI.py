from tkinter import *

w = Tk()
w.title("Miles to KMs Converter")
w.minsize(width=100, height=100)

my_label = Label(text="Unit Converter", font=("Calibri", 15, "bold"))
my_label.grid(column=2,row=0)
num = Entry(border=1, width=10)
num.grid(column=2,row=1)
t_miles = Label(text="Miles")
t_miles.grid(column=4,row=1)
t_kms = Label(text="Kilometers")
t_kms.grid(column=4,row=4)
t_answer = Label(text=f"0")
t_answer.grid(column=2,row=4)


def click_button():
    data = float(num.get())
    data_converted = round(data * 1.6, 2)
    t_answer = Label(text=f"{data_converted}")
    t_answer.grid(column=2,row=4)
    # # text_click = "Button clicked! Timer started!!"
    # text_click = work.get()
    # my_label.config(text=f"{text_click} converted")
    # my_button.config(text="Units converted to kms")
    # # my_label.pack(side="bottom")
    # # my_button.pack(side="right")



my_button = Button(text="Convert miles to kms", command=click_button)
my_button.grid(column=2,row=6)




w.mainloop()