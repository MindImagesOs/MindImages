#!/usr/bin/env python
# -*- coding: utf-8 -*-



import os

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore

from libs import plugin_manager

root = os.path.join(os.path.dirname(__file__))




class BaseGameWidget(plugin_manager.Plugin):
    def __init__(self):
        super().__init__()
        self._run_icon = 'resources/icons/base_tool.png'
        self._plugin_name = 'admin'

        self.box = QtWidgets.QVBoxLayout(self)
        self.view = QtWidgets.QGraphicsView()
        self.view.setFixedSize(600, 600)
        self.view.setStyleSheet("background-color: lightgrey")
        self.box.addWidget(self.view,
                           alignment=QtCore.Qt.AlignCenter)

    @property
    def run_icon(self):
        return os.path.join(root, self._run_icon)

    @property
    def name(self):
        return self._plugin_name