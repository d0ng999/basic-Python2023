# 클래스 객체지향
# 클래스 생성
class Person: # 클래스 정의 ()없음
    name = '익명'
    height = ''
    gender = ''
    blood_type = 'A'

    # 1. 초기화 추가
    # def __init__(self):
    #     self.name = '홍길동'
    #     self.height = '170'
    #     self.gender = 'male'
    #     self.blood_type = 'AB'

    def __init__(self, name = '홍동현', height = 171, gender = 'male') -> None:
        self.name = name # self.name의 name은 속성변수 = 다음의 name은 매개변수
        self.height = height
        self.gender = gender

    def walk(self): # self = 클래스 자기자신
        print(f'{self.name}이(가) 걷습니다.')

    def run(self, option):
        if option == 'Fast':
            self.walk()
            print(f'{self.name}이(가) 빨리 뜁니다.')
        else:
            print(f'{self.name}이(가) 천천히 뜁니다.')

    def stop(self):
        print(f'{self.name}이(가) 멈춥니다.')

    # 2. 생성자외 매직메서드(function) __str__
    def __str__(self) -> str:
        return f'출력 : 이름은 {self.name}, 성별은 {self.gender}입니다.'

# 객체를 instance, person이라는 함수를 만들 때 ()씀
donghyun = Person() # 객체생성!
# donghyun.name = '홍동현'
# donghyun.height = '171'
# donghyun.gender = '남'
# donghyun.blood_type = 'B'

print(f'{donghyun.name}의 혈액형은 {donghyun.blood_type}입니다.')

donghyun.run('Fast')
print(donghyun)

# 1. 초기화 후 새로 객체 생성
hong = Person()
hong.run('')
print(hong)

print('====================')

# 2. 파라미터를 받는 생성자 실행
ashely = Person('애슐리', 165, 'female')
print(ashely.name)
print(ashely.height)
print(ashely.gender)
print(ashely.blood_type)
print(ashely)