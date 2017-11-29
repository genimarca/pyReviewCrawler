#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 7 nov. 2017

:author: Eugenio Martínez Cámara <genimarca@gmail.com>
"""
import sys
import argparse
import logging



def config_parse_dev_mode(parent_args_parser):
    """Configures the DEV mode of the script.
    
    The DEV mode allows to print log messages.
    
    Args:
        parent_args_parser: An instance of ArgumentParser that 
            represents the main input parser of the script.
            
    Returns:
        A instance of ArgumentParser with the parser for the DEV. mode
        of the script.
    """
    
    args_parser_dev = parent_args_parser.add_subparsers(title="Arguments for DEV. mode",
                                      description="If you use the DEV mode you can use additional commands",
                                      help="Read the help for the DEV. mode")
    
    args_parser_dev_logging = args_parser_dev.add_parser("logging")
    log_level_help_msg = "The level of the logging option. Valid values:"
    log_level_help_msg += " ERROR, WARNING, INFO, DEBUG, NOTSET"
    args_parser_dev_logging.add_argument("--log-level", default="NOTSET",
                             choices=["ERROR", "WARNING", "INFO", "DEBUG", "NOTSET"],
                             help=log_level_help_msg,
                             dest="log_level")
    args_parser_dev_logging.add_argument("--log-file", help="The path of the logging file.",
                             dest="log_file")
    return parent_args_parser
    
    

def config_parse_input_args():
    """Configures the parser of the input of the script.
    
    Args:
        input_arguments: A list of strings representing the arguments
            of the script. It must not include the name of the program. 
    Returns:
        An ArgumentParser object configured for parsing the input of the
        review_crawler.py.
    """
    
    args_parser = argparse.ArgumentParser(prog="review_crawler", 
                                          description="Script for the crawling of reviews from the Internet.", 
                                          epilog="Happy of helping you.")
    args_parser.add_argument("-v", "--version", action="version", 
                             version="%(prog)s 1.0")
    args_parser.add_argument("-w", "--web-source", default="tripadvisor", 
                             choices=["tripadvisor"], 
                             help="Name in lower case of the web site of the reviews.",
                             dest="web_source")
    args_parser.add_argument("-c", "-conf-file",
                             help="Path of the configuration file",
                             dest="conf_file")
    args_parser.add_argument("-t", "--output-template", default="csv",
                             help="Template/format of the output file",
                             dest="output_template")
    args_parser.add_argument("-o", default="stdout",
                             help="Path of the output.",
                             dest="output_path")
    args_parser.add_argument("--verbose", action="store_true",
                             help="Activate verbose mode.",
                             dest="verbose")
    return args_parser
    

def config_logging(logging_level, logging_file=None):
    """Configuration of the logging of the script.
    
    Args:
        logging_level: A string representing the level of the logging.
        logging_file: A string representing the path of the logging file.
    """
    logging_level_id = 0
    if logging_level:
        logging_level_id = getattr(logging, logging_level)
    if logging_file:
        logging.basicConfig(level=logging_level_id, filename=logging_file, filemode="w")
    else:
        logging.basicConfig(level=logging_level_id)

def script_controller():
    """The controller of the script
    """
    
    input_args_parser = config_parse_input_args()
    input_args_parser = config_parse_dev_mode(input_args_parser)
    input_args = input_args_parser.parse_args(sys.argv[1:])
    if getattr(input_args, "log_level", None) is not None:
        config_logging(input_args.log_level, input_args.log_file)
        
    print("***BEGIN***")
#    script_model = ModelReviewCrawler()
#    script_model.initialize(PROPERTIESFILE=input_args.conf_file, VERBOSEMODE=input_args.verbose)
#    script_model.run_crawler()
    print("***END***")


if __name__ == '__main__':
    script_controller()