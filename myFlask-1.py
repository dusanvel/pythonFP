from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/hello')
def hello_world():
    time = datetime.now()
    pageHtml='<h1>System Date and time Flask test</h1>'\
    '<h3> Poziv python dateTime.now komande: </h3>' + str(time) +\
    '<h5> Jos jednom time:</h5>' + str(time) +\
    '<h2> <a href= http://192.168.1.101:8090> Back to Main</a> </h2>'
    return (pageHtml)

@app.route('/time')
def getTime():
    time = datetime.now()
    return "RPI3 date and time: " + str(time)
#    <h3> <a href= http://192.168.1.101:8090/hello> Click for time</a> </h3>
@app.route('/')
def hello_home():
    pageHtml='<h1>Main Menu</h1>'\
    '<h2><font color="red">Proof of concept</font></h2>'+\
    '<h3> <a href= http://192.168.1.101:8090/hello> 1) Python DateTime FLASK test</a> </h3>' +\
    '<h3> <a href= http://192.168.1.101:8090/time> 2) Click for time (sirovo)-RAW</a> </h3>' +\
    '<h5> <font color="green"> Project by Dusan & Oliver</font></h5>'
    
    return (pageHtml)
app.run(host='0.0.0.0', port= 8090)
