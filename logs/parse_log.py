import re
import json

pat = re.compile('{.*}')

samples = pat.findall(open('parsed.log').read())

samples = [json.loads(x) for x in samples]

MAX_LULL = 60

while True:
    sections = []
    for i in xrange(0, len(samples) - 2):
        if samples[i + 1]['time'] - samples[i]['time'] > MAX_LULL:
            sections.append(samples[:i + 1])
            samples = samples[i + 1:]
            break

    sections.append(samples[:i + 1])
    samples = samples[i + 1:]



