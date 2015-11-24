import datetime
import os
import json
import re
import psycopg2 as dbcon
from Medalsclass import Medals, Medal_Records
from flask import Flask, request, render_template, redirect, url_for, session

from config import app

"""@app.route('/Medals', methods=['POST', 'GET'])
def home():
    now = datetime.datetime.now()
    message = None

    if 'email' in session:
        return redirect(url_for('Medalslogin'))

    if request.method == 'POST':
        if request.form.get('password') == '234567':
            session['email'] = request.form.get('email')
            return redirect(url_for('Medals'))
        else:
            message = "Wrong password - email combination!"

    return render_template('Medalslogin.html', current_time=now.ctime(), message=message)"""

@app.route('/Medals', methods=['POST', 'GET'])
def medals_page():
    now = datetime.datetime.now()


    with dbcon.connect(app.config['dsn']) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM medals")
            rows = cursor.fetchall()
            medals = {}
            for row in rows:
                medals[int(row[0])] = Medals(row[0], row[1], row[2], row[3], row[4])
    with dbcon.connect(app.config['dsn']) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM medal_records")
            rows = cursor.fetchall()
            medal_records = {}
            for row in rows:
                medal_records[int(row[0])] = Medal_Records(row[0], row[1], row[2])

    if request.method == 'POST' and 'add' in request.form:
        year = request.form.get('year')
        if not year:
            return redirect(url_for('medals_page'))
        gold = request.form.get('gold')
        silver = request.form.get('silver')
        bronze = request.form.get('bronze')

        with dbcon.connect(app.config['dsn']) as conn:
            cursor = conn.cursor()
            cursor.execute("""INSERT INTO medals (year, gold, silver, bronze)
                VALUES (%s, %s, %s, %s) RETURNING ID""",(year, gold, silver, bronze))
            conn.commit()

            return redirect(url_for('medals_page'))

    if request.method == 'POST' and 'addrec' in request.form:
        bscore = request.form.get('bscore')
        if not bscore:
            return redirect(url_for('medals_page'))
        mid = request.form.get('mid')
        with dbcon.connect(app.config['dsn']) as conn:
            cursor = conn.cursor()
            cursor.execute("""INSERT INTO medal_records (bscore, mid)
                VALUES (%s, %s) RETURNING ID""",(bscore,mid))
            conn.commit()

            return redirect(url_for('medals_page'))

    if request.method == 'GET' and 'keyword' in request.args:
        kw = request.args.get('keyword')

        with dbcon.connect(app.config['dsn']) as conn:
            cursor = conn.cursor()
            cursor.execute("""SELECT * FROM medals WHERE gold ILIKE %(key)s OR silver ILIKE %(key)s OR bronze ILIKE %(key)s""", dict(key='%'+kw+'%'))
            rows = cursor.fetchall()
            medals = {}
            for row in rows:
                medals[int(row[0])] = Medals(row[0], row[1], row[2], row[3], row[4])

            return render_template('Medals.html', current_time=now.ctime(), medals=medals.values(), kw=kw)


    return render_template('Medals.html', current_time=now.ctime(), medals=medals.values(), medal_records=medal_records.values())

@app.route('/update/<int:id>', methods=['POST', 'GET'])
def updatemedal(id):
    with dbcon.connect(app.config['dsn']) as conn:
        cursor = conn.cursor()
        cursor.execute("""
                SELECT * FROM medals WHERE id = %s
                """, (int(id),))
        rows = cursor.fetchall()
        medal = Medals(rows[0][0], rows[0][1], rows[0][2], rows[0][3], rows[0][4])
        print(medal.id)
    if request.method == 'POST' and 'add' in request.form:
        year = request.form.get('year')
        gold = request.form.get('gold')
        silver = request.form.get('silver')
        bronze = request.form.get('bronze')

        with dbcon.connect(app.config['dsn']) as conn:
            cursor = conn.cursor()
            cursor.execute("""UPDATE medals SET YEAR=%s, GOLD=%s, SILVER=%s, BRONZE=%s WHERE ID=%s""",(int(year), gold, silver, bronze,int(id),))

            conn.commit()

            return redirect(url_for('medals_page'))
    now = datetime.datetime.now()
    return render_template('Medalsupdate.html', current_time=now.ctime(), medal=medal)

@app.route('/updaterec/<int:id>', methods=['POST', 'GET'])
def updatemedalrec(id):
    with dbcon.connect(app.config['dsn']) as conn:
        cursor = conn.cursor()
        cursor.execute("""
                SELECT * FROM medal_records WHERE id = %s
                """, (int(id),))
        rows = cursor.fetchall()
        medalrec = Medal_Records(rows[0][0], rows[0][1], rows[0][2])
        print(medalrec.id)
    if request.method == 'POST' and 'addreco' in request.form:
        bscore = request.form.get('bscore')

        with dbcon.connect(app.config['dsn']) as conn:
            cursor = conn.cursor()
            cursor.execute("""UPDATE medal_records SET bscore=%s WHERE ID=%s""",(float(bscore), int(id),))

            conn.commit()

            return redirect(url_for('medals_page'))
    now = datetime.datetime.now()
    return render_template('Medalsbestupdate.html', current_time=now.ctime(), medalrec=medalrec)

@app.route('/delete/<int:id>')
def deletemedal(id):

    with dbcon.connect(app.config['dsn']) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                DELETE FROM medals WHERE id = %s
                """, (int(id),))
            conn.commit()

            return redirect(url_for('medals_page'))

@app.route('/deleterec/<int:id>')
def deletemedalrec(id):

    with dbcon.connect(app.config['dsn']) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                DELETE FROM medal_records WHERE id = %s
                """, (int(id),))
            conn.commit()

            return redirect(url_for('medals_page'))

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
    app.secret_key = 'sZXCk15415523jdsIEOE98721'
    VCAP_APP_PORT = os.getenv('VCAP_APP_PORT')
    if VCAP_APP_PORT is not None:
        port, debug = int(VCAP_APP_PORT), False
    else:
        port, debug = 5000, True

    VCAP_SERVICES = os.getenv('VCAP_SERVICES')
    if VCAP_SERVICES is not None:
        app.config['dsn'] = get_sqldb_dsn(VCAP_SERVICES)
    else:
        app.config['dsn'] = """dbname='xwacqlyq' host='jumbo.db.elephantsql.com' port=5432 user='xwacqlyq' password='eDso0SkacPcR_R6fDRmk0iISfAqh9xjN'"""

    app.run(host='0.0.0.0', port=port, debug=debug)

