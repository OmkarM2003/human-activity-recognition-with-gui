from collections import deque
import numpy as np
import cv2
import tkinter as tk
from tkVideoPlayer import TkinterVideo
from tkinter import filedialog as fd
from collections import deque
import numpy as np
import cv2
import tkinter as tk
from tkVideoPlayer import TkinterVideo
from tkinter import *
from tkinter import filedialog
from tkinter import Button, filedialog as fd
from PIL import ImageTk, Image 
import sys
import os


win = Tk()
# Set the geometry of the window
win.geometry("600x350")

# Title of the window
win.title("Human Activity Recognition")



img =Image.open('D:\Mini Project\human-activity-recognition-master\ok.jpg')
bg = ImageTk.PhotoImage(img)
label = Label(win, image=bg)
label.place(x = 0,y = 0)

tk.Label(win, 
		 text="HUMAN ACTIVITY RECOGNITION",
		 fg = "red",
		 font = ("Times",25)).pack(padx=35, pady=20)
# Define a function to close the window
def close():
   #win.destroy()
   win.quit()

def browse():
    os.system('browser.py')

def camera():
    os.system('camera.py')

# Create a Button to call close()
at=Button(win, text= "Browse", font=("Calibri",14,"bold"), command=browse).pack(side=LEFT, padx=80, pady=50)
B=Button(win,text="Camera",font=("Calibri",14,"bold"),command= camera).pack(side=LEFT, padx=30, pady=20)
bt=Button(win, text= "Quit", font=("Calibri",14,"bold"), command=quit).pack(side=LEFT,padx=70, pady=20)

win.mainloop()
    
