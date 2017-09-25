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
 		buffers = int(f.readline().split()[1])
        cache = int(f.readline().split()[1])
    	dram_use = (total-free-buffers-cache)/1024
    	t = int(time.time())
    	sql = 'insert into dram_info (time,dram,dram_total) value (%s,%s)'%(t,dram_use,total)
    	cur.execute(sql)
    	print t,dram_use,total
    	#print 'ok'
while True:
	time.sleep(1)
    	getMem()

