#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 15 nov. 2017

:author: Eugenio Martínez Cámara <genimarca@gmail.com>
:organization: Universidad de Granada
"""

import yaml
from model.exceptions.name_search_option_error import NameSearchOptionError

class ConfigSearch(object):
    '''
    Handles the configuration of the search.
    
    Attributes:
        __path: A string that represents the path of the configuration
        file
    '''

    
    __path = ""
    __search_options = None
    
    @classmethod
    def get_path(cls):
        return cls.__path
    
    @classmethod
    def set_path(cls, a_path):
        cls.__path = a_path
        
    
    @classmethod
    def readall(cls):
        """Read the configuration information
        """
        with open(cls.__path, 'r', encoding="utf-8") as conf_file:
            cls.__search_options = yaml.load(conf_file)
        
    @classmethod
    def get_option(cls, option):
        option_value = cls.__search_options.get(option)
        
        if option_value is None:
            try:
                raise NameSearchOptionError(option)
            except NameSearchOptionError as e:
                print(e)
        else:
            return cls.__search_options.get(option)