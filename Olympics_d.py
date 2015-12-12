import datetime
from flask import redirect
from flask import request
from flask import url_for
from flask import render_template
from config import app
import Olympics
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
        Olympics = app.Olympics.get_olympics()
        now = datetime.datetime.now()
        return render_template('Olympics.html', Olympics=Olympics,
                               current_time=now.ctime())
    elif 'deleteolympics' in request.form:
        keys = request.form.getlist('deleteolympics')
        for key in keys:
            app.Olympics.delete_olympic(int(key))
            return redirect(url_for('olympic_page'))

    else:
        Listno = request.form['Listno']
        Fullname = request.form['Fullname']
        SwimmerId = request.form['SwimmerId']
        Year = request.form['Year']
        Poolid = request.form['Poolid']
        Olympic = Olympic(Listno,Fullname,SwimmerId,Year,Poolid)
        app.Olympics.add_olympic(Olympic)
        return redirect(url_for('olympic_page', key=app.Olympics.last_key))

@app.route('/Olympics/<int:key>')
def olympic_page(key):
    Olympic= app.Olympics.get_olympic(key)
    now = datetime.datetime.now()
    return render_template('Olympics.html', Olympic=Olympic, current_time=now.ctime())


@app.route('/Olympics/update')
def olympic_update():
        Toupdate = request.form['Toupdate']
        Listno = request.form['Listno']
        Fullname = request.form['Fullname']
        SwimmerId = request.form['SwimmerId']
        Year = request.form['Year']
        Poolid = request.form['Poolid']
        Olympic = Olympic(Listno,Fullname,SwimmerId,Year,Poolid)
        app.Olympics.Olympicupdate(Toupdate,Olympic)
        return redirect(url_for('olympic_page', key=app.Olympics.last_key))

@app.route('/Olympics/search')
def olympic_search():
        request.form['keywords']
        app.Olympics.olympicsearch(keywords)
        return render_template('olympics_search.html', Olympic=Olympic, current_time=now.ctime())