# 다중입력

# x, y = input('두 영단어를 입력하세요 > ').split()

# print(x)
# print(y)

# 완전 다중입력 (몇개든 상관없음)
# 중요@!#!#
# map만 쓰면 단어를 저장할 공간이 없다 -> 그래서 리스트 사용
inputs = list(map(str, input('단어를 입력하세요 > ').split()))

print(inputs)

inputs = list(map(int, input('정수를 입력하세요 > ').split()))

print(inputs)
