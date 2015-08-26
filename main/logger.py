#!/usr/bin/env python
# encoding:utf-8
 
# Copyright (C) 2010-2015 Magima Co Ltd. All rights reserved.
#
# @description
#
# @file           logger.py
# @author         0294
# @created date   2015-01-20 11:42
# @version        1.0
 
import logging, sys

from OrchestratorConfig import LOGLEVEL
from colors import red

class Logger(object):
    
    def __init__(self, loggerName , logFile, globalLogLevel):

        self.__logFile = logFile
        self.__logFileMaxSize = None
        self.__loggerName = loggerName
        
        # create logger obj
        self.__logger = logging.getLogger(self.__loggerName)

        if globalLogLevel == LOGLEVEL[0]:
            self.__logger.setLevel(logging.DEBUG)
        elif globalLogLevel == LOGLEVEL[1]:
            self.__logger.setLevel(logging.INFO)
        elif globalLogLevel == LOGLEVEL[2]:
            self.__logger.setLevel(logging.WARN)
        elif globalLogLevel == LOGLEVEL[3]:
            self.__logger.setLevel(logging.ERROR)
        else:
            print red('log level :{logLevel} set error!'.format(logLevel = globalLogLevel))
            sys.exit()

        self.__fileHandler = logging.FileHandler(self.__logFile)
        self.__fileHandler.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s  %(name)s  %(levelname)s: %(message)s')
        self.__fileHandler.setFormatter(formatter)
        self.__logger.addHandler(self.__fileHandler)

    def addLog(self, message, logLevel):

        if logLevel == LOGLEVEL[0]:
            self.__logger.debug(message)
        elif logLevel == LOGLEVEL[1]:
            self.__logger.info(message)
        elif logLevel == LOGLEVEL[2]:
            self.__logger.warn(message)
        elif logLevel == LOGLEVEL[3]:
            self.__logger.error(message)
        else:
            print red('you arg logLevel: {level} is not valid!'.format(level = logLevel))
            
    def __del__(self):
        pass
    
if __name__ == '__main__':
    logger = Logger('mylog', 'test.log', 'INFO')
    logger.addLog('hidsdsdhjksjd', 'INFO')

