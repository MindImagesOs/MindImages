#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject


class AbsGui(QObject):
    def __init__(self, name, parent):
        super().__init__()
        self.setObjectName(name)
        self.setParent(parent)

class AdminTool(QtWidgets.QFrame, AbsGui):
    def __init__(self, name, parent):
        super().__init__(name, parent)
        print(self.objectName())

