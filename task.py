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
