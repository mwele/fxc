from flask import Flask
app=Flask(__name__)

app.route('/')
def index():
    return '<h1>Hey they what\'s up?</h1>'
