from PyQt5.QtWidgets import *


class ProcessBar(object):
    def __init__(self):
        """ProcessBar"""
        self.pbar = QProgressBar()
        self.pbar_text = QLabel()
        self.pbar_text.setText("Process :")

    def get_pbar(self):
        return self.pbar

    def get_pbar_text(self):
        return self.pbar_text

    def set_zero(self):
        self.pbar.setValue(0)

    def set_max(self):
        self.pbar.setValue(100)

    def set_Value(self, index, length, ratio=100):
        self.pbar.setValue((index - 1) / length * ratio)

    def set_Text(self, text):
        self.pbar_text.setText(str(text) + ":")

    def reset_pbar(self):
        self.pbar_text.setText("Process :")
        self.pbar.setValue(0)
