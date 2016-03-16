from Tkinter import *

root = Tk()

label = Label(root, text= "hello world")
label.config(cursor = "gumby")
label.config(width = 88, height = 10,fg = "yellow", bg = "dark green")
label.config(font = ("times", "28", "bold"))
label.pack()
root.mainloop()