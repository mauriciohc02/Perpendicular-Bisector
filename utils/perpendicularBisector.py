from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import math




class PerpendicularBisector(QWidget):
    def __init__(self) -> None:
        super().__init__()
        # Set icon size and initialize UI elements
        self.icon_size = 30
        self.init_UI()
        # Init points values
        self.init_A = QPointF(350, 530)
        self.init_B = QPointF(430, 230)
        self.init_C = QPointF(640, 380)
        # A list with all the points
        self.triangle_points = [
            self.init_A,
            self.init_B,
            self.init_C
        ]
        # Initialize variables
        self.triangle_lines = list()
        self.perp_bisector = list()
        self.triangle_midpoints = list()
        self.circumcenter = tuple()
        self.radius = 0.0

        self.tracking = None


    def init_UI(self) -> None:
        """
        Create each element and object of the Widget UI
        returns: None
        rtype: None
        """
        self.button_reset_points = QPushButton(QIcon('./images/reset_animation.png'), '', self)
        self.button_reset_points.setIconSize(QSize(self.icon_size, self.icon_size))
        self.button_reset_points.setToolTip('Reset Animation')
        self.button_reset_points.clicked.connect(self.reset_points)

        self.layout_aux = QVBoxLayout()
        self.layout_aux.addWidget(self.button_reset_points)
        self.layout_aux.addStretch(1)

        self.layout_main = QHBoxLayout()
        self.layout_main.addStretch(1)
        self.layout_main.addLayout(self.layout_aux)
        self.setLayout(self.layout_main)


    def get_triangle(self) -> None:
        """
        Create a list of triangles sides with QLineF objects based on points
        returns: None
        rtype: None
        """
        self.triangle_lines = [
            QLineF(self.triangle_points[0], self.triangle_points[1]),
            QLineF(self.triangle_points[1], self.triangle_points[2]),
            QLineF(self.triangle_points[2], self.triangle_points[0])
        ]


    def get_perp_bisectors(self) -> None:
        """
        Create a list of perpendicular bisectors with QLineF objects based on midpoint and angle
        returns: None
        rtype: None
        """
        # Delete all elements of the self.triangle_midpoints list
        self.triangle_midpoints.clear()
        # Append every midpoint to self.triangle_midpoints
        for p1 in range(len(self.triangle_points)):
            p2 = (p1 + 1) if p1 < 2  else 0
            midpoint = self.midpoint(self.triangle_points[p1], self.triangle_points[p2])
            self.triangle_midpoints.append(midpoint)
        # Delete all elements of the self.perp_bisector list
        self.perp_bisector.clear()
        maxLength = math.sqrt(self.width() ** 2 * self.height() ** 2)
        # Calculate perpendicular bisector QLineF based on the window size and midpoint
        for i in range(len(self.triangle_lines)):
            angleLine = QLineF()
            basePoint = QPointF(self.triangle_midpoints[i][0], self.triangle_midpoints[i][1])
            angleLine.setP1(QPointF(self.triangle_midpoints[i][0], self.triangle_midpoints[i][1]))
            angleLine.setAngle(90)
            direction = angleLine.angleTo(self.triangle_lines[i])
            aux_line1 = QLineF(basePoint, basePoint + QPointF(1, 0))
            aux_line2 = QLineF(basePoint, basePoint + QPointF(1, 0))

            aux_line1.setLength(maxLength / 2)
            aux_line1.setAngle(direction)
            aux_line2.setLength(maxLength / 2)
            aux_line2.setAngle(direction + 180)

            line = QLineF(aux_line1.p2(), aux_line2.p2())
            self.perp_bisector.append(line)


    def get_circle(self) -> None:
        """
        Get circle parameters like circumcenter and radius
        returns: None
        rtype: None
        """
        self.circumcenter = self.perp_bisector[-1].intersects(self.perp_bisector[0])
        self.radius = self.dist_between_points(self.triangle_points[0], self.circumcenter[1])


    def draw_circle(self, painter) -> None:
        """
        Draw the circle with parameters from get_circle()
        returns: None
        rtype: None
        """
        if self.circumcenter[0] == 1:
            painter.setBrush(Qt.NoBrush)
            painter.setPen(QPen(QColor('blue'), 3, Qt.SolidLine))
            painter.drawEllipse(self.circumcenter[1], self.radius, self.radius)


    def draw_triangle(self, painter) -> None:
        """
        Draw the triangle with parameters from get_triangle()
        returns: None
        rtype: None
        """
        painter.setPen(QPen(QColor('red'), 3, Qt.SolidLine))
        painter.setBrush(QBrush(QColor('red'), style = Qt.Dense4Pattern))
        painter.drawConvexPolygon(self.triangle_points[0], self.triangle_points[1], self.triangle_points[2])
        #painter.drawConvexPolygon(self.triangle_points)

        painter.setBrush(QBrush(QColor('blue')))
        painter.setPen(QPen(QColor('black'), 2))
        for p in self.triangle_points:
            painter.drawEllipse(p, 5, 5)

        painter.setPen(QPen(QColor('blue'), 3))
        for p in range(len(self.triangle_points)):
            painter.drawText(self.triangle_points[p] + QPointF(10, 0), chr(p + 65))


    def draw_perp_bisectors(self, painter) -> None:
        """
        Draw the perpendicular bisectors with parameters from get_perp_bisectors() and circumcenter
        returns: None
        rtype: None
        """
        painter.setPen(QPen(QColor('black'), 3, Qt.DashLine))
        for i in self.perp_bisector:
            painter.drawLine(i)

        if self.circumcenter[0] == 1:
            painter.setBrush(QBrush(QColor('dimgray')))
            painter.setPen(QPen(QColor('black'), 2))
            painter.drawEllipse(self.circumcenter[1], 5, 5)
            painter.drawText(self.circumcenter[1] + QPointF(10, 0), 'D')


    def dist_between_points(self, a, b) -> float:
        """
        Get distance between two points with the formula
        returns: The distance between two points
        rtype: float
        """
        return math.sqrt((a.x() - b.x()) ** 2 + (a.y() - b.y()) ** 2)


    def midpoint(self, a, b) -> tuple:
        """
        Get midpoint between two points with the formula
        returns: The midpoint between two points
        rtype: tuple
        """
        x = (a.x() + b.x()) / 2
        y = (a.y() + b.y()) / 2

        return x, y


    def reset_points(self) -> None:
        """
        Reset animation to its initial state
        returns: None
        rtype: None
        """
        self.triangle_points = [
            self.init_A,
            self.init_B,
            self.init_C
        ]

        self.update()


    def paintEvent(self, event) -> None:
        """
        Draw the animation every time an event happen
        returns: None
        rtype: None
        """
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing)

        self.get_triangle()
        self.get_perp_bisectors()
        self.get_circle()
        
        self.draw_circle(painter)
        self.draw_triangle(painter)
        self.draw_perp_bisectors(painter)

    
    def mousePressEvent(self, event) -> None:
        """
        Selects the closest point when user click with its mouse
        returns: None
        rtype: None
        """
        i = min(
            range(len(self.triangle_points)),
            key = lambda i: (event.x() - self.triangle_points[i].x()) ** 2 + (event.y() - self.triangle_points[i].y()) ** 2
        )

        self.tracking = lambda p: self.triangle_points.__setitem__(i, p)


    def mouseMoveEvent(self, event) -> None:
        """
        Update the position of the selected point
        returns: None
        rtype: None
        """
        if self.tracking:
            self.tracking(QPointF(event.x(), event.y()))
            self.update()


    def mouseReleaseEvent(self, event) -> None:
        """
        Reset self.tracking when a mouseEvent is over
        returns: None
        rtype: None
        """
        self.tracking = None


    def __str__(self) -> str:
        return f'PerpendicularBisector Object'
