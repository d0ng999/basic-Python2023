# %% [markdown]
# # Jupyter 노트북 사용법 학습
# 
# ## 마크다운, 파이선 셀을 추가
# - 현재 셀 앞에 셀을 추가 : a
# - 현재 셀 뒤에 셀을 추가 : b
# - 현재 셀을 마크다운으로 변경 : m , 단 포커스만 있는 상태
# - 현재 셀을 코드 셀로 변경 : y, 단 포커스 상태

# %%
# 최초 작성된 Python 셀

# %% [markdown]
# ## 파이선 셀 실행
# - 셀 실행 : Ctrl + Enter
# - 셀 실행 + 다음 셀로 이동(셀이 없으면 마크다운 셀 생성) : Shift + Enter
# - 셀 실행 + 다음 셀 생성 : Alt + Enter
# - 주석 처리 : Ctrl + /  또는  Ctrl + 'k' and 'c'

# %%
print('Hello, Jupyter~!!')


# %% [markdown]
# ## 디버깅!!
# - 아무리 강조해도 지나치치 않는다!
# - 디버깅 시 주의사항♣
# - Ctrl + Alt + Shift + Enter = 디버깅

# %%
arr = [1, '2', True, 'Hello', 3.1415926585]

for i in arr:
    print(i)

# %% [markdown]
# ### 함수 디버깅
# - 함수가 다른영역에 있어도 함수를 쓸 수 있다.

# %%
def plus(x,y):
    val = x + y
    return val

def div(x,y):
    val = x / y
    return val

print('더하기')
print(plus(10,4))

# %%
print('나누기')
print(div(10,0))


