# 모듈 사용
import math as m # math라는 모듈이름을 m으로 변환 , 클래스로 안된 모듈
import code22_person as p # 우리가 만든 클래스
from code23_car import Car

pi = m.pi
print(m.pi)
print(pi)
print(m.sin(8))
print(m.ceil(3.8)) # 올림
print(m.floor(3.8)) # 내림
print(m.pow(2 , 10)) # 2의 10승

# 우리가 만든 모듈을 사용
me = p.Person('홍길순', 155, '여성')
print(me)

#
mycar = Car(' ')
print(mycar)