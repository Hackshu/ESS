# -*- coding: utf-8 -*-
__author__ = "Team Blue"

from server.modules.helper import ModuleABC


class Module(ModuleABC):
    def get_info(self):
        return {
            "Author:": ["Team Blue"],
            "Description": "Show a list of devices backed up by iTunes.",
            "References": [],
            "Stoppable": False
        }
