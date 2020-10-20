import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MainForm(QWidget):
    def __init__(self, name='MainForm'):
        super(MainForm, self).__init__()
        self.setWindowTitle(name)
        self.resize(300, 200)
        """Center"""
        screen = QDesktopWidget().screenGeometry()
        form = self.geometry()
        x_move_step = (screen.width() - form.width()) // 2
        y_move_step = (screen.height() - form.height()) // 2
        self.move(x_move_step, y_move_step)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainForm = MainForm('test QFileDialog')
    mainForm.show()
    sys.exit(app.exec_())
