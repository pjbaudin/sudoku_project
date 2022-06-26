import sys
import logging as log
import datetime as dt

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

log.basicConfig(format='%(asctime)s|%(levelname)s:%(message)s', level=log.INFO)


class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super(MainWindow, self).__init__()

        self.setWindowTitle("Sudoku GUI")

        self.setMinimumSize(QSize(700, 600))

        start_button = QPushButton("Start!")
        start_button.setCheckable(True)
        start_button.clicked.connect(self.start_clicked)
        start_button.clicked.connect(self.start_toggle)

        end_button = QPushButton("Stop!")
        end_button.setCheckable(True)

        # Set the central widget of the Window.
        self.setCentralWidget(start_button)

    def start_clicked(self):
        log.info(f"start button clicked!")

    def start_toggle(self, checked):
        log.info(f"Start toggle : {checked}")

app = QApplication(sys.argv)

# Create a Qt widget to display a window.
window = MainWindow()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()