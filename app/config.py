#!/usr/bin/env python

"""
config.py

Cless for representing an enitre configuration.

Author: Curtis Millar
Date:   24 July 2016

Copyright (c) Curtis Millar 2016. All Rights Reserved.
"""

from os.path import isfile as isFile, exists
from json import load as loadJSON, dump as saveJSON

class Config:

    def __init__(self, path):
        self.__path = path

        self.nameHosts = []
        self.macHosts = []
        self.groups = []
        self.payloads = []

        # Load the file if it exists
        if exists(self.__path):
            if isFile(self.__path):
                self.__fileInit(self.__path)
            else:
                raise IOError("Path \"{}\" exists but is not a file".format(self.__path))

    def __fileInit(self, path):
        jsonData = loadJSON(file(path, 'r'))

    def __asObject(self):
        data = {
            "groups" : {},
            "payloads" : {},
        }

        return data

    def save(self):
        saveJSON(self.__asObject(), file(self.__path, 'w'))

    def getNameHost(self, name):
        return None

    def getMacHost(self, addr):
        return None

    def getGroup(self, groupName):
        pass
