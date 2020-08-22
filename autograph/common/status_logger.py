# Imports =============================================================

# Standard Libraries
import logging

# Third-party Libraries
from PyQt5 import QtCore, QtWidgets

# =====================================================================

class QTextEditLogger(logging.Handler, QtCore.QObject):

    appendPlainText = QtCore.pyqtSignal(str)
    setScrollValue = QtCore.pyqtSignal(int)

    def __init__(self, status_bar: QtWidgets.QStatusBar):
        super().__init__()
        QtCore.QObject.__init__(self)
        self.widget = QtWidgets.QPlainTextEdit(status_bar)
        self.widget.setReadOnly(True)
        self.setScrollValue.connect(self.widget.verticalScrollBar().setValue)
        self.appendPlainText.connect(self.widget.appendPlainText)

        status_bar.addPermanentWidget(self.widget,1)
        status_bar.setContentsMargins(8,2,0,4)

        self.widget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.widget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.widget.setMaximumHeight(18)
        self.widget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.widget.setPlaceholderText("Initializing Logger ...")

    def emit(self, record):
        msg = self.format(record)
        self.appendPlainText.emit(msg)
        self.setScrollValue.emit(self.widget.verticalScrollBar().maximum() - 1)

