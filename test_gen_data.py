#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 15:19:00 2019
Here we check how the data can be generated
@author: andrey
"""

import auxgenfuns
import time
import gen_data
import math
funclist = [auxgenfuns.aux_gen_sin_day,auxgenfuns.aux_gen_sin_year,auxgenfuns.aux_gen_ladder_day]
freq = 1
synchr = True
stoptime = math.floor(time.time()+60*60)         #1 hour
artificial_data_list = gen_data.gen_artificial_data(funclist, freq, synchr, stoptime)

#print(artificial_data_list)