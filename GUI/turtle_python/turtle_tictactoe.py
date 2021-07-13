from turtle import *

bgcolor("black")

pencolor("white")
title("Tic Tac Toe")
setup(600,600)
speed(100)

up()
pensize(10)
goto(-300,100)
down()
forward(600)
up()
goto(-300,-100)
down()
forward(600)
up()
goto(-100,300)
setheading(-90)
down()
forward(600)
up()
goto(100,300)
down()
forward(600)
up()


def cross(x,y):
    pencolor("yellow")
    up()
    goto(x+20,y-20)
    setheading(-45)
    down()
    forward(226)
    up()
    goto(x+180,y-20)
    setheading(-135)
    down()
    forward(226)
    up()

def nought(x,y):
    pencolor("green")
    up()
    goto(x+100,y-180)
    setheading(0)
    down()
    circle(80)
    up()

pieces = ["","","","","","","","",""]
nextTurn = "X"

def drawpieces(pieces):
    x,y = -300,300
    for p in pieces:
        if p == "X":
            cross(x,y)
        elif p == "O":
            nought(x,y)

        x += 200

        if x > 100:
            x = - 300
            y = y - 200

# drawpieces(pieces)

def clicked(x,y):
    global nextTurn,pieces
    coloumn = (x + 300)//200
    row = (-y + 300) //200
    square = int(coloumn + 3*row)

    # print("you clicked square no.",square)
    pieces[square] = nextTurn

    # print(nextTurn,pieces[square])

    if nextTurn == "X":

        nextTurn = "O"

    else:
        nextTurn = "X"

    drawpieces(pieces)

onscreenclick(clicked)

mainloop()


