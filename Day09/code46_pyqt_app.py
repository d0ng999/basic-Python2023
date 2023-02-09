import sys
from PyQt5.QtWidgets import QApplication, QWidget

class MyApp(QWidget): # () 안에 있는 것이 MyApp의 부모
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # GUI 화면 설정
        self.setWindowTitle('Simple Window')
        # self.move(760, 440) 창의 처음 위치를 정할 수 있다.
        #  안쓰면 알아서 정중앙으로 온다

        self.resize(400, 200)
        self.show() # 핵심!!



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())