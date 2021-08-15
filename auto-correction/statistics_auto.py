#!/usr/bin/env python3

#Useful imports
import math
import numpy as np

#Statistic script for csv form auto-correction
def statistics(userlist):
    assert type(userlist) is list, 'userlist is not list'
    raw_points = []
    for user in userlist:
        for key in user:
            raw_points.append(user[key])
    arr = np.array(raw_points,dtype = float)
    mean = np.mean(arr)
    med = np.median(arr)
    var = np.var(arr, ddof=1)
    std_dev = np.std(arr,ddof=1)
    return "Mean = "+ str(mean), " Mediane = ", str(med),  " Variance = ", str(var) ," Standard deviation = ", str(std_dev)
