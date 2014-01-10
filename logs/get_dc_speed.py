#!/usr/bin/python

import re
import datetime
import time

date_len = len('2014-01-09 17:01:29')

diff_pat = re.compile('diff\ (\d{1,3})')

def get_share_diff(line):
    try:
        diff = int(diff_pat.findall(line)[0])
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

def find(f, d):
    for line in f:
        if 'accepted' not in line:
            continue

        print line,
        date_str = line[:date_len]
        #print date_str
        timestamp = epoch_from_human_time(date_str)
        #print timestamp
        timestamp = floor_hour(timestamp)
        #print timestamp
        date_str = human_time_from_epoch(timestamp)
        #print date_str

        diff = get_share_diff(line)

        if timestamp not in d:
            d[timestamp] = 0

        d[timestamp] += diff
        print diff, date_str, '\n'

    f.close()


def main(possible_files):
    d = {}
    for filename in possible_files:
        try:
            f = open(filename)
            find(f, d)
        except:
            pass

    sorted_keys = sorted(d.keys())
    print "\n"
    for k in sorted_keys:
        print "%s, shares: %d, GH/s: %f" % (human_time_from_epoch(k), d[k], (float(d[k]) * 4.295) / 3600)


possible_files = []
for i in xrange(0, 200):
    possible_files.append('d%d.log' % i)
    possible_files.append('w%d.log' % i)
    possible_files.append('s%d.log' % i)
    possible_files.append('d%d.log.1' % i)
    possible_files.append('w%d.log.1' % i)
    possible_files.append('s%d.log.1' % i)

main(possible_files)
