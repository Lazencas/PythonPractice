from cProfile import label
from email.mime import image
from logging import root
from tkinter import *

root = Tk()
root.title("My GUI")
root.geometry("640x800+100+50") # 가로 * 세로 크기 지정, 100은 x좌표, 300은y좌표
# root.resizable(False, False)# x, y 값 변경 불가(창 크기 변경 불가)

btn1 = Button(root, text="버튼1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="버튼2") #padx, pady 는 버튼내의 상하좌우 공간 여백설정, 글자가 길어지면 버튼도 그에따라 커짐.
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=5, text="버튼4") #이경우는 고정크기, 글자가 길어지면 잘린다.
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
btn5.pack()

photo = PhotoImage(file="image/btnimg.png") #png파일 아니면 오류나는듯?
btn6 = Button(root, image=photo) 
btn6.pack()

def btncmd():
    print("버튼클릭!")

btn7 = Button(root, text="동작하는 버튼", command=btncmd) #버튼에 동작 넣는거
btn7.pack()

label1 = Label(root, text="안녕하세요")
label1.pack()


label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또만나자") #클릭했을때 라벨1의 문구를 바꿈

    global photo2 #전역변수로 설정하지 않으면 가비지컬렉터가 삭제해버림
    photo2 = PhotoImage(file="image/bravo.png") 
    label2.config(image=photo2)    

btn = Button(root, text="클릭", command=change)
btn.pack()

txt = Text(root, width=30, height=5)#텍스트창 생성
txt.pack()
txt.insert(END, "글자를 입력하세요")#텍스트창에 설명첨부

e=Entry(root, width=30) #텍스트창인데 줄바뀜이 안됨, 1줄만 입력됨.
e.pack()
e.insert(0,"한 줄만 입력됨")

def bcmd():
    #내용출력
    print(txt.get("1.0", END))#1은 라인1부터 가져오고, 0은 칼럼 0번째부터 가져오는거
    print(e.get())
   #내용삭제
    txt.delete("1.0",END)
    e.delete(0, END)

btnp = Button(root, text="클리익", command=bcmd)
btnp.pack()


root.mainloop() #창이 닫히지 않게함


