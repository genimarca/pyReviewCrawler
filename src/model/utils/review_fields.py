#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 28 ene. 2018

:author: Eugenio Martínez Cámara <emcamara@decsai.ugr.es>
"""

from enum import Enum
from enum import unique

@unique
class ReviewFields(Enum):
    """The fields to store of each review.
    """

    REVIEW_TYPE_ENTITY = "REVIEW_TYPE_ENTITY",
    
    REVIEW_LOCATION_ID = "REVIEW_LOCATION_ID",
    
    REVIEW_LOCATION_NAME = "REVIEW_LOCATION_NAME",
    
    REVIEW_ENTITY_ID = "REVIEW_ENTITY_ID",
    
    REVIEW_ENTITY_NAME = "REVIEW_ENTITY_NAME"
    
    REVIEW_USER_NAME = "REVIEW_USER_NAME",
    
    REVIEW_USER_ID = "REVIEW_USER_ID",
    
    REVIEW_RAITING = "REVIEW_RAITING",
    
    REVIEW_DATE = "REVIEW_DATE",
    
    REVIEW_TITLE = "REVIEW_TITLE",
    
    REVIEW_BODY = "REVIEW_BODY"