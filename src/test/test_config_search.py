#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Created on 15 nov. 2017

:author: Eugenio Martínez Cámara <genimarca@gmail.com>
:organization: Universidad de Granada
"""

import unittest
import sys
sys.path.append("/Users/geni/Documents/datos/documentos/trabajo/entornosTrabajo/eclipseOxigen/python/review_crawler/src/")
from model.utils.search_options import SearchOptions
from model.utils.config_search_tripadvisor import ConfigSearchTripadvisor
class TestConfigSearch(unittest.TestCase):


    def setUp(self):
        ConfigSearchTripadvisor.set_path("../../test/test_data/test_config.yaml")
        ConfigSearchTripadvisor.readall()
    
    def test_opinion_language(self):
        rev_langauge = ConfigSearchTripadvisor.get_option(SearchOptions.REVIEW_LANGUAGE.value)
        self.assertEqual(rev_langauge, "es")
        
    def test_type_entity(self):
        type_entity = ConfigSearchTripadvisor.get_option(SearchOptions.TYPE_ENTITY.value)
        self.assertEqual(type_entity, "Attraction")
        
    def test_location_entity(self):
        location_entity = ConfigSearchTripadvisor.get_option(SearchOptions.LOCATION_ENTITY.value)
        self.assertEqual(location_entity, "g315916")
        
    def test_id_entity(self):
        id_entity = ConfigSearchTripadvisor.get_option(SearchOptions.ID_ENTITY.value)
        self.assertEqual(id_entity, "d519940")
    
    def test_n20_reviews_donwload(self):
        n_reviews_download = ConfigSearchTripadvisor.get_option(SearchOptions.N_REVIEWS_DOWNLOAD.value)
        self.assertEqual(n_reviews_download, 20)
    
    def test_n20integer_review_download(self):
        n_reviews_download = ConfigSearchTripadvisor.get_option(SearchOptions.N_REVIEWS_DOWNLOAD.value)
        self.assertIsInstance(n_reviews_download, int)
        
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()