print(5)
print(-10)
print(3.14)
print(1000) 
print(5+3)
print(15*9)
print(3*(3+1))
print('풍선')
print("풍선"*3)
print("ㅋ"*9)
print(5 > 10)
print(not True)
print(not(5>10))
name = "연탄이"
animal = "강아지"
age = 1
hobby = "산책"
is_adult = age>=3
print("우리집 ",animal,"의 이름은 "+name+"이에요",age,"이고 산책을 좋아하는 연탄이는 연탄이에요 으른일까요? "+str(is_adult))
print(2**4)
print(5%3)
print(5//3)
print(5/3)
print(5 >= 3)
print(6 == 3)
print(4 == 4)
print( 1 != 3)
print(1 != 1)
print((3==3)and(1<5))
print((3==3)&(1>5))
print((3==3)or(1>5))
print((3==3)|(1>5))
num = 5
num = num +3
num += 3
print(num)
print(abs(-5))
print(pow(4,3))
print(max(5, 10))
print(min(5,3))
print(round(40.1532))

from math import *
from statistics import mean
from tkinter import Menu
print(floor(3.123))#내림
print(ceil(3.122))#올림
print(sqrt(16))#제곱근

from random import * #랜덤맨
print(random()) # 0.0~1.0미만의 임의의 값 생성
print(random()*10)
print(random())
print(int(random() *10))
print(int(random() *10))
print(int(random() *10)+1)
print(randrange(1, 46)) #1~46미만의 임의의값
print(randrange(1, 46))
print(randrange(1, 46)) 
print(randint(1, 45)) #1~45이라임의의값
print(randint(1, 45)) 
print(randint(1, 45)) 
month = randint(1,12)
day = randint(4,28)
print(str(month)+"월"+str(day)+"일")
sen = "나는 소년입니다"
sen2 = """
호로로록
파이서서서서언
줄바꿔
"""
print(sen)
print(sen2)
jumin ="990120-1234567"
print("성별: "+ jumin[7])
print("연 : "+jumin[0:2]) #0부터2직전까지
print("월일 : "+jumin[2:6])#2부터 6직전까지
print("년월일 : "+jumin[:6])#처음부터 6직전까지
print("뒤일곱자리 : "+jumin[7:])#7부터 끝까지
print("뒤에서부터7자리 : "+jumin[-7:])#맨뒤에서 7번째부터 끝까지
py = "Python is Amazing"
print(py.lower())
print(py.upper())
print(py[0].isupper())#1번쨰 자리가 대문자인가? True or False
print(len(py)) #글자개수 세는거
print(py.replace("Python", "Java"))#Python 찾아서 Java 로 변경
index = py.index("n") #n이위치하는 자리
print(index)
index = py.index("n", index +1)#1번째로 찾은 n 이후의 n위치
print(index)
print(py.find("n"))
print(py.find("Java"))#Java가 없으면 -1반환, index의경우는 오류가나고 종료되버린다.
print(py.count("n"))
print("a"+"b")
#방법1
print("나는 %d살입니다."%21)
print("나는 %s를 굿한다"%'브라보')#%s는 문장
print("apple는 %c로 시작한다" %"a") #%c 한문자
print("나는 %s색과 %s색을 좋아한당" % ("파란", "빨간"))

#방법2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아한당" .format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아한당" .format("파란", "빨간"))

#방법3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))
print("나는 {color}살이며, {age}색을 좋아해요.".format(age=20, color="빨간"))

#방법4 버전 3.6이상에서 추가
age=20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해용")

print("백문이 불여일견\n백견이 불여일타")
print("저는 '나도코딩' 입니다")
print('저는 "나도코딩" 입니다')
print("저는 \"나도코딩\" 입니다")

#\\:문장내에서 \나옴
print("d\\cs\\asds\\qwdqwd")

#\r : 커서를 맨 압으로 이동
print("Red Apple\rpined")

# \b : 한글자 삭제 백스페이스누른효과
print("redapp\ble")

# \t : 탭누르는효과
print("bravo\tman")

#site = "http://hanmail.com"
site = "http://youtube.com"
print(site)
site = site[7:]
commawhere = site.index(".") #한번쓰는거 변수로 만들 필요가 없엇네
print(commawhere)
site = site[:commawhere]
print(site)
site = (site[:3]) + str(len(site)) + str(site.count('e')) + '!'
print(site)

# 리스트 [] 순서를 가지는 객체의 집합. 지하철 칸별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30
subway = ["유재석","조세호","박명수"]
print(subway)
#조세호가 몇번째 칸에 타는가?
print(subway.index("조세호"))
subway.append("하하") #뒤에추가
print(subway)
subway.insert(1,"정형돈") #삽입
print(subway)
#지하철에있는사람 뒤에서 한명씩 꺼냄
print(subway.pop())
print(subway)
print(subway.pop())
print(subway)
print(subway.pop())
print(subway)
#같은이름의 사람이 몇명인지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))
print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")

#정렬
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

#순서뒤집기
num_list.reverse()
print(num_list)

#모두지우기
#num_list.clear()
print(num_list)


#다양한 자료형 함께 사용
mix_list = ["브라보",20, True]
print(mix_list)

#리스트확장
num_list.extend(mix_list)
print(num_list)

#사전 
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3]) #이경우에는 없는값쓰면 오류나고 종료됨
print(cabinet[100])
print(cabinet.get(3)) #None이라고 나오고 다음으로 진행됨
print(cabinet.get(5,"사용가능")) #None대신 내가 지정한값이 나오게 설정 여기서는 "사용가능"
print(3 in cabinet) #해당 키가있으면 True 없으면 False
print(5 in cabinet)
cabinet["c-20"] = "조세호" #해당값이 없으면 추가, 있다면 덮어쓰기됨
print(cabinet)

