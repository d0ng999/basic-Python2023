# 연산자 - Operator
# 할당연산 - assignment
val = 1 # val라는 변수 메모리공간에 1이라는 값을 넣었다. (할당했다)

# equal 연산자(==)
print(val)

# 사칙연산
print(1 + 1)
print(1 - 1)
print(10 * 10)
print(3 / 2) # 소수점까지 결과값에 나옴
print(3 // 2) # 정수만이 결과값에 나타남
print(3 % 2) # 나머지 값이 나옴
print(10 ** 2) # 10^2
print(2 ** 10) # 2^10

# print(6 / 0) - 0으로 나누는 것은 불가능 = 오류
# print(6 // 0)
# print(6 % 0) - ZeroDivisionError

# 문자열연산
# + 와 *만 연산가능
first = 'Hello'
second = 'World!'
print(first + second)
print(first, second)
print(first + ' ' + second)
print((first + ' ') * 3)
print(len(first)) # first문자열의 길이 = len
# print(first[0])
# print(first[1])
# print(first[2])
# print(first[3])
# print(first[4])
# []는 리스트를 의미

# 파이썬에서만 인덱스를 찾는 특이한 방법
print(first[-1])
print(first[-2])
print(first[-3])
print(first[-4])
print(first[-5])

current = '2023-01-31 15:14:15'
print(len(current))
# print(current[0:4]) # 0에서 3까지 리스트를 뽑는다
# print(current[-19:-15]) #
# print(current[-19:4]) 이 세개는 같은 결과값.
print(current[5:7])
print(current[8:10])
print(current[11:13])
print(current[14:16])
print(current[17:]) # [**:]공백은 끝까지라는 의미

print(current[0:4] + '년' + current[5:7] + '월' + current[8:10] + '일' +
      current[11:13] + '시' + current[14:16] + '분' + current[17:] + '초')

# 리스트 연산
que = [1, 2, 3, 4, 5]
que[0] = 7 # 리스트 0번째 값을 변경
print(que)

que.append(10) # 리스트 맨 마지막에 10이라는 값을 추가된 공간에 넣음
print(que)

que.insert(3,99)
# 3번째에 공간, 특정 인덱스에 하나 더 만들어 99라는 값을 넣음
print(que)

que.remove(10) # 해당 값을 리스트에서 제거
print(que)

# que[5] = 10 , 길이가 안맞아서 x
# print(que)
 
# tup = (1, 2, 3, 4, 5) # ()는 튜플이라 
# tup[1] = 9 # 변경이 불가능
# print(tup)

# 문자열 == 문자 리스트
title = 'Python'
print(title[0])
# title[0] = 'p' - 문자열 리스트는 변경이 불가능
print('P' + title[1:]) # 이렇게 바꾸는 것 가능
# print(title)

# 일반적인 문자열 리스트
text = ['p', 'y', 't', 'h', 'o', 'n']
text[0] = 'P' # 각각 나열한 리스트의 경우 가능
print(text)

# 문자열 포멧팅
print("I'm so happy {0} you".format('to')) 
# .format(숫자 및 '문자') 숫자가 {0}에 들어간다.
print("I'm so happy {0} you, {1}".format('to', 'Hey')) 
# {숫자}에서 숫자는 순서를 나타낸다.
# 이걸 통해서 format()내부의 값을 순서대로 입력

# 같은 format형식이지만 최신식!!
preword = 2
sayHello = 'Hey'
print(f"I'm so happy {preword} you, {sayHello}!!")

pi = 3.141592
print(f'파이는 {pi}입니다.')
print(f'파이는 {pi:5.3f}입니다.') # {pi:0.2f}는 소수점 두 번째자리에서 컷!
print(f'파이는 {pi:10.2f}입니다.') 
# {pi:*.*f}에서 *는 숫자
# .을 기준으로 앞 숫자만큼 자릿수를 늘리고, 뒷 숫자만큼 소수점자리를 늘림.

print('================')
# .split('?') 특정 문자로 자르기
full_name = 'DH Hong.123'
vals = full_name.split() # 스페이스
# .split()에서 ()안이 공백이라 공백을 기준으로 이름을 나눈다
print(type(vals))
print(vals)

vals = full_name.split('.') # .
# ('.') .을 기준으로 이름을 나누어준다.
print(vals)

print(full_name.replace('DH', 'DongHyun'))
# .replace(' ', ' ') 앞 문자를 뒤 문자로 바꾸어 준다.

# 문자열 공백 없애기
# 예로 검색을 하다가 공백을 넣는 실수를 해도 검색이 가능하게 만들어주기 위해
hi = '         Hello~ Bye~         '
# .strip() 벗겨낸다는 뜻으로 ()가 공백이라 공백을 벗겨냄
print(hi.lstrip() + '|') # lstrip은 left쪽 공백을 벗겨냄
print(hi.rstrip() + '|') # rstrip은 right쪽 공백을 벗겨냄
print(hi.strip() + '|') # strip은 전부다 벗겨냄

# .index('문자') 리스트에서 값을 찾기
print(full_name.index('D'))
print(full_name.index(' '))

# .find() 문자를 찾는 용도
# 단, 찾는 문자가 없으면 -1이 나온다.
print(full_name.find('Z'))
print(full_name.find('D'))

# .count() 찾는 문자의 갯수를 알려줌
print(full_name.count('H'))

# 모든 단어를 대문자/소문자로 변경
# 예로 검색 시 대문자/소문자가 방해요소가 되는 것을 방지하는 목적
# .upper() 모든 알파벳을 대문자로 변경
# .lower() 소문자로 변경
print(full_name.upper())
print(full_name.lower())

# 연산자 우선순위
print(3 + 4 * 2)
print((3 + 4) * 2)


