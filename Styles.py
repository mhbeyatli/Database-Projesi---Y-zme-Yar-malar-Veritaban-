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
        Styles = app.store.get_movies()
        now = datetime.datetime.now()
        return render_template('Styles.html', Styles=Styles,
                               current_time=now.ctime())
    elif 'styles_to_delete' in request.form:
        keys = request.form.getlist('styles_to_delete')
        for key in keys:
            app.store.delete_movie(int(key))
            return redirect(url_for('styles_page'))

    else:
        title = request.form['title']
        year = request.form['year']
        style = Style(title, year)
        app.store.add_movie(style)
        return redirect(url_for('style_page', key=app.store.last_key))

@app.route('/Styles/<int:key>')
def style_page(key):
    Style= app.store.get_movie(key)
    now = datetime.datetime.now()
    return render_template('Styles.html', Style=Style, current_time=now.ctime())


@app.route('/Styles/add')
def style_edit():
    now = datetime.datetime.now()
    return render_template('style_edit.html', current_time=now.ctime())


