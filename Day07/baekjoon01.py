# # 배열 - 개수 세기

# fir_num = int(input())

# arr = list(map(int, input().split()))
# if fir_num == len(arr):
    
#     thd_num = int(input())
#     count = 0

#     for i in arr:
#         if thd_num == i:
    
#             count += 1

#     print(count)
    
# else:
#     print('땡')

# 배열 - X보다 작은 수 & 최소, 최대

arr = list(map(int, input().split()))
count = 0
for i in arr:
    if count == 0:
        
        for i in arr:
            count += 1
        
            if i == max(arr):
                print(max(arr))
                print(count)

    else:
        print('땡')

