#반복문
# print("대기번호 : 1")
# print("대기번호 : 2")

# for문
for waiting_no in range(1,6):
    print("대기번호 : {0}".format(waiting_no))

starbucks = ["아이언맨", "토르", "아이엠그루트"]
for customer in starbucks:
  print("{0}, 커피가 준비되었어요".format(customer))

# while
custom = "토르"
index = 5
while index >= 1:
    print("{0}, 커피준비요. {1}번 남았어요".format(custom, index))
    index -= 1
    if index ==0:
        print("커피처분 완료")

# person = "Unknown"
# while person != custom : #조건을 만족할때 까지 계속 반복한다
#   print("{0}, 커피가 준비되었다".format(custom))
#   person = input("이름이뭐에용?")

  # continue와 break
absent = [2, 5] #결석
no_book = [7] #책을 깜빡함
for student in range(1, 11): # 1,2,3,4,5,6,7,8,9,10
  if student in absent:
    continue
  elif student in no_book:
    print("오늘 수업 여기까지, {0}는 교무실로 와라".format(student))
    break
  print("{0}아 책을 읽어봐라".format(student)) 

  # 한줄 for문
#출석번호가 1,2,3,4,5 > 앞에 100을 붙이기로함
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

#이름을 길이로 변환
hero = ["iron man","thor", "i am groot"]
# hero = [len(i) for i in hero]
# print(hero)

#이름을 대문자로변환
hero = [i.upper() for i in hero]
print(hero)

# 택시기사인데 50명의 승객과 매칭기회가 있을 때, 총 탑승 승객수를 구하는 프로그램 작성
# 조건1: 승객별 운행 소요 시간은 5분~50분 사이의 난수
# 조건2: 당신은 소요 시간 5~15분 사이의 승객만 매칭  

from random import *
cnt =0
for i in range(1, 51):
  time = randrange(5, 51)
  if time <= 15:
     print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
     cnt += 1 
  else:
      print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

print("총 탑승 승객 : {0} 분".format(cnt))

# 함수
def open_account():
  print("새로운계좌생성되었어용")

def deposit(balance, money):
  print("입금이 완료요. 잔액은{0}원입니다.".format(balance + money))
  return balance + money

balance = 0
balance = deposit(balance, 1000)
print(balance)

def withdraw(balance, money):
  if balance >= money:
    print("출금이 완료요. 잔액은{0}원입니다.".format(balance - money))
    return balance - money
  else:
    print("출금 불가 잔액은 {0}원입니다.".format(balance))
    return balance

balance = 1000
balance = withdraw(balance, 500)
print(balance)
 
def profile(name, age, main_lang):
   print(name, age, main_lang)

profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", age=25, name="김태호")

# def prof(name, age, lang1, lang2, lang3, lang4):
#   print("이름: {0}\t 나이: {1}\t".format(name, age), end=" ") #<end=" "다음줄로 안가고 이어서 붙여서 출력
#   print(lang1, lang2, lang3, lang4)

# prof("유재석",20,"파이선","자바","호로로","뚠따")

def prof(name, age, *language):
  print("이름: {0}\t 나이: {1}\t".format(name, age), end=" ") 
  for lang in language:  #변수 만들어서 집어넣음
    print(lang, end=" ")
  print()

prof("유재석",20,"파이선","자바","호로로","뚠따")
from math import *

#표준체중구하는 프로그램 작성
def std_weight(height, gender):

  averweight = 0
  if gender == "남자" :
   averweight = height * height * 22
   averweight = round(averweight,2)
   print("키 {0}cm {1}의 표준체중은 {2}kg 입니다.".format(int(height*100), gender, averweight))
  else :
    averweight = height * height * 21
    averweight = round(averweight,2)
    print("키 {0}cm {1}의 표준체중은 {2}kg 입니다.".format(int(height*100), gender, averweight))
std_weight(1.75, "남자")

print("python", "Java")
print("python", "Java", sep=" , ") #sep 사용하면 중간에 적용가능
print("python", "Java","C", sep=" vs ")

print("python", "Java", sep=",", end="?") #문장끝에 ?를 달아버린다. 기본은 줄바꿈
print("어떤것이 좋아?")

import sys
print("python", "Java", file=sys.stdout) #표준출력
print("python", "Java", file=sys.stderr) #표준에러로 처리 

scores ={"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
  print(subject.ljust(8), str(score).rjust(4), sep=":") #8칸공간 확보하고 왼쪽정렬, 4칸확보하고 오른쪽정렬

#은행 대기순번표
for num in range(1, 21):
  print("대기번호 : "+str(num).zfill(3)) #zfill로 빈자리 0으로 채움

  #표준입력
  # answer = input("값 입력 : ") #사용자 입력을 이용해서 값을 받으면 항상 문자열로 받음
  # print("입력값은"+answer+"입니다.")

#정렬연습
print("{0: >10}".format(500))
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
print("{0:_<10} {1:_>10}".format(500, 231))
print("{0:,}".format(100000000)) #3자리마다 콤마를 찍어줌

#파일 입출력
# score_file = open("score.txt", "w", encoding="utf8") #w는 쓰기, 덮어쓰기
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8") # a는 뒤에 이어쓰기
# score_file.write("과학 : 80\n")
# score_file.write("코딩 : 100")
# score_file.close()

# 파일 한번에읽기
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

#한줄한줄 읽어오기
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="") #줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8") #전체가 몇줄인지 모를때 반복문 사용해서 읽어오기
# while True:
#  line = score_file.readline()
#  if not line:
#    break
#  print(line, end="")
# score_file.close()

# #리스트형태로
# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines() #list형태로 저장
# for line in lines:
#   print(line, end="")
# score_file.close()

#피클 데이터를 변수에 저장해서 사용하고싶을때 사용
import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"이름":"박명수", "나이":30, "취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) #profile 에 있는 정보를 file에 저장
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) #file에있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

# with
# with open("profile.pickle","rb") as profile_file:  #close문을 쓸필요없다.
#   print(pickle.load(profile_file))

# with를 이용한 파일 입출력
# with open("study.txt", "w", encoding="utf8") as study_file:  
#   study_file.write("파이썬을 공부하고 있다!")

# with open("study.txt", "r", encoding="utf8") as study_file:
#   print(study_file.read())

# 여러 순차적인이름의파일을 호로록하고 만드는거
# for i in range(1,5):
#   title =str("{0}주차.txt".format(i))
#   with open(title,"w",encoding="utf8") as report_file:
#     report_file.write("-{0}주차 주간보고-\n".format(str(i)))
#     report_file.write("부서 :\n")
#     report_file.write("이름 :\n")
#     report_file.write("업무 요약 :\n")
  
