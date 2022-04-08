#코드업100제 사용자아이디 : dkfkskgks
#  문제 풀이 1~8
#print("print(\"Hello\\nWorld\")")

#
#변수는 수나 문자등의 어떤 값을 저장할 수 있는 공간. 숫자로 시작하는 변수이름은 사용 불가, 수로 인식함.
#@@ 9번
# v = input()
# print(v)

#@@ 10번 
#숫자 0-9 와 소수점을 사용해 표현한 수를 실수라고 한다.
# n = input()
# n = int(n)
# print(n)

#@@ 11번
# f = input()
# f = float(f)
# print(f)

#@@ 12번
# a = input()
# b = input()
# print(a+"\n"+b)

#@@ 13번
# a = input()
# b = input()
# print(b+"\n"+a)

#@@@ 22년 3월 27일   &&&&&&&&&&&&&&&&&&&&
#@@ 14번
# f = input()
# print(f)
# print(f)
# print(f)

#@@ 15번
# a, b = input().split() # input().split() 를 사용하면, 공백을 기준으로 입력된 값들을 나누어(split) 자른다. 파이썬만가능.
# print(a)
# print(b)

#@@ 16번
# c1, c2 = input().split()
# print(c2, c1)

#@@ 17번 파이썬은 문자/정수/실수/문자열 등 특별한 구분 없이도 원하는 변수에 저장시켜 출력 가능. 저장된 값을 이용해 계산하거나 서로 붙여
#연결시키거나 잘라내는 작업을 하려면 저장되어있는 값의 종류를 구분해줘야 한다.
# s = input() 
# print(s, s, s) #공백으로 구분해 한 줄로 출력.

#@@ 18번
# a,b = input().split(':') # : 기호를 기준으로 자른다.
# print(a, b, sep=":") # sep를 사용하면 중간에 값 집어넣기 가능.

#@@ 19번 "연도.월.일"을 입력받아 "일-월-연도" 순서로 바꿔 출력해보자.
# y, m, d = input().split('.')
# print(d, m, y, sep='-')

#@@ 20번
# a, b = input().split('-')
# str(a)
# str(b)
# c = a+b
# print(c)

#@@ 21번
# s = input()
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])
# print(s[4])

#@@ 22번
# n = input()
# print(n[:2],n[2:4],n[4:]) #n[2:4] 2번째 자리이상 4번째 자리미만

#@@ 23번 시:분:초 형식으로 시간이 입력될 때 분만 출력해보자.
# h, m, s = input().split(':')
# print(m)

#@@ 24번 알파벳 문자와 숫자로 이루어진 단어 2개를 입력받아 순서대로 붙여 출력하는 프로그램을 작성해보자.
# a, n = input().split()
# print(a+n)

#@@@ 22년 3월 28일       &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
#@@ 25번
# a, b = input().split()
# c = int(a) + int(b)
# print(c)

#@@ 26번
# a= input()
# b=input()
# c = float(a) + float(b)
# print(c)

#@@ 27번 10진수를 입력받아 16진수(hexadecimal)로 출력
# a = input()
# n = int(a) 
# print('%x'%n) #n에 저장되어있는 값을 16진수(hexadecimal) 소문자 형태 문자열로 출력, %o로 출력하면 8진수(octal) 문자열로 출력된다.

#@@ 28번
# a = input()
# n = int(a)
# print('%X'% n)

#@@ 29번 16진수를 입력받아 8진수(octal)로 출력해보자.
# a = input()
# n = int(a, 16)  #입력된 a를 16진수로 인식해 변수 n에 저장
# print('%o'% n)

#@@ 30번 영문자 1개를 입력받아 10진수 유니코드(Unicode) 값으로 출력해보자.
# n = ord(input()) #ord()는 어떤 문자의 순서 위치 값을 의미한다. ord(c):문자c를 10진수로 변환한 값
# print(n) #유니코드는(unicode) 세계 여러나라의 문자를 공통된 값으로 저장할 때 사용하는 표준 코드이다.

