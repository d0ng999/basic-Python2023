# 클래스 객체지향
# 클래스 생성
class Person:
    name = '익명'
    height = ''
    gender = ''
    blood_type = 'A'

    def walk(self):
        print('걷습니다.')

    def run(self, option):
        if option == 'Fast':
            self.walk()
            print(f'{self.name}이(가) 빨리 뜁니다.')
        else:
            print(f'{self.name}이(가) 천천히 뜁니다.')

    def stop(self):
        print('멈춥니다.')

donghyun = Person() # 객체를 instance
donghyun.name = '홍동현'
donghyun.height = '171'
donghyun.gender = '남'
donghyun.blood_type = 'B'

print(f'{donghyun.name}의 혈액형은 {donghyun.blood_type}입니다.')

donghyun.run('Fast')