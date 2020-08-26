# Imports =============================================================

# Standard Libraries
import logging

# Third-party Libraries
from PyQt5 import QtCore, QtWidgets

# =====================================================================

class QTextEditLogger(logging.Handler, QtCore.QObject):
    """A widget implementing the plain text widget, which can also be
    used as a threadsafe log handler. This class includes functionality
    to emit both logging and scrolling to the proper row to view the
    most recent log.

    Note, this class has been hard-coded to highly optimize its
    appearance in a PyQt statusbar widget as its parent. The function
    and signals are not hardcoded, but rather the UI formatting.

    Inherits:
        logging.Handler: for functionality to handle logs as created
        across the higher level application.
        QtCore.QObject: for general Qt functionality, as well as to
        use pyqtSignals for threadsafe operations.
    """

    # Create a signal to manage the appending of a single line of text
    appendPlainText = QtCore.pyqtSignal(str)

    # Create a signal to scroll to a specified row of AbstractScrollArea
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

