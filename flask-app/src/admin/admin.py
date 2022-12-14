from flask import Blueprint, request, jsonify, make_response
import json
from src import db


admin = Blueprint('admin', __name__)

# Get bans from the database
@admin.route('/bans', methods=['GET'])
def get_admin():
    cursor = db.get_db().cursor()
    cursor.execute('select * from bans')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Submit a new ban to the record
@admin.route("/ban", methods = ['POST'])
def post_form():
    aname = request.form['aname']
    bssn = request.form['bssn']
    reason = request.form['reason']
    length = request.form['length']
    details = request.form['details']

    cursor = db.get_db().cursor()
    cursor.execute(f'insert into `bans`(`AdminName`, `BannedSSN`, `Reason`, `Length`, `Details`) values (\'{aname}\',\'{bssn}\',\'{reason}\',\'{length}\',\'{details}\')')
    return f'<h1>Done!: {aname}</h1>'