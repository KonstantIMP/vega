from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QSize
from PyQt5.QtCore import Qt

import resources

class VegaMainWindow(QMainWindow) :
    def __init__(self) :
        QMainWindow.__init__(self)

    def createUI(self) :
        self.setWindowTitle('Vega')
        #self.setWindowIcon(QIcon(QPixmap('/home/kimp/Projects/vega/resource/vega.png')))

        self.setWindowIcon(QIcon(QPixmap(':/kimp_img/vega.png')))
        
        self.setStyleSheet('QMainWindw {background-color : 0x000000;}')
        
        self.show()
