'''
Created on Jul 3, 2012

@author: wni
'''
import logging
#from UpgModelException import UpgradeModelException as UME

class Logger(object):
    """
    This class is used to create a logger for logging purpose
    Return: logger
    """
    def __init__(self,name,logfile,baselevel):
        '''
        Init()
        '''
        self.name = name
        self.logfile = logfile
        self.baselevel = baselevel        
    
    def createLogger(self):
        """
        Create a logger
        Returns: logger instance
        """
        logger = logging.getLogger(self.name)
        logger.setLevel(self.baselevel)
        fh = logging.FileHandler(self.logfile)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(lineno)d - %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger
    
    @staticmethod
    def createRotateLogger(name,logfile,block=1048576,num=10,baselevel=logging.DEBUG):
        import logging.handlers
        fh = logging.handlers.RotatingFileHandler(logfile, 'a', block, num)
        #logging.handlers.r
        logger = logging.getLogger(name)
        logger.setLevel(baselevel)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(lineno)d - %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        logger.propagate = False
        return logger

pub_logger = Logger.createRotateLogger('weixinlogger', 'logs/weixin.log')

def logAndRaise(level,message='log and raise here'):
    pub_logger.log(level, message)
    raise UME(message)

def logAndPrint(logger,level,message):
    logger.log(level, message)
    print message

def getorcreatelogger(loggers,name):
    if name in loggers:
        return loggers[name]
    else:
        logger = Logger.createRotateLogger(name, '../logs/%s.log' % name)
        return logger
     
       
