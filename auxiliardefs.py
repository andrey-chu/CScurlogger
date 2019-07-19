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

