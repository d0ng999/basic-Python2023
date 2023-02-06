# 차의 부모클래스
class Car: # Mother 클래스
    __name = '자동차'
    __color = 'white'
    __plate_number = ''
    __product_year = 1900



    def __str__(self) -> str:
        return f'부모 클래스'
    
    def get_color(self):
        return self.__color
    
    def get_name(self):
        return self.__name
    
    def run(self):
        return f'차가 달립니다.'
    
    def stop(self):
        return f'차가 멈춥니다.'
    
