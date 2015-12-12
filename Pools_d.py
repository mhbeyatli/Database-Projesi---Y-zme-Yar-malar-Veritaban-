import datetime
from flask import redirect
from flask import request
from flask import url_for
from flask import render_template
from config import app

class Pool:
    def __init__(self,Id,Poolname,City,Area):
            self.Id = Id
            self.Poolname = Poolname
            self.City = City
            self.Area = Area
@app.route('/Pools', methods=['GET', 'POST'])
def pools_page():
    if request.method == 'GET':
        Pools = app.Pools.get_pools()
        now = datetime.datetime.now()
        return render_template('Pools.html', Pools=Pools,
                               current_time=now.ctime())
    elif 'deletepools' in request.form:
        keys = request.form.getlist('deletepools')
        for key in keys:
            app.Pools.delete_pool(int(key))
            return redirect(url_for('pool_page'))

    else:
        Id = request.form['Id']
        Poolname = request.form['Poolname']
        City = request.form['City']
        Area = request.form['Area']
        Pool = Pool(Id,Poolname	,City,Area)
        app.Pools.add_pool(Pool)
        return redirect(url_for('pool_page', key=app.Pools.last_key))

@app.route('/Pools/<int:key>')
def pool_page(key):
        Pool= app.Pools.get_pool(key)
        now = datetime.datetime.now()
        return render_template('Pools.html', Pool=Pool, current_time=now.ctime())


@app.route('/Pools/update')
def pool_update():
        Toupdate = request.form['Toupdate']
        Id = request.form['Id']
        Poolname = request.form['Poolname']
        City = request.form['City']
        Area = request.form['Area']
        Pool = Pool(Id,Poolname,City,Area)
        app.Pools.Poolupdate(Toupdate,Pool)
        return redirect(url_for('pool_page', key=app.Pools.last_key))

@app.route('/Pools/search')
def pool_search():
        keywords = request.form['keywords']
        app.Pools.poolsearch(keywords)
        return render_template('pools_search.html', Pool=Pool, current_time=now.ctime())