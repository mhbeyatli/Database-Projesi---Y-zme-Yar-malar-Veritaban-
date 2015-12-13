import datetime
from flask import redirect
from flask import request
from flask import flash
from flask import url_for
from flask import render_template
from config import app

app.secret_key = 'many random bytes'
class Style:
    def __init__(self, title, year=None):
            self.title = title
            self.year = year
class Women:
    def __init__(self,name=None,time=None,styleid=None):
            self.name= name
            self.time= time
            self.styleid=styleid
class Men:
    def __init__(self,name=None,time=None,styleid=None):
            self.name= name
            self.time= time
            self.styleid=styleid

@app.route('/Styles', methods=['GET', 'POST'])
def styles_page():
    if request.method == 'GET':
        Styles = app.store.get_styles()
        now = datetime.datetime.now()
        return render_template('Styles.html', Styles=Styles, current_time=now.ctime())
    elif 'delete' in request.form:
        keys = request.form.getlist('styles_to_delete')
        for key in keys:
            app.store.delete_style(int(key))
            return redirect(url_for('styles_page'))
    elif 'update' in request.form:
        keys = request.form.getlist('styles_to_delete')
        for key in keys:
            return render_template('style_update.html', key=key)
    else:
        title = request.form['title']
        year = request.form['year']
        app.store.add_style(title,year)
        return redirect(url_for('styles_page'))

@app.route('/Styles/<int:key>')
def style_page(key):
    Style=app.store.get_style(key)
    Allmen= app.store.get_men(key)
    Allwomen=app.store.get_women(key)
    now = datetime.datetime.now()
    return render_template('person.html', Allmen=Allmen, Allwomen=Allwomen, key=key, current_time=now.ctime())

@app.route('/Styles/add')
def style_edit():
    now = datetime.datetime.now()
    return render_template('style_edit.html', current_time=now.ctime())

@app.route('/Styles/update/<key>', methods=['GET', 'POST'])
def style_update(key):
    if request.method== 'POST':
        title = request.form['title']
        year = request.form['year']
        app.store.update_style(int(key),title,year)
    return redirect(url_for('styles_page'))


@app.route('/Styles/search', methods=['GET' , 'POST'])
def style_search():
    if request.method == 'POST':
        word =request.form['word']
        Styles=app.store.search_style(word)
        now = datetime.datetime.now()
        return render_template('Styles.html', Styles=Styles, current_time=now.ctime())

@app.route('/Person/<key>', methods=['GET', 'POST'])
def men_page(key):
    ids=key
    if request.method == 'GET':
        return redirect(url_for('style_page',key=ids))
    elif 'delete' in request.form:
        keys = request.form.getlist('person_to_delete')
        for key in keys:
            app.store.delete_men(int(key))
            return redirect(url_for('style_page',key=ids))
    elif 'update' in request.form:
        keys = request.form.getlist('person_to_delete')
        for key in keys:
            return render_template('men_update.html',key=key, ids=ids)
    else:
        name = request.form['name']
        time = request.form['time']
        styleid=key
        Man1=Men(name,time,styleid)
        app.store.add_men(Man1)
        now = datetime.datetime.now()
        return redirect(url_for('style_page',key=ids))
@app.route('/Person2/<key>', methods=['GET', 'POST'])
def women_page(key):
    ids=key
    if request.method == 'GET':
        return redirect(url_for('style_page',key=key))
    elif 'delete' in request.form:
        keys = request.form.getlist('person_to_delete')
        for key in keys:
            app.store.delete_women(int(key))
            return redirect(url_for('style_page',key=ids))
    elif 'update' in request.form:
        keys = request.form.getlist('person_to_delete')
        for key in keys:
            return render_template('women_update.html',key=key, ids=ids)

    else:
        name = request.form['name']
        time = request.form['time']
        styleid=key
        woman1=Women(name,time,styleid)
        app.store.add_women(woman1)
        return redirect(url_for('style_page',key=key))

@app.route('/Person/add/<key>')
def men_edit(key):
    now = datetime.datetime.now()
    return render_template('men_edit.html',key=key, current_time=now.ctime())
@app.route('/Person2/add/<key>')
def women_edit(key):
    now = datetime.datetime.now()
    return render_template('women_edit.html',key=key, current_time=now.ctime())
@app.route('/Person/update/<key>/<ids>',methods=['GET' , 'POST'])
def person_update(key,ids):
    if request.method == 'POST':
        name = request.form['name']
        time = request.form['time']
        styleid=ids
        app.store.update_men(key,name,time,styleid)
    return redirect(url_for('style_page',key=ids))

@app.route('/Person/update2/<key>/<ids>',methods=['GET' , 'POST'])
def person_update2(key,ids):
    if request.method == 'POST':
        name = request.form['name']
        time = request.form['time']
        styleid=ids
        app.store.update_women(key,name,time,styleid)
    return redirect(url_for('style_page',key=ids))

@app.route('/Person/search/<key>', methods=['GET' , 'POST'])
def men_search(key):
    ids=key
    if request.method == 'POST':
        word =request.form['word']
        Allmen= app.store.search_men(word,ids)
        now = datetime.datetime.now()
        return render_template('person.html',key=key, Allmen=Allmen, current_time=now.ctime())

@app.route('/Person2/search/<key>', methods=['GET' , 'POST'])
def women_search(key):
    ids=key
    if request.method == 'POST':
        word =request.form['word']
        Allwomen= app.store.search_women(word,ids)
        now = datetime.datetime.now()
        return render_template('person.html',key=key, Allwomen=Allwomen, current_time=now.ctime())
