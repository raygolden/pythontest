#!/usr/bin/env python
from checksum import create_checksum
from diskwalk_api import diskwalk
from os.path import getsize

def findDupes( path = '/tmp'):
    dup = []
    record = {}
    d = diskwalk(path)
    files = d.enumreatePaths()
    for file in files:
        compound_key = (getsize(file), create_checksum(file))
        if compund_key in record:
            dup.append(file)
        else:
            record[compound_key] = file
    return dup

if __name__ == "__main__":
    dupes = findDupes()
for dup in dupes:
    print "Duplicate: %s" % dup


