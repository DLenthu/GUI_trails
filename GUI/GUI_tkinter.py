from tkinter import *
root = Tk()
root.geometry("640x480")

# l = Label(root,text = "Hello World")
# l.pack(side = TOP)

# def buttonfunction():
#     print("Button Clicked")

# b1 = Button(root,text = "Click Here",command = buttonfunction)
# b1.pack(side = LEFT)
# b2 = Button(root,text = "Click Here",command = buttonfunction)
# b2.pack(side = RIGHT)

# c = Canvas(root,height = 400,width = 480,bg = "blue")
# c.pack(side = BOTTOM)

# l = c.create_line(5,5,390,420,width = 5)
# o = c.create_oval(20,20,100,100,fill = "red")
# arc = c.create_arc(10,50,250,210,extent = 150,fill = "green") 
# r = c.create_rectangle(50,50,200,200,fill = "yellow")

mb = Menubutton(root,text = "MENU")
mb.menu =  Menu(mb)
mb["menu"] = mb.menu
mb.menu.add_command(label="Option.1 ",command = lambda:print("Oprion 1 select"))
mb.menu.add_command(label="Option.2 ",command = lambda:print("Oprion 2 select"))
mb.menu.add_command(label="Option.3 ",command = lambda:print("Oprion 3 select"))
mb.pack()

v = IntVar()


radio1 = Radiobutton(root,variable = v,value = 1,text = "It is sunny",command = lambda:print(v.get()))
radio2 = Radiobutton(root,variable = v,value = 2,text = "It is windy",command = lambda:print(v.get()))
radio3 = Radiobutton(root,variable = v,value = 3,text = "It is chily",command = lambda:print(v.get()))
radio3.pack(side = BOTTOM)
radio2.pack(side = BOTTOM)
radio1.pack(side = BOTTOM)
root.mainloop()
