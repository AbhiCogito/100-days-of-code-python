# import turtle
# turtle.mainloop()

from prettytable import PrettyTable 
from prettytable.colortable import ColorTable, Themes

from turtle import Turtle, Screen

t = ColorTable(theme = Themes.OCEAN, add_autoindex=True)
t.add_column("Name", ["Sophie", "Mysha", "Aarohi"])
t.add_column("Surname", ["Singh", "Singh", "Jadaun"])
t.add_column("Age", ["5", "6", "10"])

print(t)
# t.add_row("Row")

# donatello = Turtle()
# print(donatello)
# donatello.shape("turtle")
# donatello.color("cyan")
# display = Screen()
# print(display.canvheight)
# display.exitonclick()
#t = PrettyTable()