#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 00:09:04 2019
Auxilliar definitions: exceptions and logging
@author: andrey
"""

# Exception class
class Error(Exception):
    pass
# Class that describes wrong parameters delivered to function
class ArgumentsError(Error):
    pass

# logging definitions-- in future I want to move it to the configuration file
# the way it is described in https://docs.python.org/3/library/logging.config.html#logging-config-api

import logging
logger_client = logging.getLogger(__name__)
logger_client.setLevel(logging.DEBUG)

logger_server = logging.getLogger(__name__)
logger_server.setLevel(logging.DEBUG)


# create a file handler
handler_client = logging.FileHandler('Client.log')
handler_client.setLevel(logging.DEBUG)
handler_server = logging.FileHandler('Server.log')
handler_client.setLevel(logging.DEBUG)
handler_consolehandler = logging.StreamHandler
handler_consolehandler.setLevel(logging.DEBUG)


# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler_client.setFormatter(formatter)
handler_server.setFormatter(formatter)
# add the handlers to the logger
logger_client.addHandler(handler_client)
logger_client.addHandler(handler_consolehandler)

logger_server.addHandler(handler_server)
logger_server.addHandler(handler_consolehandler)

