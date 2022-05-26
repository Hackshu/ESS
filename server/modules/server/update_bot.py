# -*- coding: utf-8 -*-
__author__ = "Team Blue"

from server.modules.helper import *


class Module(ModuleABC):
    def get_info(self):
        return {
            "Author:": ["Team Blue"],
            "Description": "Update the bot to the latest (local) version.",
            "References": [],
            "Stoppable": False
        }

    def setup(self, set_options):
        self._view.display_error("This feature hasn't been implemented yet!")
        return False, None
