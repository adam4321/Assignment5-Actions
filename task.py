"""
CS-362 Assignment 5
Adam Wright

File of functions to test
"""


import math


def firstrun():
    return "success"


def circle_area(radius):
    local = (radius * radius) * math.pi
    return round(local, 6)


def first_last(list):
    out = []
    out.append(list.pop(0))
    out.append(list.pop())
    return out


def two_dates(date1, date2):
    return (date2 - date1).days
