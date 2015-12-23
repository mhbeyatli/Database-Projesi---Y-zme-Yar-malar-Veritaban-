##################################################
Developers Guide of Parts Implemented by ANIL AĞCA
##################################################


1.Pools
#######

1.1.Pools Table at SQL
======================


Pools table structurally has five attributes. Additional to pool name, pool id, area, city also listno is an attribute of pools table which is not being shown to end-user in any case. Listno is being used only for ordering the pools by the time they are entered. Pools table has created by following SQL code;

        .. code-block:: sql
        
               CREATE TABLE POOLS ( 
               ID INTEGER PRIMARY KEY,
               POOLNAME VARCHAR(100) UNIQUE NOT NULL, 
               CITY VARCHAR(30) NOT NULL,
               AREA INTEGER ) 

1.2.Pools Section’s HTML Files
==============================
Pools section uses four html files, in order to execute operations and show content of the table which are, “Pools.html”, “poolsadd.html”, “poolsupdate.html”, “pools_search.html”. At beginning of each html file we have main menu extended at the top (Line 1) title of the page(Line 2) and sub-menu for pools(Lines 3,4,5).

    .. code-block:: python
    
            1  {% extends "layout.html" %}
            2  {% block title %}Pools{% endblock %}
            3  <a href="{{ url_for('pool_edit')}}">Add Pool</a>
            4  <a href="{{ url_for('pool_update2')}}">Update Pools</a>
            5  <a href={{ url_for('pool_search2')}}>Search Pools</a>

1.2.1.Pools.html
================

Pools.html is being used for showing the current records to user and deleting chosen record by clicking delete button. Pools.html file is a returning by web api at /Pools route

    .. code-block:: python
    
      {% for key, Pool in Pools %}

Gathering a Pool for each time for a loop and printing it into the table which has columns as


     .. code-block:: python
     
            <th class="t1">Delete </th>
            <th class="t1">#Poolid </th>
            <th class="t1">Pool Name</th>
            <th class="t1">City</th>
            <th class="t1">Area</th>
   
And after gathering pool object at each time printing the row with;


    .. code-block:: python
    
         1  <td><input type="checkbox" name="deletepools"
         2  value="{{ key }}" /></td>
         3  <td class="t1">
         4  {{ Pool.Id }}
         5  </td>
         6  <td class="t1">
         7  {{Pool.Poolname}}
         8  </td>
         9  <td class="t1">
         10 {{ Pool.City }}
         11 </td>
         12 <td class="t1">
         13 {{Pool.Area}}
         14 </td>
At lines 4,7,10,13 prints attribute of the pool and line 1,2 creates a box which makes user able to delete the row by ticking and pressing delete button at the bottom of the page. By ticking this box html file will send message “deletepools” with a key to the python application and python will do rest of the operations.


1.2.2.poolsadd.html file
------------------------
poolsadd.html file which can be reached with route /Pools/add/ contains a form with four blank textboxes with ‘required’ and ‘autofocus’ attributes, for each value-needed attribute in it. 

1.2.3.pools_update.html file
----------------------------
Pools are being printed again like at pools.html only instead of delete checkbox, with an update checkbox added which added with following code ; 

      .. code-block:: python  
          
            <td><input type="checkbox" name="pools_to_update"
            value="{{ key }}" /></td>

Checkbox sends the key of the row and “pools_to_update” to application. After clicking the Update button.
Also form in poolsadd.html is added into this page inorder to gather new information about the updating row from the user. 

1.2.4.pools_search.html file
----------------------------
Has simple interface for search operation with a box for entering the keyword and a button for start the search. With following code

    .. code-block:: python
        
         <form action="{{ url_for('recor_search') }}" method="post">
         <table class="t1">
         <tr>
          <th>Enter the Keyword for search:</th>
          <td>
          <input type="text" name="word" required autofocus />
          </td>
          </tr>
         </table>
         <input value="Search" name="search" type="submit" />
         </form>

1.3. Python rendering and referencing functions of pools table
==============================================================
Python functions are being stored at two files which are store.py and Pools_d.py, Olympics_d.py, Sponsors_d.py. At Pools_d.py functions that are being used for rendering and establishing connection between HTML and other python functions at store.py. All functions at Pools_d.py, Olympics_d.py, Sponsors_d.py calls the related function at store.py with parameters taken from HTML, and sends renders the returning page from HTML files with taken data from SQL if any. Functions in Pools_d.py can be seen below.


   .. code-block:: python
   
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
                        return redirect(url_for('pools_page'))
            
                else:
                    Id = request.form['Id']
                    Poolname = request.form['Poolname']
                    City = request.form['City']
                    Area = request.form['Area']
                    Pools = Pool(Id,Poolname,City,Area)
                    app.store.add_pool(Pools)
                    return redirect(url_for('pools_page', key=app.store.last_key))
            
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
         

