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
data_dict_low_undumped=dicsfuns.dump_lower_than(data_dict_low, max(data_dict_low.keys())-100, 'testdumpfile.json')
#print(artificial_data_list)