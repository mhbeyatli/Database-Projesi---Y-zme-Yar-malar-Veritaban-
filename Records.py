import datetime
from flask import redirect
from flask import request
from flask import flash
from flask import url_for
from flask import render_template
from config import app

app.secret_key = 'many random bytes'
class Record:
    def __init__(self, name, rec=None):
            self.name = name
            self.rec=rec

class Recor:
    def __init__(self, name, recor=None):
            self.name = name
            self.recor=recor

class RecorLow:
    def __init__(self,name, lowrecor=None):
            self.name=name
            self.lowrecor=lowrecor

@app.route('/Records', methods=['GET', 'POST'])
def records_page():
    if request.method == 'GET':
        Records = app.store.get_records()
        Recors=app.store.get_recors()
        LowRecors=app.store.get_lowrecors()
        now = datetime.datetime.now()
        return render_template('Records.html', Records=Records,Recors=Recors,LowRecors=LowRecors,current_time=now.ctime())
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

@app.route('/Recor/update/',methods=['GET' , 'POST'])
def recor_update():
    if request.method == 'POST':
        name = request.form['name']
        recor = request.form['recor']
        keys = request.form.getlist('recor_to_update')
        for key in keys:
            app.store.update_recor(int(key),name,recor)
    return redirect(url_for('records_page'))

@app.route('/Recor/update2/')
def recor_update2():
    Recors = app.store.get_recor()
    now = datetime.datetime.now()
    return render_template('recor_update.html',Recors=Recors,current_time=now.ctime())

@app.route('/Recor/search2')
def recor_search2():
    now = datetime.datetime.now()
    return render_template('recor_search.html', current_time=now.ctime())

@app.route('/Recor/search', methods=['GET' , 'POST'])
def recor_search():
    if request.method == 'POST':
        word =request.form['word']
        Recors=app.store.recor_search(word)
        now = datetime.datetime.now()
        return render_template('Records.html',Recors=Recors, current_time=now.ctime())

@app.route('/Lowrecor', methods=['GET', 'POST'])
def lowrecor_page():

    if 'delete' in request.form:
        keys = request.form.getlist('lowrecor_to_delete')
        for key in keys:
            app.store.delete_lowrecor(int(key))
            return redirect(url_for('records_page'))

    else:
        name = request.form['name']
        lowrecor = request.form['lowrecor']
        lowrecor1=RecorLow(name,lowrecor)
        app.store.add_lowrecor(lowrecor1)
        return redirect(url_for('records_page'))

@app.route('/Lowrecor/add')
def lowrecor_edit():
    now = datetime.datetime.now()
    return render_template('lowrecor_edit.html', current_time=now.ctime())

@app.route('/LowRecor/update/',methods=['GET' , 'POST'])
def lowrecor_update():
    if request.method == 'POST':
        name = request.form['name']
        lowrecor = request.form['lowrecor']
        keys = request.form.getlist('lowrecor_to_update')
        for key in keys:
            app.store.update_lowrecor(int(key),name,lowrecor)
    return redirect(url_for('records_page'))

@app.route('/LowRecor/update2/')
def lowrecor_update2():
    LowRecors = app.store.get_lowrecor()
    now = datetime.datetime.now()
    return render_template('lowrecor_update.html',LowRecors=LowRecors,current_time=now.ctime())

@app.route('/LowRecor/search2')
def lowrecor_search2():
    now = datetime.datetime.now()
    return render_template('lowrecor_search.html', current_time=now.ctime())

@app.route('/LowRecor/search', methods=['GET' , 'POST'])
def lowrecor_search():
    if request.method == 'POST':
        word =request.form['word']
        lowrecors=app.store.lowrecor_search(word)
        now = datetime.datetime.now()
        return render_template('Records.html',LowRecors=lowrecors, current_time=now.ctime())
