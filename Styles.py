import datetime
from flask import redirect
from flask import request
from flask import url_for
from flask import render_template
from config import app

class Style:
    def __init__(self, title, year=None):
            self.title = title
            self.year = year

@app.route('/Styles', methods=['GET', 'POST'])
def styles_page():
    if request.method == 'GET':
        Styles = app.store.get_styles()
        now = datetime.datetime.now()
        return render_template('Styles.html', Styles=Styles,
                               current_time=now.ctime())
    elif 'delete' in request.form:
        keys = request.form.getlist('styles_to_delete')
        for key in keys:
            app.store.delete_style(int(key))
            return redirect(url_for('styles_page'))
 
    else:
        title = request.form['title']
        year = request.form['year']
        style = Style(title, year)
        app.store.add_style(style)
        return redirect(url_for('styles_page'))

@app.route('/Styles/<int:key>')
def style_page(key):
    Style= app.store.get_style(key)
    now = datetime.datetime.now()
    return render_template('Styles.html', Style=Style, current_time=now.ctime())

@app.route('/Styles/add')
def style_edit():
    now = datetime.datetime.now()
    return render_template('style_edit.html', current_time=now.ctime())

@app.route('/Styles/update/',methods=['GET' , 'POST'])
def style_update():
  def style_update():
    if request.method == 'POST':
        title = request.form['title']
        year = request.form['year']
        keys = request.form.getlist('styles_to_update')
        for key in keys:
            app.store.update_style(int(key),title,year)
    return redirect(url_for('styles_page'))
                                
@app.route('/Styles/update2/')
def style_update2():
    Styles = app.store.get_styles()
    return render_template('style_update.html',Styles=Styles)
    
@app.route('/Styles/search2')
def style_search2():
    now = datetime.datetime.now()
    return render_template('style_search.html', current_time=now.ctime())

@app.route('/Styles/search', methods=['GET' , 'POST'])
def style_search():
    if request.method == 'POST':
        word =request.form['word']
        Styles=app.store.search_style(word)
        now = datetime.datetime.now()
        return render_template('Styles.html', Styles=Styles, current_time=now.ctime())
