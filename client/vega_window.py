from PyQt5.QtWidgets import QMainWindow, QGridLayout
from PyQt5.QtMultimedia import QCamera, QCameraInfo
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QSize
from PyQt5.QtCore import Qt

from sys import exit

import resources

class VegaMainWindow(QMainWindow) :
    def __init__(self) :
        QMainWindow.__init__(self)

        self.central_w = QWidget(self)
        self.main_grid = QGridLayout()

        self.welcome_msg = QLabel('Welcome!')
        
        self.auth_btn = QPushButton('Authorize')

        if len(QCameraInfo.availableCameras()) == 0 :
            QMessageBox.warning(self, 'Camera not found', 'You don\'t have any cameras on your computer so you can\'t use this app...\nBuy a new camera (╯°^°)╯┻━┻', QMessageBox.Ok)
            exit(-1)

    def createUI(self) :
        self.setWindowIcon(QIcon(QPixmap(':/kimp_img/vega.png')))
        self.setStyleSheet('background-color: #2d313d;')
        self.setWindowTitle('Vega')

        self.main_grid.addWidget(self.welcome_msg, 0, 0, 1, 5)
        
        self.main_grid.addWidget(self.auth_btn, 6, 0, 1, 5)

        self.central_w.setLayout(self.main_grid)
        self.setCentralWidget(self.central_w)        

        self.show()
