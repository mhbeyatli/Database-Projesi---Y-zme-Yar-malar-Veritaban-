import datetime
from flask import redirect
from flask import request
from flask import flash
from flask import url_for
from flask import render_template
from config import app

class Olympic:
    def __init__(self,Listno,Fullname,SwimmerId,Year,Poolid):
            self.Listno = Listno
            self.Fullname = Fullname
            self.SwimmerId = SwimmerId
            self.Year = Year
            self.Poolid = Poolid
@app.route('/Olympics', methods=['GET', 'POST'])
def olympics_page():
    if request.method == 'GET':
        Olympics = app.store.get_olympics()
        now = datetime.datetime.now()
        return render_template('Olympics.html', Olympics=Olympics,
                               current_time=now.ctime())
    elif 'deleteolympics' in request.form:
        keys = request.form.getlist('deleteolympics')
        for key in keys:
            app.store.delete_olympic(int(key))
            return redirect(url_for('olympic_page'))

    else:
        Listno = request.form['Listno']
        Fullname = request.form['Fullname']
        SwimmerId = request.form['SwimmerId']
        Year = request.form['Year']
        Poolid = request.form['Poolid']
        Olympic = Olympic(Listno,Fullname,SwimmerId,Year,Poolid)
        app.store.add_olympic(Olympic)
        return redirect(url_for('olympic_page', key=app.store.last_key))

@app.route('/Olympics/<int:key>')
def olympic_page(key):
    Olympic= app.store.get_olympic(key)
    now = datetime.datetime.now()
    return render_template('Olympics.html', Olympic=Olympic, current_time=now.ctime())

@app.route('/Records/add')
def record_edit():
    now = datetime.datetime.now()
    return render_template('oympicsadd.html', current_time=now.ctime())

@app.route('/Olympics/update/',methods=['GET' , 'POST'])
def olympic_update():
    if request.method == 'POST':
        Toupdate = request.form['Toupdate']
        Listno = request.form['Listno']
        Fullname = request.form['Fullname']
        SwimmerId = request.form['SwimmerId']
        Year = request.form['Year']
        Poolid = request.form['Poolid']
        Olympic = Olympic(Listno,Fullname,SwimmerId,Year,Poolid)
        app.store.Olympicupdate(Toupdate,Olympic)
        return redirect(url_for('olympic_page', key=app.store.last_key))

@app.route('/Olympics/search')
def olympic_search():
        request.form['keywords']
        app.store.olympicsearch(keywords)
        return render_template('olympics_search.html', Olympic=Olympic, current_time=now.ctime())