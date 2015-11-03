import datetime
import os
import json
import re
import psycopg2 as dbcon
from players import Player
from records import Record
from contest import contest
from Type import types
from flask import Flask, request, render_template, redirect, url_for, session

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():
    now = datetime.datetime.now()
    message = None

    if 'email' in session:
        return redirect(url_for('admin'))

    if request.method == 'POST':
        if request.form.get('password') == '234567':
            session['email'] = request.form.get('email')
            return redirect(url_for('admin'))
        else:
            message = "Wrong password - email combination!"

    return render_template('login.html', current_time=now.ctime(), message=message)

@app.route('/players')
def players():
    now = datetime.datetime.now()

    with dbcon.connect(app.config['dsn']) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM players")
            rows = cursor.fetchall()
            players = {}
            for row in rows:
                players[int(row[0])] = Player(row[0], row[1], row[2], row[3], row[4])

    return render_template('players.html', current_time=now.ctime(), players=players.values())
@app.route('/records/')
def records():
    now = datetime.datetime.now()

    with dbcon.connect(app.config['dsn']) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM records")
            rows = cursor.fetchall()
            records = {}
            for row in rows:
                records[int(row[0])] = Record(row[0], row[1], row[2], row[3], row[4])

    return render_template('records.html', current_time=now.ctime(), players=players.values())
@app.route('/types/')
def types():
    now = datetime.datetime.now()

    with dbcon.connect(app.config['dsn']) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM types")
            rows = cursor.fetchall()
            types = {}
            for row in rows:
                types[int(row[0])] = types(row[0], row[1], row[2], row[3], row[4])

    return



@app.route('/deletety/<int:id>')
def deletety(id):
    with dbcon.connect(app.config['dsn']) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                DELETE FROM types WHERE id = %s
                """, (int(id),))
            conn.commit()
    return redirect(url_for(''))


@app.route('/addty/', methods=['POST', 'GET'])
def addty():

    now = datetime.datetime.now()
    with dbcon.connect(app.config['dsn']) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM types")
            rows = cursor.fetchall()
            types = {}
            for row in rows:
                types[int(row[0])] = types(row[0], row[1], row[2], row[3], row[4])

    if request.method == 'POST' and 'add' in request.form:
        name = request.form.get('name')
        type = request.form.get('type')
        weight = request.form.get('weight')
        height = request.form.get('height')
        with dbcon.connect(app.config['dsn']) as conn:
            cursor = conn.cursor()
            cursor.execute(
"""INSERT INTO
 types (name, type, weight,height)
                
VALUES (%s, %s, %s, %s)
 RETURNING ID""",(name, type, weight, height))
            conn.commit()

        return redirect(url_for('home'))

@app.route('/edit/players', methods=['POST', 'GET'])
def edit_players():
    if not 'email' in session:
        return redirect(url_for('edit_players'))

    now = datetime.datetime.now()

    with dbcon.connect(app.config['dsn']) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM players")
            rows = cursor.fetchall()
            players = {}
            for row in rows:
                players[int(row[0])] = Player(row[0], row[1], row[2], row[3], row[4])

    if request.method == 'POST' and 'add' in request.form:
        name = request.form.get('name')
        surname = request.form.get('surname')
        nationality = request.form.get('nationality')
        style = request.form.get('style')

        with dbcon.connect(app.config['dsn']) as conn:
            cursor = conn.cursor()
            cursor.execute("""INSERT INTO players (name, surname, nationality, style)
                VALUES (%s, %s, %s, %s) RETURNING ID""",(name, surname, nationality, style))
            conn.commit()

            return redirect(url_for('edit_players'))

    return render_template('edit_players.html', current_time=now.ctime(), players=players.values())

@app.route('/delete/<int:id>')
def delete(id):
    if not 'email' in session:
        return redirect(url_for('home'))

    with dbcon.connect(app.config['dsn']) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                DELETE FROM players WHERE id = %s
                """, (int(id),))
            conn.commit()

            return redirect(url_for('edit_players'))
