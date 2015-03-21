#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright 漏 2014 ray.huang <ray.huang@ray-gii-rmbp>
#
# Distributed under terms of the MIT license.

"""

"""

import MySQLdb



conn = MySQLdb.connect( host = 'localhost', unix_socket = '/tmp/mysqld5.6.sock',  user = 'root', passwd = '' )
curs = conn.cursor()

def generate_dicts(cur):
    import itertools
    fieldname = [ d[0].lower() for d in cur.description ]
    while True:
        rows = cur.fetchmany()
        if not rows: return
        for row in rows:
            yield dict(itertools.izip(fieldnames, row))


conn.select_db( 'mysql' )
result1 = curs.execute( 'select * from user;' )
result2 = curs.fetchall()
# for i,j  in result2:
#    print 'The status %s is: %s' % (i,j)

for r in generate_dicts(curs):
    print r['Host'], r['User'], r['Password']

conn.close()

