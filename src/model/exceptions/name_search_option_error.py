#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 16 nov. 2017

:author: Eugenio Martínez Cámara <genimarca@gmail.com>
:organization: Universidad de Granada
"""
from model.exceptions.error import Error

class NameSearchOptionError(Error):
    """Represents the error for non-allowed search option names.
    """

    def __init__(self, search_option):
        super().__init__()
        self.__message = "The option %s is not allowed." % (search_option)
    
    def __str__(self):
        return self.__message
        