"""
Program: half_birthday.py
Author: Cara Krug cjkrug@dmacc.edu
Last date modified: 10/19/2020
Purpose: demonstrate the use of DateTime
"""
import datetime


def half_birthday(date):
    """
    Description: calculate the next half birthday from provided date
    :param date: this will be the birthday datetime object
    :returns: return half-birthday datetime object
    :raises
    """
    return date + datetime.timedelta(days=182)


if __name__ == '__main__':
    pass
