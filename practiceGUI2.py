from cProfile import label
from email.mime import image
from logging import root
from msilib.schema import ComboBox
from tkinter import *
import tkinter.ttk as ttk 

root = Tk()
root.title("My GUI")
root.geometry("640x640+100+50") # 가로 * 세로 크기 지정, 100은 x좌표, 300은y좌표
# root.resizable(False, False)# x, y 값 변경 불가(창 크기 변경 불가)

values = [str(i) + "일" for i in range(1, 32)] #1~31까지의 숫자
combox = ttk.Combobox(root, height=5, values=values) # height : 아래세모 버튼 눌렀을 때 보여지는 목록 개수.
combox.pack()
combox.set("카드 결제일") #최초 목록 제목 설정

readonly_combox = ttk.Combobox(root, height=10, values=values, state="readonly") #콤보박스에 입력불가, 이건 거의다 들어가야할듯
readonly_combox.pack()
readonly_combox.current(0) # 0번째 인덱스 값 선택


# listbox = Listbox(root, selectmode="extended", height=0) #selectmode="single"로 하면 한개만 선택가능, height 값만큼만 창에 표시됨.
# listbox.insert(0, "사과")
# listbox.insert(1, "딸기")
# listbox.insert(2, "바나나")
# listbox.insert(END, "수박")
# listbox.insert(END, "포도")
# listbox.pack()

# chkvar = IntVar() # chkvar 에 int형으로 값을 저장한다
# chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
# chkbox.select() #자동 선택 처리
# chkbox.deselect() #선택 해제 처리
# chkbox.pack()

# chkvar2 = IntVar()
# chkbox2 = Checkbutton(root, text="일주일 보지 않기", variable=chkvar2)
# chkbox2.pack()  

#@@@@@@@@@@@라디오박스

# Label(root, text="메뉴를 선택하세요").pack()
# burger_var = IntVar() #여기에 int 형으로 값을 저장한다.
# btn_burger1 = Radiobutton(root, text="햄버거", value=1, variable=burger_var)
# btn_burger2 = Radiobutton(root, text="치즈버거", value=2, variable=burger_var)
# btn_burger3 = Radiobutton(root, text="치킨버거", value=3, variable=burger_var)
# btn_burger1.pack()
# btn_burger2.pack()
# btn_burger3.pack()

# drink_var = StringVar()
# btn_drink1 = Radiobutton(root, text="콜라", value="콜라", variable=drink_var)
# btn_drink1.select()#기본값 선택
# btn_drink2 = Radiobutton(root, text="사이다", value="사이다", variable=drink_var)
# btn_drink1.pack()
# btn_drink2.pack()


def btncmd():
    #@@@@@@@@리스트박스
    #항목삭제
    #listbox.delete(END) #END > 맨 뒤에 항목을 삭제, 0 > 맨 앞부터 항목삭제

    #갯수확인
    #print("리스트에는", listbox.size(), "개가 있어요")
    
    #항목확인 (시작, 끝)
    #print("1번째부터 3번쨰까지의 항목 : ", listbox.get(0,2))
 
    # 선택된 항목 확인 (위치로 반환)
    #print("선택된 항목 : ", listbox.curselection())
    
    #@@@@@@@@@@@체크박스
    # print(chkvar.get()) # 0: 체크해제, 1 : 체크
    # print(chkvar2.get())

    #@@@@@@@@@@라디오박스
    # print(burger_var.get()) #햄버거 중 선택된 라디오 항목의 값(value)을 출력
    # print(drink_var.get()) #음료 중 선택된 값을 출력
   
    #@@@@@@@@@@@콤보박스
    print(combox.get()) # 선택된 값 표시
    print(readonly_combox.get()) 

btnp = Button(root, text="클리익", command=btncmd)
btnp.pack()


root.mainloop() #창이 닫히지 않게함


