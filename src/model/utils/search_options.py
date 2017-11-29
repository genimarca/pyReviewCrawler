#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 15 nov. 2017

:author: Eugenio Martínez Cámara <genimarca@gmail.com>
:organization: Universidad de Granada
"""

from enum import Enum, unique

@unique
class SearchOptions(Enum):
    '''
    Enum type for the properties related to the search
    
    Attributes:
        REVIEW_LANGUAGE: The language of the review.
        TYPE_ENTITY: The type of the entity (Hotels, Attractions...)
        ID_ENTITY: The id of the entity.
        N_REVIEWS_DONWLOAD: The maximum number of reviews to download.
    '''

    REVIEW_LANGUAGE = "REVIEW_LANGUAGE"
    
    TYPE_ENTITY = "TYPE_ENTITY"
    
    LOCATION_ENTITY = "LOCATION_ENTITY"
    
    ID_ENTITY = "ID_ENTITY"
    
    N_REVIEWS_DOWNLOAD = "N_REVIEWS_DONWLOAD"
    