The way of working all of Pools_d.py functions, each of them is being triggered by @app.route(‘/route’). If user is asking for ‘route’ then the function after @app.route(‘/route’) is being triggered. After function below app.route takes parameters from HTML that entered by user if any and sending them to related function at store.py. Next, takes the results and renders an HTML file with results.

1.4.Pools Section’s Operation Functions
=======================================
Store.py functions are being called by only functions at Pools_d.py. Those functions are responsible for sending and taking data from SQL server with pre-written SQL codes that has gaps will be filled by user or function’s parameters data. Related codes attached below.


    .. code-block:: python
          def get_pool(self, key):
            with dbapi2.connect(self.dsn) as connection:
                cursor = connection.cursor()
                query = "SELECT ID,POOLNAME,CITY,AREA FROM POOLS WHERE (LISTNO = %s)"
                cursor.execute(query, (key,))
                Id,Poolname,City,Area = cursor.fetchone()
                return Pool(Id,Poolname,City,Area)
Function is being used for getting one pool at a time. Being used for operations needs only one object to be transferred i.e. Selecting operation.


    .. code-block:: python
       def get_pools(self):
           with dbapi2.connect(self.dsn) as connection:
               cursor = connection.cursor()
               query = "SELECT LISTNO,ID,POOLNAME,CITY,AREA FROM POOLS ORDER BY LISTNO"
               cursor.execute(query)
               Pools = [(key, Pool(Id,Poolname,City,Area))
                         for key,Id,Poolname,City,Area in cursor]
               return Pools

Function is being used for multiple transfers of Pools i.e. main page of the pools with whole pools table in it.

    .. code-block:: python
    
       def add_pool(self, Newpool):
           with dbapi2.connect(self.dsn) as connection:
               cursor = connection.cursor()
               query = "INSERT INTO POOLS (ID,POOLNAME,CITY,AREA ) VALUES (%s, %s, %s, %s)"
               cursor.execute(query, (Newpool.Id, Newpool.Poolname,Newpool.City, Newpool.Area))
               connection.commit()
               self.last_key = cursor.lastrowid

Function being used in order to add new pool. Takes parameters from function at Pools_d puts them at correct place at pre-written SQL code then executes it.
    .. code-block:: python
    
       def delete_pool(self, key):
           try:
               with dbapi2.connect(self.dsn) as connection:
                   cursor = connection.cursor()
                   query = "DELETE FROM POOLS WHERE (LISTNO = %s)"
                   cursor.execute(query, (key,))
                   connection.commit()
           except dbapi2.DatabaseError:
               flash('Due this PoolId is being used in Olympics table currently,Row cannot be deleted.')
               connection.rollback()
           finally:
               connection.close()

Function is being used at deleting operation. Has an additional try-except-finally block which is being used for error messages at deletion in restricted deletion operations. Check Error Messages page for more information.

   
    .. code-block:: python
    
          def update_pool(self, key,Id,Poolname,City,Area):
           with dbapi2.connect(self.dsn) as connection:
               cursor = connection.cursor()
               query = "UPDATE POOLS SET ID = %s, POOLNAME = %s, CITY = %s, AREA = %s WHERE (LISTNO = %s)"
               cursor.execute(query, (Id,Poolname,City,Area,key))
               connection.commit()

Function is being used for update operation. Puts parameters correct places at pre-written SQL code then executes it.

 
    .. code-block:: python
    
          def pools_search(self, word):
               with dbapi2.connect(self.dsn) as connection:
                   cursor = connection.cursor()
                   query = "SELECT LISTNO,ID,POOLNAME,CITY,AREA FROM POOLS WHERE (POOLNAME LIKE %s)"
                   cursor.execute(query,(word,))
                   Pools = [(key, Pool(Id,Poolname,City,Area))
                             for key,Id,Poolname,City,Area in cursor]
                   return Pools
   
Function is being used for Search operation. Takes entered keyword as parameter and puts it in right place at pre-written SQL code. After with code being executed function takes results and returns them to called Pools_d.py which returns it to user.


