from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return "Hello world from s2i"
app.run(host="0.0.0.0")
