#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, request
# from flask.ext.sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from forms import *
import domino
import os

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')
#db = SQLAlchemy(app)

# Automatically tear down SQLAlchemy.
'''
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()
'''

# Login required decorator.
'''
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap
'''
#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#


@app.route('/')
def home():
    return render_template('pages/home.html')


@app.route('/rules')
def rules():
    return render_template('pages/rules.html')

@app.route('/randomgame', methods=['GET', 'POST'])
def randomgame():
    lodominoes = [[0, 1, 1, 2], [1, 1, 2, 1], [2, 1, 3, 2], [3, 1, 4, 1], [4, 1, 5, 2], [5, 1, 6, 2], [6, 2, 2, 2], [7, 2, 3, 1], [8, 2, 4, 1], [9, 2, 5, 1], [10, 2, 6, 1], [11, 3, 3, 2], [12, 3, 4, 1], [13, 3, 5, 1], [14, 3, 6, 1], [15, 4, 4, 2], [16, 4, 5, 1], [17, 4, 6, 2], [18, 5, 5, 2], [19, 5, 6, 2], [20, 6, 6, 2]]
    flod = [[0, 1, 1], [0, 1, 1], [1, 1, 2], [2, 1, 3], [2, 1, 3], [3, 1, 4], [4, 1, 5], [4, 1, 5], [5, 1, 6], [5, 1, 6], [6, 2, 2], [6, 2, 2], [7, 2, 3], [8, 2, 4], [9, 2, 5], [10, 2, 6], [11, 3, 3], [11, 3, 3], [12, 3, 4], [13, 3, 5], [14, 3, 6], [15, 4, 4], [15, 4, 4], [16, 4, 5], [17, 4, 6], [17, 4, 6], [18, 5, 5], [18, 5, 5], [19, 5, 6], [19, 5, 6], [20, 6, 6], [20, 6, 6]]
    lotrios = [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 0, 3], [0, 0, 4], [0, 0, 5], [0, 1, 6], [0, 1, 20], [0, 2, 11], [0, 2, 19], [0, 2, 20], [0, 3, 15], [0, 3, 17], [0, 3, 18], [0, 3, 19], [0, 3, 20], [0, 4, 14], [0, 4, 16], [0, 4, 17], [0, 4, 18], [0, 4, 19], [0, 4, 20], [0, 5, 10], [0, 5, 13], [0, 5, 14], [0, 5, 15], [0, 5, 16], [0, 5, 17], [0, 5, 18], [0, 5, 19], [0, 5, 20], [0, 6, 6], [0, 6, 7], [0, 6, 11], [0, 7, 7], [0, 12, 15], [0, 13, 18], [0, 14, 20], [1, 1, 1], [1, 1, 6], [1, 1, 7], [1, 1, 11], [1, 2, 6], [1, 2, 7], [1, 5, 5], [1, 6, 6], [1, 7, 11], [1, 8, 15], [1, 9, 18], [1, 10, 20], [1, 11, 11], [1, 12, 19], [1, 13, 17], [1, 14, 16], [2, 2, 2], [2, 2, 6], [2, 3, 15], [2, 4, 5], [2, 4, 18], [2, 5, 5], [2, 5, 20], [2, 6, 11], [2, 7, 7], [2, 7, 11], [2, 8, 19], [2, 9, 17], [2, 10, 16], [2, 11, 11], [2, 15, 15], [3, 3, 3], [3, 3, 5], [3, 3, 12], [3, 4, 4], [3, 4, 5], [3, 5, 5], [3, 6, 15], [3, 7, 19], [3, 8, 8], [3, 9, 14], [3, 10, 13], [3, 12, 15], [3, 15, 15], [3, 18, 18], [4, 4, 4], [4, 4, 5], [4, 4, 13], [4, 5, 5], [4, 6, 18], [4, 7, 17], [4, 8, 14], [4, 9, 9], [4, 10, 12], [4, 16, 18], [4, 18, 18], [4, 20, 20], [5, 5, 5], [5, 5, 14], [5, 6, 20], [5, 7, 16], [5, 8, 13], [5, 9, 12], [5, 10, 10], [5, 19, 20], [5, 20, 20], [6, 6, 6], [6, 6, 7], [6, 6, 8], [6, 6, 9], [6, 6, 10], [6, 7, 11], [6, 7, 19], [6, 7, 20], [6, 8, 15], [6, 8, 17], [6, 8, 18], [6, 8, 19], [6, 8, 20], [6, 9, 14], [6, 9, 16], [6, 9, 17], [6, 9, 18], [6, 9, 19], [6, 9, 20], [6, 10, 13], [6, 10, 14], [6, 10, 15], [6, 10, 16], [6, 10, 17], [6, 10, 18], [6, 10, 19], [6, 10, 20], [6, 15, 15], [7, 7, 7], [7, 9, 10], [7, 10, 10], [7, 11, 11], [7, 11, 20], [7, 14, 14], [7, 18, 18], [8, 8, 8], [8, 8, 10], [8, 8, 15], [8, 9, 9], [8, 9, 10], [8, 10, 10], [8, 15, 15], [8, 15, 20], [8, 17, 17], [8, 20, 20], [9, 9, 9], [9, 9, 10], [9, 10, 10], [9, 13, 18], [9, 18, 18], [9, 18, 20], [9, 19, 19], [10, 10, 10], [10, 11, 14], [10, 15, 17], [10, 17, 20], [10, 18, 19], [10, 20, 20], [11, 11, 11], [11, 11, 12], [11, 11, 13], [11, 11, 14], [11, 12, 15], [11, 12, 17], [11, 12, 18], [11, 12, 19], [11, 12, 20], [11, 13, 16], [11, 13, 17], [11, 13, 18], [11, 13, 19], [11, 13, 20], [11, 14, 15], [11, 14, 16], [11, 14, 17], [11, 14, 18], [11, 14, 19], [11, 14, 20], [11, 20, 20], [12, 12, 12], [12, 12, 14], [12, 13, 13], [12, 13, 14], [12, 14, 14], [12, 15, 15], [12, 15, 19], [12, 15, 20], [12, 16, 17], [12, 17, 17], [13, 13, 13], [13, 13, 14], [13, 14, 14], [13, 15, 17], [13, 18, 18], [13, 18, 20], [13, 19, 19], [14, 14, 14], [14, 14, 20], [14, 15, 16], [14, 15, 17], [14, 18, 19], [14, 20, 20], [15, 15, 15], [15, 15, 16], [15, 15, 17], [15, 16, 18], [15, 16, 19], [15, 16, 20], [15, 17, 18], [15, 17, 19], [15, 17, 20], [15, 18, 19], [15, 18, 20], [15, 19, 19], [16, 16, 16], [16, 16, 17], [16, 16, 19], [16, 16, 20], [16, 17, 17], [16, 17, 18], [16, 17, 19], [16, 18, 18], [16, 18, 20], [16, 19, 19], [16, 19, 20], [17, 17, 17], [17, 17, 18], [17, 18, 19], [17, 18, 20], [17, 19, 19], [17, 20, 20], [18, 18, 18], [18, 18, 19], [18, 19, 20], [19, 19, 19], [19, 20, 20], [20, 20, 20]]
    cb = domino.classicalBoard(lodominoes, flod, lotrios)
    return render_template('pages/classical.html', classicalBoard=cb)

