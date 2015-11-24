import datetime
from flask import redirect
from flask import request
from flask import url_for
from flask import render_template
from config import app

class Record:
    def __init__(self, name, rec=None):
            self.name = name
            self.rec=rec

class Recor:
    def __init__(self, name, recor=None):
            self.name = name
            self.recor=recor
@app.route('/Records', methods=['GET', 'POST'])
def records_page():
    if request.method == 'GET':
        Records = app.store.get_records()
        now = datetime.datetime.now()
        return render_template('Records.html', Records=Records,current_time=now.ctime())
    elif 'delete' in request.form:
        keys = request.form.getlist('records_to_delete')
        for key in keys:
            app.store.delete_record(int(key))
            return redirect(url_for('records_page'))

    else:
        name = request.form['name']
        rec = request.form['rec']
        record = Record(name, rec)
        app.store.add_record(record)
        return redirect(url_for('records_page', key=app.store.last_key))

@app.route('/Records/<int:key>')
def record_page(key):
    Record= app.store.get_record(key)
    now = datetime.datetime.now()
    return render_template('Records.html', Record=Record, current_time=now.ctime())

@app.route('/Records/add')
def record_edit():
    now = datetime.datetime.now()
    return render_template('record_edit.html', current_time=now.ctime())

@app.route('/Records/update/',methods=['GET' , 'POST'])
def record_update():
    if request.method == 'POST':
        name = request.form['name']
        rec = request.form['rec']
        keys = request.form.getlist('records_to_update')
        for key in keys:
            app.store.update_record(int(key),name, rec)
    return redirect(url_for('records_page'))

@app.route('/Records/update2/')
def record_update2():
    Records = app.store.get_records()
    now = datetime.datetime.now()
    return render_template('record_update.html',Records=Records,current_time=now.ctime())

@app.route('/Records/search2')
def record_search2():
    now = datetime.datetime.now()
    return render_template('record_search.html', current_time=now.ctime())

@app.route('/Records/search', methods=['GET' , 'POST'])
def record_search():
    if request.method == 'POST':
        word =request.form['word']
        Records=app.store.record_search(word)
        now = datetime.datetime.now()
        return render_template('Records.html', Records=Records, current_time=now.ctime())



@app.route('/Recor', methods=['GET', 'POST'])
def recor_page():

    if 'delete' in request.form:
        keys = request.form.getlist('recor_to_delete')
        for key in keys:
            app.store.delete_recor(int(key))
            return redirect(url_for('records_page'))

    else:
        name = request.form['name']
        recor = request.form['recor']
        recor1=Recor(name,recor)
        app.store.add_recor(recor1)
        return redirect(url_for('records_page'))

@app.route('/Recor/add')
def recor_edit():
    now = datetime.datetime.now()
    return render_template('recor_edit.html', current_time=now.ctime())

