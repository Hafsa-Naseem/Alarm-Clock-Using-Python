from tkinter import *
import tkinter
import pygame
import datetime
from tkinter.messagebox import *
from tkinter.ttk import Combobox

hour = list(range(1,25))
minute = list(range(0,60))
second = list(range(0,60))

tkobj = Tk()
tkobj.title("Alarm Clock")
pygame.mixer.init()


label1 = Label(tkobj,text="Set alarm hour",fg="red")
label1.grid(row=0,column=0)
c1 = Combobox(tkobj,values=hour)
c1.grid(row=0,column=2)

label2 = Label(tkobj,text="Set alarm minute",fg="blue")
label2.grid(row=1,column=0)
c2 = Combobox(tkobj,values=minute)
c2.grid(row=1,column=2)

label3 = Label(tkobj,text="Set alarm second",fg="Green")
label3.grid(row=2,column=0)
c3 = Combobox(tkobj,values=second)
c3.grid(row=2,column=2)

def alarm() :
    h=int(c1.get())
    m=int(c2.get())
    s=int(c3.get())
    showinfo("Alarm notification","Alarm has been set")
    while True:
        if h==datetime.datetime.now().hour and m==datetime.datetime.now().minute and s==datetime.datetime.now().second:
            showinfo("Alarm notification", "Alarm is ringing")
            pygame.mixer.music.load("C:\python/AlarmMusic.mp3")
            pygame.mixer.music.play(loops=0)

b = Button(tkobj,text="Set Alarm",font=("Arial",9),command=alarm)
b.grid(row=4,column=1)
