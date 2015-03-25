#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright 漏 2015 ray <ray@ray-ubuntu>
#
# Distributed under terms of the MIT license.

"""
test mysql module
"""
import MySQLdb

conn = MySQLdb.connect( host='localhost', user = 'root', passwd = 'gree')

cur = conn.cursor()
result = cur.execute( " show status like 'uptime'; ")
rs = cur.fetchall()

for row in rs:
    print  row
