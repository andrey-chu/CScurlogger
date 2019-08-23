#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 15:19:00 2019
Here we check how the data can be generated
@author: andrey
"""

import auxgenfuns
import dicsfuns
import time
import gen_data
import math
import miscfuns
import os

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



funclist = [auxgenfuns.aux_gen_sin_workday,auxgenfuns.aux_gen_sin_year,auxgenfuns.aux_gen_ladder_day]
dumpfiles_dir = 'dumpfiles'
logfiles_dir = 'logs'
miscfuns.check_dir_writable(dumpfiles_dir)
freq = 1
synchr = False
stoptime = math.floor(time.time()+60*60)         #1 hour
artificial_data_dict= gen_data.gen_artificial_data(funclist, freq, synchr, stoptime)
starttime = math.floor(time.time()+60*30)         #1 hour
stoptime = math.floor(time.time()+60*90)         #1 hour
artificial_data_dict_later= gen_data.gen_artificial_data(funclist, freq, synchr, stoptime, starttime)
data_dict_union = dicsfuns.union_dics(artificial_data_dict, artificial_data_dict_later)
data_dict_low = dicsfuns.lower_than_key(data_dict_union, starttime-1000)
data_dict_high = dicsfuns.higher_or_eq_than_key(data_dict_union, starttime-1000)
data_dict_low_undumped=dicsfuns.dump_lower_than(data_dict_low, max(data_dict_low.keys())-100, os.path.join(dumpfiles_dir, 'testdumpfile.json'))
keysnum = len(data_dict_low_undumped)
maxkey=max(data_dict_low_undumped)
minkey=min(data_dict_low_undumped)
result = temp_sender.client_body('127.0.0.1', 65432, 'sendtext', data_dict_low_undumped, keysnum, maxkey, minkey)
print(result)
#print(artificial_data_list)