#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 25 ene. 2018

:author: Eugenio Martínez Cámara <emcamara@decsai.ugr.es>
"""

from model.exceptions.error import Error

class TripAdvisorReviewDownloadError(Error):
    '''
    Exception for managing errors related to the download of reviews.
    '''


    def __init__(self, review_id):
        '''
        Constructor
        '''
        super().__init__()
        self.__message = "The review %s couldn't be downloaded" % (review_id)
        
    def __str__(self):
        return self.__message