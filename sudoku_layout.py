from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt6.QtGui import QPalette, QColor

import sys
import logging as log

log.basicConfig(format='%(asctime)s|%(levelname)s:%(message)s', level=log.INFO)


def create_square(grid_layout: QGridLayout, color:str):
    for i in range(0, 3):
        for j in range(0, 3):
            grid_layout.addWidget(Color(color), i, j)

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        layout = QGridLayout()

        create_square(layout, 'red')
        create_square(layout, 'blue')

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    




app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()