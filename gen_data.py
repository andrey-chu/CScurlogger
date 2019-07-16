# -*- coding: utf-8 -*-
"""
This is code that includes function that generates a dataset as a function of
time


"""
# Exception class
class Error(Exception):
    pass
# Class that describes wrong parameters delivered to function
class ArgumentsError(Error):
    pass

def gen_artificial_data(functions, freq, synch, stoptime):
    """
    The function receives a list of the function names 
    the  sampling frequency 
    the boolean 'synch' 
    and stopping time
    """
    import time
    import math

    try:
        cur_time = math.floor(time.time()) #check current time turn into int
        # check that stoptime is not smaller than current time
        if stoptime<cur_time:
            raise ArgumentsError('stoptime is smaller then starttime!') #if not throw the error
            
        #generated_list = generated_list1
        if synch == False: # if asynchrous we will create all the data at once
            generated_list = list()*len(functions)
            args = range(cur_time,stoptime,freq)
            for itertor in range(len(functions)):     #for each function in list
                generated_iterator = map(functions[itertor], args)
                generated_list.append(list(generated_iterator)) 
        else:   # we will create data every (hopefully) second
            generated_list = [[] for i in range(len(functions))]
            for itertor2 in range(cur_time,stoptime,freq):
                
                for itertor in range(len(functions)):     #for each function in list
                    generated_list[itertor].append(functions[itertor](itertor2))
                time.sleep(freq/100)
        return generated_list
    except ArgumentsError as e:
        print(e)
        
