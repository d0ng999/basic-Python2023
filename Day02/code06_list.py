# 5. 리스트 및 튜플, 딕셔너리, 집합 등의 복합형
# 자료구조의 종류
# 배열
# 튜플
# 연결 리스트
# 원형 연결 , 이중연결, 환형 이중 연결 리스트
# 해시 테이블
# 등등...

# 1. 리스트
# 리스트는 추가, 수정 , 변경등이 가능함
# 리스트 == 배열
"""
a1 = 1
a2 = 2
a3 = 3
a4 = 4
a5 = 5
a6 = 6
a7 = 7
a8 = 8
a9 = 9
a10 = 10
print(a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10)
print(a1 ,a2, a3, a4, a5, a6, a7, a8, a9, a10)
"""

a = [1,2,3,4,5,6,7,8,9,10] # list는 []를 사용
print(a)
sum = 0
for i in a:
    sum += i

print(sum)

arr1 = [1,2,3]
arr2 = [1.1,2.2,3.3]
arr3 = ['Hello', 12, 'World!!', 213] # 자료형은 list
print(arr1, arr2, arr3)
print(type(arr1))

arr4 = [] # 빈 리스트
arr5 = list() # 이것도 마찬가지
print(arr5)

arr6 = [1,2,3,4,[6,7,8,[9,10]]] # 리스트 안에 다른 리스트
print(arr6)

arr7 = [[1,2,3,4],[5,6,7,8]] # 3차원 배열
print(arr7)


# 2. 튜플 - 수정, 변경등이 불가능
tuple1 = (1,2,3,4)
print(tuple1)
print(type(tuple1))

arr5.append(4) # 빈 리스트에는 .append()를 이용해서 넣을 수 있음
print(arr5)

# 주석 단축키는 ctrl + /
# tuple1.append(4) - 오류이지만 빨간줄은 안나옴!!
# 튜플은 .append()를 사용해도 넣지 못함
# 리스트와 튜플은 순서가 있다. (0부터 시작)
# []는 리스트용, {}는 딕셔너리용, ()는 튜플용

# 3. 딕셔너리 - 해시 테이블
# 딕셔너리는 순서가 없음
# 딕셔너리 {'' : ''}
spiderman = {'name' : 'Peter Parker',
              'age' : 18,
           'weapon' : 'Web shooter', 
          'deseter' : '탈영병'} # {}는 한 줄에 다 쓸 필요없다
print(spiderman)
print(spiderman['deseter']) # ctrl + space = 변수 목록
print(type(spiderman))

# 4. 집합
# 비순차적이다. {}는 비순차적.
set1 = set([1,2,3,4])
print(set1)

set1 = set("Hello, World!")
print(set1) # 결과는 {'W', 'd', 'l', 'H', ' ', 'o', 'e', 'r', ',', '!'}
# 비순차적이고 중복은 1개만 출력, 문자는 1개씩만
# print('arr1의 2번 인덱스 값은' + str(arr2[1]))