#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 16:21:42 2019
Some miscellaneous functions
@author: andrey
"""
def check_dir_writable(path1):
    """
    checks for the path exists and it is writtable
    if not exists creates the dir
    It's easier to ask for forgiveness than for permission
    """
    # Let us first try to write a file in the path:
    # If it suceeds-- delete the file and report True
    # If it fails: analyse the errors:
        # If it because the directory does not exist: create and try again
        # If it is for the other reason: report the error
    import os
    testfile = 'testfile'
    testfile_with_path = os.path.join(path1, testfile)
    try:
        fp = open(testfile_with_path)
    except PermissionError as e:
        print(e)
    else:
        with fp:
            return fp.read()
