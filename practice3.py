
# class House:
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year


#     def show_detail(self):
#         print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

# house = []

# #예외처리 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# try:
#     print("나누기 전용 계산기")
#     num1 = int(input("첫번째 숫자를 입력 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("에러! 잘못된 값을 입력하였어요")
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:  #위의 밸류에러, 제로디비전에러를 제외한 거의 모든 에러 예외처리 가능
#     print(err)