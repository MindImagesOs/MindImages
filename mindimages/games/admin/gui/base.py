#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
from PyQt5 import QtWidgets



class Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # self.setFixedSize(500, 500)

        self.box = QtWidgets.QVBoxLayout(self)
        self.btn = QtWidgets.QPushButton()

        self.box.addWidget(self.btn)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Widget()
    main.show()
    sys.exit(app.exec_())