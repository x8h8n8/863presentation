#!/usr/bin/python
#-*- coding: UTF-8 -*-
import time
import MySQLdb as mysql

db = mysql.connect(user="root",passwd="123456",db="memory",host="localhost")
db.autocommit(True)
cur = db.cursor()

def getHmfs():
    with open('./hmfs_status.txt') as f:
        l = f.readline().split()
        hmfs_use = int(l[1])
<<<<<<< HEAD
        print hmfs_use
        hmfs_t = int(l[2])
        print hmfs_t
    	t = int(time.time())
    	sql = 'insert into hmfs_info (time,hmfs,hmfs_total) value (%s,%s,%s)'%(t,hmfs_use,hmfs_t)
    	cur.execute(sql)
    	print t,hmfs_use,hmfs_t
    	 #print 'ok'
=======
        hmfs_t = int(l[2])
    t = int(time.time())
    sql = 'insert into hmfs_info (time,hmfs,hmfs_total) value (%s,%s,%s)'%(t,hmfs_use,hmfs_t)
    cur.execute(sql)
    print t,hmfs_use,hmfs_t
        #print 'ok'
>>>>>>> c3200e2704092f17edf907a1276cc28dae7b7323
while True:
    time.sleep(1)
    getHmfs()

