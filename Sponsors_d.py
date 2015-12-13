import datetime
from flask import redirect
from flask import request
from flask import flash
from flask import url_for
from flask import render_template
from config import app

class Sponsor:
    def __init__(self,Sponsorid,Swimmername,Birthyear):
            self.Sponsorid = Sponsorid
            self.Swimmername = Swimmername
            self.Birthyear = Birthyear

@app.route('/Sponsors', methods=['GET', 'POST'])
def sponsors_page():
    if request.method == 'GET':
        Sponsors = app.store.get_sponsors()
        now = datetime.datetime.now()
        return render_template('Sponsors.html', Sponsors=Sponsors, current_time=now.ctime())
    elif 'deletesponsors' in request.form:
        keys = request.form.getlist('deletesponsors')
        for key in keys:
            app.store.delete_sponsor(int(key))
            return redirect(url_for('sponsors_page'))

    else:
        Sponsorid = request.form['Sponsorid']
        Swimmername = request.form['Swimmername']
        Birthyear= request.form['Birthyear']
        Sponsors = Sponsor(Sponsorid,Swimmername,Birthyear)
        app.store.add_sponsor(Sponsors)
        return redirect(url_for('sponsors_page', key=app.store.last_key))

@app.route('/Sponsors/<int:key>')
def sponsor_page(key):
    Sponsor= app.store.get_sponsor(key)
    now = datetime.datetime.now()
    return render_template('Sponsors.html', Sponsor=Sponsor, current_time=now.ctime())

@app.route('/Sponsors/add/')
def sponsor_edit():
    now = datetime.datetime.now()
    return render_template('sponsorsadd.html', current_time=now.ctime())


@app.route('/Sponsors/update/',methods=['GET' , 'POST'])
def sponsor_update():
    if request.method == 'POST':
        Sponsorid = request.form['Sponsorid']
        Swimmername = request.form['Swimmername']
        Birthyear = request.form['Birthyear']
        keys = request.form.getlist('sponsors_to_update')
        for key in keys:
            app.store.update_sponsor(int(key),Sponsorid,Swimmername,Birthyear)
    return redirect(url_for('sponsors_page'))

@app.route('/Sponsor/update2/')
def sponsor_update2():
    Sponsors = app.store.get_sponsors()
    now = datetime.datetime.now()
    return render_template('sponsors_update.html',Sponsors = Sponsors,current_time=now.ctime())

@app.route('/Sponsors/search2')
def sponsor_search2():
    now = datetime.datetime.now()
    return render_template('sponsors_search.html', current_time=now.ctime())

@app.route('/Sponsors/search', methods=['GET' , 'POST'])
def sponsor_search():
    if request.method == 'POST':
        word = request.form['word']
        Sponsors=app.store.sponsors_search(word)
        now = datetime.datetime.now()
        return render_template('Sponsors.html', Sponsors=Sponsors, current_time=now.ctime())