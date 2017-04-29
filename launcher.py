#!/usr/local/bin python

from flask import Flask

app = Flask( __name__ )

@app.route("/")
def welcome():
    return "Welcome to BeeBox!"

if __name__ == '__main__':
    app.run()