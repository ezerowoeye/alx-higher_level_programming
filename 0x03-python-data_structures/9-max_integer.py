#!/usr/bin/python3
def max_integer(my_list=[]):
    max_num = None
    if len(my_list) == 0:
        return (None)
    else:
        for i in my_list:
            if (max_num is None or  i > max_num):
                max_num = i
    return(max_num)
