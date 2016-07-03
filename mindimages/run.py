#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import yaml
from PyQt5 import QtWidgets

from gui import base_window

from libs import plugin_manager




def get_config(path):
    with open(path, "r") as obj:
        return yaml.load(obj)


config_default = "config.yaml"
config_path = os.path.join('etc', config_default)
config = get_config(config_path)
css_path = os.path.join('css', config["base"]["css_default"])


config_games_plugin = "games_plugins.yaml"
config_games_plugin_path = os.path.join('etc', config_games_plugin)

def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(open('{}'.format(css_path), "r").read())
    m = base_window.Main(config)


    plugin = plugin_manager.Manager(get_config(config_games_plugin_path), m)

    m.add_plugin(plugin.plugins_list())

    m.show()
    m.showFullScreen()
    app.exec()


if __name__ == '__main__':
    pass
    main()
