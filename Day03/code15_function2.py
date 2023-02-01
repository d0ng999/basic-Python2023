# 1. 파라미터 O 리턴 O
# 2. 파라미터 O 리턴 X
# 3. 파라미터 X 리턴 O
# 4. 파라미터 X 리턴 X

def add(x, y):
    result = x + y
    print(result) # 이 상황에서는 return 생략가능 
    
def sub(x, y):
    result = x - y
    print(result)

def div(x, y):
    result = x // y
    print(result)
    
def multi():
    result = ('x * y')
    print(result)

def hello():
    print('Hello!!~')

def hello2():
    msg = 'Hello, Hello!'
    return msg   

# 함수호출
add(1024, 5) # val이라는 변수에 add라는 함수가 대입, add함수정의는 result = x + y인 것.
sub(1024, 1000)
multi()
div(1024, 123)
hello()
print(hello2())