#값 삭제
del cabinet[3]
print(cabinet)

#value들만 풀력
print(cabinet.values())

#key, value 쌍으로 출력
print(cabinet.items())
cabinet.clear()
print(cabinet)

#튜플> 할 수있는게 리스트보다 적지만 속도가 리스트보다 빠름, 값을 추가하거나 변경이 불가능함.
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])
name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)
name, age, hobby = ("김종국",20,"코딩")

#집합 (set) 중복안됨, 순서없음
my_set = {1,2,3,4,5,6,6,6,6}
print(my_set)
java = {"유재석","김태호", "양세형"}
python = set(["유재석","박명수"])

#자바와 파이선 가능한사람 > 교집합
print(java & python)
print(java.intersection(python))

#합집합 자바나 파이선 가능한사람
print(java | python)
print(java.union(python))

#차집합 자바가능하지만 파이선못하는사람
print(java-python)
print(java.difference(python))

#파이선할줄아는사람 늘어남
python.add("김태호")
print(python)

#자바를까먹음
java.remove("김태호")
print(java)

#자료구조변경
mn = {"컴피", "우유", "주스"}
print(mn, type(mn))

mn = list(mn)
print(mn, type(mn))

mn = tuple(mn)
print(mn, type(mn))

mn = set(mn)
print(mn, type(mn))

#랜덤모듈 셔플, 샘플
from random import *
Lst = [1,2,3,4,5]
print(Lst)
shuffle(Lst)
print(sample(Lst,4))

users = range(1, 21)#1부터 20까지 숫자를 생성
users = list(users)
print(users)
shuffle(users)
print(users)
winners = sample(users, 4) #4명중에 1명은치킨, 3명은커피
print(winners)
print("--당첨자 발표--")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("--축하합니다--")

#조건문
weather = input("호록?")
if weather == "비" or weather =="눈":
    print("우산챙겨요")
elif weather == "미세먼지":
    print("마스크챙겨")
else:
        print('준비물엄성')

temp = int(input("기온이몇?"))
if 30 <= temp:
    print("더워요 나가면 죽어요")
elif 10 <= temp and temp < 30:
    print("괜찮은날씨군요")
elif 0 <= temp and temp < 10 :
    print("외투챙겨요")
else:
    print("너무추워, 나가지마")

