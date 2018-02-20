
# A very simple Flask Hello World app for you to get started with...

from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'
@app.route('/science')
def hello_world2():
    return 'I love science!'

@app.route('/', mathods=["GET"])
def index():
    return render_template("main_page.html")