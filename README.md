# studyPython2023
부경대 IoT Python 학습 리포지토리

설정 ctrl + ,

## 1일차
1. 기본구성
    - Git/Github 설치 및 연동
    - Visual Studio Code 설치 및 연동
    - Python 설치

2. Python 기본
    - 콘솔출력
    - 주석

```Python
# 백틱 ``` : 코드 블럭을 작성할 수 있다.
# desc : 콘솔출력 / 여기는 주석입니다!
print('Hello, Python!!') # 콘솔출력 함수
```

## 2일차 
1. Python 기본
    - 콘솔출력+
        - 파라미터 end와 sep를 배움
```python
# python에서는 함수의 끝은 enter = 다음 줄로 넘어감
# end=' '는 enter를 공백으로 변경.
print('*', end=' ')
# 원래는 a b c로 출력되는 것처럼 공백으로 띄어쓰기가 되지만
# sep='?'는 공백구분자를 ?으로 대체해준다.
print('a', 'b', 'c', sep='/')
```
    - 변수
        - 변수지정이 엄격하지 않음
        - id = 메모리주소 
        - 변수명은 영어 _ 숫자의 조합으로 완성가능
```python
val = 'Hello'
print(val)
print(id(val))
plant_major_upper_code = 'U13TEMP'
print(id(plant_major_upper_code))
```
    - 자료형(type(변수)함수)
        - None : 값이 없는 값으로 0도 아니고, 빈 공간도 아니다.
```python
print(None) 
print(0 == None) # False 거짓이라는 뜻
print('' == None) # False
```
        - 숫자형 : int(정수형), float(유리수형), str(string의 약자, 문자열형)등..
```python
val = 0b1010 # 0b는 이진수를 표현하기 위한 것. 0b**** 형태
print(type(val))
val = 4_520_000 # 숫자사이에 _는 단위를 표현을 위해 사용
val = 4_530.99 # 소수점도 가능
```
        - 문자열형
            - " ", ' ' 두 가지의 형태로 쓸 수 있다.
```python
val = 'Hell\nWorld' # 탈출문자 \n은 enter를 누른 것
val = 'Hell\tWorld' # \t는 tab을 누른 것
val = 'Hell\t\bWorld' # \b는 backspace을 누른 것
val = 'Life is short\nYou need Python'
val = '''Life is short,
You need Python''' # '''~~~'''여러 줄을 함께 사용할 수 있다.
# 단 문자열을 쓸 때, '를 여러번 쓸 일이 생긴다면 ""가 편하다.
#''에서는 '를 \'이렇게 사용해야한다.
val = 'Hi, I\'m \'Hong\'' # 이 두개는 서로 같다. ""와 ''의 차이는 없음
```
        - 불형 or Boolean형
            - 참인지 거짓인지 판별하는 자료형태
```python
참 = True
거짓 = False
print(거짓 == True) # 거짓이라는 False 값 변수가 True인지 물어봄
print(거짓 == False)
print(거짓 is False) # ==대신 is 도 가능.
print(bool(1)) # 1 == True
print(bool(0)) # 0 is False
```
    - 리스트 및 튜플, 딕셔너리, 집합 등의 복합형
        - 리스트 = 배열
        - 리스트는 []를 사용
        - []는 순서를 가지고 있음
```python
arr1 = [1,2,3]
arr2 = [1.1,2.2,3.3]
arr3 = ['Hello', 12, 'World!!', 213] # 자료형은 list
print(arr1, arr2, arr3)
print(type(arr1))
arr4 = [] # 빈 리스트
arr5 = list() # 이것도 마찬가지
arr6 = [1,2,3,4,[6,7,8,[9,10]]] # 리스트 안에 다른 리스트
arr7 = [[1,2,3,4],[5,6,7,8]] # 3차원 배열
# 리스트는 수정 및 변경이 가능
arr5.arrend(4) # .arrend(숫자)를 사용해서 빈 리스트에 숫자를 넣었다.
```
        - 튜플 
            - 튜플은 수정, 변경이 불가능
            - 튜플은 ()를 사용
```python
tuple1 = (1,2,3,4)
print(tuple1)
print(type(tuple1))
# tuple1.append(4) - 오류이지만 빨간줄은 안나옴!!
```
        - 딕셔너리
            - 해시 테이블이라고도 함
            - 딕셔너리는 {}를 사용
            - {}는 순서가 없음
```python
# 딕셔너리 {'' : ''}
spiderman = {'name' : 'Peter Parker',
              'age' : 18,
           'weapon' : 'Web shooter', 
          'deseter' : '탈영병'} # {}는 한 줄에 다 쓸 필요없다
