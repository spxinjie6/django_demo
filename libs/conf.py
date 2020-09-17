#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: xinjie
@file: conf.py
@time: 2020/09/17
"""
import os
import configparser
import subprocess

host = subprocess.getoutput("hostname")
if host == "xx":
    env = "production"
else:
    env = "development"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(BASE_DIR + "/etc/{}/django_demo.conf".format(env))

conf = configparser.ConfigParser()
conf.read(PATH)

def fetch_args(section):
    if section not in conf.sections():
        raise (configparser.NoSectionError, "{} does't exists!".format(section))

    options = {}
    for option in conf.options(section):
        option_value = conf.get(section, option)

        if option_value.isdigit():
            option_value = int(option_value)
        if option_value == "True":
            option_value = True
        if option_value == "False":
            option_value = False
        options[option] = option_value
    return options
