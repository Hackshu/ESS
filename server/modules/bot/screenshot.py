# -*- coding: utf-8 -*-
__author__ = "Team Blue"

import subprocess

OUTPUT_FILE = "/var/tmp/image-cache.png"


def run_command(command):
    out, err = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    return out + err


def run(options):
    run_command("screencapture -x " + OUTPUT_FILE)
    print(run_command("base64 " + OUTPUT_FILE))
    run_command("rm -rf " + OUTPUT_FILE)
