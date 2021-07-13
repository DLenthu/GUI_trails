from turtle import *

bgcolor("black")
title("Checkers")
setup(800,800)

def square():
    begin_fill()
    forward(200)
    right(90)
    forward(200)
    right(90)
    forward(200)
    right(90)
    forward(200)
    right(90)
    end_fill()

def row(level,type):
    if type == 0:
        up()
        goto(-400,level)
        fillcolor("#bbbbbb")
        square()

        up()
        goto(-200,level)
        fillcolor("#555555")
        square()

        up()
        goto(0,level)
        fillcolor("#bbbbbb")
        square()

        up()
        goto(200,level)
        fillcolor("#555555")
        square()

    else:
        up()
        goto(-400,level)
        fillcolor("#555555")
        square()

        up()
        goto(-200,level)
        fillcolor("#bbbbbb")
        square()

        up()
        goto(0,level)
        fillcolor("#555555")
        square()

        up()
        goto(200,level)
        fillcolor("#bbbbbb")
        square()

row(400,0)
row(200,1)
row(0,0)
row(-200,1)


mainloop()