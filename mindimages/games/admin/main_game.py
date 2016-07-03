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
from games.admin.scr import seqlogic
from libs import plugin_manager


root = os.path.join(os.path.dirname(__file__))
config_path = os.path.join(root, 'etc/config.yaml')
icon_dir = os.path.join(root, 'resources/icons')
seq_path = os.path.join(root, 'etc/seq.yaml')


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
    def __init__(self, parent):
        """
        базовое окно
        """
        super().__init__()
        self._parent = parent
        self.setParent(self._parent)

        self.setStyleSheet("background-color: #DEDEDE")
        self._run_icon = 'resources/icons/base_tool.png'
        self._plugin_name = 'admin'
        self.cfg = get_config(config_path)

        self.box = QtWidgets.QVBoxLayout(self)

        # окно контейнер в котором размещены рабочие виджеты
        self.center_widget = CentralWidget()
        self.box.addWidget(self.center_widget,
                           alignment=QtCore.Qt.AlignCenter)

        self.seq = seqlogic.SeqImages(get_config(seq_path))

        # сцена
        self.scene = graphics.Scene(self.cfg['scene_geometry'])

        # представление
        self.view = graphics.View(self.cfg['view-size'],
                                  scene=self.scene,
                                  parent=self)
        self.view.setStyleSheet("background-color: #F3F3F3")
        self.view.setObjectName('admin')
        self.center_widget.add_view(self.view)


        self.top_tool = tools.AdminTool('admin_top_tool',
                                        self,
                                        tools.AdminTool.horizontal,
                                        icon_dir)
        self.top_tool.setStyleSheet("background-color: #D0D0D0")
        self.top_tool.setFixedHeight(self.cfg['top_tool_height'])
        self.top_tool.set_margins(*self.cfg['h_tool_box_margin'])
        self.top_tool.set_spacing(self.cfg['h_tool_box_spacing'])
        self.top_tool.add_items(self.cfg['top_buttons'])

        self.center_widget.add_top_tool(self.top_tool)
        self.left_tool = tools.AdminTool('admin_left_tool',
                                         self,
                                         tools.AdminTool.vertical,
                                         icon_dir)
        self.left_tool.setStyleSheet("background-color: #D0D0D0")
        self.left_tool.setFixedWidth(self.cfg['left_tool_width'])
        self.left_tool.set_margins(*self.cfg['v_tool_box_margin'])
        self.left_tool.set_spacing(self.cfg['v_tool_box_spacing'])
        self.center_widget.add_left_tool(self.left_tool)

    @property
    def run_icon(self):
        return os.path.join(root, self._run_icon)

    @property
    def name(self):
        return self._plugin_name

    def return_to_content(self):
        self._parent.return_to_content()
