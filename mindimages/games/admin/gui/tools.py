#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
from PyQt5 import QtWidgets

class Tool(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: cyan")
