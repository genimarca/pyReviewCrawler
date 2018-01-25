"""
Created on 30 nov. 2017

:author: Eugenio Martínez Cámara <genimarca@gmail.com>
"""

import unittest
import sys
sys.path.append("/Users/geni/Documents/datos/documentos/trabajo/entornosTrabajo/eclipseOxigen/python/review_crawler/src/")
from model.data_crawling_tripadvisor import DataCrawlingTripadvisor

class TestDataCrawlingTripadvisor(unittest.TestCase):

    
    
    def test_build_base_url(self):
        
        crawling_handler = DataCrawlingTripadvisor()
        
        crawling_handler.review_language = "es"
        
        crawling_handler.entity_type = "Attraction"
        
        crawling_handler.build_base_url()
        
        response_base_url = crawling_handler.base_url
        
        self.assertEqual(response_base_url, "https://www.tripadvisor.es")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()