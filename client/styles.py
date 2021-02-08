global_css = '''QGroupBox {
                    border: 2px solid #e8324f;
                    border-radius: 7px;
                }
                QGroupBox::title {
                    color: #ffffff;
                    font-size: 18px;
                    padding-top: -8px;
                    padding-left: 0px;
                }
                QLabel {
                    font-size: 14px;
                    color: #ffffff;
                }
                QLineEdit {
                    background-color: #2d313d;
                    border: 2px solid #ffffff;
                    border-radius: 4px;
                    color : #ffffff;
                }
                QLineEdit::focus {
                    border: 2px solid #e8324f;
                    border-radius: 7px
                }
                QComboBox {
                    background-color: #2d313d;
                    border-radius: 4px;
                    border: 2px solid white;
                    color: white;
                }
                QComboBox::down-arrow {
                    image: url(:/kimp_img/arrow.png);
                }
                QComboBox::hover {
                    border-color: #e8324f;
                    border-radius: 7px;
                }
                QComboBox::drop-down{
                    border-radius: 7px;
                    background-color: #2d313d;
                    color: white;
                    padding: 0px;
                }
                QListView {
                    background-color: #2d313d;
                    color: white;
                    border: 2px solid #e8324f;
                    selection-background-color: #e8324f;
                }
                QListView::item::hover {
                       background-color: #ffffff;
                       color: #e8324f;
                }
                QMainWindow {
                    background-color: #2d313d;   
                }
                QPushButton{
                    font-size: 14px;
                    background-color: #2d313d;
                    color: #ffffff;
                    border-radius: 8px;
                    border: 2px solid #e8324f;
                }
                QPushButton:hover{
                    background-color: #ffffff;
                    color: #2d313d;
                }
                QPushButton:pressed{
                    background-color: #ffffff;
                    color: #e8324f;
                    border-color: #ffffff;
                }'''