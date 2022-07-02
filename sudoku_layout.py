import enum
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel
from PyQt6.QtGui import QPalette, QColor

import sys
import numpy as np
import logging as log

log.basicConfig(format='%(asctime)s|%(levelname)s:%(message)s', level=log.INFO)


def generate_array():
    return np.array([
         [[4,1,3],
          [7,1,6],
          [6,1,5]],
         [[1,1,9],
          [2,1,4],
          [5,1,6]],
         [[9,1,2],
          [3,1,4],
          [8,1,3]],
         [[6,7,2],
          [2,4,1],
          [7,3,4]]
         ])

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

        self.setWindowTitle("Sudoku - App")

        arr = generate_array()
        it = np.nditer(arr, flags=['multi_index'])

        position_1 = [[i, j] for i in range(3) for j in range(3)]
        position_2 = [[i, j+3] for i in range(3) for j in range(3)]
        position_3 = [[i, j+6] for i in range(3) for j in range(3)]
        position_4 = [[i+3, j] for i in range(3) for j in range(3)]

        positions = position_1 + position_2 + position_3 + position_4

        layout = QGridLayout()

        for position, val in zip(positions, it):
            log.info(f"position: {position} has value {str(val)}")
            
            layout.addWidget(QLabel(str(val)), *position)


        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())