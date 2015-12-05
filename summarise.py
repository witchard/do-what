#!/usr/bin/env python

import sys
import datetime as d
import pprint


def to_date(date):
    return d.datetime.strptime(date, '%Y-%m-%d:%H:%M:%S')


# Process command line args
if len(sys.argv) < 2:
    print "Usage: proc.py do-what-file [start] [end]"
    sys.exit(1)

file = sys.argv[1]
end = d.datetime.now()
start = end - d.timedelta(1)
if len(sys.argv) > 2:
    start = to_date(sys.argv[2])
if len(sys.argv) > 3:
    end = to_date(sys.argv[3])

# Read app data
apps = {}
total = 0
for line in open(file, 'r').readlines():
    bits = line.strip().split(' ', 1)
    date = to_date(bits[0])
    if date >= start and date <= end:
        try:
            apps[bits[1]] += 1
        except KeyError:
            apps[bits[1]] = 1
        total += 1

# Compute percentages
details = []
for key, value in apps.items():
    details.append( ((float(value) / total)*100, key) )

# Print
for pct, app in sorted(details):
    print "%0.3f %s" % (pct, app)
