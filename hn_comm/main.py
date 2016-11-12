# coding=GBK
'''
Created on Jul 3, 2016

@author: stanley
'''
import sys
import time

if __name__ == '__main__':
    #if len(sys.argv) != 2:
    #    print "Usage python main.py data"
    #    sys.exit(-1)
    #f = open(sys.argv[1], 'r')
    f = open("shop_hn_161003.txt", 'r')

    line = f.readline()
    ISOTIMEFORMAT = '%Y-%m-%d %X'
    cnt = 0
    print "%s" % (time.strftime(ISOTIMEFORMAT, time.localtime()))
    while line != "":
        line = f.readline()

        # if(cnt>10000):
        #    break
        cols = line.split("\t")
        print len(cols)
        if len(cols) != 14:
            continue
        cnt += 1
        #print cols[0], cols[1]
    print cnt
    print "%s" % (time.strftime(ISOTIMEFORMAT, time.localtime()))
    pass
