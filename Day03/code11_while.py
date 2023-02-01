# while문
# while + 조건문
hit = 100 # 변수 초기화!! 중요☆

while True: # 무한반복
    hit += 1 # hit를 1씩 증가시킨다.

    print(f'나무를 {hit}번 찍었습니다.')
    if hit == 10:
        print('나무가 넘어졌습니다.')
        break
    else:
        print(f'나무가 아직 넘어가지 않았습니다. 힘들어~')
        # None

print(f'나무찍기 끝')