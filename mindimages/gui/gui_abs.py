#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
модуль предаставляет классы наслдеованые от qt классов для использования в основной программе
"""
import os

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QObject

_box_margin = (1, 10, 21, 1)
_box_spacing = 10

class AbsGui(QObject):
    def __init__(self, name, parent):
        super().__init__()
        self.setObjectName(name)
        self.setParent(parent)





class Box(QtWidgets.QBoxLayout):
    _horizontal = QtWidgets.QBoxLayout.LeftToRight
    _vertical = QtWidgets.QBoxLayout.TopToBottom

    def __init__(self, direction, QWidget_parent=None,
                 margin=_box_margin, spacing=_box_spacing):
        """

        :param direction: Box._horizontal \ Box._vertical
        :param QWidget_parent: QWidget
        :param margin: поле вокруг
        :param spacing: интервал (шаг) между виджетами
        """
        super().__init__(direction, QWidget_parent)
        self.setDirection(direction)
        self.setContentsMargins(*margin)
        self.setSpacing(spacing)


class Frame(QtWidgets.QFrame, AbsGui):
    def __init__(self, name, parent):
        super().__init__(name, parent)


class StackedLayout(QtWidgets.QStackedLayout):
    def __init__(self, *__args):
        super().__init__(*__args)

    def add_widget(self, QWidget):
        self.addWidget(QWidget)

    def add_content(self, QWidget):
        self.insertWidget(0, QWidget)

    def return_to_content(self):
        self.setCurrentIndex(0)

class MenegerFrame(QtWidgets.QFrame, AbsGui):
    def __init__(self, name, parent):
        super().__init__(name, parent)

class ToolGame(QtWidgets.QFrame, AbsGui):
    def __init__(self, name, parent):
        super().__init__(name, parent)

class SettingButton(QtWidgets.QPushButton, AbsGui):
    def __init__(self, name, parent, size):
        """

        :type size_button: int
        :type size_icon: int
        :type name: str
        """
        super().__init__(name, parent)
        self.setIconSize(QtCore.QSize(size, size))
        self.setFixedSize(size + 2, size + 2)

class GameButton(QtWidgets.QToolButton, AbsGui):
    def __init__(self, path, name, index, parent, size=None):
        super().__init__(name, parent)
        self.index = index
        self.setIcon(QtGui.QIcon(path))
        if size is not None:
            self.setIconSize(QtCore.QSize(size, size))

    # def __repr__(self):
    #     return """
    #     object - {};
    #     object_name - {};
    #     index - {}
    #     """.format(self.__class__.__name__, self._name, self.index)


class ToolWidget(Frame):
    horizontal = 'Horizontal'
    vertical = 'Vertical'
    def __init__(self, name, parent, direction, icon_dir):
        super().__init__(name, parent)

        self.icon_dir = icon_dir
        self.direction = direction
        self.box = self.create_box()


    def create_box(self):
        if self.direction == self.horizontal:
            box = QtWidgets.QHBoxLayout(self)
        elif self.direction == self.vertical:
            box = QtWidgets.QVBoxLayout(self)
        else: raise Exception('нет такого направления')
        return box

    def set_margins(self, l, t, r, b):
        self.box.setContentsMargins(l, t, r, b)

    def set_spacing(self, s):
        self.box.setSpacing(s)

    def add_items(self, items, ext='.png', size=None):
        for i in items:
            if i == 'Stretch':
                self.box.addStretch()
            else:
                path_icon = os.path.join(self.icon_dir, i + ext)
                btn = GameButton(path_icon, i, i, self, size)

                btn.clicked.connect(self.parent().return_to_content)
                self.box.addWidget(btn)