import tkinter.ttk as ttk
from tkinter import *
import time

root = Tk()
root.title("my gui")
root.geometry("640x640")


#프로그레스바도 ttk 필요
#prog = ttk.Progressbar(root, maximum=100, mode="indeterminate") # indeterminate : 왔다리갔다리
# prog = ttk.Progressbar(root, maximum=100, mode="determinate") #원래 우리가 아는 프로그레스바
# prog.start(10)# 10ms 마다 움직임 숫자가 적을 수록 빨리 움직임.
# prog.pack()

p_var2 = DoubleVar()
prog2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2) #length값은 길이 조절
prog2.pack()



def buttoncommand():
    #prog.stop() #작동중지
    for i in range(101): #1~100까지
        time.sleep(0.01) #0.01초 대기
        
        p_var2.set(i) # progressbar의 값 설정
        prog2.update() #이걸 해줘야 실시간으로 적용됨, 아니면 끝난 결과만 화면에 나타남
        print(p_var2.get())


btn = Button(root, text="중지", command=buttoncommand)
btn.pack()

root.mainloop()