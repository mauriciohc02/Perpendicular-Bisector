import sys
from utils.appUI import AppUI
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName('Perpendicular Bisector')

    myApp = AppUI()
    myApp.show()

    sys.exit(app.exec())
