import datetime
import os
import json
import re
import psycopg2 as dbcon
from Medalsclass import Medals, Medal_Records, Fr_Medals
from flask import Flask, request, render_template, redirect, url_for, session, flash

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
                #medals[int(row[0])] = Medals(row[0], row[1], row[2], row[3], row[4])
                medals[int(row[0])] = Medals(row[0], row[1], row[2], row[3])
    with dbcon.connect(app.config['dsn']) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM medal_records")
            rows = cursor.fetchall()
            medal_records = {}
            for row in rows:
                medal_records[int(row[0])] = Medal_Records(row[0], row[1], row[2])
    with dbcon.connect(app.config['dsn']) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM fr_medals")
            rows = cursor.fetchall()
            fr_medals = {}
            for row in rows:
                fr_medals[int(row[0])] = Fr_Medals(row[0], row[1], row[2],row[3])

    if request.method == 'POST' and 'add' in request.form:
        #year = request.form.get('year')
        #if not year:
            #return redirect(url_for('medals_page'))
        gold = request.form.get('gold')
        silver = request.form.get('silver')
        bronze = request.form.get('bronze')

        with dbcon.connect(app.config['dsn']) as conn:
            cursor = conn.cursor()
            #cursor.execute("""INSERT INTO medals (year, gold, silver, bronze)
                #VALUES (%s, %s, %s, %s) RETURNING ID""",(year, gold, silver, bronze))
            cursor.execute("""INSERT INTO medals (gold, silver, bronze)
                VALUES (%s, %s, %s) RETURNING ID""",(gold, silver, bronze))
            conn.commit()

            return redirect(url_for('medals_page'))

    if request.method == 'POST' and 'addfr' in request.form:

        frname = request.form.get('frname')
        if not frname:
            return redirect(url_for('medals_page'))
        age = request.form.get('age')
        cid = request.form.get('cid')
        try:
            with dbcon.connect(app.config['dsn']) as conn:
                cursor = conn.cursor()
                cursor.execute("""INSERT INTO fr_medals (name, age, cid)
                VALUES (%s, %s, %s) RETURNING ID""",(frname, age, cid))
                conn.commit()
        except dbcon.DatabaseError:
            flash('An Invalid Competition ID is choosen')
            conn.rollback()
        finally:
            conn.close()
        return redirect(url_for('medals_page'))

    if request.method == 'POST' and 'addrec' in request.form:
        bscore = request.form.get('bscore')
        if not bscore:
            return redirect(url_for('medals_page'))
        mid = request.form.get('mid')
        try:
            with dbcon.connect(app.config['dsn']) as conn:
                cursor = conn.cursor()
                cursor.execute("""INSERT INTO medal_records (bscore, mid)
                VALUES (%s, %s) RETURNING ID""",(bscore,mid))
                conn.commit()
        except dbcon.DatabaseError:
            flash('An Invalid Competition ID is choosen')
            conn.rollback()
        finally:
            conn.close()
        return redirect(url_for('medals_page'))

    if request.method == 'GET' and 'keyword' in request.args:
        kw = request.args.get('keyword')

        with dbcon.connect(app.config['dsn']) as conn:
            cursor = conn.cursor()
            cursor.execute("""SELECT * FROM medals WHERE gold ILIKE %(key)s OR silver ILIKE %(key)s OR bronze ILIKE %(key)s""", dict(key='%'+kw+'%'))
            rows = cursor.fetchall()
            medals = {}
            for row in rows:
                #medals[int(row[0])] = Medals(row[0], row[1], row[2], row[3], row[4])
                medals[int(row[0])] = Medals(row[0], row[1], row[2], row[3])

            return render_template('Medals.html', current_time=now.ctime(), medals=medals.values(), kw=kw, medal_records=medal_records.values(), fr_medals=fr_medals.values())

    if request.method == 'GET' and 'keyword' in request.args:
        kwfr = request.args.get('keyword')

        with dbcon.connect(app.config['dsn']) as conn:
            cursor = conn.cursor()
            cursor.execute("""SELECT * FROM fr_medals WHERE name ILIKE %(key)s""", dict(key='%'+kwfr+'%'))
            rows = cursor.fetchall()
            fr_medals = {}
            for row in rows:
                #medals[int(row[0])] = Medals(row[0], row[1], row[2], row[3], row[4])
                fr_medals[int(row[0])] = Fr_Medals(row[0], row[1], row[2],row[3])

            return render_template('Medals.html', current_time=now.ctime(), medals=medals.values(), kw=kw, medal_records=medal_records.values(), fr_medals=fr_medals.values())




    return render_template('Medals.html', current_time=now.ctime(), medals=medals.values(), medal_records=medal_records.values(), fr_medals=fr_medals.values())

