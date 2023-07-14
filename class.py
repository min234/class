#예제 1
class Student:
    def start(self):
        print('안녕하세요')
    def printName(self,name):
        print('이름은 {0} 입니다'.format(name))

stu = Student()
Student.start(stu)
stu.printName('홍길동')

#예제 2
class Student:
    schoolName = 'Korea'

stu1 = Student() # 객체 생성
stu2 = Student()

#id () : 객체의 주소를 돌려주는 내장함수
print('stu1의 주소 : {0}'.format(id(stu1)))
print('stu2의 주소 : {0}'.format(id(stu2)))

#위의 2개의 객체는 각각 생성자를 호출해서 만들어진 것이므로 서로 다른 영역 차지하고 만듬

Student.schoolName='Seoul'

print("\nStudent의 학교 : ", Student.schoolName)
print("stu1의 학교 : ", stu1.schoolName)
print("stu2의 학교 : ", stu2.schoolName)

'''
schoolName은 메소드 외부에서 만들어진 것이므로 
class변수가 되고 클래스 변수는 1개만 만들어서
클래스와 클래스로부터 만들어진 객체 모두가 공유해서 사용
따라서 위의 3개의 출력문은 모두 동일한 값을 출력
'''

#예제 3

class Student:
    schoolName ='Korea'

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

stu1 = Student()
stu2 = Student()

stu1.setName('홍길동')
stu2.setName('윤동주')
#호출할 땐 self안씀. 메소드 안에서만 self 써서 다른곳에서도 가져다 쓸 수 있음.
print("stu1의 이름 : {0}".format(stu1.getName()))
print("stu2의 이름 : {0}".format(stu2.getName()))


#클래스 생성 예제 : ball
class Ball:
    # 객제의 attribute를 지정
    size = 0
    color = ''
    direction = ''

    def bounce(self):#객체의 method를 지정
        if self.direction == 'down' :
            self.direction == 'up'
        else :
            self.direction = 'down'

myBall = Ball()
yourBall = Ball()

myBall.color = 'red' #myball 객체의 color 멤버 변수값 지정
yourBall.color = 'blue' #yourball 객체의 color 멤버 변수값 지정

print(myBall.color, ' ', yourBall.color)

#객체 초기화 실습
class Ball:

    def __init__(self, size, color, direction):
        self.size = size
        self.color = color
        self.direction = direction


    def bounce(self):
        if self.direction =='down':
            self.direction = 'up'
        else:
            self.direction = 'down'
        print("Bounce to",self.direction)

myBall = Ball('small', 'Red', 'down')#객체의 초기값을 입력하여 생성
yourBall = Ball('small', 'Red', 'up')

for i in range(0,3):#공 튕기기
    myBall.bounce()
    yourBall.bounce()
    #생성자와 소멸자 예제


# 소멸자 예제
class IceCream:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        print(name+"의 가격은"+ str(price)+"원 입니다.")

    def __del__(self):
        print(self.name +"객체가 소멸합니다.")

ice_cream = IceCream('부라보콘',1000)

del ice_cream
ice_cream = IceCream('부라보',1000)
#생성자와 소멸자 예제 3
from time import ctime

class Student:
    #생성자
    def __init__(self, name = 'noname'):
        print('{0}에 객체가 생성되었습니다'.format(ctime()))
        self.name = name

    schoolNAme = 'korea'
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name

    #소멸자
    def __del__(self):
        print('{0}에 객체가 소멸되었습니다'.format(ctime()))

stu1 = Student("중앙")
stu2 = Student()
print("stu1의 이름 : {0}".format(stu1.getName()))
print("stu2의 이름 : {0}".format(stu2.getName()))
del stu1
del stu2

#############################################################

#클래스에 메소드 추가하기 1
class BusinessCard:
    def set_info(self, name, email, addr):
        self.name = name
        self.email = email
        self.addr = addr
member1 = BusinessCard()
print(member1)

#############################################################

# 클래스에 메소드 추가하기 2
class BusinessCard:
    def set_info(self, name, email, addr):
        self.name = name
        self.email = email
        self.addr = addr

    def print_info(self):
        print("------------------")
        print("Name     :  ", self.name)
        print("Email     :  ", self.email)
        print("Address     :  ", self.addr)
        print("------------------")

member1 = BusinessCard()
member1.set_info("Yuna Kim","yunaKim@naver.com","Seoul")

#############################################################

#생성자 - 자동호출, 객체 초기화
#인스턴스 생성과 동시에 자동으로 호출되는 메소드 사용 : 생성자
class BusinessCard:
    def __init__(self, name, email, addr):
        self.name = name
        self.email = email
        self.addr = addr

    def print_info(self):
        print("---------------------------------------")
        print("Name     :  ", self.name)
        print("Email    :  ", self.email)
        print("Address  :  ", self.addr)
        print("---------------------------------------")

member1 = BusinessCard("Yuna Kim","yunaKim@naver.com","Seoul")
member1.print_info()