import code29_module_name # 지정된 파일에 쓰인 모든 함수를 불러옴
# 자기 파일의 이름은 __main__이라 표현하고, import로 다른 파일을 불러오면 그 파일의 이름을 파일이름으로 알려줌
print(f'code30_module_main : {__name__}') # __name__은 파일의 이름을 알려주는 것

# C에서 int main(void)와 동일
if __name__ == '__main__':
    print('main을 실행합니다.')