2.Olympics
##########
2.1. Olympics table at SQL
==========================
Olympics table has five attributes. Four of them are being seen by user and two foreign keys which references ‘Pools’ and ‘Sponsors’ tables. And the attribute named LISTNO that not being seen by user is being used for ordering rows. Code for creating table at SQL can be seen below.



    .. code-block:: python

      CREATE TABLE OLYMPICS( 
      LISTNO SERIAL PRIMARY KEY,
      FULLNAME VARCHAR(20), 
      SPONSORID INTEGER 
      REFERENCES SPONSORS(SPONSORID)
      ON DELETE RESTRICT ON UPDATE, 
      YEAR INTEGER,
      POOLID INTEGER REFERENCES POOLS(ID)
      ON DELETE RESTRICT ON UPDATE CASCADE ) 

1.2.Pools Section’s HTML Files
==============================
Pools section uses four html files, in order to execute operations and show content of the table which are, “Pools.html”, “poolsadd.html”, “poolsupdate.html”, “pools_search.html”. At beginning of each html file we have main menu extended at the top (Line 1) title of the page(Line 2) and sub-menu for pools(Lines 3,4,5).

    .. code-block:: python
    
            1  {% extends "layout.html" %}
            2  {% block title %}Pools{% endblock %}
            3  <a href="{{ url_for('pool_edit')}}">Add Pool</a>
            4  <a href="{{ url_for('pool_update2')}}">Update Pools</a>
            5  <a href={{ url_for('pool_search2')}}>Search Pools</a>

1.2.1.Pools.html
================

Pools.html is being used for showing the current records to user and deleting chosen record by clicking delete button. Pools.html file is a returning by web api at /Pools route

    .. code-block:: python
    
      {% for key, Pool in Pools %}

Gathering a Pool for each time for a loop and printing it into the table which has columns as


     .. code-block:: python
     
            <th class="t1">Delete </th>
            <th class="t1">#Poolid </th>
            <th class="t1">Pool Name</th>
            <th class="t1">City</th>
            <th class="t1">Area</th>
   
And after gathering pool object at each time printing the row with;


    .. code-block:: python
    
         1  <td><input type="checkbox" name="deletepools"
         2  value="{{ key }}" /></td>
         3  <td class="t1">
         4  {{ Pool.Id }}
         5  </td>
         6  <td class="t1">
         7  {{Pool.Poolname}}
         8  </td>
         9  <td class="t1">
         10 {{ Pool.City }}
         11 </td>
         12 <td class="t1">
         13 {{Pool.Area}}
         14 </td>
At lines 4,7,10,13 prints attribute of the pool and line 1,2 creates a box which makes user able to delete the row by ticking and pressing delete button at the bottom of the page. By ticking this box html file will send message “deletepools” with a key to the python application and python will do rest of the operations.


1.2.2.poolsadd.html file
------------------------
poolsadd.html file which can be reached with route /Pools/add/ contains a form with four blank textboxes with ‘required’ and ‘autofocus’ attributes, for each value-needed attribute in it. 

1.2.3.pools_update.html file
----------------------------
Pools are being printed again like at pools.html only instead of delete checkbox, with an update checkbox added which added with following code ; 

      .. code-block:: python  
          
            <td><input type="checkbox" name="pools_to_update"
            value="{{ key }}" /></td>

Checkbox sends the key of the row and “pools_to_update” to application. After clicking the Update button.
Also form in poolsadd.html is added into this page inorder to gather new information about the updating row from the user. 

1.2.4.pools_search.html file
----------------------------
Has simple interface for search operation with a box for entering the keyword and a button for start the search. With following code

    .. code-block:: python
        
         <form action="{{ url_for('recor_search') }}" method="post">
         <table class="t1">
         <tr>
          <th>Enter the Keyword for search:</th>
          <td>
          <input type="text" name="word" required autofocus />
          </td>
          </tr>
         </table>
         <input value="Search" name="search" type="submit" />
         </form>


2.3. Python rendering and referencing functions of pools table
==============================================================
Python functions are being stored at two files which are store.py and Pools_d.py, Olympics_d.py, Sponsors_d.py. At Pools_d.py functions that are being used for rendering and establishing connection between HTML and other python functions at store.py. All functions at Pools_d.py, Olympics_d.py, Sponsors_d.py calls the related function at store.py with parameters taken from HTML, and sends renders the returning page from HTML files with taken data from SQL if any. Functions in Pools_d.py can be seen below.


   .. code-block:: python
   
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
                        return redirect(url_for('pools_page'))
            
                else:
                    Id = request.form['Id']
                    Poolname = request.form['Poolname']
                    City = request.form['City']
                    Area = request.form['Area']
                    Pools = Pool(Id,Poolname,City,Area)
                    app.store.add_pool(Pools)
                    return redirect(url_for('pools_page', key=app.store.last_key))
            
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
         

