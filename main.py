from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<p> Hello, welcome to my app. </p>"

@app.route("/home/<user_name>", methods=['GET', 'POST'])
def greet(user_name):
    return 'Welcome %s' % user_name