from flask import Flask,render_template,request
import MySQLdb as mysql

con = mysql.connect(user='root',passwd='123456',host='localhost',db='memory')

con.autocommit(True)
cur = con.cursor()
app = Flask(__name__)
import json

@app.route('/')
def index():
    return render_template('index.html')

tmp_time1 = 0
@app.route('/dram_use')
def dram_use():
    global tmp_time1
    if tmp_time1>0:
        sql = 'select dram,time from dram_info where time>%s' % (tmp_time1/1000)
    else:
        sql = 'select dram,time from dram_info'
    cur.execute(sql)
    arr = []
    for i in cur.fetchall():
        arr.append([i[1]*1000,i[0]])
    if len(arr)>0:
        tmp_time1 = arr[-1][0]
    return json.dumps(arr)

tmp_time2 = 0
@app.route('/nvm_use')
def nvm_use():
    global tmp_time2
    if tmp_time2>0:
        sql = 'select hmfs,osnvm,time from nvm_info where time>%s' % (tmp_time2/1000)
    else:
        sql = 'select hmfs,osnvm,time from nvm_info'
    cur.execute(sql)
    arr = []
    for i in cur.fetchall():
        arr.append([i[2]*1000,i[0]+i[1]])
    if len(arr)>0:
        tmp_time2 = arr[-1][0]
    return json.dumps(arr)

if __name__=='__main__':
    app.run(host='0.0.0.0',port=9092,debug=True)

