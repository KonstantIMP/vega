from PyQt5.QtWidgets import QMainWindow, QGridLayout
from PyQt5.QtMultimedia import QCamera, QCameraInfo
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QGroupBox, QComboBox
from PyQt5.QtMultimediaWidgets import QCameraViewfinder 
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QSize
from PyQt5.QtCore import Qt

from sys import exit

from config import *

import resources
import styles

class VegaMainWindow(QMainWindow) :
    def __init__(self) :
        QMainWindow.__init__(self)

        self.central_widget = QWidget(self)
        self.main_grid = QGridLayout(self.central_widget)

        self.option_group = QGroupBox(None)

        self.group_grid = QGridLayout(self.option_group)

        self.addr_msg = QLabel('Database addr')
        self.camera_msg = QLabel('Camera')

        self.camera_combo = QComboBox()
        self.addr_edit = QLineEdit()

        self.camera_place = QGroupBox(None)

        self.auth_btn = QPushButton('Log in')
        self.camera_grid = QGridLayout(self.camera_place)

        self.camera_widget = QCameraViewfinder()
        self.camera_obj = QCamera(QCameraInfo.defaultCamera())

        self.veg_cfg = Config()

    def createUI(self) :
        self.setWindowIcon(QIcon(QPixmap(':/kimp_img/vega.png')))
        self.setStyleSheet(styles.global_css)
        self.setWindowTitle('Vega')

        

        self.camera_grid.addWidget(self.camera_widget, 0, 0, 5, 5)

        self.camera_place.setTitle('Camera')
        self.main_grid.addWidget(self.camera_place, 2, 0, 5, 5)

        self.camera_obj.setViewfinder(self.camera_widget)
        self.main_grid.addWidget(self.auth_btn, 7, 0, 1, 5)

        self.central_widget.setLayout(self.main_grid)
        self.setCentralWidget(self.central_widget)
        self.show()

    def initValues(self) :
        self.addr_edit.setText(self.veg_cfg.get_db_addr())

        if self.veg_cfg.get_debug() == True :
            self.group_grid.addWidget(self.addr_msg, 0, 0, 1, 2)
            self.group_grid.addWidget(self.camera_msg, 1, 0, 1, 2)

            self.addr_edit.setAlignment(Qt.AlignRight)
            self.group_grid.addWidget(self.addr_edit, 0, 2, 1, 5)

            for i in QCameraInfo.availableCameras() :
                self.camera_combo.addItem(i.deviceName())
            self.camera_combo.setCurrentText(QCameraInfo.defaultCamera().deviceName())
            self.group_grid.addWidget(self.camera_combo, 1, 2, 1, 5)

            self.option_group.setTitle('Option')
            self.main_grid.addWidget(self.option_group, 0, 0, 2, 5)
        else : self.option_group.hide()

    def cameraStart(self) :
        if self.camera_obj.status() != QCamera.UnavailableStatus :
            print('Camera started')
            self.camera_obj.start()
