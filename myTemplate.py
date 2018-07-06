from flask import render_template
from flask import Flask
#from app import app
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Ljubisa'}
    posts = [
        {
            'author': {'username': 'Dusan'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Oliver'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',title='Home',  user=user, posts=posts)


@app.route('/g1_cmd')
def g1_cmd():
    cmd_name="getDateTime"
    cmd_xvalue="x67"
    var_status="x80 x85 x80 xBA x80 x8A"
    full_msg="x01 x23 x20 x04 data...x05 BCC x03"
    return render_template('g1CMD.html'  , varStatus=var_status, cmdName=cmd_name, cmdXvalue=cmd_xvalue, fullMsg=full_msg)
@app.route('/g2_cmd')
def g2_cmd():

    return render_template('g2CMD.html')
@app.route('/g3_cmd')
def g3_cmd():

    return render_template('g3CMD.html' )

app.run(host='0.0.0.0', port= 8090)
