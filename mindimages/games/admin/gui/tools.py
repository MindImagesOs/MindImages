#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject
from gui import gui_abs



class AdminTool(gui_abs.ToolWidget):
    def __init__(self, name, parent, direction, icon_dir):
        super().__init__(name, parent, direction, icon_dir)




