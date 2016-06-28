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
        package_obj = __import__("games.admin.main_game")
        mod = getattr(getattr(package_obj, 'admin'), 'main_game')
        print(mod.x)

