import datetime

from flask import render_template

from config import app



@app.route('/Records')
def records_page():
    now = datetime.datetime.now()
    return render_template('Records.html', current_time=now.ctime())