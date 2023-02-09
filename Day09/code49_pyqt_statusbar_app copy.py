import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate, QTime

class MyApp(QMainWindow): # () 안에 있는 것이 MyApp의 부모
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 메뉴바 - 액션
        actExit = QAction(QIcon('./Day09/logout.png'), 'Exit', self)
        actExit.setShortcut('Ctrl+Q')
        actExit.setStatusTip('앱 종료')
        actExit.triggered.connect(qApp.quit) # 종료하는 이벤트 추가

        actSave = QAction(QIcon('./Day09/save.png'), 'Save', self)
        actSave.setShortcut('Ctrl+S')
        actSave.setStatusTip('저장')

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(actExit)

        # 툴바
        toolbar = self.addToolBar('MainToolBar')
        toolbar.addAction(actSave)
        toolbar.addAction(actExit)


        # 상태바 출력
        now = QDate.currentDate() # 현재 일자
        time = QTime.currentTime() # 현재 시간
        self.statusBar().showMessage(now.toString('yyyy-MM-dd') + ' ' + time.toString('hh:mm:ss'))
        self.setWindowIcon(QIcon('./Day09/iot.png'))
        # GUI 화면 설정
        self.setWindowTitle('Window')
        # self.move(760, 440) 창의 처음 위치를 정할 수 있다.
        # 안쓰면 알아서 정중앙
        self.resize(400, 200)
        self.setCenter() # 이거쓰면 어떤 해상도에도 창이 정중앙에 뜬다.
        self.show() # 핵심!!

    # 화면 중심 셋팅
    def setCenter(self):
        qr = self.frameGeometry() # 창 자기자신의 위치 값
        cp = QDesktopWidget().availableGeometry().center() # 모니터 화면 중심잡기
        qr.moveCenter(cp)
        self.move(qr.topLeft())




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())