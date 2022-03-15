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

        
