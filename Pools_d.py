import datetime
from flask import redirect
from flask import request
from flask import flash
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
        Pools = app.store.get_pools()
        now = datetime.datetime.now()
        return render_template('Pools.html', Pools=Pools, current_time=now.ctime())
    elif 'deletepools' in request.form:
        keys = request.form.getlist('deletepools')
        for key in keys:
            app.store.delete_pool(int(key))
            return redirect(url_for('pool_page'))

    else:
        Id = request.form['Id']
        Poolname = request.form['Poolname']
        City = request.form['City']
        Area = request.form['Area']
        Pools = Pool(Id,Poolname,City,Area)
        app.store.add_pool(Pools)
        return redirect(url_for('pool_page', key=app.store.last_key))

@app.route('/Pools/add/')
def pool_edit():
    now = datetime.datetime.now()
    return render_template('poolsadd.html', current_time=now.ctime())



@app.route('/Pools/<int:key>')
def pool_page(key):
        Pool= app.store.get_pool(key)
        now = datetime.datetime.now()
        return render_template('Pools.html', Pool=Pool, current_time=now.ctime())



@app.route('/Pools/update/',methods=['GET' , 'POST'])
def pool_update():
    if request.method == 'POST':
        Id = request.form['Id']
        Poolname = request.form['Poolname']
        City = request.form['City']
        Area = request.form['Area']
        keys = request.form.getlist('pools_to_update')
        for key in keys:
            app.store.update_pool(int(key),Id,Poolname,City,Area)
    return redirect(url_for('pools_page'))

@app.route('/Pools/update2/')
def pool_update2():
    Pools = app.store.get_pools()
    now = datetime.datetime.now()
    return render_template('pools_update.html',Pools = Pools,current_time=now.ctime())

@app.route('/Pools/search2')
def pool_search2():
    now = datetime.datetime.now()
    return render_template('pools_search.html', current_time=now.ctime())

@app.route('/Pools/search', methods=['GET' , 'POST'])
def pool_search():
    if request.method == 'POST':
        word =request.form['word']
        Pools=app.store.pools_search(word)
        now = datetime.datetime.now()
        return render_template('Pools.html', Pools=Pools, current_time=now.ctime())
