#!/usr/bin/python

for i in range(1,100):
    if (i % 2 == 0 and i % 5 == 0):
        print "easy peasy"
        continue
    if (i % 2 == 0):
        print "easy"
        continue
    if (i % 5 == 0):
        print "peasy"
        continue
    print i
