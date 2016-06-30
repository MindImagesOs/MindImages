#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
модуль является точкой входа для менеджера плагинов
класс BaseGameWidget во всех модулях-играх должен иметь только
это имя и должен быть унаследован от plugin_manager.Plugin

'''

import os

import yaml
from PyQt5 import QtCore
from PyQt5 import QtWidgets

from games.admin.gui import graphics, tools
from libs import plugin_manager

root = os.path.join(os.path.dirname(__file__))
config_path = os.path.join(root, 'etc/config.yaml')


def get_config(path):
    with open(path, "r") as obj:
        return yaml.load(obj)


class CentralWidget(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()

        # self.setStyleSheet("background-color: lightgrey")
        self.box = QtWidgets.QVBoxLayout(self)
        self.box.setSpacing(0)
        self.box.setContentsMargins(0, 0, 0, 0)
        self.hbox = QtWidgets.QHBoxLayout()
        self.hbox.setSpacing(0)
        self.hbox.setContentsMargins(0, 0, 0, 0)
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
        self.setStyleSheet("background-color: #F5F5F5")
        self._run_icon = 'resources/icons/base_tool.png'
        self._plugin_name = 'admin'
        self.cfg = get_config(config_path)

        self.box = QtWidgets.QVBoxLayout(self)
        self.center_widget = CentralWidget()
        self.box.addWidget(self.center_widget,
                           alignment=QtCore.Qt.AlignCenter)

        self.view = graphics.View(self.cfg['view-size'])
        self.view.setStyleSheet("background-color: #FCFCFC")
        self.view.setObjectName('admin')
        self.center_widget.add_view(self.view)
        self.top_tool = tools.AdminTool('admin_top_tool', self)
        self.top_tool.setStyleSheet("background-color: #EFEFEF")
        self.top_tool.setFixedHeight(self.cfg['top_tool_height'])

        self.center_widget.add_top_tool(self.top_tool)
        self.left_tool = tools.AdminTool('admin_left_tool', self)
        self.left_tool.setStyleSheet("background-color: #EFEFEF")
        self.left_tool.setFixedWidth(self.cfg['left_tool_width'])
        self.center_widget.add_left_tool(self.left_tool)

    @property
    def run_icon(self):
        return os.path.join(root, self._run_icon)

    @property
    def name(self):
        return self._plugin_name
