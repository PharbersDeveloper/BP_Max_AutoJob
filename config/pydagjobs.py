# -*- coding: utf-8 -*-
"""alfredyang@pharbers.com.

This module document the YAML Config container for Pharbers jobs
"""
from config.phcontainer import PhYAMLContainer


class PhYAMLDAGJobs(object):
    def __init__(self, dt):
        self.name = ""
        self.command = ""
        self.dict2obj(dt)

    def dict2obj(self, dt):
        self.__dict__.update(dt)
