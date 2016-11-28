#!/usr/bin/env python
# coding=utf-8

import os
import sys
import fileinput

SUPPORT_POSTFIX = ["K", "M", "G", "T", "P"]
KB_VALUE = 1024
MB_VALUE = 1024 * 1024
GB_VALUE = 1024 * 1024 * 1024
TB_VALUE = 1024 * 1024 * 1024 * 1024
PB_VALUE = 1024 * 1024 * 1024 * 1024 * 1024


def convertToByte(unit):
    byteValue = 0;
    postFix = unit[-1:].upper()
    rawValue = float(unit[:-1])
    if not postFix in SUPPORT_POSTFIX:
        print "unsupport unit", unit, "skip it!"
    if postFix == "K":
        byteValue = rawValue * KB_VALUE
    elif postFix == "M":
        byteValue = rawValue * MB_VALUE
    elif postFix == "G":
        byteValue = rawValue * GB_VALUE
    elif postFix == "T":
        byteValue = rawValue * TB_VALUE
    elif postFix == "P":
        byteValue = rawValue * PB_VALUE
    return byteValue

if __name__ == "__main__":
    byteValues = []

    # see more stdin on http://stackoverflow.com/questions/1450393/how-do-you-read-from-stdin-in-python
    # convert each
    for line in fileinput.input():
        # strip trailing spaces
        line = line.strip()
        # print the processing data
        print "Processing ", line
        byteValue = convertToByte(line)
        byteValues.append(byteValue)

    # calculate total
    totalBytes = reduce(lambda x,y: x + y, byteValues)
    print "Total bytes is {totalBytes} bytes, or {totalKB} KB, or {totalMB} MB, or {totalGB} GB, or {totalTB} TB, or {totalPB} PB".format(
        totalBytes=totalBytes,
        totalKB=totalBytes / MB_VALUE,
        totalMB=totalBytes / MB_VALUE,
        totalGB=totalBytes / GB_VALUE,
        totalTB=totalBytes / TB_VALUE,
        totalPB=totalBytes / PB_VALUE
    )
