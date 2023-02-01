# 복잡한 계산기 만들어보기@!#!@#@!#!#
def calc(option, *args):
    result = 0
    if option == 'add':
        for i in args:
            result += i

    elif option == 'mul':
        result = 1
        for i in args:
            result *= i

    elif option == 'sub':
        result = args[0]
        for i in args[1:]:
            result -= i

    elif option == 'div':
        result = args[0]
        for i in args[1:]:
            result /= i
    
    return result

print(calc('add', 5, 7, 17))
print(calc('mul', 40, 5, 7))
print(calc('sub', 512, 6, 78,234))
print(calc('div', 512, 4, 8))

# 여러개의 값을 return 할 때
# 튜플 사용
def new_calc(x, y):
    return(x*y, x/y, x+y, x-y)
# 받을 때는 튜플(소괄호) 생략가능
res1, res2, res3, res4 = new_calc(5,7)
# (res1, res2, res3, res4) = new_calc(5,7)
print(f'{res1}, {res2:2.2f}, {res3}, {res4}' )