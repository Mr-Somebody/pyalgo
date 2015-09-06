#!/usr/bin/python
#-*- coding: utf-8 -*-
#Author: liujian
#Date: 2015/09/06 17:01:06
#Dec: 


def lcs(a, b):
    """common sub-string
    Args:
    a: string a
    b: string b

    Returns:
    a dict with (i, j) as its key,
    value is the longest sub-string end with a[i] and b[j]
    """
    rmap = {}
    for j in xrange(0, len(b)):
        if a[0] == b[j]:
            rmap[(0, j)] = 1
        else:
            rmap[(0, j)] = 0
    for i in xrange(0, len(a)):
        if a[i] == b[0]:
            rmap[(i, 0)] = 1
        else:
            rmap[(i, 0)] = 0
    for i in xrange(1, len(a)):
        for j in xrange(1, len(b)):
            if a[i] == b[j]:
                rmap[(i, j)] = rmap[(i - 1, j - 1)] + 1
            else:
                rmap[(i, j)] = 0
    return rmap
