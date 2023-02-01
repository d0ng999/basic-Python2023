# 구구단을 외자!
for x in range(1, 10):
    print(f'{x}단 시작 : ', end = ' ')
    for y in range(1,10):
        print(f'{x} * {y} = {x*y:>2},', end = ' ') # :>2 오른쪽정렬하게 만들어줌, 숫자는 자릿수를 맞춰줌
    print()

# 디버깅하는법
