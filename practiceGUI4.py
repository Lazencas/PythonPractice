
from tkinter import *


root = Tk()
root.title("my gui")
root.geometry("640x640")

def create_new_file():
    print("새 파일을 만들게요")

menu =  Menu(root) #여기에 들어가는 root는 메인윈도우
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New window")
menu_file.add_separator()#구분줄
menu_file.add_command(label="Open File")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable") #비활성화
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit) #종료
menu.add_cascade(label="File", menu=menu_file)


menu.add_cascade(label="Edit")

#메뉴에서의 라디오버튼
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="Language", menu=menu_lang)

#메뉴에서의 체크박스
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu_view.add_checkbutton(label="Show what")
menu.add_cascade(label="View", menu=menu_view)


root.config(menu=menu)
root.mainloop()