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
        
    @property
    def entity_id(self):
        ...
        
    @entity_id.setter
    @abstractmethod
    def entity_id(self, a_entity_id):
        ...
    
    @property
    def base_url(self):
        ...
        
    @property
    def review(self):
        ...
    
    @abstractmethod
    def build_base_url(self):
        ...
        
    @property
    def max_num_reviews(self):
        ...
    
    @max_num_reviews.setter
    @abstractmethod
    def max_num_reviews(self, a_max_num_reviews):
        ...
    
    @property
    def timeout(self):
        ...
        
    @timeout.setter
    @abstractmethod
    def timeout(self, a_timeout):
        ...
    
    @property
    def pause_btween_requests(self):
        ...    
    
    @pause_btween_requests.setter
    def pause_btween_requests(self, a_pause_btween_requests):
        ...        
    
    @property
    def max_attempts(self):
        ...    
    
    @max_attempts.setter
    def max_attempts(self, a_max_attempts):
        ...
    
    @abstractmethod
    def get_review_ids(self):
        ...
        
    @abstractmethod
    def get_review(self, review_id):
        ...
        