print(spiderman)
print(spiderman['deseter']) # ctrl + space = 변수 목록
print(type(spiderman))
```
        - 집합     
            - set함수
            - 집합은 {}를 사용
            - {}는 순서가 없음.
```python
# 비순차적이다. {}는 비순차적.
set1 = set([1,2,3,4])
print(set1)
set1 = set("Hello, World!")
print(set1) # 결과는 {'W', 'd', 'l', 'H', ' ', 'o', 'e', 'r', ',', '!'}
# 비순차적이고 중복은 1개만 출력, 문자는 1개씩만
```
    - 연산자
        - 할당연산자 Assignment
```python
val = 1 # val라는 변수 메모리공간에 1이라는 값을 넣었다. (할당했다)
```
        - equal 연산자 (==)
        - 사칙연산자
            - 단, 0으로 나누는 것은 불가능
```python
print(1 + 1)
print(1 - 1)
print(10 * 10)
print(3 / 2) # 소수점까지 결과값에 나옴
print(3 // 2) # 정수만이 결과값에 나타남
print(3 % 2) # 나머지 값이 나옴
print(10 ** 2) # 10^2
print(2 ** 10) # 2^10
```
        - 문자열 연산자
            - +와 *만 사용가능
```python
first = 'Hello'
second = 'World!'
print(first + second)
print(first, second)
print(first + ' ' + second)
print((first + ' ') * 3)
print(len(first)) # first문자열의 길이 = len
```
        - 리스트 연산
            - .append() : 리스트 맨 마지막에 값을 추가
            - .insert( , ) : 특정 인덱스에 값을 추가
            - .remove() : 특정 값을 리스트에서 제거
```python
que = [1, 2, 3, 4, 5]
que.append(10)
que.insert(3,99)
que.remove(10)
```
        - 리스트에서 인덱스 찾는 법
            - [숫자] : 숫자는 몇 번째인지를 나타내고, 항상 시작은 0부터
```python
first = 'Hello'
print(first[0])
print(first[-1])
print(first[1:3]) # first 리스트에서 1번째부터 2번째의 인덱스 값
print(fisrt[1:]) # [**:]공백은 끝까지라는 의미
```

        - 문자열 포멧팅(별표)
```python
pi = 3.141592
print(f'파이는 {pi}입니다.')
print(f'파이는 {pi:5.3f}입니다.') # {pi:0.2f}는 소수점 두 번째자리에서 컷!
print(f'파이는 {pi:10.2f}입니다.') 
```

```python
# 변수
val = 1
# 자료형
print(type(val)) # <class 'int'>
```

2. 깃헙 
    - 코드블럭작성
        - 사용 방법은 (```..```)으로 사용 가능


## 3일차
1. 파이썬 기본
    - 흐름제어
        - if
            - if, elif, else 문
        - for
            - for 변수 in 리스트
            - if문이랑 같이
            - 구구단 연습 (7줄)
            - range 문 연습 range(초기값, 끝 값, 증감)
            - continue & break
        - while
            - while 조건문 + if문
            - 나무찍기 연습
    - 구구단 프로그램
    - 함수
        - def 함수명 (파라미터): -> 함수 정의
        - 변수 = 함수식
        - return 변수
        - 복잡한 계산기 만들기
        - lambda함수라는게 있다

## 4일차
1. 파이썬 기본
    - 가상환경
        - pip 중요 python package index
        - 글로벌
    - 객체지향 프로그래밍(OOP)
        - 현실세계의 모든 객체(명사 + 동사)를 컴퓨터세계로~
        - 명사(변수) 와 동사(함수)
        - 붕어빵 틀 = class
        - class 클래스 명:
        - 속성변수 = 값
        - +함수
        - __init__, __str__ 자주 사용함.
    - 패키지
        - 패키지는 모듈의 집합
        - 모듈, import, from, as

## 5일차
1. 파이썬 기본
    - 패키지 
    - 입출력
    - 예외처리
    - 객체지향