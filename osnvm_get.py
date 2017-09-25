#!/usr/bin/python
#-*- coding: UTF-8 -*-
import time
import MySQLdb as mysql

db = mysql.connect(user="root",passwd="123456",db="memory",host="localhost")
db.autocommit(True)
cur = db.cursor()

def getOsnvm():
    with open('/home/viking/HuangKaiXin/HMFS-Daisy/pcmapi/demo-test/memdata.txt') as f:
        osnvm_use = int(f.readline().split()[1])
    t = int(time.time())
    sql = 'insert into osnvm_info (time,osnvm) value (%s,%s)'%(t,osnvm_use)
    cur.execute(sql)
    print t,osnvm_use
        #print 'ok'
while True:
    time.sleep(1)
    getOsnvm()

