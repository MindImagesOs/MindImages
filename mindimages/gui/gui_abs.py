#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
модуль предаставляет классы наслдеованые от qt классов для использования в основной программе
"""


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
    def __init__(self, path, name, index, parent):
        super().__init__(name, parent)
        self.index = index
        self.setIcon(QtGui.QIcon(path))

    # def __repr__(self):
    #     return """
    #     object - {};
    #     object_name - {};
    #     index - {}
    #     """.format(self.__class__.__name__, self._name, self.index)


class ToolWidget(Frame):
    horizontal = 'Horizontal'
    vertical = 'Vertical'
    def __init__(self, name, parent, direction, cfg):
        super().__init__(name, parent)
        self.cfg = cfg
        self.direction = direction
        self.box = self.create_box()


    def create_box(self):
        if self.direction == self.horizontal:
            box = QtWidgets.QHBoxLayout(self)
        elif self.direction == self.vertical:
            box = QtWidgets.QVBoxLayout(self)
        else: raise Exception('нет такого направления')
        box.setSpacing(0)
        box.setContentsMargins(0, 0, 0, 0)
        return box

    def add_item(self, item):
        self.box.addWidget(item)