#!/usr/bin/env python

import logging
import logging.handlers

class Logger(object):
    @staticmethod
    def createLogger(name="efoodin",level=logging.DEBUG,fd="general.log"):
        logger = logging.getLogger(name)
        logger.setLevel(level)
        #handler = logging.FileHandler(fd)
        handler = logging.handlers.RotatingFileHandler(fd,'a',1048576*10,20)
        handler.setLevel(level)
        
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.propagate = False
        return logger
    
def checkjsonkey(check_list,jsonobj):
    for item in check_list:
        if item not in jsonobj:
            return False
    return True

#global_logger = Logger.createLogger()
    