1.4.Pools Section’s Operation Functions
=======================================
Store.py functions are being called by only functions at Pools_d.py. Those functions are responsible for sending and taking data from SQL server with pre-written SQL codes that has gaps will be filled by user or function’s parameters data. Related codes attached below.


    .. code-block:: python
          def get_pool(self, key):
            with dbapi2.connect(self.dsn) as connection:
                cursor = connection.cursor()
                query = "SELECT ID,POOLNAME,CITY,AREA FROM POOLS WHERE (LISTNO = %s)"
                cursor.execute(query, (key,))
                Id,Poolname,City,Area = cursor.fetchone()
                return Pool(Id,Poolname,City,Area)
Function is being used for getting one pool at a time. Being used for operations needs only one object to be transferred i.e. Selecting operation.


    .. code-block:: python
       def get_pools(self):
           with dbapi2.connect(self.dsn) as connection:
               cursor = connection.cursor()
               query = "SELECT LISTNO,ID,POOLNAME,CITY,AREA FROM POOLS ORDER BY LISTNO"
               cursor.execute(query)
               Pools = [(key, Pool(Id,Poolname,City,Area))
                         for key,Id,Poolname,City,Area in cursor]
               return Pools

Function is being used for multiple transfers of Pools i.e. main page of the pools with whole pools table in it.

    .. code-block:: python
    
       def add_pool(self, Newpool):
           with dbapi2.connect(self.dsn) as connection:
               cursor = connection.cursor()
               query = "INSERT INTO POOLS (ID,POOLNAME,CITY,AREA ) VALUES (%s, %s, %s, %s)"
               cursor.execute(query, (Newpool.Id, Newpool.Poolname,Newpool.City, Newpool.Area))
               connection.commit()
               self.last_key = cursor.lastrowid

Function being used in order to add new pool. Takes parameters from function at Pools_d puts them at correct place at pre-written SQL code then executes it.
    .. code-block:: python
    
       def delete_pool(self, key):
           try:
               with dbapi2.connect(self.dsn) as connection:
                   cursor = connection.cursor()
                   query = "DELETE FROM POOLS WHERE (LISTNO = %s)"
                   cursor.execute(query, (key,))
                   connection.commit()
           except dbapi2.DatabaseError:
               flash('Due this PoolId is being used in Olympics table currently,Row cannot be deleted.')
               connection.rollback()
           finally:
               connection.close()

Function is being used at deleting operation. Has an additional try-except-finally block which is being used for error messages at deletion in restricted deletion operations. Check Error Messages page for more information.

   
    .. code-block:: python
    
          def update_pool(self, key,Id,Poolname,City,Area):
           with dbapi2.connect(self.dsn) as connection:
               cursor = connection.cursor()
               query = "UPDATE POOLS SET ID = %s, POOLNAME = %s, CITY = %s, AREA = %s WHERE (LISTNO = %s)"
               cursor.execute(query, (Id,Poolname,City,Area,key))
               connection.commit()

Function is being used for update operation. Puts parameters correct places at pre-written SQL code then executes it.

 
    .. code-block:: python
    
          def pools_search(self, word):
               with dbapi2.connect(self.dsn) as connection:
                   cursor = connection.cursor()
                   query = "SELECT LISTNO,ID,POOLNAME,CITY,AREA FROM POOLS WHERE (POOLNAME LIKE %s)"
                   cursor.execute(query,(word,))
                   Pools = [(key, Pool(Id,Poolname,City,Area))
                             for key,Id,Poolname,City,Area in cursor]
                   return Pools
   
Function is being used for Search operation. Takes entered keyword as parameter and puts it in right place at pre-written SQL code. After with code being executed function takes results and returns them to called Pools_d.py which returns it to user.



3. Sponsors
###########

3.1.Sponsors Table at SQL
=========================

Sponsors table has four attributes structurally which are ListNo, Sponsorid,SponsorName, Year. ListNo is being used only for ordering the rows and not being shown to user in any case. Primary key of the table Is ID and being referenced by Olympics table in order to get additional information with a sponsor having that id without using any additional rows at Olympics table.Sponsors table has been created by following SQL code;


      .. code-block:: python

         CREATE TABLE SPONSORS( 
         LISTNO SERIAL,
         SPONSORID INTEGER PRIMARY KEY,
         SPONSORNAME VARCHAR(30),
         YEAR INTEGER )
