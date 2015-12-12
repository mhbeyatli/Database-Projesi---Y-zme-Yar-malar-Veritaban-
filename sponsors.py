import datetime
from flask import redirect
from flask import request
from flask import flash
from flask import url_for
from flask import render_template
from config import app

app.secret_key = 'many random bytes'


class Sponsors:
    def __init__(self,name, sponsor=None):
            self.swimmername=name
            self.birthyear=birthyear
            

@app.route('/sponsor', methods=['GET', 'POST'])
def sponsor_page():

    if 'delete' in request.form:
        keys = request.form.getlist('sponsor_to_delete')
        for key in keys:
            app.store.delete_sponsor(int(key))
            return redirect(url_for('records_page'))

    else:
        name = request.form['name']
        sponsor = request.form['sponsor']
        sponsor1=RecorLow(name,sponsor)
        app.store.add_sponsor(sponsor1)
        return redirect(url_for('records_page'))

@app.route('/sponsor/add')
def sponsor_edit():
    now = datetime.datetime.now()
    return render_template('sponsor_edit.html', current_time=now.ctime())

@app.route('/sponsor/update/',methods=['GET' , 'POST'])
def sponsor_update():
    if request.method == 'POST':
        name = request.form['name']
        sponsor = request.form['sponsor']
        keys = request.form.getlist('sponsor_to_update')
        for key in keys:
            app.store.update_sponsor(int(key),name,sponsor)
    return redirect(url_for('records_page'))

@app.route('/sponsor/update2/')
def sponsor_update2():
    sponsors = app.store.get_sponsor()
    now = datetime.datetime.now()
    return render_template('sponsor_update.html',sponsors=sponsors,current_time=now.ctime())

@app.route('/sponsor/search2')
def sponsor_search2():
    now = datetime.datetime.now()
    return render_template('sponsor_search.html', current_time=now.ctime())

@app.route('/sponsor/search', methods=['GET' , 'POST'])
def sponsor_search():
    if request.method == 'POST':
        word =request.form['word']
        sponsors=app.store.sponsor_search(word)
        now = datetime.datetime.now()
        return render_template('Records.html',sponsors=sponsors, current_time=now.ctime())
