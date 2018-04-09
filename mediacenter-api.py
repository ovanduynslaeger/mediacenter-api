#!flask/bin/python
import os;
from flask import Flask, jsonify
from subprocess import call

app = Flask(__name__)

@app.route('/mediacenter/<string:cmd>', methods=['GET'])
def mediaCenter(cmd):
    os.environ['DISPLAY'] = ":0.0"
    if cmd == 'start':
        ret = callMethod('mediacenter/'+cmd,['ls', '-l'])
        return ret
    if cmd == 'stop':
        ret = callMethod('mediacenter/'+cmd,['ls', '-l'])
        return ret

def callMethod(api,method):
    try:    
        ret = call(method)
        if ret != 0:
         if ret < 0:
             return jsonify({'api': api, 'return': {'status': 'err', 'code': -ret, 'message': 'Killed by signal'}})
         else:
             return jsonify({'api': api, 'return' : {'status': 'err', 'code': ret, 'message': 'Command failed with return code'}})
        else:
             return jsonify({'api': api, 'return' : { 'status':'ok'} } )
    except:
     return jsonify({'api': api, 'return': {'status': 'err', 'code': '-1', 'message': 'Exception'}})

if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))

    