#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 16:21:42 2019
Some miscellaneous functions
@author: andrey
"""
from auxiliardefs import logger_client
def check_dir_writable(path1):
    """
    checks for the path exists and it is writtable
    if not exists creates the dir
    It's easier to ask for forgiveness than for permission
    """
    # Let us first try to write a file in the path:
    # If it suceeds-- delete the file and report True
    # If it fails:
        # If it is for any other reason: report the error
    import os
    try:
        os.makedirs(path1)
    except OSError as e:
        logger_client.info('Directory %s exists. Exception %s should be ignored.', path1, e)
    finally:
        testfile = 'testfile1'
        testfile_with_path = os.path.join(path1, testfile)
        touch(testfile_with_path)
        try:
            fp = open(testfile_with_path)
        except PermissionError as e:
            logger_client.error(e, exc_info=True)
            return False
        except FileNotFoundError as e:
            logger_client.error(e, exc_info=True)
            return False
        else:
            with fp:
                pass
            os.remove(testfile_with_path)
            return True
def touch(filewithpath):
    import os
    with open(filewithpath, 'a'):
        os.utime(filewithpath, None)
        

     
