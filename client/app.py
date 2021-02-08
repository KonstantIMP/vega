from PyQt5.QtWidgets import QApplication
from vega_window import VegaMainWindow

if __name__ == '__main__' :
    vega_client_app = QApplication([])
    
    vega_client_win = VegaMainWindow()
    vega_client_win.createUI()
    vega_client_win.cameraStart()

    vega_client_app.exec()
