from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Just completed my frst Argocd deployment...HELL Woooah!!!'
