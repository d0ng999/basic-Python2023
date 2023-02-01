# for 문
arr = [1,2,3,4,5]
sum = 0

for item in arr:
    #print(f'{item:0.2f}')
    print(item)
    sum += item # sum = sum + item 같다

print('sum은', sum, '입니다')

# range함수 리스트[변수 for 변수값 in 범위리스트]
vals = [i for i in range(1,11)] # ==> vals = [1,2,3,4,5,6,7,8,9,10]
print(vals)

# continue & break문
# continue 와 break문은 for 문에서만 사용가능하다.
# for 문안에 있는 if문에서는 사용가능.
vals1 = [i for i in range(1,11)]
num = 0
for item in vals1:
    num += 1
    if num % 2 == 0:
        # continue # 계속 진행
        break # break는 if문이 만족하면 for문을 완전히 탈출한다.
    else:
        print(num, '번 수는', item, '입니다')
