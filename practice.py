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

site = "http://hanmail.com"
print(site)
site = site[7:]
commawhere = site.index(".")
print(commawhere)
site = site[:commawhere]
print(site)
site = (site[:3]) + str(len(site)) + str(site.count('e')) + '!'
print(site)