3.3. Python rendering and referencing functions of pools table
==============================================================
Python functions are being stored at two files which are store.py and Pools_d.py, Olympics_d.py, Sponsors_d.py. At Pools_d.py functions that are being used for rendering and establishing connection between HTML and other python functions at store.py. All functions at Pools_d.py, Olympics_d.py, Sponsors_d.py calls the related function at store.py with parameters taken from HTML, and sends renders the returning page from HTML files with taken data from SQL if any. Functions in Pools_d.py can be seen below.


   .. code-block:: python
   
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
                        return redirect(url_for('pools_page'))
            
                else:
                    Id = request.form['Id']
                    Poolname = request.form['Poolname']
                    City = request.form['City']
                    Area = request.form['Area']
                    Pools = Pool(Id,Poolname,City,Area)
                    app.store.add_pool(Pools)
                    return redirect(url_for('pools_page', key=app.store.last_key))
            
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
         
1.4.Pools Section’s Operation Functions
=======================================
Store.py functions are being called by only functions at Pools_d.py. Those functions are responsible for sending and taking data from SQL server with pre-written SQL codes that has gaps will be filled by user or function’s parameters data. Related codes attached below.


    .. code-block:: python
          def get_pool(self, key):
            with dbapi2.connect(self.dsn) as connection:
                cursor = connection.cursor()
                query = "SELECT ID,POOLNAME,CITY,AREA FROM POOLS WHERE (LISTNO = %s)"
                cursor.execute(query, (key,))
                Id,Poolname,City,Area = cursor.fetchone()
                return Pool(Id,Poolname,City,Area)
Function is being used for getting one pool at a time. Being used for operations needs only one object to be transferred i.e. Selecting operation.


    .. code-block:: python
       def get_pools(self):
           with dbapi2.connect(self.dsn) as connection:
               cursor = connection.cursor()
               query = "SELECT LISTNO,ID,POOLNAME,CITY,AREA FROM POOLS ORDER BY LISTNO"
               cursor.execute(query)
               Pools = [(key, Pool(Id,Poolname,City,Area))
                         for key,Id,Poolname,City,Area in cursor]
               return Pools

Function is being used for multiple transfers of Pools i.e. main page of the pools with whole pools table in it.

    .. code-block:: python
    
       def add_pool(self, Newpool):
           with dbapi2.connect(self.dsn) as connection:
               cursor = connection.cursor()
               query = "INSERT INTO POOLS (ID,POOLNAME,CITY,AREA ) VALUES (%s, %s, %s, %s)"
               cursor.execute(query, (Newpool.Id, Newpool.Poolname,Newpool.City, Newpool.Area))
               connection.commit()
               self.last_key = cursor.lastrowid

Function being used in order to add new pool. Takes parameters from function at Pools_d puts them at correct place at pre-written SQL code then executes it.
    .. code-block:: python
    
       def delete_pool(self, key):
           try:
               with dbapi2.connect(self.dsn) as connection:
                   cursor = connection.cursor()
                   query = "DELETE FROM POOLS WHERE (LISTNO = %s)"
                   cursor.execute(query, (key,))
                   connection.commit()
           except dbapi2.DatabaseError:
               flash('Due this PoolId is being used in Olympics table currently,Row cannot be deleted.')
               connection.rollback()
           finally:
               connection.close()

Function is being used at deleting operation. Has an additional try-except-finally block which is being used for error messages at deletion in restricted deletion operations. Check Error Messages page for more information.

   
    .. code-block:: python
    
          def update_pool(self, key,Id,Poolname,City,Area):
           with dbapi2.connect(self.dsn) as connection:
               cursor = connection.cursor()
               query = "UPDATE POOLS SET ID = %s, POOLNAME = %s, CITY = %s, AREA = %s WHERE (LISTNO = %s)"
               cursor.execute(query, (Id,Poolname,City,Area,key))
               connection.commit()

Function is being used for update operation. Puts parameters correct places at pre-written SQL code then executes it.

 
    .. code-block:: python
    
          def pools_search(self, word):
               with dbapi2.connect(self.dsn) as connection:
                   cursor = connection.cursor()
                   query = "SELECT LISTNO,ID,POOLNAME,CITY,AREA FROM POOLS WHERE (POOLNAME LIKE %s)"
                   cursor.execute(query,(word,))
                   Pools = [(key, Pool(Id,Poolname,City,Area))
                             for key,Id,Poolname,City,Area in cursor]
                   return Pools
   
Function is being used for Search operation. Takes entered keyword as parameter and puts it in right place at pre-written SQL code. After with code being executed function takes results and returns them to called Pools_d.py which returns it to user.
         