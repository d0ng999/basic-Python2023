# 이미지처리 위젯
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        pixmap = QPixmap('./Day10/puppy.png')

        lblImage = QLabel(self)
        lblImage.setPixmap(pixmap)
        lblSize = QLabel(str(pixmap.width()) + 'x' + str(pixmap.height()))
        lblSize.setAlignment(Qt.AlignmentFlag.AlignCenter) # Qt.AlignCenter도 가능

        vbox = QVBoxLayout(self)
        vbox.addWidget(lblImage)
        vbox.addWidget(lblSize)

        self.setLayout(vbox)
                
        # 필수
        self.setWindowTitle('이미지 위젯')
        # self.setGeometry(300,300,300,300)
        self.showFullScreen() # 화면 창만 풀 스크린 되고, 사진의 크기는 그대로!
        # self.setCenter()

    def setCenter(self):
        qr = self.frameGeometry() # 창 자기자신의 위치 값
        cp = QDesktopWidget().availableGeometry().center() # 모니터 화면 중심잡기
        qr.moveCenter(cp)
        self.move(qr.topLeft())        
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())