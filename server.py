import datetime
import os
import json
import re
from flask import render_template
from config import app
from store import Store
import Medals
import Openwater
import Styles
import Olympics_d
import Pools_d
import Records
import psycopg2 as dbapi2


def get_elephantsql_dsn(vcap_services):
    """Returns the data source name for ElephantSQL."""
    parsed = json.loads(vcap_services)
    uri = parsed["elephantsql"][0]["credentials"]["uri"]
    match = re.match('postgres://(.*?):(.*?)@(.*?)(:(\d+))?/(.*)', uri)
    user, password, host, _, port, dbname = match.groups()
    dsn = """user='{}' password='{}' host='{}' port={}
        dbname='{}'""".format(user, password, host, port, dbname)
    return dsn


@app.route('/')
def home_page():
    now = datetime.datetime.now()
    return render_template('home.html', current_time=now.ctime())


if __name__ == '__main__':

    VCAP_APP_PORT = os.getenv('VCAP_APP_PORT')
    if VCAP_APP_PORT is not None:
        port, debug = int(VCAP_APP_PORT), False
    else:
        port, debug = 5000, True
    VCAP_SERVICES = os.getenv('VCAP_SERVICES')
    if VCAP_SERVICES is not None:
        app.config['dsn'] = get_elephantsql_dsn(VCAP_SERVICES)
    else:
        app.config['dsn'] = """dbname='xwacqlyq' host='jumbo.db.elephantsql.com' port=5432 user='xwacqlyq' password='eDso0SkacPcR_R6fDRmk0iISfAqh9xjN'"""
    app.store=Store(app.config['dsn'])
    app.run(host='0.0.0.0', port=port, debug=debug)

