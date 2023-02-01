# if문
# == 같다 // != 같지 않다
# 들여쓰기 중요!★♬

name = '동현'
state = '아픔'

if name == '동현': # 끝에 :을 꼭 넣기!
    print('진료실에서 담당의사를 만납니다.')

    if state == '아픔2':
        print('선생님, 아파요')
        print('어디가 아프십니까?')

    else:
        print('어디가 아프십니까')
        print('안아픈데요')
        print('왜 오셨어요?')

    # print('선생님, 배가 아파용~')
    # print('어디 아프세요:)')

elif name == '동현': # else if == elif
    print('주사실로 갑니다~')
    print('주사를 맞습니다')

else: # 끝에 :을 꼭 넣기!
    print('조용히 기다립니다.')