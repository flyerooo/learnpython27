from Tkinter import *
import tkMessageBox

root = Tk()
def callback():
    if tkMessageBox.showerror("Jeff","HI Jeff"):
        print "Clicked Yes"
    else:
        print "Clicked No"
button = Button(root, text = "Button1", command = callback)
button.pack()
root.mainloop()