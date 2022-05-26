# -*- coding: utf-8 -*-
__author__ = "Team Blue"

from server.modules.helper import ModuleABC


class Module(ModuleABC):
    def get_info(self):
        return {
            "Author:": ["Team Blue"],
            "Description": "Return basic information about the bot.",
            "References": [],
            "Stoppable": False
        }
