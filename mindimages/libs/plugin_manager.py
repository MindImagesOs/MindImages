#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import yaml

config_default = "games_plugins.yaml"
config_path = os.path.join('etc', config_default)

def get_config(path):
    with open(path, "r") as obj:
        return yaml.load(obj)

class Manager:
    def __init__(self):
        self.config = get_config(config_path)


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
            pluguns_list.append(mod.BaseGameWidget())
        return pluguns_list