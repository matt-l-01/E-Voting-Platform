from flask import Blueprint, request, jsonify, make_response
import json
from src import db


voter = Blueprint('voter', __name__)

# Gets all the votes from the database
@voter.route('/votes', methods=['GET'])
def get_voter():
    cursor = db.get_db().cursor()
    cursor.execute('select * from votes')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Submits a new vote to the database
@voter.route("/vote", methods = ['POST'])
def post_form():
    name = request.form['name']
    ssn = request.form['ssn']
    email = request.form['email']
    candidate = request.form['candidate']

    cursor = db.get_db().cursor()
    cursor.execute(f'insert into `votes`(`VoterName`, `SSN`, `Email`, `CandidateVote`) values (\'{name}\',\'{ssn}\',\'{email}\',\'{candidate}\')')
    return f'<h1>Done!: {name}</h1>'