#!/usr/bin/python
import os
import Tkinter
from Tkinter import *
from ScrolledText import *
import tkFileDialog
import tkMessageBox
import ScrolledText


# A class to edit the material internal to the template
# DONT look at this crap code, no idea lol
global ReturnText


def build(textPad, Text):
    textPad.insert('1.0', Text)


def save_command(textPad, root):
    global ReturnText
    # slice off the last character from get, as an extra return is added
    data = textPad.get('1.0', END+'-1c')
    # file.write(data)
    # file.close()
    ReturnText = str(data)
    root.destroy()


def exit_command(root):
    if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()


def about_command():
    label = tkMessageBox.showinfo("About", "SimplyTemplate Editor")


def root(Text):
    global ReturnText
    root = Tkinter.Tk(className="SimplyTemplate Test Editor")
    textPad = ScrolledText.ScrolledText(
        root, width=100, height=15)  # creates text area
    menu = Menu(root)
    root.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(
        label="Save", command=lambda: save_command(textPad, root))
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=lambda: exit_command(root))
    helpmenu = Menu(menu)
    menu.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="About...", command=about_command)
    # end of menu creation
    textPad.pack()
    build(textPad, Text)
    root.mainloop()
    try:
        if ReturnText:
            return ReturnText
    except:
        print " [!] No text returned / changed"
        pass
