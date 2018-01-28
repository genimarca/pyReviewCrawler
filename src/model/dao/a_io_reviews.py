#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 28 ene. 2018

:author: Eugenio Martínez Cámara <emcamara@decsai.ugr.es>
"""

from abc import ABCMeta, abstractmethod

class AIOReviews(metaclass=ABCMeta):
    """Abstract class that set the method for permanently writing the reviews.
    """


    @abstractmethod
    def output_method_configuration(self, **args):
        ...
    
    @abstractmethod
    def write_header(self):
        ...
    
    @abstractmethod
    def write_reviews(self, reviews):
        ...
    
    @abstractmethod
    def write_review_one_by_one(self, review):
        ...
        
