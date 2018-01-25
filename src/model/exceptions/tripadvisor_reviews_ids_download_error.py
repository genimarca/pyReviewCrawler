#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 4 dic. 2017

:author: Eugenio Martínez Cámara <emcamara@decsai.ugr.es>
"""
from model.exceptions.error import Error

class TripAdvisorReviewsIdsDownloadError(Error):
    '''
    Excepción para cuando no se pueden descargar la web relativa a los ids
    de las opiniones
    '''


    def __init__(self, entity_id):
        super().__init__()
        self.__message = "The Ids of the reviews of %s have not been able to download" % (entity_id)
        
    
    def __str__(self):
        return(self.__message)