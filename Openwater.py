import datetime
from flask import redirect
from flask import request
from flask import url_for
from flask import render_template
from config import app

class Openwall: 
    def __init__(self, comp,location,year,swimmers,prize, winnername, winnersurname ): 
        self.comp = comp
        self.location = location
        self.year = year
        self.swimmers = swimmers
        self.prize = prize
        self.winnername = winnername
        self.winnersurname = winnersurname

@app.route('/OpenWaterhome/')
def openwhome_page():
    Openwater= app.store.get_openwall()
    now = datetime.datetime.now()
    return render_template('Openwhome.html', Openwater=Openwater, current_time=now.ctime())
class Openw: 
    def __init__(self, compid, winnerid, year=None): 
        self.compid = compid
        self.winnerid = winnerid
        self.year = year

@app.route('/OpenWater/', methods=['GET', 'POST'])
def openwater_page():
    if request.method == 'GET':
        Openwater = app.store.get_openws()
        now = datetime.datetime.now()
        return render_template('OpenWater.html', Openwater=Openwater,
                               current_time=now.ctime())
    elif 'delete' in request.form:
        keys = request.form.getlist('openw_to_delete')
        for key in keys:
            app.store.delete_openw(int(key))
            return redirect(url_for('openwater_page'))
    elif 'update' in request.form:
        keys = request.form.getlist('openw_to_delete')
        for key in keys:
            return render_template('openw_update.html',key=key)
    else:
        compid = request.form['compid']
        winnerid = request.form['winnerid']
        year = request.form['year'] 
        openw = Openw(compid,winnerid, year)
        app.store.add_openw(openw)
        return redirect(url_for('openwater_page', key=app.store.last_key))

@app.route('/OpenWater/<int:key>')
def openw_page(key):
    Openw= app.store.get_openw(key)
    now = datetime.datetime.now()
    return render_template('OpenWater.html', Openw=Openw, current_time=now.ctime())

@app.route('/OpenWater/add')
def openw_add():
    now = datetime.datetime.now()
    return render_template('openw_add.html', current_time=now.ctime())


@app.route('/OpenWater/update/<key>',methods=['GET' , 'POST'])
def openw_update(key):
    if request.method == 'POST':
        compid = request.form['compid']
        winnerid = request.form['winnerid']
        year = request.form['year']
        keys = request.form.getlist('openw_to_update')
        app.store.update_openw(int(key),compid,winnerid,year)
        return redirect(url_for('openwater_page'))


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

class Swimmer: 
    def __init__(self ,name, surname, nationality): 
        self.name = name
        self.surname = surname
        self.nationality = nationality

@app.route('/Swimmers', methods=['GET', 'POST'])
def swimmers_page():
    if request.method == 'GET':
        Openwater = app.store.get_swimmers()
        now = datetime.datetime.now()
        return render_template('Swimmers.html', Openwater=Openwater,
                               current_time=now.ctime())
    elif 'delete' in request.form:
        keys = request.form.getlist('swimmer_to_delete')
        for key in keys:
            app.store.delete_swimmer(int(key))
            return redirect(url_for('swimmers_page'))
    elif 'update' in request.form:
        keys = request.form.getlist('swimmer_to_delete')
        for key in keys:
            return render_template('swimmer_update.html',key=key)
    else:
        name = request.form['name']
        surname = request.form['surname']
        nationality = request.form['nationality'] 
        swimmer = Swimmer(name,surname, nationality)
        app.store.add_swimmer(swimmer)
        return redirect(url_for('swimmers_page', key=app.store.last_key))

@app.route('/Swimmers/<int:key>')
def swimmer_page(key):
    Swimmer= app.store.get_swimmer(key)
    now = datetime.datetime.now()
    return render_template('Swimmers.html', Swimmer=Swimmer, current_time=now.ctime())

@app.route('/Swimmers/add')
def swimmer_add():
    now = datetime.datetime.now()
    return render_template('swimmer_add.html', current_time=now.ctime())


@app.route('/Swimmers/update/<key>',methods=['GET' , 'POST'])
def swimmer_update(key):
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        nationality = request.form['nationality']
        keys = request.form.getlist('swimmer_to_update')
        app.store.update_openw(int(key),name,surname,nationality)
        return redirect(url_for('swimmers_page'))


@app.route('/Swimmers/search2')
def swimmer_search2():
    now = datetime.datetime.now()
    return render_template('swimmer_search.html', current_time=now.ctime())

@app.route('/Swimmers/search', methods=['GET' , 'POST'])
def swimmer_search():
    if request.method == 'POST':
        word =request.form['word']
        Openwater=app.store.search_swimmer(word)
        now = datetime.datetime.now()
        return render_template('Swimmers.html', Openwater=Openwater, current_time=now.ctime())
  
class Competition: 
    def __init__(self ,compname,snumber,location, prize): 
        self.compname = compname
        self.snumber = snumber
        self.location = location 
        self.prize = prize
        
@app.route('/Competitions', methods=['GET', 'POST'])
def competitions_page():
    if request.method == 'GET':
        Openwater = app.store.get_comps()
        now = datetime.datetime.now()
        return render_template('Competitions.html', Openwater=Openwater,
                               current_time=now.ctime())
    elif 'delete' in request.form:
        keys = request.form.getlist('comp_to_delete')
        for key in keys:
            app.store.delete_comp(int(key))
            return redirect(url_for('competitions_page'))
    elif 'update' in request.form:
        keys = request.form.getlist('comp_to_delete')
        for key in keys:
            return render_template('comp_update.html',key=key)
    else:
        compname = request.form['compname']
        snumber = request.form['snumber']
        location = request.form['location'] 
        prize = request.form['prize'] 
        comp = Competition(compname,snumber, location,prize)
        app.store.add_comp(comp)
        return redirect(url_for('competitions_page', key=app.store.last_key))

@app.route('/Competitions/<int:key>')
def comp_page(key):
    Competition= app.store.get_comp(key)
    now = datetime.datetime.now()
    return render_template('Competitions.html', Competition=Competition, current_time=now.ctime())

@app.route('/Competitions/add')
def comp_add():
    now = datetime.datetime.now()
    return render_template('comp_add.html', current_time=now.ctime())


@app.route('/Competitions/update/<key>',methods=['GET' , 'POST'])
def comp_update(key):
    if request.method == 'POST':
        compname = request.form['compname']
        snumber = request.form['snumber']
        location = request.form['location']
        prize = request.form['prize']
        keys = request.form.getlist('comp_to_update')
        app.store.update_comp(int(key),compname,snumber,location,prize)
        return redirect(url_for('competitions_page'))

@app.route('/Competitions/search2')
def comp_search2():
    now = datetime.datetime.now()
    return render_template('comp_search.html', current_time=now.ctime())

@app.route('/Competitions/search', methods=['GET' , 'POST'])
def comp_search():
    if request.method == 'POST':
        word =request.form['word']
        Openwater=app.store.search_comp(word)
        now = datetime.datetime.now()
        return render_template('Competitions.html', Openwater=Openwater, current_time=now.ctime())
  
        