@app.route('/classical', methods=['GET', 'POST'])
def classical():
    raw = request.args.get('setup')
    #domino.shuffle(raw)
    print(raw)
    lodominoes = [[0, 1, 1, 2], [1, 1, 2, 1], [2, 1, 3, 2], [3, 1, 4, 1], [4, 1, 5, 2], [5, 1, 6, 2], [6, 2, 2, 2], [7, 2, 3, 1], [8, 2, 4, 1], [9, 2, 5, 1], [10, 2, 6, 1], [11, 3, 3, 2], [12, 3, 4, 1], [13, 3, 5, 1], [14, 3, 6, 1], [15, 4, 4, 2], [16, 4, 5, 1], [17, 4, 6, 2], [18, 5, 5, 2], [19, 5, 6, 2], [20, 6, 6, 2]]
    flod = [[0, 1, 1], [0, 1, 1], [1, 1, 2], [2, 1, 3], [2, 1, 3], [3, 1, 4], [4, 1, 5], [4, 1, 5], [5, 1, 6], [5, 1, 6], [6, 2, 2], [6, 2, 2], [7, 2, 3], [8, 2, 4], [9, 2, 5], [10, 2, 6], [11, 3, 3], [11, 3, 3], [12, 3, 4], [13, 3, 5], [14, 3, 6], [15, 4, 4], [15, 4, 4], [16, 4, 5], [17, 4, 6], [17, 4, 6], [18, 5, 5], [18, 5, 5], [19, 5, 6], [19, 5, 6], [20, 6, 6], [20, 6, 6]]
    lotrios = [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 0, 3], [0, 0, 4], [0, 0, 5], [0, 1, 6], [0, 1, 20], [0, 2, 11], [0, 2, 19], [0, 2, 20], [0, 3, 15], [0, 3, 17], [0, 3, 18], [0, 3, 19], [0, 3, 20], [0, 4, 14], [0, 4, 16], [0, 4, 17], [0, 4, 18], [0, 4, 19], [0, 4, 20], [0, 5, 10], [0, 5, 13], [0, 5, 14], [0, 5, 15], [0, 5, 16], [0, 5, 17], [0, 5, 18], [0, 5, 19], [0, 5, 20], [0, 6, 6], [0, 6, 7], [0, 6, 11], [0, 7, 7], [0, 12, 15], [0, 13, 18], [0, 14, 20], [1, 1, 1], [1, 1, 6], [1, 1, 7], [1, 1, 11], [1, 2, 6], [1, 2, 7], [1, 5, 5], [1, 6, 6], [1, 7, 11], [1, 8, 15], [1, 9, 18], [1, 10, 20], [1, 11, 11], [1, 12, 19], [1, 13, 17], [1, 14, 16], [2, 2, 2], [2, 2, 6], [2, 3, 15], [2, 4, 5], [2, 4, 18], [2, 5, 5], [2, 5, 20], [2, 6, 11], [2, 7, 7], [2, 7, 11], [2, 8, 19], [2, 9, 17], [2, 10, 16], [2, 11, 11], [2, 15, 15], [3, 3, 3], [3, 3, 5], [3, 3, 12], [3, 4, 4], [3, 4, 5], [3, 5, 5], [3, 6, 15], [3, 7, 19], [3, 8, 8], [3, 9, 14], [3, 10, 13], [3, 12, 15], [3, 15, 15], [3, 18, 18], [4, 4, 4], [4, 4, 5], [4, 4, 13], [4, 5, 5], [4, 6, 18], [4, 7, 17], [4, 8, 14], [4, 9, 9], [4, 10, 12], [4, 16, 18], [4, 18, 18], [4, 20, 20], [5, 5, 5], [5, 5, 14], [5, 6, 20], [5, 7, 16], [5, 8, 13], [5, 9, 12], [5, 10, 10], [5, 19, 20], [5, 20, 20], [6, 6, 6], [6, 6, 7], [6, 6, 8], [6, 6, 9], [6, 6, 10], [6, 7, 11], [6, 7, 19], [6, 7, 20], [6, 8, 15], [6, 8, 17], [6, 8, 18], [6, 8, 19], [6, 8, 20], [6, 9, 14], [6, 9, 16], [6, 9, 17], [6, 9, 18], [6, 9, 19], [6, 9, 20], [6, 10, 13], [6, 10, 14], [6, 10, 15], [6, 10, 16], [6, 10, 17], [6, 10, 18], [6, 10, 19], [6, 10, 20], [6, 15, 15], [7, 7, 7], [7, 9, 10], [7, 10, 10], [7, 11, 11], [7, 11, 20], [7, 14, 14], [7, 18, 18], [8, 8, 8], [8, 8, 10], [8, 8, 15], [8, 9, 9], [8, 9, 10], [8, 10, 10], [8, 15, 15], [8, 15, 20], [8, 17, 17], [8, 20, 20], [9, 9, 9], [9, 9, 10], [9, 10, 10], [9, 13, 18], [9, 18, 18], [9, 18, 20], [9, 19, 19], [10, 10, 10], [10, 11, 14], [10, 15, 17], [10, 17, 20], [10, 18, 19], [10, 20, 20], [11, 11, 11], [11, 11, 12], [11, 11, 13], [11, 11, 14], [11, 12, 15], [11, 12, 17], [11, 12, 18], [11, 12, 19], [11, 12, 20], [11, 13, 16], [11, 13, 17], [11, 13, 18], [11, 13, 19], [11, 13, 20], [11, 14, 15], [11, 14, 16], [11, 14, 17], [11, 14, 18], [11, 14, 19], [11, 14, 20], [11, 20, 20], [12, 12, 12], [12, 12, 14], [12, 13, 13], [12, 13, 14], [12, 14, 14], [12, 15, 15], [12, 15, 19], [12, 15, 20], [12, 16, 17], [12, 17, 17], [13, 13, 13], [13, 13, 14], [13, 14, 14], [13, 15, 17], [13, 18, 18], [13, 18, 20], [13, 19, 19], [14, 14, 14], [14, 14, 20], [14, 15, 16], [14, 15, 17], [14, 18, 19], [14, 20, 20], [15, 15, 15], [15, 15, 16], [15, 15, 17], [15, 16, 18], [15, 16, 19], [15, 16, 20], [15, 17, 18], [15, 17, 19], [15, 17, 20], [15, 18, 19], [15, 18, 20], [15, 19, 19], [16, 16, 16], [16, 16, 17], [16, 16, 19], [16, 16, 20], [16, 17, 17], [16, 17, 18], [16, 17, 19], [16, 18, 18], [16, 18, 20], [16, 19, 19], [16, 19, 20], [17, 17, 17], [17, 17, 18], [17, 18, 19], [17, 18, 20], [17, 19, 19], [17, 20, 20], [18, 18, 18], [18, 18, 19], [18, 19, 20], [19, 19, 19], [19, 20, 20], [20, 20, 20]]
    cb = domino.classicalBoard(lodominoes, flod, lotrios, raw)
    return render_template('pages/classical.html', classicalBoard=cb)

