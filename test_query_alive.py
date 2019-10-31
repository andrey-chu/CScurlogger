#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 15:19:00 2019
Here we check how the data can be generated
@author: andrey
"""


# logging definitions-- in future I want to move it to the configuration file
# the way it is described in https://docs.python.org/3/library/logging.config.html#logging-config-api
# there are two loggers, one for client one for server, one logs in client.log, one in server.log,
# both duplicate into stderr of console howere I have to call them explicitly in function
import logging
import logging.handlers
import temp_sender
log_file_max_size = 1024 * 1024 * 20 # megabytes
log_num_backups = 3

logger_root = logging.getLogger()
logger_root.setLevel(logging.DEBUG)

logger_client = logging.getLogger('Client')
logger_client.setLevel(logging.DEBUG)

logger_server = logging.getLogger('Server')
logger_server.setLevel(logging.DEBUG)


# create a file handler
handler_client = logging.handlers.RotatingFileHandler('Client.log', maxBytes=log_file_max_size, backupCount=log_num_backups)
handler_client.setLevel(logging.DEBUG)
handler_server = logging.handlers.RotatingFileHandler('Server.log', maxBytes=log_file_max_size, backupCount=log_num_backups)
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




result = temp_sender.client_body('192.168.2.189', 65432, 'alivequery')
print(result)
#print(artificial_data_list)