#@@@ 22년 3월 29일   &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
#@@ 31번 10진 정수 1개를 입력받아 유니코드 문자로 출력해보자.
# n = int(input()) # chr() 정수값 > 문자 , ord() 문자  > 정수값 형태로 바꿔주는 반대 역할
# chr(n) #????? 
# print(chr(n))

#@@ 32번
# n = int(input()) #파이썬은 입력받을때 그냥 형태를 지정해주는게 좋을지도?
# print(-n)

#@@ 33번 문자 1개를 입력받아 그 다음 문자를 출력해보자. 영문자 'A'의 다음 문자는 'B'이고, 숫자 '0'의 다음 문자는 '1'이다.
# c = ord(input())
# c =chr(c+1)
# print(c)

#@@ 34번 정수 2개(a, b)를 입력받아 a에서 b를 뺀 차를 출력하는 프로그램을 작성해보자.
# a, b=input().split()
# c = int(a) - int(b)
# print(c)

#@@ 35번 실수 2개(f1, f2)를 입력받아 곱을 출력하는 프로그램을 작성해보자.
# f1, f2 = input().split()
# f3 = float(f1) * float(f2)
# print(f3)

#@@ 36번 단어와 반복 횟수를 입력받아 여러 번 출력해보자.
# word, repeat = input().split() 
# print(word*int(repeat)) #이거는 좀 신기하다. 문자*정수 하면 그만큼 반복출력.

#@@ 37번
# n = input()
# s = input()
# print(int(n)*s)

#@@ 38번 a를 b번 곱한 거듭제곱을 출력
# a, b = input().split()
# c = int(a)**int(b)
# print(c)

#@@ 42번 실수 1개를 입력받아 소숫점 이하 두 번째 자리까지의 정확도로 반올림한 값을 출력
# a = float(input()) #실수는 컴퓨터에서 2진정수화 되는 과정에서 아주 작은 부분이 저장되지 않고 사라지는 잘림오차가 자주 발생한다. 정교한계산X
# print(format(a,".2f"))

#@@ 43번 f1 을 f2 로 나눈 값을 출력해보자. 이 때 소숫점 넷째자리에서 반올림하여 무조건 소숫점 셋째 자리까지 출력한다.
# f1, f2 = input().split() #유효숫자는 측정을 통해 기록되는 숫자중 의미있는 숫자.
# f3 = float(f1) / float(f2)
# print(format(f3,".3f"))

#@@ 46번 정수 1개를 입력받아 2배 곱해 출력해보자.
# n = int(input()) # n=10과 같이 입력받지 않고 직접넣은 코드에서, 숫자로 시작하는 단어는 자동으로 수로 인식한다.
# print(n<<1) #파이썬은 실수값에 대한 비트시프트연산은 허용하지 않고 오류가 발생한다.

#@@ 49번 
# a, b =input().split()
# print(a==b)

#@@ 53번
# n = bool(int(input()))
# print(not n)

#@@@ 22년 3월 30일               &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
#@@ 54번 2개의 정수값이 입력될 때, 그 불 값이 모두 True 일 때에만 True 를 출력하는 프로그램을 작성해보자.
# a, b= input().split()
# print(bool(int(a)) and bool(int(b)))

#@@ 56번 2개의 정수값이 입력될 때, 그 불 값(True/False) 이 서로 다를 때에만 True 를 출력하는 프로그램을 작성해보자. &&&&&&
# a, b = input().split()
# c = bool(int(a))
# d = bool(int(b))
# print((c and(not d))or((not c)and d))

#@@@ 22년 3월 31일
#@@ 57번 2개의 정수값이 입력될 때,그 불 값(True/False) 이 서로 같을 때에만 True 를 출력하는 프로그램을 작성해보자.
# a, b = input().split()
# c = bool(int(a))
# d = bool(int(b))
# print((c and d)or(not c and not d))

#@@ 58번 2개의 정수값이 입력될 때, 그 불 값(True/False) 이 모두 False 일 때에만 True 를 출력하는 프로그램을 작성해보자.
# a, b = input().split()
# c = bool(int(a))
# d = bool(int(b))
# print(not c and not d)

