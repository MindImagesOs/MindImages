#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import yaml
from PyQt5 import QtWidgets

from gui import base_window
from games.admin import main_game
from libs import plagin_manager

t = plagin_manager.Manager()


def get_config(path):
    with open(path, "r") as obj:
        return yaml.load(obj)


config_default = "config.yaml"
config_path = os.path.join('etc', config_default)
config = get_config(config_path)
css_path = os.path.join('css', config["base"]["css_default"])


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(open('{}'.format(css_path), "r").read())
    m = base_window.Main(config)


    # admin_widget = main_game.base.Widget()
    # admin_run_button = main_game.tool_button
    # m.add_game(1, admin_widget, admin_run_button)

    m.show()
    m.showFullScreen()
    app.exec()


if __name__ == '__main__':
    pass
    main()
