#!/usr/bin/python

for i in range(1,20):
    # do we need to print i?
    NeedToPrint = True
    # if i is divisible by 3, then print buzz
    if (i % 3 == 0):
        print "buzz",
        NeedToPrint = False
    # if i is divisible by 5, then print fizz
    if (i % 5 == 0):
        print "fizz",
        NeedToPrint = False
    if (NeedToPrint):
        print i, 
    print 
