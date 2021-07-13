import turtle
import random

tim = turtle.Turtle()
colors = ["red","blue","green","orange","yellow"]

tim.color("red","blue")
tim.width(5)

tim.begin_fill()
tim.circle(50)
tim.end_fill()

turtle.mainloop()