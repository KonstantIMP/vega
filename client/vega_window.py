from PyQt5.QtWidgets import QMainWindow, QGridLayout
from PyQt5.QtMultimedia import QCamera, QCameraInfo
from PyQt5.QtWidgets import QGroupBox, QComboBox
from PyQt5.QtMultimediaWidgets import QCameraViewfinder 
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

        self.option_group = QGroupBox(self.central_w)
        
        self.auth_btn = QPushButton('Authorize')

        if len(QCameraInfo.availableCameras()) == 0 :
            QMessageBox.warning(self, 'Camera not found', 'You don\'t have any cameras on your computer so you can\'t use this app...\nBuy a new camera (╯°^°)╯┻━┻', QMessageBox.Ok)
            exit(-1)

        self.camera = QCamera(QCameraInfo.defaultCamera())
        self.camera_w = QCameraViewfinder()

    def createUI(self) :
        self.setWindowIcon(QIcon(QPixmap(':/kimp_img/vega.png')))
        self.setStyleSheet('background-color: #2d313d;')
        self.setWindowTitle('Vega')

        self.option_group.setTitle('Options')
        self.option_group.setStyleSheet(
        'QGroupBox {'
        '   border: 2px solid #e8324f;'
        '   border-radius: 7px;'
        '}'
        'QGroupBox::title {'
        '   color: #ffffff;'
        '   font-size: 16px;'
        '   padding-top: -8px;'
        '   padding-left: 0px;'
        '}')
        self.main_grid.addWidget(self.option_group, 0, 0, 2, 5)


        self.camera.setViewfinder(self.camera_w)
        self.camera.setCaptureMode(QCamera.CaptureMode.CaptureStillImage)


        
        self.auth_btn.setStyleSheet(
        'QPushButton{'
        '   font-size: 14px;'
        '   background-color: #2d313d;'
        '   color: #ffffff;'
        '   border-radius: 8px;'
        '   border: 2px solid #e8324f;'
        '}'
        'QPushButton:hover{'
        '   background-color: #ffffff;'
        '   color: #2d313d;'
        '}'
        'QPushButton:pressed{'
        '   background-color: #ffffff;'
        '   color: #e8324f;'
        '   border-color: #ffffff;'
        '}')        

        self.main_grid.addWidget(self.auth_btn, 7, 0, 1, 5)

        self.central_w.setLayout(self.main_grid)
        self.setCentralWidget(self.central_w)        

        self.show()
