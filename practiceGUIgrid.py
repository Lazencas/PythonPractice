
from cgitb import text
from textwrap import fill
from tkinter import *
import tkinter.messagebox as msgbox
from turtle import right
from urllib import response


root = Tk()
root.title("my gui")
root.geometry("640x640")

# btn1 = Button(root, text="버튼1")
# btn2 = Button(root, text="버튼2")
# # btn1.pack(side='left')
# # btn2.pack(side='right')

# btn1.grid(row=0, column=0)
# btn2.grid(row=1 ,column=1)

#padx / pady 이미지 기준으로 늘리는거라 글자수가 좀 길거나 크면 옆에거랑 크기가 안맞을 수 있음   ,  width / height 이게 더 칸맞추기 좋음
#sticky = W , 스티키는 해당 방향으로 달라붙고 늘어남.

# 맨 윗줄
btn_f16 = Button(root, text='f16', width=5, height=2)
btn_f17 = Button(root, text='f17', width=5, height=2)
btn_f18 = Button(root, text='f18', width=5, height=2)
# btn_f19 = Button(root, text='f19')

btn_f16.grid(row=0, column=0, sticky=N+E+W+S, padx=2, pady=2)
btn_f17.grid(row=0, column=1, sticky=N+E+W+S, padx=2, pady=2)
btn_f18.grid(row=0, column=2, sticky=N+E+W+S, padx=2, pady=2)
# btn_f19.grid(row=0, column=3)

# 2번째 줄
btn_clear = Button(root, text='clear', width=5, height=2)
btn_equal = Button(root, text='equal', width=5, height=2)
btn_div = Button(root, text='div', width=5, height=2)
btn_mul = Button(root, text='mul', width=5, height=2)

btn_clear.grid(row=1, column=0, columnspan=2, sticky=N+E+W+S, padx=2, pady=2)
# btn_equal.grid(row=1, column=1)
btn_div.grid(row=1, column=2, sticky=N+E+W+S, padx=2, pady=2)
btn_mul.grid(row=0, column=3, rowspan=2, sticky=N+E+W+S, padx=2, pady=2)


#3번째 줄
btn_1 = Button(root, text='1', width=5, height=2)
btn_2 = Button(root, text='2', width=5, height=2)
btn_3 = Button(root, text='3', width=5, height=2)
btn_4 = Button(root, text='4', width=5, height=2)

btn_1.grid(row=2, column=0, sticky=N+E+W+S, padx=2, pady=2)
btn_2.grid(row=2, column=1, sticky=N+E+W+S, padx=2, pady=2)
btn_3.grid(row=2, column=2, sticky=N+E+W+S, padx=2, pady=2)
btn_4.grid(row=2, column=3, sticky=N+E+W+S, padx=2, pady=2)


root.mainloop()