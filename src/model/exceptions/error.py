#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 16 nov. 2017

:author: Eugenio Martínez Cámara <genimarca@gmail.com>
:organization: Universidad de Granada
"""

class Error(Exception):
    """Base exception class
    
    Attributes:
        __message: A String that represents the error message
    """


    def __init__(self):
        self.__message = ""
        