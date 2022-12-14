from flask import Blueprint
from src import db

views = Blueprint('views', __name__)

# Routes for statistical views for the server (number of each entries)

@views.route('/bans')
def showbans():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT COUNT(*) FROM bans')
    return ('The server contains ' + str(cursor.fetchone()[0]) + ' ban entries')

@views.route('/votes')
def showvotes():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT COUNT(*) FROM votes')
    return ('The server contains ' + str(cursor.fetchone()[0]) + ' vote entries')

@views.route('/complaints')
def showcomplaints():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT COUNT(*) FROM complaints')
    return ('The server contains ' + str(cursor.fetchone()[0]) + ' complaint entries')

@views.route('/candidates')
def showcandidates():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT COUNT(*) FROM candidates')
    return ('The server contains ' + str(cursor.fetchone()[0]) + ' candidate entries')