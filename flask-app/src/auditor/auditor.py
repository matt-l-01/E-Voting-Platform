from flask import Blueprint, request, jsonify, make_response
import json
from src import db


auditor = Blueprint('audit', __name__)

# Gets the list of complaints from the database
@auditor.route('/complaints', methods=['GET'])
def get_auditor():
    cursor = db.get_db().cursor()
    cursor.execute('select * from complaints')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Submits a new complaint to the database
@auditor.route("/complaint", methods = ['POST'])
def post_form():
    aname = request.form['aname']
    cand = request.form['candidate']
    vname = request.form['vname']
    complaint = request.form['complaint']

    cursor = db.get_db().cursor()
    cursor.execute(f'insert into `complaints`(`AuditorName`, `Candidate`, `VoterName`, `Complaint`) values (\'{aname}\',\'{cand}\',\'{vname}\',\'{complaint}\')')
    return f'<h1>Done!: {aname}</h1>'