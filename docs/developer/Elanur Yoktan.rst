######################################################
Developers Guide of Parts Implemented by Elanur Yoktan
######################################################

Openwater Swimming
==================

   In this section, there are 3 tables which are Openwater, Swimmers and Competition.
   And also in main page there is a table which include all tables.

Main Page of Openwater
----------------------

   In main page of openwater there is a table which created with multiple left joins 
   on 3 tables. get_openwall() function is used with GET method to write all rows in 
   the Openwater table and also swimmer and competition informations. 
   
      .. code-block:: python
      
            Openwater= app.store.get_openwall()
           
      .. code-block:: python
      
         query = "SELECT COMPETITION.ID, COMPETITION.COMPNAME, COMPETITION.LOCATION, 
                  OPENWATER.YEAR, COMPETITION.NUMBER_OF_SWIMMERS, COMPETITION.PRIZE, 
                  SWIMMERS.NAME, SWIMMERS.SURNAME 
                  FROM  OPENWATER LEFT JOIN COMPETITION 
                  ON COMPETITION.ID = OPENWATER.COMPID 
                  LEFT JOIN SWIMMERS 
                  ON SWIMMERS.ID = OPENWATER.WINNERID 
                  ORDER BY OPENWATER.YEAR"


Openwater Table
---------------

   Openwater table is used in "Comppetition Results" page. Operations for in this 
   table are add,delete and update. In this page get_openws() function is used with 
   GET method to write all rows in the Openwater table.
   
   .. code-block:: python
      
            Openwater= app.store.get_openws()
           
   .. code-block:: python
   
            query = "SELECT ID, COMPID, WINNERID, YEAR FROM OPENWATER ORDER BY YEAR" 
                       
Swimmers Table
--------------

   Swimmers table is used in "Swimmers" page. Operations for in this table are add,
   delete and search. In this page get_swimmers() function is used with GET method to 
   write all rows in the Swimmers table.
   
   .. code-block:: python
      
            Openwater= app.store.get_swimmers()
           
      .. code-block:: python
   
            query = "SELECT ID, NAME, SURNAME, NATIONALITY FROM SWIMMERS ORDER BY ID"
            
            
Competition Table
-----------------

   Competiton table is used in "Competition Info" page. Operations for in this table 
   are add, delete, update and search. In this page get_comps() function is used with
   GET method to write all rows in the Competition table.
   
   .. code-block:: python
      
            Openwater = app.store.get_swimmers()
           
   .. code-block:: python
   
            query = "SELECT ID,COMPNAME,NUMBER_OF_SWIMMERS, LOCATION, PRIZE FROM COMPETITION ORDER BY ID"

Add operation
~~~~~~~~~~~~~

   To add a new tuple, add button is clicked in the Openwater.html. With this button, 
   openw_add() function is called.

   This function returns to openw_add.html
   
   .. code-block:: python
   
         @app.route('/OpenWater/add')
         def openw_add():
         now = datetime.datetime.now()
         return render_template('openw_add.html', current_time=now.ctime())
         
         
   After submitting the text boxes in the openw_add.html, with the post method it 
   calls the openwater_page()/swimmers_page()/competitions_page() function and it goes 
   to the else part of this function.
   
   openwater_page():
   
   .. code-block:: python
   
         compid = request.form['compid']
         winnerid = request.form['winnerid']
         year = request.form['year'] 
         openw = Openw(compid,winnerid, year)
         app.store.add_openw(openw)
         return redirect(url_for('openwater_page', key=app.store.last_key))
         
   swimmers_page():
        
   .. code-block:: python
         
         name = request.form['name']
         surname = request.form['surname']
         nationality = request.form['nationality'] 
         swimmer = Swimmer(name,surname, nationality)
         app.store.add_swimmer(swimmer)
         return redirect(url_for('swimmers_page', key=app.store.last_key))


   competitions_page():
    
   .. code-block:: python
    
         compname = request.form['compname']
         snumber = request.form['snumber']
         location = request.form['location'] 
         prize = request.form['prize'] 
         comp = Competition(compname,snumber, location,prize)
         app.store.add_comp(comp)
         return redirect(url_for('competitions_page', key=app.store.last_key))
         
   In the store.py there is add_openw()/add_swimmer()/add_comp() function include 
   this query:
    
   add_openw():
    
   .. code-block:: python
         
         query = "INSERT INTO OPENWATER (COMPID, WINNERID,  YEAR) VALUES (%s, %s, %s)"
     
   add_swimmer():   
    
   .. code-block:: python
    
         query = "INSERT INTO SWIMMERS (NAME, SURNAME, NATIONALITY) VALUES (%s, %s, %s)"
    
   add_comp():
    
   .. code-block:: python
         
         query = "INSERT INTO COMPETITION (COMPNAME,NUMBER_OF_SWIMMERS, LOCATION,PRIZE) VALUES (%s, %s, %s,%s)"
     
   If foreign keys are used in table add function has an expectation in case of 
   unreasonable enters
     
   .. code-block:: python
     
         except dbapi2.DatabaseError:
            flash('There is no data has this id. Check winner id or competition id! ')
            connection.rollback()
     
