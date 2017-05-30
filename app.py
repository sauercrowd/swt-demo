from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
import time 
import redis

r = redis.Redis(host='redis',port=6379)

import socket
ip = socket.gethostname()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',name=str(ip))

@app.route('/note',methods=['GET','POST'])
def note():
    if request.method == 'POST':
        request.get_data()
        note = request.data
        uid = 'x'
        if 'uid' not in request.cookies:
            resp = make_response('not set')
            uid = str("%.20f" % time.time())
            resp.set_cookie('uid',uid)
            print("UID: "+uid)
        else:
            uid = request.cookies['uid']
        setNote(uid,note)
        return 'ok'
    else:
        if 'uid' in request.cookies:
            res = getNote(request.cookies['uid'])
            if res == None:
                return ''
            return res
        else:
            return ''


@app.route('/set')
def set(uid):
    r.set('foo','bar')
    value = r.get('foo')
    print(value)
    return value


def setNote(uid, note):
    r.set(uid,note)

def getNote(uid):
    return r.get(uid)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)
