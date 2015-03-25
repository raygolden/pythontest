#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright 漏 2015 ray <ray@ray-ubuntu>
#
# Distributed under terms of the MIT license.

"""
Test for mysql replication lag
"""
import MySQLdb

conn = MySQLdb.connect( host = 'localhost', user = 'root', passwd = 'gree' )

curs = conn.cursor()

conn.select_db( 'mysql' )
result1 = curs.execute( "show status like 'uptime';" )
rs = curs.fetchall()
for row in rs:
    print row

