"""
Created on 9 nov. 2017

:author: Eugenio Martínez Cámara <genimarca@gmail.com>
"""

import unittest
import sys
sys.path.append("/Users/geni/Documents/datos/documentos/trabajo/entornosTrabajo/eclipseOxigen/python/review_crawler/src/")
from review_crawler import config_parse_input_args
from review_crawler import config_parse_dev_mode


class TestScriptInputArguments(unittest.TestCase):
    """Class for testing the parsing of the input of the script
    """

    def setUp(self):
        self.__input_args_parser = config_parse_input_args()

    def test_help_argument(self):
        self.assertIsNotNone(self.__input_args_parser.format_help())
        
    def test_dev_mode_help_argument(self):
        self.__input_args_parser = config_parse_dev_mode(self.__input_args_parser)
        self.assertIsNotNone(self.__input_args_parser.format_help())
        
    def test_web_site_argument_no(self):
        msg_str = "The default value of the web source must be tripadvisor"
        input_args = self.__input_args_parser.parse_args([])
        self.assertEqual(input_args.web_source, "tripadvisor", msg_str)
    
    def test_web_site_argument_yes(self):
        msg_str = "The web source argument value is not booking"
        input_args = self.__input_args_parser.parse_args(["-w", "tripadvisor"])
        self.assertEqual(input_args.web_source, "tripadvisor", msg=msg_str)
        
    def test_output_template_argument_no(self):
        msg_str = "The default output template is csv"
        input_args = self.__input_args_parser.parse_args([])
        self.assertEqual(input_args.output_template, "csv", msg_str)
        
    def test_output_template_argument_yes(self):
        msg_str = "The value of the output template must be xml"
        input_args = self.__input_args_parser.parse_args(["-t", "xml"])
        self.assertEqual(input_args.output_template, "xml", msg_str)
        
    def test_output_path_argument_no(self):
        msg_str = "The default output is stdout"
        input_args = self.__input_args_parser.parse_args([])
        self.assertEqual(input_args.output_path, "stdout", msg_str)
        
    def test_output_path_argument_yes(self):
        msg_str = "The value of the output path must be /home/geni/reviews.txt"
        input_args = self.__input_args_parser.parse_args(["-o", "/home/geni/reviews.txt"])
        self.assertEqual(input_args.output_path, "/home/geni/reviews.txt", msg_str)
        
    def test_verbose_argument(self):
        self.__input_args_parser.parse_args(["--verbose"])
        input_args = self.__input_args_parser.parse_args(["--verbose"])
        self.assertTrue(input_args.verbose)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()