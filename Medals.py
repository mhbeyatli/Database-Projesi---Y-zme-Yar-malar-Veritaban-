import datetime

from flask import render_template

from config import app


@app.route('/Medals')
def medals_page():
    now = datetime.datetime.now()
    return render_template('Medals.html', current_time=now.ctime())