#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from functools import partial

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot

from gui import gui_abs as gui
from gui import manager_window


class Main(QtWidgets.QMainWindow):
    def __init__(self, config):
        super().__init__()
        self.cfg = config["base"]
        self.center = gui.Frame("center_frame", self)
        self.setCentralWidget(self.center)

        self.stack = gui.StackedLayout(self.center)

        self.global_game_window = manager_window.MangerWindow(
            "manager_window", self, config["global_game_window"],
            self.center,
        )
        self.stack.add_content(self.global_game_window)

    def register_control(self, control_object, slot, *args):
        control_object.clicked.connect(getattr(self, slot))

    @QtCore.pyqtSlot()
    def exit(self):
        sys.exit()

    @QtCore.pyqtSlot(int)
    def press_game(self, s):
        pass
        self.stack.setCurrentIndex(s)

    @pyqtSlot(int)
    def press_game(self, s):
        self.stack.setCurrentIndex(s)

    def add_plugin(self, plugin_list):
        for index, plugin in enumerate(plugin_list, start=1):
            run_btn = self.global_game_window.add_run_button(
                plugin.run_icon,
                plugin.name, index)
            run_btn.clicked.connect(partial(self.press_game, index))
            self.stack.addWidget(plugin)

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == QtCore.Qt.Key_1:
            self.stack.setCurrentIndex(1)
        elif QKeyEvent.key() == QtCore.Qt.Key_0:
            self.return_to_content()

    def return_to_content(self):
        self.stack.return_to_content()