from PyQt6.QtWidgets import QMainWindow

class VegaMainWindow(QMainWindow) :
    def __init__(self) :
        QMainWindow.__init__(self)

    def createUI(self) :
        self.setWindowTitle('Vega')
        self.show()
