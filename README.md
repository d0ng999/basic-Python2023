# studyPython2023
부경대 IoT Python 학습 리포지토리

설정 ctrl + ,

## 1일차
1. 기본구성
    - Git/Github 설치 및 연동
    - Visual Studio Code 설치 및 연동
    - Python 설치

2. Python 기본
    - 콘솔출력
    - 주석

## 2일차 
1. Python 기본
    - 콘솔출력+
        - 파라미터 end와 sep를 배움
    - 변수
        - 변수지정이 엄격하지 않음
        - id = 메모리주소 
        - 변수명은 영어 _ 숫자의 조합으로 완성가능
    - 자료형(type(변수)함수)
        - None : 값이 없는 값으로 0도 아니고, 빈 공간도 아니다.
        - 숫자형 : int(정수형), float(유리수형), str(string의 약자, 문자열형)등..
        - 문자열형
            - " ", ' ' 두 가지의 형태로 쓸 수 있다.
        - 불형 or Boolean형
            - 참인지 거짓인지 판별하는 자료형태
    - 리스트 및 튜플, 딕셔너리, 집합 등의 복합형
        - 리스트 = 배열
        - 리스트는 []를 사용
        - []는 순서를 가지고 있음
        - 튜플 
            - 튜플은 수정, 변경이 불가능
            - 튜플은 ()를 사용
        - 딕셔너리
            - 해시 테이블이라고도 함
            - 딕셔너리는 {}를 사용
            - {}는 순서가 없음
        - 집합     
            - set함수
            - 집합은 {}를 사용
            - {}는 순서가 없음.
    - 연산자
        - 할당연산자 Assignment
        - equal 연산자 (==)
        - 사칙연산자
            - 단, 0으로 나누는 것은 불가능
        - 문자열 연산자
            - +와 *만 사용가능
        - 리스트 연산
            - .append() : 리스트 맨 마지막에 값을 추가
            - .insert( , ) : 특정 인덱스에 값을 추가
            - .remove() : 특정 값을 리스트에서 제거
        - 리스트에서 인덱스 찾는 법
            - [숫자] : 숫자는 몇 번째인지를 나타내고, 항상 시작은 0부터
        - 문자열 포멧팅(별표)

2. 깃헙 
    - 코드블럭작성
        - 사용 방법은 (```..```)으로 사용 가능

## 3일차
1. 파이썬 기본
    - 흐름제어
        - if
            - if, elif, else 문
        - for
            - for 변수 in 리스트
            - if문이랑 같이
            - 구구단 연습 (7줄)
            - range 문 연습 range(초기값, 끝 값, 증감)
            - continue & break
        - while
            - while 조건문 + if문
            - 나무찍기 연습
    - 구구단 프로그램
    - 함수
        - def 함수명 (파라미터): -> 함수 정의
        - 변수 = 함수식
        - return 변수
        - 복잡한 계산기 만들기
        - lambda함수라는게 있다

## 4일차
1. 파이썬 기본
    - 가상환경
        - pip 중요 python package index
        - 글로벌
    - 객체지향 프로그래밍(OOP)
        - 현실세계의 모든 객체(명사 + 동사)를 컴퓨터세계로~
        - 명사(변수) 와 동사(함수)
        - 붕어빵 틀 = class
        - class 클래스 명:
        - 속성변수 = 값
        - +함수
        - __init__, __str__ 자주 사용함.
        - 인터넷은 ~!
    - 패키지
        - 패키지는 모듈의 집합
        - 모듈, import, from, as

## 5일차
1. 파이썬 기본
    - 패키지 
        - random, urllib - request(s), math 등등...을 불러왔다아
    - 입출력
        - 파일입출력 open('파일명', 'w, r, a')
        - open, close 필수
        - 파일 읽기, 쓰기, 첨부하기(w, r, a)
        - csv파일 - encoding = 'utf-8'
    - 예외처리
        - try: 문에 예외가 발생할 가능성이 있는 함수 넣기
        - except:
        - finally:

## 6일차
1. 파이썬 기본
    - 콘솔출력 보충
        - Escape 문
        - \n, \b, \t 이정도만
        - 문자열 포멧팅 소수점자리 지정 {:.2f}
    - 객체지향 
        - 객체지향 특징
        - 상속, 다중상속

2. 파이썬 응용
    - 주소록 프로그램 [소스](https://github.com/d0ng999/studyPython2023/blob/main/project/address_app.py)
    - 집가서 다시 해보기

![실행화면](https://raw.githubusercontent.com/d0ng999/studyPython2023/main/images/address_app.png)
실행화면

## 7일차
1. 파이썬 응용
    - 주피터 노트북
        - 노트북 생성 : 파일메뉴 > 새파일
    - 리스트 연산 추가
    - 라이브러리 사용법
        

## 8일차 
1. 파이썬 응용
    - 라이브러리 사용법       
    - folium (지도 라이브러리)
        (https://github.com/d0ng999/studyPython2023/blob/main/Day08/code45_web_crawling_tutorial.ipynb)
        - 기상청 오늘의 날씨 크롤링
        - 데이터 포털 OpenAPI 크롤링
        - BeautifulSoup 크롤링
 ![실행화면](https://raw.githubusercontent.com/d0ng999/studyPython2023/main/images/jupyter_folium.png)
 실행화면

Folium OpenAPI 연동화면

# 9일차
1. 파이썬 응용
    - GUI 개발 
        - Tkinter 소개
        - PyQt 설치 및 사용법
(https://www.flaticon.com/)
(https://wikidocs.net/) (PyQt5 Tutorial - 파이썬으로 만드는 나만의 GUI 프로그램)
(https://wikibook.co.kr/)