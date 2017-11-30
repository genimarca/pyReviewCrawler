#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 30 nov. 2017

:author: Eugenio Martínez Cámara <emcamara@decsai.ugr.es>
"""

from abc import ABCMeta, abstractmethod

class ADataCrawling(metaclass=ABCMeta):
    '''
    Abstract class for the definition of a crawler.
    '''

    @property
    def review_language(self):
        ...
    
    @review_language.setter
    @abstractmethod
    def review_language(self, a_review_language):
        ...
        
    @property
    def entity_type(self):
        ...
    
    @entity_type.setter
    @abstractmethod
    def entity_type(self, a_entity_type):
        ...
        
    @property
    def entity_location(self):
        ...
    
    @entity_location.setter
    @abstractmethod
    def entity_location(self, a_entity_location):
        ...
        
    @abstractmethod
    def build_base_url(self):
        ...
        
    @abstractmethod
    def get_review_ids(self):
        ...
        
    @abstractmethod
    def get_review(self, review_id):
        ...