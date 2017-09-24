from flask import Flask,render_template,request
import MySQLdb as mysql

con = mysql.connect(user='root',passwd='Make8868',host='localhost',db='memory')

con.autocommit(True)
cur = con.cursor()
app = Flask(__name__)
import json

@app.route('/')
def index():
    return render_template('index.html')

tmp_time1 = 0
@app.route('/mem_use')
def mem_use():
    global tmp_time1
    if tmp_time1>0:
        sql = 'select memuse,time from mem_info where time>%s' % (tmp_time1/1000)
    else:
        sql = 'select memuse,time from mem_info'
    cur.execute(sql)
    arr = []
    for i in cur.fetchall():
        arr.append([i[1]*1000,i[0]])
    if len(arr)>0:
        tmp_time1 = arr[-1][0]
    return json.dumps(arr)

tmp_time2 = 0
@app.route('/free')
def free():
    global tmp_time2
    if tmp_time2>0:
        sql = 'select free,time from mem_info where time>%s' % (tmp_time2/1000)
    else:
        sql = 'select free,time from mem_info'
    cur.execute(sql)
    arr = []
    for i in cur.fetchall():
        arr.append([i[1]*1000,i[0]])
    if len(arr)>0:
        tmp_time2 = arr[-1][0]
    return json.dumps(arr)

tmp_time3 = 0
@app.route('/buffers')
def buffers():
    global tmp_time3
    if tmp_time3>0:
        sql = 'select buffers,time from mem_info where time>%s' % (tmp_time3/1000)
    else:
        sql = 'select buffers,time from mem_info'
    cur.execute(sql)
    arr = []
    for i in cur.fetchall():
        arr.append([i[1]*1000,i[0]])
    if len(arr)>0:
        tmp_time3 = arr[-1][0]
    return json.dumps(arr)

tmp_time4 = 0
@app.route('/cache')
def cache():
    global tmp_time4
    if tmp_time4>0:
        sql = 'select cache,time from mem_info where time>%s' % (tmp_time4/1000)
    else:
        sql = 'select cache,time from mem_info'
    cur.execute(sql)
    arr = []
    for i in cur.fetchall():
        arr.append([i[1]*1000,i[0]])
    if len(arr)>0:
        tmp_time4 = arr[-1][0]
    return json.dumps(arr)


if __name__=='__main__':
    app.run(host='0.0.0.0',port=9092,debug=True)

