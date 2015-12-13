import datetime
from flask import redirect
from flask import request
from flask import flash
from flask import url_for
from flask import render_template
from config import app

class Olympic:
    def __init__(self,Fullname,SwimmerId,Year,Poolid):
            self.Fullname = Fullname
            self.SwimmerId = SwimmerId
            self.Year = Year
            self.Poolid = Poolid
@app.route('/Olympics', methods=['GET', 'POST'])
def olympics_page():
    if request.method == 'GET':
        Olympics = app.store.get_olympics()
        now = datetime.datetime.now()
        return render_template('Olympics.html', Olympics=Olympics, current_time=now.ctime())
    elif 'deleteolympics' in request.form:
        keys = request.form.getlist('deleteolympics')
        for key in keys:
            app.store.delete_olympic(int(key))
            return redirect(url_for('olympics_page'))

    else:
        Fullname = request.form['Fullname']
        SwimmerId = request.form['SwimmerId']
        Year = request.form['Year']
        Poolid = request.form['Poolid']
        Olympics = Olympic(Fullname,SwimmerId,Year,Poolid)
        app.store.add_olympic(Olympics)
        return redirect(url_for('olympics_page', key=app.store.last_key))

@app.route('/Olympics/<int:key>')
def olympic_page(key):
    Olympic= app.store.get_olympic(key)
    now = datetime.datetime.now()
    return render_template('Olympics.html', Olympic=Olympic, current_time=now.ctime())

@app.route('/Olympics/add/')
def olympic_edit():
    now = datetime.datetime.now()
    return render_template('olympicsadd.html', current_time=now.ctime())


@app.route('/Olympics/update/',methods=['GET' , 'POST'])
def olympic_update():
    if request.method == 'POST':
        Fullname = request.form['Fullname']
        SwimmerId = request.form['SwimmerId']
        Year = request.form['Year']
        Poolid = request.form['Poolid']
        keys = request.form.getlist('olympics_to_update')
        for key in keys:
            app.store.update_olympic(int(key),Fullname,SwimmerId,Year,Poolid)
    return redirect(url_for('olympics_page'))

@app.route('/Olympic/update2/')
def olympic_update2():
    Olympics = app.store.get_olympics()
    now = datetime.datetime.now()
    return render_template('olympics_update.html',Olympics = Olympics,current_time=now.ctime())

@app.route('/Olympics/search2')
def olympic_search2():
    now = datetime.datetime.now()
    return render_template('olympics_search.html', current_time=now.ctime())

@app.route('/Olympics/search', methods=['GET' , 'POST'])
def olympic_search():
    if request.method == 'POST':
        word =request.form['word']
        Olympics=app.store.olympics_search(word)
        now = datetime.datetime.now()
        return render_template('Olympics.html', Olympics=Olympics, current_time=now.ctime())