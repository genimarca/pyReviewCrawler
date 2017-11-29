#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 16 nov. 2017

:author: Eugenio Martínez Cámara <genimarca@gmail.com>
:organization: Universidad de Granada
"""

from model.utils.config_search import ConfigSearch
from model.utils.search_options import SearchOptions

class ConfigSearchTripadvisor(ConfigSearch):
    """For the processing of the search options of the web source
    TripAdvisor
    """

    def __init__(self, params):
        super().__init__()
    
    
    @classmethod
    def get_option(cls, option):
        option_value = super(ConfigSearchTripadvisor, cls).get_option(option)
        if option == SearchOptions.N_REVIEWS_DOWNLOAD: 
            if option_value is None:
                option_value = -1
            else:
                try:
                    option_value = int(option_value)
                except ValueError:
                    pass
        return option_value
            