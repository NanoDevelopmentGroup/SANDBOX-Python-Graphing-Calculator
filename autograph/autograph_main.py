# Imports =============================================================

# Standard Libraries
import sys
import logging

# Third-party Libraries
from PyQt5 import uic, QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

# Local Application Libraries
from gui.ui_utils import find_form

# =====================================================================

print('passed')

class AutoGraphMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(AutoGraphMainWindow, self).__init__()

        # Load the main window GUI file
        uic.loadUi(find_form('autograph_mainform.ui'),self)

        self.plotwindow = MplWidget(self.groupBox_Graph)

        self.show()


class MplWidget(QtWidgets.QWidget):
    def __init__(self, group_box: QtWidgets.QGroupBox, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        vertical_layout = QtWidgets.QVBoxLayout()
        vertical_layout.alignment
        vertical_layout.addWidget(self.canvas)
        vertical_layout.addWidget(NavigationToolbar(self.canvas,self))

        self.canvas.axes = self.canvas.figure.add_subplot(111)
        group_box.setLayout(vertical_layout)


def main():
    autograph_app = QtWidgets.QApplication(sys.argv)
    window = AutoGraphMainWindow()
    autograph_app.exec_()

if __name__ == '__main__':
    main()