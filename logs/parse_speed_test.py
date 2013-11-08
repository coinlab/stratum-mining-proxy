#!/usr/bin/python
import json
import re
import sys
from subprocess import check_output

def main(filename):
    try:
        stuff = check_output(('tail -n 50000 %s' % filename).split())
        #stuff = open(filename).read()
    except IOError:
        print "unable to open %s" % filename
        return

    comp = re.compile('{.*}')

    all = comp.findall(stuff)


    all_json = [json.loads(x) for x in all]
    all_json = [x for x in all_json if int(x["difficulty"]) > 256]
    all_hashes = [x['hash'] for x in all_json]

    """
    for a in all_json:
        off_by = int(float(int(a['ntime'], 16)) - float(int(a['time'])))
        if off_by < -100:
            print '%6d' % off_by
        elif off_by > 300:
            print '%6d' % off_by
    """
    elapsed = int(float(all_json[-1]['time']) - float(all_json[0]['time']))

    #display_hashes(all_hashes, elapsed)
    return display_counts_64(all_hashes, elapsed)



def display_counts_64(all, elapsed):
    arr = [0] * 256
    total = 0
    win = 0
    garbage = 0
    weird = 0
    for a in all:
        index = int(a[8:10], 16)
        total += 1
        if int(a[0:8], 16) == 0:
            arr[index] += 1
            if int(a[8:10], 16) <= 15:
                win += 1
            else:
                weird += 1
                print a[:8], a[8:10], a[10:]
        else:
            arr[index] += 1
            garbage += 1

    #print_arr(arr)
    print 'win: %d %.2f%%, weird: %d %.2f%%, garbage: %d %.2f%%, total: %d' % (
        win, float(win) / total * 100, weird, float(weird) / total * 100, garbage, float(garbage) / total * 100, total)

    win -= 1
    print 'Time elapsed: %.2f min or %.2f hrs' % (float(elapsed) / 60, float(elapsed) / 3600)
    #print 'gh/s at diff 16: %f' % (float(win) / elapsed * 4.295 * 16,)
    #print 'gh/s at diff 64: %f' % (float(win) / elapsed * 4.295 * 64,)
    #print 'gh/s at diff 256: %f' % (float(win) / elapsed * 4.295 * 256,)
    print 'gh/s at diff 1024: %f' % (float(total) / elapsed * 4.295 * 256,)
    return float(total) / elapsed * 4.295 * 256
"""
    print 'expected speeds: '
    print '96x250: %.2f' % (.25 * 96)
    print '96x500: %.2f' % (.50 * 96)
    print '96x600: %.2f' % (.60 * 96)
    print '256x100: %.2f' % (.1 * 256)
    print '256x250: %.2f' % (.25 * 256)
    print '256x500: %.2f' % (.50 * 256)
    print '256x600: %.2f' % (.60 * 256)
"""

def print_arr(arr):
    for i in xrange(0, len(arr), 4):
        if i == 252:
            print ""
        print '%02x: %4d, %02x: %4d, %02x: %4d, %02x: %4d' % (i, arr[i], i + 1, arr[i + 1], i+2, arr[i+2], i+3, arr[i+3])
        if i == 16 or i == 252:
            print ""


def display_hashes(all, elapsed):
    arr = [0] * 256
    total = 0
    for a in all:
        index = int(a[8:10], 16)
        arr[index] += 1
        print a[:8], a[8:10], a[10:]
        total += 1

    for i in xrange(0, 256):
        print '%02x' % i, arr[i]
    print 'total: %d' % total
    print 'gh/s at diff 1: %f' % (float(total) / elapsed * 4.295,)


if len(sys.argv) < 2:
    print "no args"
    sys.exit(1)

TotalSpeed = 0.0
args = sys.argv[1:]
for arg in args:
    TotalSpeed += main(arg)

print "TotalSpeed:\n%.2f GH/s" % TotalSpeed
