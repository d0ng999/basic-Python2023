# 함수정의 - 실행이 아니다.
# def + 함수명(파라미터):
# 파라미터를 이용한 함수를 만듦
# return ***
# 디버깅 중단점 설정 후 F5누르고 F10 -> 단계별로 확인가능
# F11은 함수사용 시 사용

def add(x, y):
    aa = x + y
    return aa

def sub(x, y):
    result = x - y
    return result

def div(x, y):
    result = x / y
    return result

def multi(x, y):
    result = x * y
    return result

# 함수호출
val = add(1024, 5) # val이라는 변수에 add라는 함수가 대입, add함수정의는 result = x + y인 것.
print(val)
val = sub(1024, 1000)
print(val)
val = multi(1024, 10)
print(val)
val = div(1024, 123)
print(f'{val:2.2f}')