import datetime

from flask import render_template

from config import app



@app.route('/OpenWater')
def openwater_page():
    now = datetime.datetime.now()
    return render_template('OpenWater.html', current_time=now.ctime())