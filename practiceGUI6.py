
from cgitb import text
from textwrap import fill
from tkinter import *
import tkinter.messagebox as msgbox
from turtle import right
from urllib import response


root = Tk()
root.title("my gui")
root.geometry("640x640")

frame = Frame(root)
frame.pack()

scroll = Scrollbar(frame)
scroll.pack(side="right", fill="y")

# set이 없으면 스크롤을 내려도 다시 올라옴
listbox = Listbox(frame, selectmode="extended", height=10,  yscrollcommand=scroll.set)
for i in  range(1, 32):
    listbox.insert(END, str(i) + "일") 
    listbox.pack(side="left")

    scroll.config(command=listbox.yview)

root.mainloop()