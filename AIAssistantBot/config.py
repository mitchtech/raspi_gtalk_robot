#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import ConfigParser

class config:

    def __init__(self, cfgFile="cfg.ini"):
        if cfgFile and os.path.isfile(cfgFile):
            self.cfgFile = cfgFile
        else:
            raise ValueError("Configuration File '%s' not exist!"%cfgFile)

    def get(self, section, option, type="str"):
        cfgp = ConfigParser.ConfigParser()
        cfgp.read(self.cfgFile)
        value = None
        if cfgp.has_option(section, option):
            if type=="str":
                value = cfgp.get(section, option)
            if type=="int":
                value = cfgp.getint(section, option)
            elif type=="float":
                value = cfgp.getfloat(section, option)
            elif type=="boolean":
                value = cfgp.getboolean(section, option)

        return value

    def set(self, section, option, value):
        cfgp = ConfigParser.ConfigParser()
        cfgp.read(self.cfgFile)

        if value:
            if not cfgp.has_section(section):
                cfgp.add_section(section)
            cfgp.set(section, option, str(value))
        else:
            if cfgp.has_option(section, option):
                cfgp.remove_option(section, option)
        cfgp.write(open(self.cfgFile, "w"))
        return True
