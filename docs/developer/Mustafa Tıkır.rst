##################################
Parts Implemented by Mustafa TIKIR
##################################

   The topic of this part is records of swimmers.

   There are 3 tables which are created in the elephantSQL. So, in the codes there is no code like create table...

   Also, each table has 4 fucntions. All operations are done aim of the implement these 4 functions for each table.

   How these functions work is going to be explained in this developer guide.

   All 3 tables' functions are quite similar. So, i am going to explain funcitons of one table. After that, developer will see
   codes are really similar.

   In this part, project has implemented in object oriented approach.

   Also, there are couples of connections about HTML, Python, SQL. These connections are going to be explained deeply.

   Project's codes start with implementing an web page with CSS codes. All, codes and pages related to html is stored in templates
   directory.

   All, html codes have css codes in this part of project and it is implemented with given code part

   .. code-block:: python

      {% extends "layout.html" %}
      {% block title %}Home{% endblock %}
      {% block content %}
         Write what ever you want
      {% endblock %}



   Also, the main page of html pages is home.html, and, Records page can be accessed from the main page and all other pages,
   cause the layout.html is added to all html pages.


   Let me explain how the functions' codes work.

   **Note**

   All functions are going to be explained just for Records list

1. Add Funciton
===============

   For adding an recor to database, add button in Records.html should be clicked. When it is clicked, a new page
   with form appears.

   .. code-block:: python

      <a href="{{ url_for('record_edit')}}"><input class="button" type="submit" value="Add" name="Add" /></a>

   This web page's name is record_edit.html. In this web page, the form for adding new data sould be fullfilled correctly.

   After save button is clicked, the form send its data to Records.py with the function records_page

    .. code-block:: python

      <form action="{{ url_for('records_page') }}" method="post">

   Records.py is the main python page for this part. It determines what is going to happen with given data, and it send forms or
   information to SQL statements which are stored in store.py.

   SQL statements stay as embedded in python codes in store.py

   So, lets turn back to add fucntion

   records_page's code is:

   .. code-block:: python

       @app.route('/Records', methods=['GET', 'POST'])
      def records_page():
          if request.method == 'GET':
              Records = app.store.get_records()
              Recors=app.store.get_recors()
              LowRecors=app.store.get_lowrecors()
              now = datetime.datetime.now()
              return render_template('Records.html', Records=Records,Recors=Recors,LowRecors=LowRecors,current_time=now.ctime())
          elif 'delete' in request.form:
              keys = request.form.getlist('records_to_delete')
              for key in keys:
                  app.store.delete_record(int(key))
                  return redirect(url_for('records_page'))

          else:
              name = request.form['name']
              rec = request.form['rec']
              record = Record(name, rec)
              app.store.add_record(record)
              return redirect(url_for('records_page', key=app.store.last_key))

   The given data has a POST value. Code select the else part. And, send the data to add_record function which is stored
    in store.py

    add_record's code is given below from store.py

   .. code-block:: python

       def add_record(self, record1):
           with dbapi2.connect(self.dsn) as connection:
               cursor = connection.cursor()
               query = "INSERT INTO RECO (NAME, REC) VALUES (%s, %s)"
               cursor.execute(query, (record1.name, record1.rec))
               connection.commit()

   With this code, add_record gets the data as variable name record1, and sends it to SQL statement as a parameter.

   SQL statement is INSERT INTO "table name"(value1,value2) VALUES(%s %s)


