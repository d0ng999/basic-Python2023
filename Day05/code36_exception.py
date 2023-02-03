# 예외처리
# try 문


def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b
try:
    x, y = input('두 수를 입력하세요 > ').split() # split를 쓰면 int랑 같이 못씀
    x = int(x)
    y = int(y)
except Exception as e: #  이 상태에서 발생하는 에러는 x, y에 값이 없는 형태, 그래서 더 이상 진행 불가능
    print(e)
    exit() # 종료를 의미하는 함수, finally함수를 하고 끝냄..
finally:
    print('꺄륵') # exit 함수를 써도 finally 함수 실행뒤에 끝

# # 원시적인 방법
# if y == 0:
#     print('y에 0을 넣지마세요')
#     exit()

print('계산 테스트')

# 예외 처리 방법
try: # try 문안에 오류가 발생할 가능성이 있는 함수를 넣기
    print(div(x, y))
# except ZeroDivisionError as z: # 예외문을 정할 수 있다.
#     print('0으로 나누면 안되용') , 
except Exception as e: # Exception 에러는 항상 마지막에 쓰기!! Exception 에러가 모든 에러의 부모에러이다!
    print(e) # Exception 에러만 사용하는게 편하다!!
finally:
    print('계산은 계속됩니다')

print(add(x, y))
print(mul(x, y))