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
        hmfs_t = int(l[2])
    with open('/home/viking/HuangKaixin/HMFS-Daisy/pcmapi/demo-test/memdata.txt') as f1:
        l1 = f1.readline().split()
        osnvm_use = int(l1[1])
    t = int(time.time())
    sql = 'insert into nvm_info (time,hmfs,osnvm) value (%s,%s,%s)'%(t,hmfs_use,osnvm_use)
    cur.execute(sql)
    print t,hmfs_use,osnvm_use

while True:
    time.sleep(1)
    getHmfs()

