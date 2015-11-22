import datetime

from flask import render_template

from config import app


@app.route('/Olympics')
def olympics_page():
    now = datetime.datetime.now()
    return render_template('Olympics.html', current_time=now.ctime())