# urllib 에서 필요한 모듈 꺼내쓰기!
# 파일이름이 모듈.py가 되지 않게 조심하기
# urllib.request // urllib.response
from urllib.request import Request, urlopen

req = Request('https://www.naver.com')
res = urlopen(req)
print(res.status)