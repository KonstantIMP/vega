from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QPixmap, QIcon

import resources

class VegaMainWindow(QMainWindow) :
    def __init__(self) :
        QMainWindow.__init__(self)

    def createUI(self) :
        self.setWindowTitle('Vega')
        self.setWindowIcon(QIcon(QPixmap(':/kimp/img/vega.png')))
        self.show()
