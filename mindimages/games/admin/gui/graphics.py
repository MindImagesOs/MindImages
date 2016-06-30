#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from PyQt5 import QtWidgets, QtGui

class GraficsImage(QtWidgets.QGraphicsPixmapItem):
    def __init__(self, path, name):
        super().__init__()
        self.name = name
        self.path = path
        self._pixmap = QtGui.QPixmap(path)
        self.setPixmap(self._pixmap)

    def set_geometry(self, geometry):
        pass


class Scene(QtWidgets.QGraphicsScene):
    def __init__(self, geometry, parent=None):
        super().__init__()

        self.parent = parent
        self.setSceneRect(*geometry)




class View(QtWidgets.QGraphicsView):
    def __init__(self, size=None, scene=None, parent=None):
        super().__init__()
        self.setFixedSize(size, size)


if __name__ == '__main__':
    from cube import paths
    app = QtWidgets.QApplication(sys.argv)
    scene = Scene((0, 0, 500, 500))
    main = View(502, 502)
    main.setScene(scene)
    main.show()
    image_pth = os.path.join(paths.images, '2.png')
    image_obj = GraficsImage(image_pth, 2)
    scene.addItem(image_obj)
    sys.exit(app.exec_())