#@@@ 22년 4월 1일                    &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# 59번 입력 된 정수를 비트단위로 참/거짓을 바꾼 후 정수로 출력해보자. 비트단위(bitwise)연산자 ~ 를 붙이면 된다.(~ : tilde, 틸드라고 읽는다.)
# a = int(input())
# a = ~a
# print(a)

#@@ 60번 입력된 정수 두 개를 비트단위로 and 연산한 후 그 결과를 정수로 출력해보자.
# a, b = input().split()
# a = int(a)
# b= int(b)
# print(a&b) #이 계산은 네트워크에서 데이터 주고받기 위해 같은 네트워크에 있는지를 판단하기 위해 사용.
#비트단위 연산은 빠른 계산이 필요한 그래픽처리에서 마스크연산(특정부분을 가리고 출력하는)을 수행하는 데에 효과적으로 사용된다.

#@@ 61번
# a, b = input().split()
# a =  int(a)
# b = int(b)
# print(a|b)
#비트연산자 계산은 왜 더 빠르지? > 컴퓨터가 애초에 숫자를 비트단위로 계산하니까 비트계산하면 숫자 > 비트단위로 변환하는 과정이 없어도 되서그럴듯 
#근데 그게 어느정도 빠를려나......

#@@ 62번 입력된 정수 두 개를 비트단위로 xor 연산한 후 그 결과를 정수로 출력해보자.
# a, b = input().split() # ^는 배타적 논리합, 서로 다를 때 1
# a =  int(a)
# b = int(b)
# print(a^b)
#두 장의 이미지가 겹쳐졌을 때 색이 서로 다른 부분만 처리 할 수 있다.
#배경이 되는 그림과 배경위에서 움직이는 그림이 있을 때, 두 그림에서 차이만 골라내 배경위에서 움직이는 그림의 색으로 바꿔주면
#전체 그림을 구성하는 모든 점들의 색을 다시 계산해 입히자 않고 보다 효과적으로 그림을 처리할 수 있게 된다.

#@@ 63번 입력된 두 정수(a, b) 중 큰 값을 출력하는 프로그램을 작성해보자. 단, 3항 연산을 사용한다.
# a, b = input().split()
# a =int(a)
# b = int(b)
# c = (a if(a>=b) else b)
# print(int(c))

#@@ 64번 입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자. 단, 3항 연산을 사용한다.
# a, b, c = input().split()
# a =int(a)
# b = int(b)
# c = int(c)
# d = (a if(a<=b) else b)
# e = (d if(d<=c) else c)
# print(e)

# a, b, c = input().split()
# a =int(a)
# b = int(b)
# c = int(c)
# print(c if c<=(a if(a<=b) else b) else (a if(a<=b) else b))

#@@ 65번 3개의 정수(a, b, c)가 입력되었을 때, 짝수만 출력해보자.
# a, b, c = input().split()
# a = int(a)
# b = int(b)
# c = int(c)
# if(a % 2 ==0) :
#  print(a)

# if(b % 2 ==0) :
#  print(b)

# if(c % 2 ==0) :
#  print(c)
 # python 에서는 논리적 실행단위인 코드블록(code block)을 표현하기 위해 들여쓰기를 사용.
 # 한 소스코드 내에서 들여쓰기 길이와 방법으 똑같아야 한다.

#@@ 71번 0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.
# n = 1
# while n!=0:
#     n = int(input())
#     if n!=0:
#         print(n)

#@@ 72번 정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.
# n = int(input())
# while n > 0 :
#     if(n > 0) :
#         print(n)
#         n -= 1

#@@@ 22년 4월 2일                       &&&&&&&&&&&&&&&&&&&&

#@@ 76번 정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.
# n = int(input())
# for i in range(n+1) :
#     print(i)

#@@ 77번 정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.
# a = 0
# int(a)
# n = int(input())
# for i in range(1,n+1):
#     if (i%2 == 0):
#         a += i
# print(a)

#@@@ 22년 4월 8일
#@@ 78번 영문 소문자 'q'가 입력될 때까지 입력한 문자를 계속 출력하는 프로그램을 작성해보자.
# c = 'a'
# while c!='q':
#  c = input()
#  print(c)
