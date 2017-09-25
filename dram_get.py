#!/usr/bin/python
#-*- coding: UTF-8 -*-
import time
import MySQLdb as mysql

db = mysql.connect(user="root",passwd="123456",db="memory",host="localhost")
db.autocommit(True)
cur = db.cursor()

def getMem():
	with open('/proc/meminfo') as f:
		total = int(f.readline().split()[1])
        free = int(f.readline().split()[1])
		f.readline()
        	buffers = int(f.readline().split()[1])
        	cache = int(f.readline().split()[1])
    	mem_use = total-free-buffers-cache
    	t = int(time.time())
    	sql = 'insert into mem_info (free,buffers,cache,time,memuse) value (%s,%s,%s,%s,%s)'%(free,buffers,cache,t,mem_use)
    	cur.execute(sql)
    	print free,buffers,cache,t,mem_use
    	#print 'ok'
while True:
	time.sleep(1)
    	getMem()

