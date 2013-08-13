import re
import json

pat = re.compile('{.*}')

samples = pat.findall(open('parsed.log').read())

samples = [json.loads(x) for x in samples]

MAX_LULL = 60

sections = []

while len(samples) <= 1:
    for i in xrange(0, len(samples) - 2):
        if samples[i + 1]['time'] - samples[i]['time'] > MAX_LULL:
            sections.append(samples[:i + 1])
            samples = samples[i + 1:]
            break

    sections.append(samples[:i + 1])
    samples = samples[i + 1:]

"2013-07-30 19:53:48,687 INFO proxy jobs.gen_message # right here, time 1375214028.69, target 00000000ffff0000000000000000000000000000000000000000000000000000, hash 0000000004fd0c8f57a1c1d45e6d2d82d5f614fb773c8e4739d2a805def810f8, ntime 51F81989, nonce 098AE810, error None"

for section in sections:
    print "start: %s, end: %s" % (section[0][:25], section[:1][0][:25])

