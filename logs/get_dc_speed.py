#!/usr/bin/python

import re
import datetime
import time
from subprocess import call

import save_logs

date_len = len('2014-01-09 17:01:29')

def get_share_diff(line):
    try:
        diff = int(line[-5:-1])
        #print "Get share diff: %d" % diff
        return diff
    except Exception, e:
        print "Get share diff exception, %s, returning 0" % e
        return 0

def floor_hour(timestamp):
    return (int(timestamp) / 3600) * 3600

def epoch_from_human_time(date_str):
    return int(time.mktime(time.strptime(date_str, '%Y-%m-%d %H:%M:%S')))

def human_time_from_epoch(timestamp):
    return datetime.datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M')

def human_date_from_epoch(timestamp):
    return datetime.datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d')

def find(f, d):
    for line in f:
        if 'accepted' not in line:
            continue

        #print line,
        date_str = line[:date_len]
        #print date_str
        timestamp = epoch_from_human_time(date_str)
        #print timestamp
        timestamp = floor_hour(timestamp)
        #print timestamp
        #date_str = human_time_from_epoch(timestamp)
        #print date_str

        diff = get_share_diff(line)

        if timestamp not in d:
            d[timestamp] = 0

        d[timestamp] += diff
        #print diff

    f.close()


def main(possible_files, output_filename):
    d = {}
    for filename in possible_files:
        try:
            f = open(filename)
            find(f, d)
            print "Done with %s" % filename
        except IOError:
            pass

    try:
        old = [x for x in open(output_filename).read().split('\n') if len(x) > 0]
    except IOError, e:
        old = []
        print "Error opening %s: %s" % (output_filename, e)

    for line in old:
        line = line.split(',')
        timestamp = int(line[1])
        shares = int(line[2])
        if timestamp in d:
            d[timestamp] += shares
        else:
            d[timestamp] = shares

    sorted_keys = sorted(d.keys())
    s = ''
    for k in sorted_keys:
        s += "%s,%d,%d,%f\n" % (human_time_from_epoch(k), k, d[k], (float(d[k]) * 4.295) / 3600000)
        #print "%s, shares: %d, TH/s: %f" % (human_time_from_epoch(k), d[k], (float(d[k]) * 4.295) / 3600000)

    open('%s_%s' % (human_date_from_epoch(int(time.time())), output_filename), 'w').write(s)
    open(output_filename, 'w').write(s)


def init():
    output_filename = '%s_dc_speed.csv' % (open('/etc/hostname').read().replace('\n', ''))
    print "output_filename: %s" % output_filename

    possible_files = []

    for i in xrange(0, 200):
        for j in xrange(0, 100):
            possible_files.append('d%d.log.%d' % (i, j))
            possible_files.append('w%d.log.%d' % (i, j))
            possible_files.append('s%d.log.%d' % (i, j))

    main(possible_files, output_filename)

    for i in xrange(0, 200):
        for j in xrange(0, 10):
            remove('d%d.log.%d' % (i, j))
            remove('w%d.log.%d' % (i, j))
            remove('s%d.log.%d' % (i, j))


def remove(filename):
    try:
        open(filename).close()
        call(('rm %s' % filename).split())
    except IOError:
        pass


init()
