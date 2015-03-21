#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright  2014 ray.huang <ray.huang@ray-gii-rmbp>
#
# Distributed under terms of the MIT license.

"""
test use disct to retrive db data 
"""
import MySQLdb
import MySQLdb.cursors
import ConfigParser
import string, os, sys

cf = ConfigParser.ConfigParser()
cf.read("./config.ini")
status = cf.get( "status","status" )
queriedstatus = status.split( ',' )
#queriedstatus = tuple((status[0])[1])
statusDict = {}
for i in range( len( queriedstatus )):
    statusDict[queriedstatus[ i ]] = 0 
print statusDict
db = MySQLdb.connect( host = 'localhost', user = 'root', passwd = '', cursorclass = MySQLdb.cursors.DictCursor)
cursor = db.cursor( MySQLdb.cursors.DictCursor )
cursor.execute( ' show status ;' )
rs = cursor.fetchall()
#print type(rs1)
#for row in rs:
#    print row
#for temp1 in queriedstatus:
#    print temp1
#print type(queriedstatus)
for row in  rs :
    if statusDict.has_key( row.get("Variable_name") ):
        print row.get( "Variable_name" ), row.get( "Value" )
         
cursor.close()
db.close()