@app.route('/solution', methods=['GET', 'POST'])
def solution():
    raw = request.args.get('setup')
    #domino.shuffle(raw)
    print(raw)
    lodominoes = [[0, 1, 1, 2], [1, 1, 2, 1], [2, 1, 3, 2], [3, 1, 4, 1], [4, 1, 5, 2], [5, 1, 6, 2], [6, 2, 2, 2], [7, 2, 3, 1], [8, 2, 4, 1], [9, 2, 5, 1], [10, 2, 6, 1], [11, 3, 3, 2], [12, 3, 4, 1], [13, 3, 5, 1], [14, 3, 6, 1], [15, 4, 4, 2], [16, 4, 5, 1], [17, 4, 6, 2], [18, 5, 5, 2], [19, 5, 6, 2], [20, 6, 6, 2]]
    flod = [[0, 1, 1], [0, 1, 1], [1, 1, 2], [2, 1, 3], [2, 1, 3], [3, 1, 4], [4, 1, 5], [4, 1, 5], [5, 1, 6], [5, 1, 6], [6, 2, 2], [6, 2, 2], [7, 2, 3], [8, 2, 4], [9, 2, 5], [10, 2, 6], [11, 3, 3], [11, 3, 3], [12, 3, 4], [13, 3, 5], [14, 3, 6], [15, 4, 4], [15, 4, 4], [16, 4, 5], [17, 4, 6], [17, 4, 6], [18, 5, 5], [18, 5, 5], [19, 5, 6], [19, 5, 6], [20, 6, 6], [20, 6, 6]]
    lotrios = [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 0, 3], [0, 0, 4], [0, 0, 5], [0, 1, 6], [0, 1, 20], [0, 2, 11], [0, 2, 19], [0, 2, 20], [0, 3, 15], [0, 3, 17], [0, 3, 18], [0, 3, 19], [0, 3, 20], [0, 4, 14], [0, 4, 16], [0, 4, 17], [0, 4, 18], [0, 4, 19], [0, 4, 20], [0, 5, 10], [0, 5, 13], [0, 5, 14], [0, 5, 15], [0, 5, 16], [0, 5, 17], [0, 5, 18], [0, 5, 19], [0, 5, 20], [0, 6, 6], [0, 6, 7], [0, 6, 11], [0, 7, 7], [0, 12, 15], [0, 13, 18], [0, 14, 20], [1, 1, 1], [1, 1, 6], [1, 1, 7], [1, 1, 11], [1, 2, 6], [1, 2, 7], [1, 5, 5], [1, 6, 6], [1, 7, 11], [1, 8, 15], [1, 9, 18], [1, 10, 20], [1, 11, 11], [1, 12, 19], [1, 13, 17], [1, 14, 16], [2, 2, 2], [2, 2, 6], [2, 3, 15], [2, 4, 5], [2, 4, 18], [2, 5, 5], [2, 5, 20], [2, 6, 11], [2, 7, 7], [2, 7, 11], [2, 8, 19], [2, 9, 17], [2, 10, 16], [2, 11, 11], [2, 15, 15], [3, 3, 3], [3, 3, 5], [3, 3, 12], [3, 4, 4], [3, 4, 5], [3, 5, 5], [3, 6, 15], [3, 7, 19], [3, 8, 8], [3, 9, 14], [3, 10, 13], [3, 12, 15], [3, 15, 15], [3, 18, 18], [4, 4, 4], [4, 4, 5], [4, 4, 13], [4, 5, 5], [4, 6, 18], [4, 7, 17], [4, 8, 14], [4, 9, 9], [4, 10, 12], [4, 16, 18], [4, 18, 18], [4, 20, 20], [5, 5, 5], [5, 5, 14], [5, 6, 20], [5, 7, 16], [5, 8, 13], [5, 9, 12], [5, 10, 10], [5, 19, 20], [5, 20, 20], [6, 6, 6], [6, 6, 7], [6, 6, 8], [6, 6, 9], [6, 6, 10], [6, 7, 11], [6, 7, 19], [6, 7, 20], [6, 8, 15], [6, 8, 17], [6, 8, 18], [6, 8, 19], [6, 8, 20], [6, 9, 14], [6, 9, 16], [6, 9, 17], [6, 9, 18], [6, 9, 19], [6, 9, 20], [6, 10, 13], [6, 10, 14], [6, 10, 15], [6, 10, 16], [6, 10, 17], [6, 10, 18], [6, 10, 19], [6, 10, 20], [6, 15, 15], [7, 7, 7], [7, 9, 10], [7, 10, 10], [7, 11, 11], [7, 11, 20], [7, 14, 14], [7, 18, 18], [8, 8, 8], [8, 8, 10], [8, 8, 15], [8, 9, 9], [8, 9, 10], [8, 10, 10], [8, 15, 15], [8, 15, 20], [8, 17, 17], [8, 20, 20], [9, 9, 9], [9, 9, 10], [9, 10, 10], [9, 13, 18], [9, 18, 18], [9, 18, 20], [9, 19, 19], [10, 10, 10], [10, 11, 14], [10, 15, 17], [10, 17, 20], [10, 18, 19], [10, 20, 20], [11, 11, 11], [11, 11, 12], [11, 11, 13], [11, 11, 14], [11, 12, 15], [11, 12, 17], [11, 12, 18], [11, 12, 19], [11, 12, 20], [11, 13, 16], [11, 13, 17], [11, 13, 18], [11, 13, 19], [11, 13, 20], [11, 14, 15], [11, 14, 16], [11, 14, 17], [11, 14, 18], [11, 14, 19], [11, 14, 20], [11, 20, 20], [12, 12, 12], [12, 12, 14], [12, 13, 13], [12, 13, 14], [12, 14, 14], [12, 15, 15], [12, 15, 19], [12, 15, 20], [12, 16, 17], [12, 17, 17], [13, 13, 13], [13, 13, 14], [13, 14, 14], [13, 15, 17], [13, 18, 18], [13, 18, 20], [13, 19, 19], [14, 14, 14], [14, 14, 20], [14, 15, 16], [14, 15, 17], [14, 18, 19], [14, 20, 20], [15, 15, 15], [15, 15, 16], [15, 15, 17], [15, 16, 18], [15, 16, 19], [15, 16, 20], [15, 17, 18], [15, 17, 19], [15, 17, 20], [15, 18, 19], [15, 18, 20], [15, 19, 19], [16, 16, 16], [16, 16, 17], [16, 16, 19], [16, 16, 20], [16, 17, 17], [16, 17, 18], [16, 17, 19], [16, 18, 18], [16, 18, 20], [16, 19, 19], [16, 19, 20], [17, 17, 17], [17, 17, 18], [17, 18, 19], [17, 18, 20], [17, 19, 19], [17, 20, 20], [18, 18, 18], [18, 18, 19], [18, 19, 20], [19, 19, 19], [19, 20, 20], [20, 20, 20]]
    cb = domino.classicalBoard(lodominoes, flod, lotrios, raw)
    return render_template('pages/solution.html', classicalBoard=cb)


@app.route('/prompt', methods=['GET', 'POST'])
def prompt():
    return render_template('pages/prompt.html')

@app.route('/classical/swap', methods=['GET', 'POST'])
def swap():
    raw = request.args.get('setup')
    rawSwaps = request.args.get('swaps')
    swaps = []
    for i in range(len(swaps)/4):
        swaps += [[int(swaps[i] + swaps[i+1]),int(swaps[i+2] + swaps[i+3])]]
    
    return render_template('pages/invalid.html')


@app.route('/login')
def login():
    form = LoginForm(request.form)
    return render_template('forms/login.html', form=form)

@app.route('/register')
def register():
    form = RegisterForm(request.form)
    return render_template('forms/register.html', form=form)


@app.route('/forgot')
def forgot():
    form = ForgotForm(request.form)
    return render_template('forms/forgot.html', form=form)

# Error handlers.


@app.errorhandler(500)
def internal_error(error):
    #db_session.rollback()
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
