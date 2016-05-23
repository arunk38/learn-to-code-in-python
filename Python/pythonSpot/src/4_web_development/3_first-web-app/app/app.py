from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy.orm import sessionmaker
from tabledef import *
from random import randint
engine = create_engine('sqlite:///tutorial.db', echo=True)
app = Flask(__name__)

users_dict = {'admin' : 'password',
              'arun' : 'arun',
              'sowmya' : 'segu'}


@app.route("/")
def home(name = None):
    if not session.get('logged_in') or name is None:
        return render_template('login.html')
    else:
        return welcome(name)


def welcome(name):
    quotes = [
        "'If people do not believe that mathematics is simple, it is only because they do not realize how complicated\
         life is.' -- John Louis von Neumann ",
        "'Computer science is no more about computers than astronomy is about telescopes' --  Edsger Dijkstra ",
        "'To understand recursion you must first understand recursion..' -- Unknown",
        "'You look at things that are and ask, why? I dream of things that never were and ask, why not?' -- Unknown",
        "'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
        "'Not everyone will understand your journey. That's fine. Its not their journey to make sense of. Its yours.'\
         -- Unknown"]


    randomNumber = randint(0, len(quotes) - 1)
    quote = quotes[randomNumber]

    return render_template(
        'home.html', **locals())


@app.route('/login', methods=['POST'])
def do_admin_login():
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])

    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]))
    result = query.first()
    if result:
        session['logged_in'] = True
        return home(POST_USERNAME)
    else:
        session['logged_in'] = False
        flash('wrong password!')
    return home()


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=4000)