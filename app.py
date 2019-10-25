from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def index_page():
    return 'FORM WILL BE HERE'
