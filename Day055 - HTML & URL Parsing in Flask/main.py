# Created by Ricardo Lousada
from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        text = function()
        new_text = f"<b>{text}</b>"
        return new_text
    return wrapper


def make_emphasis(function):
    text = function()
    return f"<em>{text}</em>"

def is_authenticated_decorator(function):
    def wrapper(*args,**kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper


def make_underlined(function):
    text = function()
    return f"<u>{text}</u>"

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/bye")
@make_bold
def bye():
    return "<p>Bye<p>"

@app.route("/username/<name>/<int:number>")
def great(name,number):
    return f"Hello {name}, how are you? you are {number} years old"




if __name__ == "__main__":
    app.run(debug=True)