@app.route('/update/<int:id>', methods=['POST', 'GET'])
def updatemedal(id):
    with dbcon.connect(app.config['dsn']) as conn:
        cursor = conn.cursor()
        cursor.execute("""
                SELECT * FROM medals WHERE id = %s
                """, (int(id),))
        rows = cursor.fetchall()
        #medal = Medals(rows[0][0], rows[0][1], rows[0][2], rows[0][3], rows[0][4])
        medal = Medals(rows[0][0], rows[0][1], rows[0][2], rows[0][3])
        print(medal.id)
    if request.method == 'POST' and 'add' in request.form:
        #year = request.form.get('year')
        gold = request.form.get('gold')
        silver = request.form.get('silver')
        bronze = request.form.get('bronze')

        with dbcon.connect(app.config['dsn']) as conn:
            cursor = conn.cursor()
            #cursor.execute("""UPDATE medals SET YEAR=%s, GOLD=%s, SILVER=%s, BRONZE=%s WHERE ID=%s""",(int(year), gold, silver, bronze,int(id),))
            cursor.execute("""UPDATE medals SET GOLD=%s, SILVER=%s, BRONZE=%s WHERE ID=%s""",(gold, silver, bronze,int(id),))
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

@app.route('/updatemedalfr/<int:id>', methods=['POST', 'GET'])
def updatemedalfr(id):
    with dbcon.connect(app.config['dsn']) as conn:
        cursor = conn.cursor()
        cursor.execute("""
                SELECT * FROM fr_medals WHERE id = %s
                """, (int(id),))
        rows = cursor.fetchall()
        fr_medals = Fr_Medals(rows[0][0], rows[0][1], rows[0][2],rows[0][3])
        print(fr_medals.id)
    if request.method == 'POST' and 'addfru' in request.form:
        name = request.form.get('name')
        age = request.form.get('age')

        with dbcon.connect(app.config['dsn']) as conn:
            cursor = conn.cursor()
            cursor.execute("""UPDATE fr_medals SET NAME=%s, AGE=%s WHERE ID=%s""",(name, int(age), int(id),))

            conn.commit()

            return redirect(url_for('medals_page'))
    now = datetime.datetime.now()
    return render_template('Medalsfrupdate.html', current_time=now.ctime(), fr_medals=fr_medals)


@app.route('/delete/<int:id>')
def deletemedal(id):
    try:
        with dbcon.connect(app.config['dsn']) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                DELETE FROM medals WHERE id = %s
                """, (int(id),))
            conn.commit()

    except dbcon.DatabaseError:
        flash('This line is connected to another table.')
        conn.rollback()
    finally:
        conn.close()
    return redirect(url_for('medals_page'))


@app.route('/deleterec/<int:id>')
def deletemedalrec(id):
    try:
        with dbcon.connect(app.config['dsn']) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                DELETE FROM medal_records WHERE id = %s
                """, (int(id),))
            conn.commit()
    except dbcon.DatabaseError:
        flash('This line is connected to another table.')
        conn.rollback()
    finally:
        conn.close()
    return redirect(url_for('medals_page'))

@app.route('/deletefr/<int:id>')
def deletemedalfr(id):

    with dbcon.connect(app.config['dsn']) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                DELETE FROM fr_medals WHERE id = %s
                """, (int(id),))
            conn.commit()

            return redirect(url_for('medals_page'))
