#!/usr/bin/python
#-*- coding: utf-8 -*-
#Author: liujian
#Date: 2015/09/06 18:19:25
#Dec: 


def bisearch(vlist, target, s, e):
    """
    """
    if not vlist:
        return - 1
    e = min(e, len(vlist)) - 1
    s = max(s, 0)
    while s <= e:
        mid = (s + e) / 2
        if vlist[mid] == target:
            return mid
        elif vlist[mid] < target:
            s = mid + 1
        else:
            e = mid - 1
    return -1


def seqsearch(vlist, target, s, e):
    """
    """
    if not vlist:
        return -1
    e = min(e, len(vlist)) - 1
    s = max(s, 0)
    while s <= e:
        if target == vlist[s]:
            return s
        s += 1
    return -1


print bisearch([1,2,3,4,5,6,7], 10, 0, 7)
print bisearch([1,2,3,4,5,6,7], 4, 0, 7)
print bisearch([1,2,3,4,5,6,7], 1, 0, 7)
print bisearch([1,2,3,4,5,6,7], 7, 0, 7)


print seqsearch([1,2,3,4,5,6,7], 10, 0, 7)
print seqsearch([1,2,3,4,5,6,7], 4, 0, 7)
print seqsearch([1,2,3,4,5,6,7], 1, 0, 7)
print seqsearch([1,2,3,4,5,6,7], 7, 0, 7)