2. Delete Function
==================

   For deleteing an record from database, empty button sould be clicked which stands on left hand side of that record,
    and delete button sould be clicked.

    When delete button is pressed, code sends the button and delete parameter to record_page function in Records.py

    .. code-block:: python

      <input class="button" type="submit" value="Delete" name="delete" />

    After it is sended , records_page function selects the elif statement, and finds the button which is clicked,
    and sends the paramanters t delete_record fuction which is in store.py

    .. code-block:: python

      @app.route('/Records', methods=['GET', 'POST'])
      def records_page():
          if request.method == 'GET':
              Records = app.store.get_records()
              Recors=app.store.get_recors()
              LowRecors=app.store.get_lowrecors()
              now = datetime.datetime.now()
              return render_template('Records.html', Records=Records,Recors=Recors,LowRecors=LowRecors,current_time=now.ctime())
          elif 'delete' in request.form:
              keys = request.form.getlist('records_to_delete')
              for key in keys:
                  app.store.delete_record(int(key))
                  return redirect(url_for('records_page'))

          else:
              name = request.form['name']
              rec = request.form['rec']
              record = Record(name, rec)
              app.store.add_record(record)
              return redirect(url_for('records_page', key=app.store.last_key))

   When the parameters have sent to store.py delete fucntion gets the parameters and deletes that tuple with the SQL statement.
   If that tuple has foreign key in another table, that gives an database error and it is catched with python code.

    .. code-block:: python

          def delete_record(self, key):
           try:
               with dbapi2.connect(self.dsn) as connection:
                   cursor = connection.cursor()
                   query = "DELETE FROM RECO WHERE (ID = %s)"
                   cursor.execute(query, (key,))
                   connection.commit()
           except dbapi2.DatabaseError:
               flash('Cannot be deleted, if it record has a child or children')
               connection.rollback()
           finally:
               connection.close()

3. Update Function
==================

   For update function to implement, update button should be clicked in Records.html and it opens new page.

   That calls the update2 fucntion in Records.py.

   .. code-block:: python

      <input class="button" type="button" value="Update" name="update" onclick="location.href='Records/update2';" />

   And update2 fucniton is

   .. code-block:: python

         @app.route('/Records/update2/')
           def record_update2():
          Records = app.store.get_records()
          now = datetime.datetime.now()
          return render_template('record_update.html',Records=Records,current_time=now.ctime())

   get_records function gets all the records from database and returns them.

   Body of get_record() fuction

   .. code-block:: python

       def get_records(self):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "SELECT ID, NAME, REC FROM RECO ORDER BY ID"
            cursor.execute(query)
            Records = [(key, Record(name, rec))
                      for key, name, rec in cursor]
            return Records

   So, after that record_update.html show us all the data in database, and it is ready to update.

   In this page, desired tuple have to be selected and its new data should be entered.

   After that, save button sould be clicked.

   When the save button is clicked, the update2 fucntion in Records.py is called.

   After the necessary things is done, record_update function in Records.py is going to be called.

   And that function arranges the parameters and sends them to update_record function in store.py

   .. code-block:: python

      @app.route('/Records/update/',methods=['GET' , 'POST'])
      def record_update():
          if request.method == 'POST':
              name = request.form['name']
              rec = request.form['rec']
              keys = request.form.getlist('records_to_update')
              for key in keys:
                  app.store.update_record(int(key),name, rec)
          return redirect(url_for('records_page'))

   update_record function in store.py send the parameters to SQL query and updates that tuple

   .. code-block:: python

    def update_record(self, key, name, rec):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "UPDATE RECO SET NAME = %s, REC = %s WHERE (ID = %s)"
            cursor.execute(query, (name, rec, key))
            connection.commit()


4. Search Function
==================

   For implementing search function in Records list, search button for given table sould be pressed first.

   After it is pressed, Records.html page chances its directory. It calls search2 dunction in records.py

   .. code-block:: python

      <input class="button" type="button" value="Search" name="update" onclick="location.href='Records/search2';" />

   That directory calls the function record_search2()

   .. code-block:: python

         @app.route('/Records/search2')
          def record_search2():
          now = datetime.datetime.now()
          return render_template('record_search.html', current_time=now.ctime())

   That function calls the record_search.html

   In that html, desired swimmers name is entered, and after search button is clicked, record_search function in Records.py is called.

   .. code-block:: python

      @app.route('/Records/search', methods=['GET' , 'POST'])
      def record_search():
          if request.method == 'POST':
              word =request.form['word']
              Records=app.store.record_search(word)
              now = datetime.datetime.now()
              return render_template('Records.html', Records=Records, current_time=now.ctime())

   In that function, record_search function in store.py is called with given keyword.

   .. code-block:: python

       def record_search(self, tosearch):
               with dbapi2.connect(self.dsn) as connection:
                   cursor = connection.cursor()
                   query = "SELECT ID, NAME, REC FROM RECO WHERE (NAME LIKE %s)"
                   cursor.execute(query,(tosearch,))
                   Records = [(key, Record(name, rec))
                             for key, name, rec in cursor]
                   return Records


   This python code includes an SQL query, and that query searchs the given keyword in database. After operation is done,
   code returns the seached record.
