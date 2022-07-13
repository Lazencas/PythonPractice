# 연관된 함수나 변수의 집합이라고 볼 수 있고 이것을 이용해 객체를 찍어 낼 수 있으므로 하나의 틀이라고도 볼 수 있다.
from turtle import speed
from unicodedata import name

#일반유닛
class Unit:
    def __init__(self, name, hp, speed):    #init은 생성자, 객체가 만들어질때 자동으로 호출되는 부분, self의 정체는 뭐냐!? 
        self.name = name #멤버변수이고 클래스내에서 정의된 변수이며 이 변수로 초기화를 할 수 있고 사용도 가능하다.        
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name,location,self.speed))   

#공격유닛        
class AttackUnit(Unit): # Unit클래스를 상속받음. 여기에서 상속해주는 Unit클래스는 부모클래스, 상속받은 AttackUnit클래스는 자식클래스
    def __init__(self, name, hp, damage, speed):
        # self.name = name    상속받은 Unit클래스에 있기때문에 안써도 됨. 대신 유닛클래스에서 만든 생성자를 호출해줘서 초기화해야함
        # self.hp = hp
        Unit.__init__(self, name, hp, speed)  #이런식으로 상속해주는 클래스의 생성자를 호출해서 초기화
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage)) #self없이 쓴 location은 전달받은 값을 바로 사용

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


marine1 = AttackUnit("마린", 40, 5, 2) #클래스로부터 만들어지는 개체를 객체라고 볼 수 있다.
marine2 = AttackUnit("마린", 40, 5, 2)

#레이스 : 공중유닛, 비행기, 클로킹(상대방에게 보이지 않음)
wraith1 = AttackUnit("레이스", 80, 5, 5)
print("유닛이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))  # 이런식으로 클래스의 멤버변수를 가져다 사용가능

#마컨당한 레이스
wraith2 = AttackUnit("레이스", 80, 5, 5)
wraith2.clocking = True   #클래스 외부에서 내가 원하는 멤버변수를 확장가능하지만 이 wraith2라는 객체에 대해서만 적용된다.

if wraith2.clocking == True :
 print("{0} 는 현재 클로킹 상태입니다".format(wraith2.name))

firebat1 = AttackUnit("파이어뱃",50,16,2)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)

# 드랍쉽 : 공중 유닛, 수송기, 공격X
#날 수 있는 기능의 클래스
class Flyable:
    def __init__(self, flying_speed):    #def랑 __init__ 사이 한칸 뛰어야함 안그러면 오류남.
     self.flying_speed = flying_speed

    def fly(self, name, location):
         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

#공중 공격 유닛 클래스, 다중상속
class FlyableAttackUnit(AttackUnit, Flyable): #공중나는것과 공격이 가능해야하기때문 2가지 클래스한테 상속받음      
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage, speed)  #상속받은 클래스 초기화할때는 사이 안뜀.
        Flyable.__init__(self, flying_speed)

    def move(self, location):  #일반유닛에 있던 지상유닛이동을 상속받아서 새로 덮어씀, 혹은 재정의. 메소드 오버라이딩 이라고한다.
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

#발키리
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly("valkyrie.name", "3시")

vulture = AttackUnit("벌쳐", 80, 10, 20)

battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
battlecruiser.move("9시")

#건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
      #  Unit.__init__(self, name, hp, 0)
      super().__init__(name, hp, 0)  #다중상속 받을경우 super는 맨처음것만 init함수가 호출됨.
      self.location = location

# supply_depot = BuildingUnit("서플라이디폿", 500, "7시")
