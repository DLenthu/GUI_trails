import turtle
from turtle import Turtle,Screen
import random

screen = Screen()
t = Turtle()
t.shape("turtle")
t.speed(-1)
colors = ["red","blue","green","orange","yellow"]

def dragging(x,y):
    t.ondrag(None)
    t.setheading(t.towards(x,y))
    t.goto(x,y)
    t.ondrag(dragging)

def clickmiddle(x,y):
    t.clear()

def up():
    t.setheading(90)
    t.forward(100)

def down():
    t.setheading(270)
    t.forward(100)

def left():
    t.setheading(180)
    t.forward(100)    

def right():
    t.setheading(0)
    t.forward(100)

def clickleft(x,y):
    t.color(random.choice(colors))

def clickright(x,y):
    t.stamp()

def main():
    turtle.listen()
    t.ondrag(dragging)
    turtle.onscreenclick(clickleft,1)
    turtle.onscreenclick(clickright,3)

    turtle.onkey(up,"Up")
    turtle.onkey(down,"Down")
    turtle.onkey(left,"Left")
    turtle.onkey(right,"Right")

    turtle.onscreenclick(clickmiddle,2)

    screen.mainloop()

main()