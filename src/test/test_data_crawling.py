"""
Created on 29 nov. 2017

:author: Eugenio Martínez Cámara <emcamara@decsai.ugr.es>
"""
from unittest import main
from unittest import TestCase
from unittest.mock import patch

class TestDataCrawling(TestCase):


    @patch("model.DataCrawling")
    def test_get_reviews(self, DataCrawling):
        
        crawling_handler = DataCrawling()
        
        crawling_handler.build_base_url()
        crawling_handler.get_reviews_ids.return_value = ["539156073", "543828773"]
        crawling_handler.get_review.return_value = "ñadkfalñdjfañlf"
        
        response_reviews_ids = crawling_handler.get_review_ids()
        response_review = crawling_handler.get_review(response_reviews_ids[0])
        
        crawling_handler.build_base_url.assert_called_once_with()
        crawling_handler.get_review_ids.assert_called_once_with()
        self.assertEqual(["539156073", "543828773"], response_reviews_ids)
        crawling_handler.get_review.assert_called_with("539156073")
        self.assertEqual("ñadkfalñdjfañlf", response_review)
    
        
        
        
        
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    main()