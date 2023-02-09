import sys
from PyQt5.QtWidgets import QApplication, QWidget 
from PyQt5.QtGui import QIcon

class MyApp(QWidget) :
    
    def __init__(self) :
        super().__init__()
        self.initUI()

    def initUI(self) :
        # GUI 화면 설정
        self.setWindowTitle('simple window')
        # 아이콘 추가
        self.setWindowIcon(QIcon('./Day09/iot.png'))
        # self.move(1500,300)
        
        self.resize(400,200)
        self.show()

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
