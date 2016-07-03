#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets


class Manager:
    def __init__(self, config, parent):
        self.parent = parent
        self.config = config


    def plugins_list(self):
        """

        :return: список объектов класса унаследованного от
        QtWidgets
        """
        pluguns_list = []
        for plugin in self.config['plugins']:
            object_str = '.'.join([self.config['base_games_dir'],
                                   plugin,
                                   self.config['mod_entry_point']])
            package_obj = __import__(object_str)
            mod = getattr(getattr(package_obj, plugin),
                          self.config['mod_entry_point'])
            pluguns_list.append(mod.BaseGameWidget)
        return pluguns_list


class Plugin(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: white")


    @property
    def run_icon(self):
        """
         метод должен вернуть путь к иконке str
        """
        raise Exception('необходимо переопределить в классе потомке')

    @property
    def name(self):
        """
        метод должен вернуть имя плагина str
        """
        raise Exception('необходимо переопределить в классе потомке')

    def return_to_content(self):
        """
        вызывается метод класса родителя возвращающий к окну родителя
        """
        raise Exception('необходимо переопределить в классе потомке')