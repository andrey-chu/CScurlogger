#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 18:03:37 2019
Aux functions for server, maybe I will include them in the class as methods
@author: andrey
"""
def data_is_complete1(data):
    return data['recordsnum'] == len(data['content']['value']) and data['recordsmax'] == max(data['content']['value']) and data['recordsmin'] == min(data['content']['value'])
def data_is_complete(data, recordsnum, recordsmax, recordsmin):
    print('Received data: length is',len(data), ', max ', max(data), 'min ', min(data))
    print('Received data info: length is',recordsnum, ', max ', recordsmax, 'min ', recordsmin)
    is_complete= recordsnum == len(data) and recordsmax == int(max(data)) and recordsmin == int(min(data))
    print(f'Will return {is_complete}')
    return recordsnum == len(data) and recordsmax == int(max(data)) and recordsmin == int(min(data))
