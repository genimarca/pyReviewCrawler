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
from model.exceptions.tripadvisor_reviews_ids_download_error import TripAdvisorReviewsIdsDownloadError
from model.exceptions.tripadvisor_review_download_error import TripAdvisorReviewDownloadError


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
        self.__base_url = "https://www.tripadvisor.%s" % (self.__review_language)
        
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
                
            
        
        
    def __is_no_more_reviews(self, new_reviews_ids, reviews_ids):
        """It checks if there is new donwloaded review ids.
        
        Args:
            new_reviews_ids: List of String with the last ids donwloaded.
            reviews_ids: Set of review ids.
        """
        no_more_reviews_ids = False
        for r_id in new_reviews_ids:
            if r_id in reviews_ids:
                no_more_review_ids = True
                break
        return no_more_review_ids
    
    
    def get_review_ids(self):
        """Download the number of ids of reviews indicated by the property
        max_num_reviews.
        
        Return: A list of ids of reviews
        """
        review_page_step = 10
        download_url = "%s/%s_Review-%s-%s-Reviews" % (self.__entity_type,
                                                    self.__base_url,
                                                    self.__entity_location,
                                                    self.__entity_id)
        re_review_id_pattern = re.compile(r'/ShowUserReviews-g%s-d%s-r([0-9]+)-' % 
                                          (self.__entity_location, self.__entity_id))
        
        
        
        n_reviews_downloaded = 0
        page_reviews_ids = 0
        no_more_review_ids = False
        while(n_reviews_downloaded < self.__max_num_reviews and not no_more_review_ids):
            download_url = "%s-or%s" % (download_url, page_reviews_ids * review_page_step)
            htmlwebpage = self.__get_webpage(download_url)
            reviews_ids = set()
            if not htmlwebpage:
                review_ids = None
                raise TripAdvisorReviewsIdsDownloadError(self.__entity_id)
            else:
                new_reviews_ids = re_review_id_pattern.findall(htmlwebpage.decode("utf-8"))
                no_more_review_ids = self.__is_no_more_reviews(new_reviews_ids, reviews_ids)
                if not no_more_review_ids:
                    review_ids.update(new_reviews_ids)
                    if len(new_reviews_ids) + len(reviews_ids) > self.__max_num_reviews:
                        reviews_ids = review_ids[:self.__max_num_reviews]
                    page_reviews_ids +=1
        return reviews_ids
        
    def get_review(self, review_id):
        """Download a review
        
        Args:
            review_id: A String object whose value is the id of the review to
            download
        Return:
            A String object that corresponds to the html page of the review 
            whose id is review_id
        """
        
        download_url = "%s/ShowUserReviews-%s-%s-r%s" % (self.__base_url,
                                                  self.__entity_location,
                                                  self.__entity_id,
                                                  review_id)
        htmlwebpage = self.__get_webpage(download_url)
        if not htmlwebpage:
            raise TripAdvisorReviewDownloadError(review_id)
        
        return htmlwebpage
    
    def parse_individual_review(self, htmlwebpage):
        """It parses an individual review of an entity_type
        
        Args:
            htmlwebpage: A String object corresponding to the html page of
            an individual review
        """
        
        re_user_name = re.compile(r"scrname.+>(.+)<", re.S)
        re_user_id = re.compile()
        re_rating = 
        re_title_review
        re_body_review =
        
        