Delete function
~~~~~~~~~~~~~~~

   To Delete a tuple, first tuple is selected by select box and Delete button is clicked.
   By clicking it, with the POST method openwater_page() function is called.
   
   .. code-block:: python
   
         elif 'delete' in request.form:
            keys = request.form.getlist('openw_to_delete')
            for key in keys:
               app.store.delete_openw(int(key))
               return redirect(url_for('openwater_page'))
               
   Sql query is:
        
   .. code-block:: python
   
         query = "DELETE FROM OPENWATER WHERE (ID = %s) "
         
   If tuple that wanted removed, is used in another table as a foreign key exceptation
   works. Because delete is restrict.
   
   .. code-block:: python
   
         except dbapi2.DatabaseError:
            flash('Cannot be deleted: this data is used in another table!')
            connection.rollback()
            
Update function
~~~~~~~~~~~~~~~

   For updating a tuple, related row is selected by select box and submitted by update
   button. With the POST method, openwater_page() function is called.
   
   .. code-block:: python
   
         elif 'update' in request.form:
            keys = request.form.getlist('openw_to_delete')
            for key in keys:
               return render_template('openw_update.html',key=key)
  
   This function returns key of the tuple that will be updated to openw_update.html

   .. code-block:: python
   
      def openw_update(key):
      if request.method == 'POST':
         compid = request.form['compid']
         winnerid = request.form['winnerid']
         year = request.form['year']
         keys = request.form.getlist('openw_to_update')
         app.store.update_openw(int(key),compid,winnerid,year)
         return redirect(url_for('openwater_page'))

   Key, compid, winnerid and year sending to update_openw() function in store.py. 
   Its query is:

   .. code-block:: python

       query = "UPDATE OPENWATER SET COMPID = %s, WINNERID = %s, YEAR = %s WHERE (ID = %s)"

   With this query, it is updated in database
   
   If foreign keys are used in table add function has an expectation in case of 
   unreasonable enters
     
     .. code-block:: python
     
         except dbapi2.DatabaseError:
            flash('There is no data has this id. Check winner id or competition id! ')
            connection.rollback()

Search Function
~~~~~~~~~~~~~~~

   For search function there is little textbox in the main table and search button. 
   When it is filled and clicked openw_search() function is called

    .. code-block:: python
    
         def openw_search():
            if request.method == 'POST':
            word =request.form['word']
            Openwater=app.store.search_openw(word)
            now = datetime.datetime.now()
            return render_template('OpenWater.html', Openwater=Openwater, current_time=now.ctime())
    

   Word that comes from the textbox is sent to the sql code to find some tuples and 
   it returns the all rows that are matched. query is:

   .. code-block:: python

        query = "SELECT ID, COMPID, WINNERID, YEAR FROM OPENWATER WHERE (ID = %s)"


   These matched tuples are sent to the main html and shown in the table. 
   
