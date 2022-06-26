from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sudoku Solver")

        self.label = QLabel()

        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        self.input.textChanged.connect(self.change_window_title)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(container)

    def change_window_title(self):
        win_title = ' - '.join(["Sudoku Solver", self.input.text()])
        self.setWindowTitle(win_title)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()