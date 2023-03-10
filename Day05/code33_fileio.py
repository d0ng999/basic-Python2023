# 파일 만들기
# 파일/폴더 경로
# 절대경로 - 모든 파일 주소를 다 적어주면 된다.
# ASCII 코드 -> 한 단어를 표현하는 체계(영어)
# Unicode(UTF-8) -> 모든 나라언어를 다 표현가능

file = open('../sample06.txt', 'w', encoding = 'utf-8') # 파일 만듦 + 인코딩
# 상대경로 ./를 쓰면 자기 자신의 파일 = studyPython2023
# ..은 부모파일을 의미함
# .은 나 자신을 말한다.
# 자신의 파일 주소를 기준으로 .과 /를 이용해서 파일 주소를 입력 = 상대경로


file.write('안녕하세요~\n')
file.write('두번째 파일이다아아\n') # 아스키로 표현
file.write('절대경로에 파일이 생성될거예요.\n')

file.close()

print('sample02.txt가 생성되었습니다.')

