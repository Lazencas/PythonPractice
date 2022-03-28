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

#@@@ 22년 3월 27일
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

#@@@ 22년 3월 28일
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

