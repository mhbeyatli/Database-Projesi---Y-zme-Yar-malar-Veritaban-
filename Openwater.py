import datetime
from flask import redirect
from flask import request
from flask import url_for
from flask import render_template
from config import app

class Openw: 
    def __init__(self, comp, winnerid, year=None): 
        self.comp = comp
        self.winnerid = winnerid
        self.year = year

@app.route('/OpenWater', methods=['GET', 'POST'])
def openwater_page():
    if request.method == 'GET':
        Openwater = app.store.get_openw()
        now = datetime.datetime.now()
        return render_template('OpenWater.html', Openwater=Openwater,
                               current_time=now.ctime())
    elif 'delete' in request.form:
        keys = request.form.getlist('openw_to_delete')
        for key in keys:
            app.store.delete_openw(int(key))
            return redirect(url_for('openwater_page'))
 
    else:
        comp = request.form['competition']
        winner = request.form['winner']
        year = request.form['year']
        openw = Openw(comp,winner, year)
        app.store.add_openw(openw)
        return redirect(url_for('openwater_page'))
    
@app.route('/OpenWater/<int:key>')
def openw_page(key):
    Openwater= app.store.get_openw(key)
    now = datetime.datetime.now()
    return render_template('OpenWater.html', Openwater=Openwater, current_time=now.ctime())

@app.route('/OpenWater/add')
def openw_add():
    now = datetime.datetime.now()
    return render_template('openw_add.html', current_time=now.ctime())

@app.route('/OpenWater/update/',methods=['GET' , 'POST'])
def openw_update():
    if request.method == 'POST':
        comp = request.form['competition']
        winner = request.form['winner']
        year = request.form['year']
        keys = request.form.getlist('openw_to_update')
        for key in keys:
            app.store.update_openw(int(key),comp,winner,year)
    return redirect(url_for('openwater_page'))
                                
@app.route('/OpenWater/update2/')
def openw_update2():
    Openwater = app.store.get_openw()
    now = datetime.datetime.now()
    return render_template('openw_update.html',Openwater=Openwater,current_time=now.ctime())

@app.route('/OpenWater/search2')
def openw_search2():
    now = datetime.datetime.now()
    return render_template('openw_search.html', current_time=now.ctime())

@app.route('/OpenWater/search', methods=['GET' , 'POST'])
def openw_search():
    if request.method == 'POST':
        word =request.form['word']
        Openwater=app.store.search_openw(word)
        now = datetime.datetime.now()
        return render_template('OpenWater.html', Openwater=Openwater, current_time=now.ctime())

@app.route('/OpenWater/tables')
def openw_tables():
    now = datetime.datetime.now()
    return render_template('openw_tables.html', current_time=now.ctime())
