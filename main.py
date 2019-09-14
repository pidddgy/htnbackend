#!python3
from flask import Flask
app = Flask(__name__)

# foodname -> string
# blacklist -> comma seperated list of strings e.g. "apple,banna,orange"
@app.route('/<foodname>/<blacklist>')
def f(foodname, blacklist):
    return blacklist