@app.route('/edit/players', methods=['POST', 'GET'])
def edit_records():
    if not 'email' in session:
        return redirect(url_for('home'))

    now = datetime.datetime.now()

    with dbcon.connect(app.config['dsn']) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM players")
            rows = cursor.fetchall()
            players = {}
            for row in rows:
                records[int(row[0])] = Record(row[0], row[1], row[2], row[3], row[4])

    if request.method == 'POST' and 'add' in request.form:
        record = request.form.get('record')
        name = request.form.get('name')
        surname = request.form.get('surname')
        style = request.form.get('style')

        with dbcon.connect(app.config['dsn']) as conn:
            cursor = conn.cursor()
            cursor.execute("""INSERT INTO players (record,name, surname, style)
                VALUES (%s, %s, %s, %s) RETURNING ID""",(record,name, surname, style))
            conn.commit()

            return redirect(url_for('edit_records'))

    return render_template('edit_players.html', current_time=now.ctime(), players=players.values())

@app.route('/deleterc/<int:id>')
def deleterecord(id):
    if not 'email' in session:
        return redirect(url_for('home'))

    with dbcon.connect(app.config['dsn']) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                DELETE FROM records WHERE id = %s
                """, (int(id),))
            conn.commit()

            return redirect(url_for('edit_records'))

@app.route('/admin')


@app.route('/deleteanl/<int:id>')
def deleteanl(id):
    with dbcon.connect(app.config['dsn']) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                DELETE FROM contest WHERE id = %s
                """, (int(id),))
            conn.commit()
            
            return redirect(url_for('home'))


@app.route('/addanl/', methods=['POST', 'GET'])
def addanl():

    now = datetime.datetime.now()
    with dbcon.connect(app.config['dsn']) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM contest")
            rows = cursor.fetchall()
            contest = {}
            for row in rows:
                contest[int(row[0])] = contest(row[0], row[1], row[2], row[3], row[4])

    if request.method == 'POST' and 'add' in request.form:
        name = request.form.get('name')
        surname = request.form.get('surname')
        type = request.form.get('type')
        degree = request.form.get('degree')
        with dbcon.connect(app.config['dsn']) as conn:
            cursor = conn.cursor()
            cursor.execute(
"""INSERT INTO
 contest (name, surname, type, degree)

VALUES (%s, %s, %s, %s)
 RETURNING ID""",(name, surname, type, degree))
            conn.commit()

            return redirect(url_for('home'))

def admin():
    if 'email' in session:
        return render_template('admin.html', username=session['email'])
    else:
        return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('home'))

def get_sqldb_dsn(vcap_services):
    """Returns the data source name for ElephantSQL."""
    parsed = json.loads(vcap_services)
    uri = parsed["elephantsql"][0]["credentials"]["uri"]
    match = re.match('postgres://(.*?):(.*?)@(.*?)(:(\d+))?/(.*)', uri)
    user, password, host, _, port, dbname = match.groups()
    dsn = """user='{}' password='{}' host='{}' port={}
             dbname='{}'""".format(user, password, host, port, dbname)
    return dsn

if __name__ == '__main__':
    app.secret_key = 'sZXCkjdsIEOE98721'

    VCAP_APP_PORT = os.getenv('VCAP_APP_PORT')
    if VCAP_APP_PORT is not None:
        port, debug = int(VCAP_APP_PORT), False
    else:
        port, debug = 5000, True

    VCAP_SERVICES = os.getenv('VCAP_SERVICES')
    if VCAP_SERVICES is not None:
        app.config['dsn'] = get_sqldb_dsn(VCAP_SERVICES)
    else:
        app.config['dsn'] = """dbname='mzeqlsdz' host='horton.elephantsql.com' port=5432 user='mzeqlsdz' password='XkyJ3SH4oKAm6Q6tFhkHvfm2tHRxtz95'"""

    app.run(host='0.0.0.0', port=port, debug=debug)