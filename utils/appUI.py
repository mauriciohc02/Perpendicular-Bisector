from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import * 

from utils.perpendicularBisector import PerpendicularBisector




class AppUI(QMainWindow):
    def __init__(self) -> None:
        """
        Constructor with basic attributes
        returns: None
        rtype: None
        """
        super().__init__()
        self.title = 'Perpendicular Bisector Animation'
        self.left = 300
        self.top = 200
        self.base_width = 1080
        self.base_height = 720
        self.min_width = 640
        self.min_height = 480
        self.initUI()


    def initUI(self) -> None:
        """
        Create each element and object of the UI
        returns: None
        rtype: None
        """
        # Set an icon image and title for the app
        self.setWindowIcon(QIcon('images/app_icon.png'))
        self.setWindowTitle(self.title)
        # Set an init size and a minimum size of window
        self.setGeometry(self.left, self.top, self.base_width, self.base_height)
        self.setMinimumSize(self.min_width, self.min_height)
        # Container where elements will be
        container = PerpendicularBisector()
        self.setCentralWidget(container)


    def __str__(self) -> str:
        return f'AppUI Object'