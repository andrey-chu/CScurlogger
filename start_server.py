#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 13:14:37 2019
Start server module
@author: andrey
"""

import logging
from logging.handlers import RotatingFileHandler
from test_server import test_server1
log_file_max_size = 1024 * 1024 * 20 # megabytes
log_num_backups = 3

logger_root = logging.getLogger()
logger_root.setLevel(logging.DEBUG)

logger_client = logging.getLogger('Client')
logger_client.setLevel(logging.DEBUG)

logger_server = logging.getLogger('Server')
logger_server.setLevel(logging.DEBUG)


# create a file handler
handler_client = RotatingFileHandler('Client.log', maxBytes=log_file_max_size, backupCount=log_num_backups)
handler_client.setLevel(logging.DEBUG)
handler_server = RotatingFileHandler('Server.log', maxBytes=log_file_max_size, backupCount=log_num_backups)
handler_client.setLevel(logging.DEBUG)
handler_consolehandler = logging.StreamHandler()
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

"""
There is a problem here, I want to choose logger in the function depending on what executable
was it called from Client or Server in this way it does not allow it-----> find solution 
"""


data = test_server1()