#input : 사용자 입력을 받는 함수
# lang = input("언어를 입력")
# print("{0}는 버러지언어".format(lang))

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
#print(dir())
import imp
import random
from unicodedata import name #외장함수
print(dir())
import pickle
print(dir())
print(dir(random))

name = "jim"
print(dir(name))

#---------------외장 함수들-----------------------
# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우dir)
import glob
print(glob.glob("*.py")) # 확장자 py인 모든 파일 출력

# os : 운영체제에서 제공하는 기본기능
# import os 
# print(os.getcwd()) #현재 디렉토리 

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder) #폴더생성
#     print(folder, "폴더를 생성하였습니다.")
# print(os.listdir())

# time : 시간 관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
print("오늘 날짜는 ", datetime.date.today())

#timedelta : 두 날짜 사이의 간격
today = datetime.date.today() #오늘 날짜 저장
td = datetime.timedelta(days=100) #100일 저장
print("우리가 만난지 100일은",today + td) #오늘부터 100일 후



