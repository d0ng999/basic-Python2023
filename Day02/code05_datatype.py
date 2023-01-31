# 자료형(Class)의 5종류 
# 1. None = 난 몰라 (값이 없다. 0도 아님, 비어있다는 것이 아님) 

print(None) 
print(0 == None) # False
print('' == None) # False

# 2. 숫자형 
val = 3 # int 정수 자료형
print(type(val)) #type(변수)함수 - 변수의 자료형을 알려줌.

val = 3.14 # float 유리수 자료형
print(type(val))

val = 'Hello' # str(string) 문자열 자료형
print(type(val))

val = 0b1010 # 0b는 이진수를 표현하기 위한 것. 0b**** 형태
print(type(val))

val = 12.2513511654646448848498413213154648796543164987
print(type(val))

val = 4_520_000 # 숫자사이에 _는 단위를 표현을 위해 사용
print(val)

val = 4_530.99 # 소수점도 가능
print(val)

# 3. 문자열형 
val = 'Life is short, You need Python'
print(val)
print(type(val))

val = 'Hell\nWorld' # 탈출문자 \n은 enter를 누른 것
print(val)
val = 'Hell\tWorld' # \t는 tab을 누른 것
print(val)
val = 'Hell\t\bWorld' # \b는 backspace을 누른 것
print(val)

val = 'Life is short\nYou need Python'
val = '''Life is short,
You need Python''' # '''~~~'''여러 줄을 함께 사용할 수 있다.
print(val)

val = "Hi, I'm 'Hong'"
print(val)
val = 'Hi, I\'m \'Hong\'' # 이 두개는 서로 같다. ""와 ''의 차이는 없음
print(val)
# 단 문자열을 쓸 때, '를 여러번 쓸 일이 생긴다면 ""가 편하다.
#''에서는 '를 \'이렇게 사용해야한다.

# 4. 불형 or Boolean형
참 = True
거짓 = False
print(type(거짓))
print(1 + 1 == 2)

print(거짓 == True) # 거짓이라는 False 값 변수가 True인지 물어봄
print(거짓 == False)
print(거짓 is False) # ==대신 is 도 가능.

print(bool(1)) # 1 == True
print(bool(0)) # 0 is False