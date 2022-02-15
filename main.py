import tkinter
from tkinter.ttk import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter.font import Font
import time

#create a Window
window = tkinter.Tk()
window.title("Revision App")
window.resizable(False, False)
window.configure

bigfont = Font(family='helvetica', size=16, weight='bold', underline=1)


#command for button1
def openmemory():
    memorywindow = tkinter.Toplevel(window)
    memorywindow.title("Memory")
    memorywindow.resizable(False, False)

#command for button2
def opensecondarystorage():
    secondarystoragewindow = tkinter.Toplevel(window)
    secondarystoragewindow.title("Secondary Storage")
    secondarystoragewindow.resizable(False, False)


#command for button3
def openstorageunits():
    storageunitswindow = tkinter.Toplevel(window)
    storageunitswindow.title("Units of Storage")
    storageunitswindow.resizable(False, False)

#command for button4
def opendatastorage():
    datastoragewindow = tkinter.Toplevel(window)
    datastoragewindow.title("Data Storage")
    datastoragewindow.resizable(False, False)

#command for button5
def openrandomiser():
    randomiserwindow = tkinter.Toplevel(window)
    randomiserwindow.title("Randomiser")
    randomiserwindow.resizable(False, False)

#create a title
label1 = tkinter.Label(
    window, text="Revise Computer Science\nWelcome to the app").grid(row=0,
                                                                     column=0)

#create Button
button1 = tkinter.Button(window,
                         text="Memory",
                         bg='violet',
                         command=openmemory).grid(row=1, column=0, sticky="ew")

button2 = tkinter.Button(window,
                         text="Secondary Storage",
                         bg='silver',
                         command=opensecondarystorage).grid(row=2,
                                                            column=0,
                                                            sticky="ew")

button3 = tkinter.Button(window,
                         text="Units of Storage",
                         bg='orange',
                         command=openstorageunits).grid(row=3,
                                                        column=0,
                                                        sticky="ew")

button4 = tkinter.Button(window,
                         text="Data Storage",
                         bg='lightgreen',
                         command=opendatastorage).grid(row=1,
                                                       column=1,
                                                       sticky="ew")

button5 = tkinter.Button(window, 
                         text="Topic Randomiser",
                         bg='beige',
                         command=openrandomiser).grid(row=2,
                                                      column=1, 
                                                      sticky="ew")