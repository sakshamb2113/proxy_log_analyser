from PyQt5.QtWidgets import QApplication
from MainWindow import MainWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
