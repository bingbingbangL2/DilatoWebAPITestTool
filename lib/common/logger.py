'''
Created on Mar 15, 2016

@author: bxia
'''

import logging
import os, sys
from datetime import datetime

_logger = None
_logDir = None
SCRIPT_NAME = os.path.basename(sys.argv[0])

CONSOLE_LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DEBUGFILE_LOG_FORMAT = "%(asctime)s - %(filename)s:%(module)s:%(lineno)s[%(threadName)s] - %(levelname)s - %(message)s"

#script_name + timestamp
LOG_NAME_FORMAT = '%s-%s.log'
DATE_FORMAT = '%Y-%m-%dT%H-%M-%S'

def setupLogDir(relapath = './log', abspath = None):
    if abspath:
        logDir = abspath
    else:
        logDir = os.path.join(os.getcwd(), relapath)
    _logDir = logDir
    if not os.path.exists(logDir):
        os.makedirs(logDir)
    return logDir

def getLogger(console_level = logging.INFO, logfile_level = logging.DEBUG):
    global _logger
    logger = logging.getLogger(SCRIPT_NAME)
    if logger != _logger:
        _logger = logger;
        logger.setLevel(logging.DEBUG)
        # create console handler
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(console_level)
        ## If user already setup the log dir, use it; or initialize it
        if not _logDir:
            logDir = setupLogDir()
        logName = LOG_NAME_FORMAT % (SCRIPT_NAME, datetime.now().strftime(DATE_FORMAT))
        logfile = os.path.join(logDir, logName)
        # create file handler and set level to DEBUG
        fh = logging.FileHandler(logfile)
        fh.setLevel(logfile_level)
        
        ch.setFormatter(logging.Formatter(CONSOLE_LOG_FORMAT))
        fh.setFormatter(logging.Formatter(DEBUGFILE_LOG_FORMAT))
        
        logger.addHandler(ch)
        logger.addHandler(fh)
    
    return _logger
        
        
if __name__ == '__main__':
    _logger = getLogger()
    _logger.info("INFO")
    _logger.warning("warning")
    _logger.debug("debug")
    _logger.error("error")    