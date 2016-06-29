#!/usr/bin/env python
# -*- coding: utf-8 -*-



import os

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore

root = os.path.join(os.path.dirname(__file__))
run_icon = 'resouces/icons/base_tool.png'



class BaseGameWidget(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: white")

        self.box = QtWidgets.QVBoxLayout(self)
        self.view = QtWidgets.QGraphicsView()
        self.view.setFixedSize(600, 600)
        self.view.setStyleSheet("background-color: green")
        self.box.addWidget(self.view,
                           alignment=QtCore.Qt.AlignCenter)

    @property
    def run_icon(self):
        return os.path.join(root, run_icon)

    @property
    def name(self):
        return 'admin'