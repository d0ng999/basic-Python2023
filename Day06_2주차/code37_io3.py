# 콘솔출력 보충
# # Escape 문자
# print('1. Hello.\r\nWorld')
# print('2. Hello.\nWorld')



# print('3. Hello.\tWorld') # \t는 tab
# print('4. Hello.\n\t\bWorld')
# print('5. Hello.\n\'World\'') # \'문자열 내 ''를 넣는 방법
# print('6. Hello.\n"World"') # ""는 그냥 써도 가능
# print('7. Hello.\'World\'') 
# print('8. Hello.\\ World') # \를 문자에 표현하는 방법 = \\
# print('9. Hello\000') # \0은 문자열이 끝났다는 것을 알려줌

# 문자열 포멧팅
me = '저'
name = '홍동현'
age = 40
print('%s는 %s이고, %d예요.'% (me, name, age))
print(f'{253.23432:0.2f}')

print('%4.4f'%(254.13212)) #4.4f에서 앞 자리수는 전체자리수.소수점자리f
# 단 전체자리수가 전체길이에 비해 커져야 앞에 자릿수를 맞추기위해 공백처리해줌
