from PyQt5.QtWidgets import QMainWindow, QGridLayout
from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5.QtWidgets import QWidget
from PyQt5.QtMultimedia import QCamera, QCameraInfo
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QSize
from PyQt5.QtCore import Qt

import resources

class VegaMainWindow(QMainWindow) :
    def __init__(self) :
        QMainWindow.__init__(self)

        self.central_w = QWidget(self)
        self.main_grid = QGridLayout()

        self.welcome_msg = QLabel('Welcome!')
        
        self.auth_btn = QPushButton('Authorize')

        print(QCameraInfo.availableCameras())

    def createUI(self) :
        self.setWindowIcon(QIcon(QPixmap(':/kimp_img/vega.png')))
        self.setStyleSheet('background-color: #2d313d;')
        self.setWindowTitle('Vega')

        self.main_grid.addWidget(self.welcome_msg, 0, 0, 1, 5)
        
        self.main_grid.addWidget(self.auth_btn, 6, 0, 1, 5)

        self.central_w.setLayout(self.main_grid)
        self.setCentralWidget(self.central_w)        

        self.show()
