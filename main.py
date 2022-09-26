<<<<<<< HEAD
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QCheckBox, QDialog, QMainWindow, QVBoxLayout, QWidget, QHBoxLayout
import pyqtgraph as pg
import sys
from random import randint


class MainWindow(QMainWindow):

    def __init__(self, window_width: int, time_to_update: int, x: list, y1: list, y2: list):
        super(MainWindow, self).__init__()
        self.data_line2 = None
        self.data_line1 = None
        self.setWindowTitle("Graphics")

        # Create cool window
        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setBackground('w')
        self.graphWidget.setTitle("Position", color = "b", size = "25pt")
        styles = {"color": "#f00", "font-size": "20px"}
        self.graphWidget.setLabel("left", "y", **styles)
        self.graphWidget.setLabel("bottom", "x", **styles)
        self.graphWidget.addLegend()
        self.graphWidget.showGrid(x = True, y = True)

        # Set data for graphics
        self.shown_x1 = []
        self.shown_x2 = []
        self.shown_y2 = []
        self.shown_y1 = []
        self.x = x
        self.y1 = y1
        self.y2 = y2

        # Print graphics
        self.pen1 = pg.mkPen(color = "b")
        self.pen2 = pg.mkPen(color = "r")
        self.data_line1 = self.graphWidget.plot(self.shown_x1, self.shown_y1, pen=self.pen1, symbol='+', symbolSize=10, symbolBrush="r")
        self.data_line2 = self.graphWidget.plot(self.shown_x2, self.shown_y2, pen=self.pen2, symbol='+', symbolSize=10, symbolBrush="b")

        # Create buttons
        self.check_button1 = QCheckBox("Line 1")
        self.check_button1.setChecked(True)
        self.check_button2 = QCheckBox("Line 2")
        self.check_button2.setChecked(True)

        # Add elements to layout
        layout_v = QVBoxLayout()
        layout_v.addWidget(self.graphWidget)
        layout_h = QHBoxLayout()
        layout_v.addLayout(layout_h)
        layout_h.addWidget(self.check_button1)
        layout_h.addWidget(self.check_button2)

        # Create central widget
        widget = QWidget()
        widget.setLayout(layout_v)
        self.setCentralWidget(widget)

        # Set update settings
        self.timer = QtCore.QTimer()
        self.timer.setInterval(time_to_update)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def update_plot_data(self):
        self.x = self.x[1:]
        self.x.append(self.x[-1] + 1)
        self.y1 = self.y1[1:]
        self.y1.append(randint(0, 20))
        self.y2 = self.y2[1:]
        self.y2.append(randint(0, 20))

        if self.check_button1.isChecked():
            self.shown_x1 = self.x
            self.shown_y1 = self.y1
        else:
            self.shown_x1 = []
            self.shown_y1 = []

        if self.check_button2.isChecked():
            self.shown_x2 = self.x
            self.shown_y2 = self.y2
        else:
            self.shown_x2 = []
            self.shown_y2 = []

        self.data_line1.setData(self.shown_x1, self.shown_y1)
        self.data_line2.setData(self.shown_x2, self.shown_y2)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    update_time = 100
    width = 15
    x = [i for i in range(width)]
    y1 = [i for i in range(width)]
    y2 = [i + 5 for i in range(width)]
    w = MainWindow(width, update_time, x, y1, y2)
    w.show()
=======
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QCheckBox, QDialog, QVBoxLayout, QHBoxLayout
import pyqtgraph as pg
import sys
from random import randint


class MainWindow(QDialog):

    def __init__(self, time_to_update: int, x: list, y1: list, y2: list):
        QDialog.__init__(self)
        super().__init__()
        self.data_line2 = None
        self.data_line1 = None
        self.setWindowTitle("Graphics")

        # Create cool window
        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setBackground('w')
        self.graphWidget.setTitle("Position", color = "b", size = "25pt")
        styles = {"color": "#f00", "font-size": "20px"}
        self.graphWidget.setLabel("left", "y", **styles)
        self.graphWidget.setLabel("bottom", "x", **styles)
        self.graphWidget.addLegend()
        self.graphWidget.showGrid(x = True, y = True)

        # Set data for graphics
        self.shown_x1 = []
        self.shown_x2 = []
        self.shown_y2 = []
        self.shown_y1 = []
        self.x = x
        self.y1 = y1
        self.y2 = y2

        # Print graphics
        self.pen1 = pg.mkPen(color = "b")
        self.pen2 = pg.mkPen(color = "r")
        self.data_line1 = self.graphWidget.plot(self.shown_x1, self.shown_y1, pen=self.pen1, symbol='+', symbolSize=10, symbolBrush="r")
        self.data_line2 = self.graphWidget.plot(self.shown_x2, self.shown_y2, pen=self.pen2, symbol='+', symbolSize=10, symbolBrush="b")

        # Create buttons
        self.check_button1 = QCheckBox("Line 1")
        self.check_button1.setChecked(True)
        self.check_button2 = QCheckBox("Line 2")
        self.check_button2.setChecked(True)

        # Add elements to layout
        layout_v = QVBoxLayout()
        layout_v.addWidget(self.graphWidget)
        layout_h = QHBoxLayout()
        layout_h.addWidget(self.check_button1)
        layout_h.addWidget(self.check_button2)
        layout_v.addLayout(layout_h)
        self.setLayout(layout_v)

        # Set update settings
        self.timer = QtCore.QTimer()
        self.timer.setInterval(time_to_update)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def update_plot_data(self):
        self.x = self.x[1:]
        self.x.append(self.x[-1] + 1)
        self.y1 = self.y1[1:]
        self.y1.append(randint(0, 20))
        self.y2 = self.y2[1:]
        self.y2.append(randint(0, 20))

        if self.check_button1.isChecked():
            self.shown_x1 = self.x
            self.shown_y1 = self.y1
        else:
            self.shown_x1 = []
            self.shown_y1 = []

        if self.check_button2.isChecked():
            self.shown_x2 = self.x
            self.shown_y2 = self.y2
        else:
            self.shown_x2 = []
            self.shown_y2 = []

        self.data_line1.setData(self.shown_x1, self.shown_y1)
        self.data_line2.setData(self.shown_x2, self.shown_y2)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    update_time = 100
    width = 15
    x = [i for i in range(width)]
    y1 = [i for i in range(width)]
    y2 = [i + 5 for i in range(width)]
    w = MainWindow(update_time, x, y1, y2)
    w.show()
>>>>>>> bd5d33e (Turn window into dialog)
    sys.exit(app.exec_())