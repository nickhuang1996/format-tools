from abc import ABCMeta, abstractmethod
from PyQt5.QtWidgets import *


class ButtonBase(metaclass=ABCMeta):
    def __init__(self, MainForm):
        self.btn = QPushButton(MainForm)
    @abstractmethod
    def get_btn(self):
        pass



