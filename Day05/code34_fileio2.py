# 파일 읽어오기
# 파일을 open하면 반드시 close해주어야 한다.
file = open('./Day05/sample03.txt', 'r', encoding = 'utf-8')

while True:
    text = file.read()

    if not text:
        break
    print(text)

file.close()
