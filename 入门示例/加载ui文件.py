from PyQt6.QtWidgets import QApplication
from PyQt6 import uic
import sys

app = QApplication(sys.argv)

ui = uic.loadUi('./ui_1.ui')
ui.show()

sys.exit(app.exec())