# 주소록 프로그램
# 2023-02-06
# DongHyun
# 예외처리!!
# 파일이 없을 때 발생하는 예외 - 예외 발생은 디버깅으로
# 입력시 개수가 다를 때
# 메뉴번호 입력 시 숫자외의 문자는 예외발생

import os # 운영체제용 모듈 

# 2번
class Contact:
    # 생성자 - 이름, 전번, 이메일, 주소
    def __init__(self, name, phone_num, email, address) -> None:
        self.__name      = name
        self.__phone_num = phone_num
        self.__email     = email
        self.__address   = address

    #4번
    # __str__ 재정의
    def __str__(self) -> str:
        str_res = (f'이  름 : {self.__name}\n'
                   f'핸드폰 : {self.__phone_num}\n'
                   f'이메일 : {self.__email}\n'
                   f'주  소 : {self.__address}')
        return str_res
    
    # 11번 - 객체존재여부 확인
    def isNameExist(self, name):
        if self.__name == name:
            return True
        else:
            return False
        
    # 13. 각 멤버변수에 접근할 수 있는 함수
    # getName, getPhoneNum, getEmail, getAddress
    def getName(self) -> str:
        return self.__name

    def getPhoneNum(self) -> str:
        return self.__phone_num
    
    def getEmail(self) -> str:
        return self.__email
    
    def getAddress(self) -> str:
        return self.__address

# 5번 - 사용자입력
def set_contact():
    name, phone_num, email, address = input('정보입력(이름/전번/이메일/주소) : ').split('/')
    #    print(name, phone_num, email, address)  
    # 7번 contact 객체 만들기
    contact = Contact(name = name, phone_num = phone_num, email = email, address = address)
    return(contact)

# 10번 - 주소록 출력
def get_contacts(list):
    for item in list:
        print(item)
        print('====================')

# 12번 - 주소록 삭제
def del_contact(list, name):
    count = 0 # 찾는 이름 카운트
    for i, item in enumerate(list): # 리스트 내에 것들을 순서대로 i에 나타내게 만들어줌
        if item.isNameExist(name):
            count += 1
            del list[i] # 리스트 삭제
    
    if count > 0: # 메세지 출력
        print('삭제했습니다.')
    else:
        print('주소록이 없습니다.')

# 14번 - 주소록 저장
def save_contacts(list):

    file = open('C:/Source/studyPython2023/project/contacts.txt', 'w', encoding = 'utf - 8')

    for item in list:
        text = f'{item.getName()}/{item.getPhoneNum()}/{item.getEmail()}/{item.getAddress()}'
        file.write(f'{text}\n')

    file.close() # 파일 입출력 시 마지막에 항상 종료!!@!@!@!@!#!@#@!#!@#!@#!@#

# 15번 - 주소록 읽어오기
def load_contacts(list):
    try:
        file = open('C:/Source/studyPython2023/project/contacts.txt', 'r', encoding = 'utf - 8')
    except Exception as e:
        f = open('C:/Source/studyPython2023/project/contacts.txt', 'w', encoding = 'utf - 8')
        f.close()
        return # 파일이 없는 경우 except문에 파일을 생성해준후 닫고 return으로 함수에서 탈출
    

    while True:
        line = file.readline().replace('\n','') # replace = 앞의 문자를 뒤의 문자로 대체

        if not line:
            break
        lines = line.split('/')
        contact = Contact(lines[0], lines[1], lines[2], lines[3])
        list.append(contact)

    file.close()


# 8번 기타: 화면 클리어
def clear_console():
    command = 'clear' # 리눅스나 유닉스 화면 클리어 명령어 = clear
    if os.name in ('nt', 'dos'): # Window 운영체제라면
        command = 'cls'
    os.system(command)

# 6번 메뉴표시
def get_menu():
    str_menu = ('주소록앱 v1.0\n'
                '1. 연락처 추가\n'
                '2. 연락처 출력\n'
                '3. 연락처 삭제\n'
                '4. 앱종료\n')
    print(str_menu)
    try:
        menu = int(input('메뉴 입력 : '))
    except Exception as e:
        menu = 0 # int형 숫자만 들어가면 함수는 다시 시작하니, 문자열을 넣게 되는 경우에 입력값이 0으로 변하게끔 예외처리를 했다.

    return menu

# 3번
def run():
    contacts = [] # 주소록을 담기위한 빈 리스트 생성
    load_contacts(contacts) # 주소록 읽어오기.
    clear_console() # 기타 8번
    while True:
        sel_menu = get_menu()
        if sel_menu == 1: # 9번 연락처추가
            try: # 연락처 입력 개수가 잘못되었을 때의 예외처리!!!
                contact = set_contact()
                contacts.append(contact)
                input('주소록 입력 성공') # 아무것도 안받는 입력
            except Exception as e:
                print('이름/전번/이메일/주소 순으로 입력하세요')
                input()
            finally:
                clear_console()

        elif sel_menu == 2:
            get_contacts(contacts)
            input('주소록 출력 완료') # 아무것도 안받는 입력
            clear_console()

        elif sel_menu == 3:
            name = input('삭제할 이름 입력 : ')
            del_contact(contacts, name)
            input()
            clear_console()

        elif sel_menu == 4: # 종료시 주소록 파일 저장
            save_contacts(contacts)
            break
        else:
            clear_console() # 기타 8번

    # temp = Contact('홍동현', '010-3204-5278',
    #                'tlxmscksals@naver.com', '경상남도 불라불라')
    # set_contact()

# 1번
if __name__ == '__main__':
#    print('주소록앱 시작합니다.')
    run()
