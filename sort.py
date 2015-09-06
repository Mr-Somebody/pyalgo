#!/usr/bin/python
#-*- coding: utf-8 -*-
#Author: liujian
#Date: 2015/09/06 11:30:29
#Dec: 


def insert_sort(vlist, s, e):
    """insert sort
    """
    if not vlist:
        return
    cur = s + 1
    while cur < e:
        v = vlist[cur]
        pos = cur - 1
        while pos >= s and vlist[pos] > v:
            vlist[pos + 1] = vlist[pos]
            pos -= 1
        vlist[pos + 1] = v
        cur += 1


def shell_sort(vlist, s, e):
    """shell sort
    """
    if not vlist:
        return
    step = (e - s) / 2
    while step >= 1:
        cur = s + step
        while cur < e:
            v = vlist[cur]
            pos = cur - step
            while pos >= s and vlist[pos] > v:
                vlist[pos + step] = vlist[pos]
                pos -= step
            vlist[pos + step] = v
            cur += 1
        step /= 2


def bubble_sort(vlist, s, e):
    """bubble sort
    """
    if not vlist:
        return
    cur = s
    while cur < e:
        pos = e - 1
        while pos > cur:
            if vlist[pos] < vlist[pos - 1]:
                tmp = vlist[pos - 1]
                vlist[pos - 1] = vlist[pos]
                vlist[pos] = tmp
            pos -= 1
        cur += 1

        
def quick_sort(vlist, s, e):
    """quick sort
    Args:
    vlist: the list to sort
    s: start position
    e: end position

    Returns:
    None
    """
    if not vlist or s >= e - 1:
        return
    low = s
    high = e - 1
    mark = vlist[low]
    while low < high:
        while low < high and vlist[high] >= mark:
            high -= 1
        vlist[low] = vlist[high]
        while low < high and vlist[low] <= mark:
            low += 1
        vlist[high] = vlist[low]
    vlist[high] = mark
    qsort(vlist, s, high)
    qsort(vlist, high + 1, e)


def select_sort(vlist, s, e):
    """select sort
    """
    if not vlist:
        return
    cur = s
    while cur < e:
        pos = cur + 1
        minv = cur
        while pos < e:
            if vlist[pos] < vlist[minv]:
                minv = pos
            pos += 1
        if minv != cur:
            tmp = vlist[cur]
            vlist[cur] = vlist[minv]
            vlist[minv] = tmp
        cur += 1


def heap_sort(vlist, s, e):
    """heap sort
    """
    if not vlist:
        return
    # create heap
    cur = (e - s) / 2 + s
    while cur >= s:
        v = vlist[cur]
        pos = cur
        while pos < e:
            lc = (pos - s) * 2 + s + 1
            rc = lc + 1
            if lc < e and vlist[lc] > v:
                vlist[pos] = vlist[lc]
                pos = lc
            if rc < e and vlist[rc] > vlist[pos]:
                if pos == lc:
                    pos = (pos - s - 1) / 2 + s
                vlist[pos] = vlist[rc]
                pos = rc
            vlist[pos] = v
            if pos == lc or pos == rc:
                continue
            break
        cur -= 1
    # sort
    cur = e - 1
    while cur > s:
        v = vlist[cur]
        vlist[cur] = vlist[s]
        pos = s
        while pos < cur:
            lc = (pos - s) * 2 + s + 1
            rc = lc + 1
            if lc < cur and vlist[lc] > v:
                vlist[pos] = vlist[lc]
                pos = lc
            if rc < cur and vlist[rc] > vlist[pos]:
                if pos == lc:
                    pos = (pos - s - 1) / 2 + s
                vlist[pos] = vlist[rc]
                pos = rc
            vlist[pos] = v
            if pos == lc or pos == rc:
                continue
            break
        cur -= 1


def merge_sort(vlist, s, e):
    """merge sort
    """
    pass


def radix_sort(vlist, s, e):
    """radix sort
    """
    pass
        
a = [0,9,8,7,1,2,4,3,5,7,6]
print 'befor:',a
heap_sort(a, 0, 11)
print 'after:',a
b = [9,8,7,6,5,4,3,2,1,0,0]
print 'befor:',b
heap_sort(b, 0, 11)
print 'after:',b

