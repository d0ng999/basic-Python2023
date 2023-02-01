# 무한반복 예제
# 입력함수 - input
# key = input('이름 : ')
# print(f'안녕하세요, {key}님!@!')
num = 0

while True:
    print('메뉴를 선택하세요.')
    print('  1. 회원입력')
    print('  2. 회원검색')
    print('  3. 회원수정')
    print('  4. 회원삭제')
    print('  5. 프로그램 종료')
    # num = (input('메뉴번호 입력 >')) --- 여기서 num은 1을 문자로 인식한다.
    num = input('메뉴번호 입력 >')
    num = int(num) # 1이라는 문자를 숫자로 변경시켜준다.

    if num == 1:
        print('회원입력 시작!')
    elif num == 2:
        print('회원검색 실시!')
    elif num == 3:
        print('회원수정 시작!')
    elif num == 4:
        print('회원삭제!')
    elif num == 5:
        print('프로그램 종료!')
        break
    elif num:
        print('메뉴번호가 아닙니다.')
    else:
        continue
    # else:
    #     print('메뉴번호가 아닙니다.')
    #     break


