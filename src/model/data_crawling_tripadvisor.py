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
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from model.utils.review_fields import ReviewFields

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
        self.__review = None
    
    
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
    
    @property
    def review(self):
        
        return self.__review
    
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
        html_webpage = self.__get_webpage(download_url)
        if not html_webpage:
            raise TripAdvisorReviewDownloadError(review_id)
        
        return (html_webpage, download_url) 
    
    def __parse_user_id (self, url_webpage):
        """Get the user id of the user who wrote the opinion.
        
        Args:
            url_webpage: The url of the webpage from where the informatino 
            have to be downloaded.
        Returns:
            A String Object with the id of the user.
        """
        
        browser_options = Options()
        browser_options.add_argument("--headless")
        browser_driver = webdriver.Chrome(chrome_options=browser_options)
        browser_driver.get(url_webpage)
        wait = WebDriverWait(browser_driver, 5)
        aux_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".scrname")))
        user_element = browser_driver.find_element_by_css_selector(".scrname")
        user_element.click()
        user_id = browser_driver.find_element_by_css_selector(".memberOverlayRedesign > a").get_attribute("href")
        browser_driver.quit()
        return user_id
    
    
    def parse_individual_review(self, html_webpage, url_webpage):
        """It parses an individual review of an entity_type
        
        Args:
            html_webpage: A String object corresponding to the html page of
            an individual review
            url_webpage: A String object corresponding to the url of the 
            webpage of the data.
        """
        
        #Name of the location
        re_location_name = re.compile(r"ui_pill inverted.*\"(.*)\"<", re.S)
        
        #Name of the entity
        re_entity_name = re.compile(r"HEADING.+>(.*)<", re.S)
        
        re_user_name = re.compile(r"scrname.+>(.+)<", re.S)
        re_review_rating = re.compile(r"reviewItemInline.+ui_bubble_rating bubble_([0-5][0-5])", re.S)
        re_review_date = re.compile(r"raitingDate relativeDate.+title=\"(.+)\"", re.S)
        re_review_title = re.compile(r"quote.+noQuotes\">(.+)<")
        re_review_body = re.compile(r"p.+partial_entry\">.*\"(.+)\"")
        
        location_name = re_location_name.match(html_webpage)
        
        entity_name = re_entity_name.match(html_webpage)
        
        user_name = re_user_name.match(html_webpage)
        user_id = self.__parse_user_id(url_webpage)
        review_raiting = re_review_rating.match(html_webpage)
        review_date = re_review_date.match(html_webpage)
        review_title = re_review_title.match(html_webpage)
        review_body = re_review_body.match(html_webpage)
        
        self.__review = {
            ReviewFields.REVIEW_TYPE_ENTITY.value: self.__entity_type,
            ReviewFields.REVIEW_LOCATION_ID.value: self.__entity_location,
            ReviewFields.REVIEW_LOCATION_NAME.value: location_name,
            ReviewFields.REVIEW_ENTITY_ID: self.__entity_id,
            ReviewFields.REVIEW_ENTITY_NAME: entity_name,
            ReviewFields.REVIEW_USER_NAME.value: user_name,
            ReviewFields.REVIEW_USER_ID.value: user_id,
            ReviewFields.REVIEW_RAITING.value: review_raiting,
            ReviewFields.REVIEW_DATE.value: review_date,
            ReviewFields.REVIEW_TITLE.value: review_title,
            ReviewFields.REVIEW_BODY.value: review_body
        }