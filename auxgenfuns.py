#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 15:19:28 2019
Here there are some stupid functions that emulate the data for the application
@author: andrey
"""

def aux_gen_sin_day(x): # sinus of a day length starts at 1 jan 1970
    import math
    day_length = 24*60*60
    return math.sin(x/(day_length*2*math.pi))

def aux_gen_sin_year(x): # sinus of a year length starts at 1 jan 1970
    import math
    year_length = 24*60*60*365
    return math.sin(x/(year_length*2*math.pi))

def aux_gen_ladder_day(x): # ladder of a day length starts at 1 jan 1970
    import math
    day_length = 24*60*60
    return math.floor(x/day_length)/365/10


