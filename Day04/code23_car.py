# class 차량
import os

# __클래스 변수를 고정시켜서 외부에서는 변수를 바꿀 수 없게 만들어주는 함수
class Car:
    __number = '54라 9538'

    def get_number(self):
        return self.__number

    # 클래스 외부에서는 변경을 못하지만 멤버함수로는 내부에서 바꿀 수 있다. set
    def set_number(self, number):
        self.__number = number

    def __init__(self, number) -> None:
        self.__number = number
        print('__init__')
        
    # def __new__(cls):
    #     print('__new__')
    #     return super().__new__(cls) # super는 car 클래스의 부모 클래스

    def __str__(self) -> str:
        return f'차 번호는 {self.__number}입니다.'


yourcar = Car('88호 1234')
print(yourcar)
yourcar.__number = '54라 9538' #클래서 외부에서는 값을 바꿀 수 없다. 접근 불가능
print(yourcar)

yourcar.set_number('77오 2232')
print(yourcar)

mycar = Car('number')
print(mycar)
print(f'나의 차는 아이오닉이고, 차 번호는 {mycar.get_number()}입니다')

# mycar.__number = '132거 8874'
# print(mycar.get_number())
# print(mycar)

# print(os.environ)
