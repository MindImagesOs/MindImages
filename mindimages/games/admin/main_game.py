#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
модуль является точкой входа для менеджера плагинов
класс BaseGameWidget во всех модулях-играх должен иметь только
это имя и должен быть унаследован от plugin_manager.Plugin

'''


import os

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore

from libs import plugin_manager
from games.admin.gui import graphics, tools

root = os.path.join(os.path.dirname(__file__))

class CentralWidget(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600, 600)
        self.setStyleSheet("background-color: lightgrey")
        self.box = QtWidgets.QVBoxLayout(self)
        self.hbox = QtWidgets.QHBoxLayout()
        self.box.insertLayout(1, self.hbox)

    def add_top_tool(self, widget):
        self.box.insertWidget(0, widget)

    def add_left_tool(self, widget):
        self.hbox.insertWidget(0, widget)

    def add_view(self, widget):
        self.hbox.insertWidget(1, widget)





class BaseGameWidget(plugin_manager.Plugin):
    def __init__(self):
        super().__init__()
        self._run_icon = 'resources/icons/base_tool.png'
        self._plugin_name = 'admin'

        self.box = QtWidgets.QVBoxLayout(self)
        self.center_widget = CentralWidget()
        self.box.addWidget(self.center_widget,
                           alignment=QtCore.Qt.AlignCenter)

        self.view = graphics.View(502)
        self.center_widget.add_view(self.view)
        self.top_tool = tools.Tool()
        self.center_widget.add_top_tool(self.top_tool)
        self.left_tool = tools.Tool()
        self.center_widget.add_left_tool(self.left_tool)



    @property
    def run_icon(self):
        return os.path.join(root, self._run_icon)

    @property
    def name(self):
        return self._plugin_name

