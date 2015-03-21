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


conn = MySQLdb.connect( host = 'localhost', user = 'root', passwd = 'gree')
curs = conn.cursor()
conn.select_db('mysql')
result1 = curs.execute( 'show global status;')
result2 = curs.fetchall()
for i, j in result2:
    print ' The status %s is: %s' % (i, j)
