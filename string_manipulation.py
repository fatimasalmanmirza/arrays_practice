#!/bin/python3


import math
import os
import random
import re
import sys


#Complete the makeAnagram function in the editor below.
# It must return an integer representing the minimum total characters 
#that must be deleted to make the strings anagrams.
def freq(a):
    f_table = {}
    for i in a:
        if i in f_table:
            f_table[i] += 1
        else:
            f_table[i] = 1
    return f_table

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    dict_a = freq(a)
    dict_b = freq(b)

    for k,a_val in dict_a.items():
        if k in dict_b:
            b_val = dict_b[k]
            min_val = min(a_val, b_val)
            dict_a[k] -= min_val
            dict_b[k] -= min_val


    s_sum = sum(dict_a.values())
    l_sum = sum(dict_b.values())
    return s_sum + l_sum

if __name__ == '__main__':
    a = 'fcrxzwscanmligyxyvym'
    b = 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'

    res = makeAnagram(a, b)
    print(res)