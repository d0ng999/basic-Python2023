# random 모듈 사용
import random # 무작위 숫자를 만들어주는 모듈

# print(random.choice(range(1,7)))

numbers = [i for i in range(1,46)] # i라는 변수의 리스트 범위가 1~45까지

lottery = []

for i in range(6): # range(6) = 0, 1, 2, 3, 4, 5
    lottery.append(random.choice(numbers))

print(lottery)