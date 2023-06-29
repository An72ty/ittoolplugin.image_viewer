# -*- coding: utf-8 -*-
from __future__ import annotations
from rich.console import Console
# Import system ptools
import libs.ptools as ptools
# Create globals
AppData = None
console = Console()

modulesNames = ['errors', 'commandManager']
NAME = "image viewer"

# Init fuction init AppData


def init(data):
    global AppData
    AppData = data


class NotAllModulesConnected(Exception):
    pass


class p(ptools.Plugin):
    def __init__(
        self,
        data,
        modules: list = ...
    ) -> p:
        super().__init__(data, modules)
        connectedModulesNames = [module.NAME for module in self.modules]
        if connectedModulesNames == modulesNames:
            self.errors.Functions.debug('Connected plugin {0}'.format(NAME))
        else:
            raise NotAllModulesConnected('Connected modules: {0} Not connected: {1}'.format(
                connectedModulesNames, modulesNames))

    def activate(self) -> bool:
        self.errors.Functions.debug('Plugin {0} activated'.format(NAME))
        AppData.groups.list['System tools'].addCommand([
            self.commandManager.Command('test', self.print, 'описание')])
        AppData.groups.update()

    def print(self):
        print(".")
