# 차의 부모클래스를 상속한 제네시스 클래스
from code38_car2 import *

class Genesis(Car): # 자식클래스

    def __init__(self, name, color, 
                 plate_number, product_year) -> None:
        super().__init__()
        self.__name = name
        self.__color = color
        self.__plate_number = plate_number
        self.__product_year = product_year

        print(f'{self.__name} 인스턴스가 생성!')
    
    def get_color(self):
        return self.__color

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def run(self):
        return f'{self.__name}이가 달립니다.'

    def stop(self):
        return f'{self.__name}이가 멈춥니다'




gv80 = Genesis('gv80', 'black', '66로 1234', 2022)
# gv80.set_name('gv80')
print(f'이 차의 이름은 {gv80.get_name()}입니다')
print(gv80.run())
print(gv80.get_color())