"""
Helper functions for k-Means clustering

This file contains the functions for enforcing preconditions for k-means clustering.
We have written the first for you.  You will probably want to write others.

YOUR NAME(S) AND NETID(S) HERE
DATE COMPLETED HERE
"""
import math
import random
import numpy


def is_point(value):
    """
    Returns True if value is a list of int or float

    Parameter value: a value to check
    Precondition: value can be anything
    """
    if (type(value) != list):
        return False
    for x in value:
        if (not type(x) in [int,float]):
            return False
    return True



def is_point_list(value):
    """
    Returns True if value is a 2d list of int or float

    This function also checks that all points in value have same dimension.

    Parameter value: a value to check
    Precondition: value can be anything
    """
    if (type(value) != list):
        return False
    elif (len(value) == 0):
        return True


    dim = len(value[0])
    for x in value:
        if (len(x) != dim or not is_point(x)):
            return False
    return True


def addPoint_helper(self,point):
    """
    Returns True if point is a list of int or float

    This function also checks that the dimension of the point has the same dimension as self

    Parameter self: a dataset
    Precondition: A dataset of like-dimension lists

    Parameter point: a value
    Precondition: value can be anything
    """

    if is_point(point) == True:
        if len(point)== self._dim:
            return True
    else:
        return False

def is_seed_list(value, k, size):
    """
    Returns True if value is k-element list of indices between 0 and 1.

    Parameter value: a value to check
    Precondition: value can be anything

    Parameter k: The required list size
    Precondition: k is an int > 0

    Paramater size: The database size
    Precondition: size is an int > 0
    """
    if (type(value) != list):
        return False
    elif (len(value) != k):
        return False

    okay = True
    for x in value:
        if type(x) != int or x < 0 or x >= size:
            okay = False

    return okay
