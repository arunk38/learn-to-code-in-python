from flask import  Flask, flash, redirect, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return "Flask App!!"


@app.route("/user/")
def hello():

    users = [ "Frank", "Steve", "Alice", "Bruce" ]
    return render_template('user.html', users=users)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
