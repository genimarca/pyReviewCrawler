#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 28 ene. 2018

:author: Eugenio Martínez Cámara <emcamara@decsai.ugr.es>
"""
from model.dao.a_io_reviews import AIOReviews
from model.utils.review_fields import ReviewFields
class IOReviewsCSV(AIOReviews):
    """Implementation of AIOReviews abstract class. This implementation 
    writes the reviews in a CSV file
    """


    def __init__(self):
        """
        Constructor
        """
        self.__path = None
        self.__separator = "\t"
        
    def output_method_configuration(self, **args):
        """Set the required parameters of the output method.
        
        Args:
            path: A String with the value of the output path
        """
        
        self.__path = args["path"]
        
    def write_header(self):
        """Write the header of the output file
        """
        
        with open(self.__path, "w", encoding="utf-8") as out_file:
            out_file.write("%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s\n" % 
                           (ReviewFields.REVIEW_TYPE_ENTITY.value,
                            self.__separator,
                            ReviewFields.REVIEW_LOCATION_ID.value,
                            self.__separator,
                            ReviewFields.REVIEW_LOCATION_NAME.value,
                            self.__separator,
                            ReviewFields.REVIEW_ENTITY_ID.value,
                            self.__separator,
                            ReviewFields.REVIEW_ENTITY_NAME.value,
                            self.__separator,
                            ReviewFields.REVIEW_USER_ID.value,
                            self.__separator,
                            ReviewFields.REVIEW_USER_NAME.value,
                            self.__separator,
                            ReviewFields.REVIEW_DATE.value,
                            self.__separator,
                            ReviewFields.REVIEW_RAITING.value,
                            self.__separator,
                            ReviewFields.REVIEW_TITLE.value,
                            self.__separator,
                            ReviewFields.REVIEW_BODY.value))
    
    def write_reviews(self, reviews):
        AIOReviews.write_reviews(self, reviews)
        
    def write_review_one_by_one(self, review):
        """Write the review in a csv file.
        
        Args:
            review: A Dict object with the fields of a review.
        """
        
        with open(self.__path, "a", encoding="utf-8") as out_file:
            buffer_to_write = "%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s\n" % (review[ReviewFields.REVIEW_TYPE_ENTITY.value],
                            self.__separator,
                            review[ReviewFields.REVIEW_LOCATION_ID.value],
                            self.__separator,
                            review[ReviewFields.REVIEW_LOCATION_NAME.value],
                            self.__separator,
                            review[ReviewFields.REVIEW_ENTITY_ID.value],
                            self.__separator,
                            review[ReviewFields.REVIEW_ENTITY_NAME.value],
                            self.__separator,
                            review[ReviewFields.REVIEW_USER_ID.value],
                            self.__separator,
                            review[ReviewFields.REVIEW_USER_NAME.value],
                            self.__separator,
                            review[ReviewFields.REVIEW_DATE.value],
                            self.__separator,
                            review[ReviewFields.REVIEW_RAITING.value],
                            self.__separator,
                            review[ReviewFields.REVIEW_TITLE.value],
                            self.__separator,
                            review[ReviewFields.REVIEW_BODY.value])
            out_file.write(buffer_to_write)