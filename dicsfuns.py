#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 21:47:56 2019
Here come additional functions that treat the data dictonaries
@author: andrey
"""

def is_equal_dics(dic1, dic2):
    """
    in Python 3 you can just compare
    """
    return dic1==dic2

def difference_dics(dic1, dic2):
    return { k : dic1[k] for k in set(dic1) - set(dic2) }

def union_dics(dic1, dic2):
    return {**dic1, **dic2}

def lower_than_key(dic1, thresh):
    return { k : v for (k,v) in dic1.items() if k<thresh }

def higher_or_eq_than_key(dic1, thresh):
    return { k : v for (k,v) in dic1.items() if k>=thresh }

def dump_lower_than(dict1, thresh, filename):
    """
    The function dumps the part of the dictionary that is lower than the 
    given threshold to the file and returns the part without it in 
    a new dictionary
    """
    import json
    to_dump = lower_than_key(dict1, thresh)
    to_leave = higher_or_eq_than_key(dict1, thresh)
    with open(filename, 'w') as fp:
        json.dump(to_dump, fp)
        return to_leave
    
def load_dic_from_json(filename):
    import json
    with open(filename, 'r') as fp:
        dict1=json.load(fp)
        return dict1
    
def append_lower_than(dict1, thresh, filename):
    """
    The function appends the part of the dictionary that is lower than the 
    given threshold to the file and returns the part without it in 
    a new dictionary
    """
    import json
    with open(filename, 'r') as fp:
        dict2=json.load(fp)
        u_dict1_dict2 = union_dics(dict1, dict2)
    dump_lower_than(u_dict1_dict2, thresh, filename)