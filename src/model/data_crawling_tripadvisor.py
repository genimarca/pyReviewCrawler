#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 1 dic. 2017

:author: Eugenio Martínez Cámara <emcamara@decsai.ugr.es>
"""
import re
import urllib.request as url_request
import urllib.error as url_error
from model.a_data_crawling import ADataCrawling
from time import sleep
from socket import socket
from model.exceptions.reviews_ids_download_error import ReviewsIdsDownloadError


class DataCrawlingTripadvisor(ADataCrawling):
    '''It implements the abstract class ADataCrawling
    '''
    
    def __init__(self):
        self.__review_language = ""
        self.__entity_type = ""
        self.__entity_location = ""
        self.__entity_id = ""
        self.__base_url = ""
        self.__max_num_reviews = None
        self.__timeout = None
        self.__pause_btween_requessts = None
        self.__max_attempts = None
    
    
    @property
    def review_language(self):
        return self.__review_language
    
    @review_language.setter
    def review_language(self, a_review_language):
        self.__review_language = a_review_language
        
    @property
    def entity_type(self):
        return self.__entity_type
    
    @entity_type.setter
    def entity_type(self, a_entity_type):
        self.__entity_type = a_entity_type
    
    @property
    def entity_location(self):
        return self.__entity_location
    
    @entity_location.setter
    def entity_location(self, a_entity_location):
        self.__entity_location = a_entity_location
        
    @property
    def entity_id(self):
        return self.__entity_id
    
    @entity_id.setter
    def entity_id(self, a_entity_id):
        self.__entity_id = a_entity_id
        
    @property
    def base_url(self):
        return self.__base_url
    
    @base_url.setter
    def base_url(self, a_base_url):
        self.__base_url = a_base_url
        
    @property
    def max_num_reviews(self):
        return self.__max_num_reviews
    
    @max_num_reviews.setter
    def max_num_reviews(self, a_max_num_reviews):
        self.__max_num_reviews = a_max_num_reviews
        
    @property
    def timeout(self):
        return self.__timeout
    
    @timeout.setter
    def timeout(self, a_timeout):
        self.__timeout = a_timeout
    
    
    @property
    def pause_btween_requests(self):
        return self.__pause_btween_requessts
    
    @pause_btween_requests.setter
    def pause_btween_requests(self, a_pause_btween_requests):
        self.__pause_btween_requessts = a_pause_btween_requests
        
    @property
    def max_attempts(self):
        return self.__max_attempts
    
    @max_attempts.setter
    def max_attempts(self, a_max_attempts):
        self.__max_entries = a_max_attempts
    
    def build_base_url(self):
        """Build the base url for downloading the reviews
        
        :requires: To set the properties `review_languag` and `entity_type`.
        Returns: A String
        """
        self.__base_url = "https://www.tripadvisor.%s/%s" % (self.__review_language,
                                                  self.__entity_type)
        
    def __get_webpage(self, url):
        """Donwload a web page
        
        Returns: A String in case a succesful donwload or Null otherwise
        """
        htmlpage = None
        attempts = 0
        while attempts < self.__max_attempts and htmlpage is None:
            try:
                with url_request.urlopen(url, timeout=self.__timeout) as url_handler:
                    htmlpage = url_handler.read()
                    sleep(self.__pause_btween_requessts)
            except (url_error.URLError, socket.timeout, socket.error):
                attempts += 1
        return htmlpage
                
            
        
        
    
    def get_review_ids(self):
        """Download the number of ids of reviews indicated by the property
        max_num_reviews.
        
        Return: A list of ids of reviews
        """
        
        download_url = "%s_Review-%s-%s-Reviews" % (self.__base_url,
                                                    self.__entity_location,
                                                    self.__entity_id)
        re_review_id_pattern = re.compile(r'/ShowUserReviews-g%s-d%s-r([0-9]+)-' % 
                                          (self.__entity_location, self.__entity_id))
        
        htmlwebpage = self.__get_webpage(download_url)
        review_ids = []
        if not htmlwebpage:
            review_ids = None
            raise ReviewsIdsDownloadError(self.__entity_id)
        else:
            re_review_id_pattern.findall(htmlwebpage)
        
    def get_review(self, review_id):
        ADataCrawling.get_review(self, review_id)