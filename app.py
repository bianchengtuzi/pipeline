from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return "Hello world from s2i to github"
app.run(host="0.0.0.0")
