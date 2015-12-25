###########################################
Parts Implemented by Muhammed Habib Beyatlı
###########################################

Medals
======
      This is the html codes of the navigation bar of this section from layout.html.

      .. code-block:: python

                  <li class="nav"><a class= "nav" href="{{ url_for('medals_page')}}">Swimming Medals</a></li>

      These are the Bootstrap libraries in the layout.html.

      .. code-block:: python

            <link rel="stylesheet" href="{{ url_for('static', filename='css/bootstrap.css') }}" />
            <script src="{{ url_for('static', filename='js/jquery.min.js') }}"></script>
            <script src="{{ url_for('static', filename='js/bootstrap.js') }}"></script>

      This is the code which provides the pop-up messages in layout.html.

      .. code-block:: python

          {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}

             <ul class=flashes>
             {% for category, message in messages %}
                  <script>
                     var message = {{ message|tojson }};
                  alert(message)
               </script>

             {% endfor %}
             </ul>
            {% endif %}
           {% endwith %}

      In this section there are 3 tables which are MEDALS, MEDAL_RECORDS, and FR_MEDALS.

1.Classes
=========

1.1 Medals Class
----------------

    The code given below is the Medals class which belongs to Medalclass.py

    .. code-block:: python

            class Medals:
               def __init__(self, id, gold="", silver="", bronze=""):
                  self.id = id
                  self.gold = gold
                  self.silver = silver
                  self.bronze = bronze

1.2 Medal_Records Class
-----------------------

    The code given below is the Medal_Records class which belongs to Medalclass.py

    .. code-block:: python

            class Medal_Records:
                def __init__(self, id, bscore, mid):
                  self.id = id
                  self.bscore = bscore
                  self.mid = mid


1.3 Fr_Medals Class
-------------------

   The code given below is the Fr_Medals class which belongs to Medalclass.py

    .. code-block:: python

            class Fr_Medals:
               def __init__(self, id, frname, age, cid):
               self.id = id
               self.frname = frname
               self.age = age
               self.cid = cid


2.Presentation of tables in HTML files.
=======================================

2.1 Medals Table
----------------

       This is the code given below which shows the column names of Medals table.

    .. code-block:: python

            <table class="table table-bordered">
              <thead>
                <tr>
                  <th>Competition ID</th>
                  <th>Gold</th>
                  <th>Silver</th>
                  <th>Bronze</th>
                </tr>
              </thead>

      This is the code given below which shows the value via Medals class which is in the Medalsclass.py
      If there is nothing to show, it will return 'Nothing found' message in the else part of the code.
      There is also 'delete' and 'update' buttons which are connected to 'deletemedal' and 'updatemedal' functions in Medals.py.

      .. code-block:: python

      <tbody>
         {% if medals %}
            {% for i in medals %}
            <tr>
               <td>{{ i.id }}</td>
               <td>{{ i.gold }}</td>
               <td>{{ i.silver }}</td>
               <td>{{ i.bronze }}</td>
               <td>
                  <a href="{{ url_for('deletemedal', id=i.id) }}">Delete</a>
               </td>
               <td>
                  <a href="{{ url_for('updatemedal', id=i.id) }}">Update</a>
               </td>
            </tr>
           {% endfor %}
        {% else %}
         <tr>
             <td colspan="5" align="center">Nothing found.</td>
           </tr>
        {% endif %}
      </tbody>

2.2 Medal_Records Table
-----------------------

      This is the code given below which shows the column names of Medal_Records table.

      .. code-block:: python

            <table class="table table-bordered">
                <thead>
                  <tr>
                     <th>Best Score ID</th>
                     <th>Best Score (Minutes)</th>
                     <th>Competition ID</th>
                  </tr>
                 </thead>

      This is the code given below which shows the value via Medal_Records class which is in the Medalsclass.py
      If there is nothing to show, it will return 'Nothing found' message in the else part of the code.
      There is also 'delete' and 'update' buttons which are connected to 'deletemedalrec' and 'updatemedalrec' functions in Medals.py.
      .. code-block:: python

                  <tbody>
                     {% if medal_records %}
                        {% for j in medal_records %}
                        <tr>
                           <td>{{ j.id }}</td>
                           <td>{{ j.bscore }}</td>
                           <td>{{ j.mid }}</td>
                           <td>
                              <a href="{{ url_for('deletemedalrec', id=j.id) }}">Delete</a>
                           </td>
                           <td>
                              <a href="{{ url_for('updatemedalrec', id=j.id) }}">Update</a>
                           </td>
                        </tr>
                       {% endfor %}
                    {% else %}
                     <tr>
                         <td colspan="5" align="center">Nothing found.</td>
                       </tr>
                    {% endif %}
                  </tbody>
                </table>

2.3 Fr_Medals Table
-------------------

           This is the code given below which shows the column names of Fr_Medals table.

      .. code-block:: python

                  <table class="table table-bordered">
                        <thead>
                          <tr>
                            <th>Name ID</th>
                            <th>Name</th>
                            <th>Age</th>
                            <th>Best Score ID</th>
                          </tr>
                        </thead>

       This is the code given below which shows the value via Fr_Medals class which is in the Medalsclass.py
       If there is nothing to show, it will return 'Nothing found' message in the else part of the code.
       There is also 'delete' and 'update' buttons which are connected to 'deletemedalfr' and 'updatemedalfr' functions in Medals.py.

       .. code-block:: python

                  <tbody>
                     {% if fr_medals %}
                        {% for k in fr_medals %}
                        <tr>
                           <td>{{ k.id }}</td>
                           <td>{{ k.frname }}</td>
                           <td>{{ k.age }}</td>
                           <td>{{ k.cid }}</td>
                           <td>
                              <a href="{{ url_for('deletemedalfr', id=k.id) }}">Delete</a>
                           </td>
                           <td>
                              <a href="{{ url_for('updatemedalfr', id=k.id) }}">Update</a>
                           </td>
                        </tr>
                       {% endfor %}
                    {% else %}
                     <tr>
                         <td colspan="5" align="center">Nothing found.</td>
                       </tr>
                    {% endif %}
                  </tbody>
                </table>

3.Adding Forms of tables in HTML files
======================================
3.1 Adding form of Medals
-------------------------
      This is the add button which leads to open the adding form of Medals table.

      .. code-block:: python

            <button class="btn btn-default" data-toggle="modal" data-target="#myModal">Add New Competition</button>

      The code given below is the adding form of Medals table. It is made with Bootstrap. When 'Add New Competition' button is clicked, it is opened a new form to fill.
      The name of this form 'add' which provide the connection between function and page.

      .. code-block:: python

            <div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
                 <div class="modal-dialog" role="document">
                   <div class="modal-content">
                     <div class="modal-header">
                       <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                       <h4 class="modal-title" id="myModalLabel">Add New Competition</h4>
                     </div>
                     <form method="post">
                        <div class="modal-body">
                          <div class="form-group">
                            <label for="surname">Gold</label>
                            <input type="text" class="form-control" id="gold" name="gold" placeholder="Gold">
                          </div>
                          <div class="form-group">
                            <label for="nationality">Silver</label>
                            <input type="text" class="form-control" id="silver" name="silver" placeholder="Silver">
                          </div>
                          <div class="form-group">
                            <label for="style">Bronze</label>
                            <input type="text" class="form-control" id="bronze" name="bronze" placeholder="Bronze">
                          </div>
                        </div>
                        <div class="modal-footer">
                          <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                          <button type="submit" name="add" class="btn btn-primary">Save</button>
                        </div>
                     </form>
                   </div>
                 </div>
               </div>

3.2 Adding form of Medal_Records
--------------------------------
      This is the add button which leads to open the adding form of Medal_Records table.

      .. code-block:: python

            <button class="btn btn-default" data-toggle="modal" data-target="#myModalhigh">Add New Best Score</button>

      The code given below is the adding form of Medal_Records table. It is made with Bootstrap. When 'Add New Best Score' button is clicked, it is opened a new form to fill.
      The name of this form 'addrec' which provide the connection between function and page.

      .. code-block:: python

            <div class="modal fade" id="myModalhigh" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
                 <div class="modal-dialog" role="document">
                   <div class="modal-content">
                     <div class="modal-header">
                       <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                       <h4 class="modal-title" id="myModalLabel">Add New Best Score</h4>
                     </div>
                     <form method="post">
                        <div class="modal-body">
                          <div class="form-group">
                            <label for="surname">High Score (Must be Entered)</label>
                            <input type="text" class="form-control" id="bscore" name="bscore" placeholder="High Score">
                          </div>
                          <div class="form-group">
                            <label for="surname">Comptetition ID</label>
                            <input type="text" class="form-control" id="mid" name="mid" placeholder="Comptetition ID">
                          </div>
                        </div>
                        <div class="modal-footer">
                          <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                          <button type="submit" name="addrec" class="btn btn-primary">Save</button>
                        </div>
                     </form>
                   </div>
                 </div>
               </div>

3.3 Adding form of Fr_Medals
----------------------------
      This is the add button which leads to open the adding form of Fr_Medals table.

      .. code-block:: python

            <button class="btn btn-default" data-toggle="modal" data-target="#myModalFR">Add Front-Runner Name</button>

      The code given below is the adding form of Fr_Medals table. It is made with Bootstrap. When 'Add Front-Runner Name' button is clicked, it is opened a new form to fill.
      The name of this form 'addfr' which provide the connection between function and page.

      .. code-block:: python

            <div class="modal fade" id="myModalFR" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
                 <div class="modal-dialog" role="document">
                   <div class="modal-content">
                     <div class="modal-header">
                       <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                       <h4 class="modal-title" id="myModalLabel">Add Front-Runner Name</h4>
                     </div>
                     <form method="post">
                        <div class="modal-body">
                          <div class="form-group">
                            <label for="surname">Name</label>
                            <input type="text" class="form-control" id="frname" name="frname" placeholder="Name">
                          </div>
                          <div class="form-group">
                            <label for="surname">Age</label>
                            <input type="text" class="form-control" id="age" name="age" placeholder="age">
                          </div>
                          <div class="form-group">
                            <label for="surname">Best Score ID</label>
                            <input type="text" class="form-control" id="cid" name="cid" placeholder="Best Score ID">
                          </div>
                        </div>
                        <div class="modal-footer">
                          <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                          <button type="submit" name="addfr" class="btn btn-primary">Save</button>
                        </div>
                     </form>
                   </div>
                 </div>
               </div>

4.Returning values from database to table
=========================================
4.1 Returning Medals values
---------------------------

      The code given below selects all the values in the Medals table, list them in array, and render it to the Medals.html page

      .. code-block:: python

            def medals_page():
                  with dbcon.connect(app.config['dsn']) as conn:
                        cursor = conn.cursor()
                        cursor.execute("SELECT * FROM medals")
                        rows = cursor.fetchall()
                        medals = {}
                        for row in rows:
                            medals[int(row[0])] = Medals(row[0], row[1], row[2], row[3])
            return render_template('Medals.html', current_time=now.ctime(), medals=medals.values(), medal_records=medal_records.values(), fr_medals=fr_medals.values())


4.2 Returning Medal_Records values
----------------------------------

      The code given below selects all the values in the Medal_Records table, list them in array, and render it to the Medals.html page

      .. code-block:: python

            def medals_page():
                  with dbcon.connect(app.config['dsn']) as conn:
                  cursor = conn.cursor()
                  cursor.execute("SELECT * FROM medal_records")
                  rows = cursor.fetchall()
                  medal_records = {}
                  for row in rows:
                     medal_records[int(row[0])] = Medal_Records(row[0], row[1], row[2])
            return render_template('Medals.html', current_time=now.ctime(), medals=medals.values(), medal_records=medal_records.values(), fr_medals=fr_medals.values())


4.3 Returning Fr_Medals values
------------------------------

      The code given below selects all the values in the Fr_Medals table, list them in array, and render it to the Medals.html page

      .. code-block:: python

            def medals_page():
                  with dbcon.connect(app.config['dsn']) as conn:
                  cursor = conn.cursor()
                  cursor.execute("SELECT * FROM fr_medals")
                  rows = cursor.fetchall()
                  fr_medals = {}
                  for row in rows:
                      fr_medals[int(row[0])] = Fr_Medals(row[0], row[1], row[2],row[3])
            return render_template('Medals.html', current_time=now.ctime(), medals=medals.values(), medal_records=medal_records.values(), fr_medals=fr_medals.values())

5. Add Functions
================
5.1 Medals Add
--------------
      The code given below, use the POST method and 'add' form which is mentioned before adding new record to the Medals table and the database. Because of ID is serial, it is not necessary indicated that.

      .. code-block:: python

            def medals_page():
            if request.method == 'POST' and 'add' in request.form:
                    gold = request.form.get('gold')
                    silver = request.form.get('silver')
                    bronze = request.form.get('bronze')

                    with dbcon.connect(app.config['dsn']) as conn:
                        cursor = conn.cursor()
                        cursor.execute("""INSERT INTO medals (gold, silver, bronze)
                            VALUES (%s, %s, %s) RETURNING ID""",(gold, silver, bronze))
                        conn.commit()
                        return redirect(url_for('medals_page'))
            return render_template('Medals.html', current_time=now.ctime(), medals=medals.values(), medal_records=medal_records.values(), fr_medals=fr_medals.values())


5.2 Medal_Records Add
---------------------
      The code given below, use the POST method and 'addrec' form which is mentioned before adding new record to the Medal_Records table and the database. Because of ID is serial, it is not necessary indicated that.
      If the bscore attribute is null, it will do nothing and directly return to the main function because bscore is a not null attribute.
      If the MID attribute of Medal_Records and the ID attribute of Medals cannot match, it is shown a pop-up error message because MID is foreign key of the ID.

      .. code-block:: python

            def medals_page():
            if request.method == 'POST' and 'addrec' in request.form:
                    bscore = request.form.get('bscore')
                    if not bscore:
                        return redirect(url_for('medals_page'))
                    mid = request.form.get('mid')
                    try:
                        with dbcon.connect(app.config['dsn']) as conn:
                            cursor = conn.cursor()
                            cursor.execute("""INSERT INTO medal_records (bscore, mid)
                            VALUES (%s, %s) RETURNING ID""",(bscore,mid))
                            conn.commit()
                    except dbcon.DatabaseError:
                        flash('An Invalid Competition ID is choosen')
                        conn.rollback()
                    finally:
                        conn.close()
                    return redirect(url_for('medals_page'))
            return render_template('Medals.html', current_time=now.ctime(), medals=medals.values(), medal_records=medal_records.values(), fr_medals=fr_medals.values())


5.3 Fr_Medals Add
-----------------
      The code given below, use the POST method and 'addfr' form which is mentioned before adding new record to the Fr_Medals table and the database. Because of ID is serial, it is not necessary indicated that.
      If the frname attribute is null, it will do nothing and directly return to the main function because frname is a not null attribute.
      If the CID attribute of Fr_Medals and the ID attribute of Medal_Records cannot match, it is shown a pop-up error message because CID is foreign key of the ID.

      .. code-block:: python

            def medals_page():
            if request.method == 'POST' and 'addfr' in request.form:
                 frname = request.form.get('frname')
                 if not frname:
                     return redirect(url_for('medals_page'))
                 age = request.form.get('age')
                 cid = request.form.get('cid')
                 try:
                     with dbcon.connect(app.config['dsn']) as conn:
                         cursor = conn.cursor()
                         cursor.execute("""INSERT INTO fr_medals (name, age, cid)
                         VALUES (%s, %s, %s) RETURNING ID""",(frname, age, cid))
                         conn.commit()
                 except dbcon.DatabaseError:
                     flash('An Invalid Competition ID is choosen')
                     conn.rollback()
                 finally:
                     conn.close()
                 return redirect(url_for('medals_page'))
            return render_template('Medals.html', current_time=now.ctime(), medals=medals.values(), medal_records=medal_records.values(), fr_medals=fr_medals.values())


6. Delete Functions
===================
6.1 Medals Delete
-----------------

         This function related to HTML of Medals table which is mentioned before. When the 'Delete' button clicked on the web page, it send it to deletemedal(id) function and delete the record regarding to ID.
         If the ID attribute of Medals table and a MID attribute of Medal_Records table match, it is shown a pop-up error message because they are restricted foreign key.

         .. code-block:: python

               @app.route('/delete/<int:id>')
               def deletemedal(id):
                   try:
                       with dbcon.connect(app.config['dsn']) as conn:
                           cursor = conn.cursor()
                           cursor.execute("""
                               DELETE FROM medals WHERE id = %s
                               """, (int(id),))
                           conn.commit()

                   except dbcon.DatabaseError:
                       flash('This line is connected to another table.')
                       conn.rollback()
                   finally:
                       conn.close()
                   return redirect(url_for('medals_page'))

6.2 Medal_Records Delete
------------------------

         This function related to HTML of Medal_Records table which is mentioned before. When the 'Delete' button clicked on the web page, it send it to deletemedalrec(id) function and delete the record regarding to ID.
         If the ID attribute of Medal_Records table and a CID attribute of Fr_Medals table match, it is shown a pop-up error message because they are restricted foreign key.

         .. code-block:: python

               @app.route('/deleterec/<int:id>')
               def deletemedalrec(id):
                   try:
                       with dbcon.connect(app.config['dsn']) as conn:
                           cursor = conn.cursor()
                           cursor.execute("""
                               DELETE FROM medal_records WHERE id = %s
                               """, (int(id),))
                           conn.commit()
                   except dbcon.DatabaseError:
                       flash('This line is connected to another table.')
                       conn.rollback()
                   finally:
                       conn.close()
                   return redirect(url_for('medals_page'))


6.3 Fr_Medals Delete
--------------------

         This function related to HTML of Fr_Medals table which is mentioned before. When the 'Delete' button clicked on the web page, it send it to deletefr(id) function and delete the record regarding to ID.

         .. code-block:: python

            @app.route('/deletefr/<int:id>')
            def deletemedalfr(id):

                with dbcon.connect(app.config['dsn']) as conn:
                        cursor = conn.cursor()
                        cursor.execute("""
                            DELETE FROM fr_medals WHERE id = %s
                            """, (int(id),))
                        conn.commit()

                        return redirect(url_for('medals_page')


7. Update Functions
===================
7.1 Medals Update
-----------------

      This is the HTML file of update page of Medals and 'Save' button. It is made by Bootstrap value="{{medal.attribute}}" provide the fill the blanks in form with old values.
      The name of form is 'add'.

      .. code-block:: python

            <form method="post">
                  <div class="modal-body">
                    <div class="form-group">
                      <label for="surname">Gold</label>
                      <input type="text" class="form-control" id="gold" name="gold" placeholder="Gold" value="{{medal.gold}}">
                    </div>
                    <div class="form-group">
                      <label for="nationality">Silver</label>
                      <input type="text" class="form-control" id="silver" name="silver" placeholder="Silver" value="{{medal.silver}}">
                    </div>
                    <div class="form-group">
                      <label for="style">Bronze</label>
                      <input type="text" class="form-control" id="bronze" name="bronze" placeholder="Bronze" value="{{medal.bronze}}">
                    </div>
                  </div>
                  <div class="modal-footer">
                    <button type="submit" name="add" class="btn btn-primary">Save</button>
                  </div>
               </form>

      The function given below uses both POST and GET methods. POST provides to reach the record and GET provides the change on it.
      It is related to 'add' form which is mentioned before.

      .. code-block:: python

          @app.route('/update/<int:id>', methods=['POST', 'GET'])
          def updatemedal(id):
          with dbcon.connect(app.config['dsn']) as conn:
              cursor = conn.cursor()
              cursor.execute("""
                      SELECT * FROM medals WHERE id = %s
                      """, (int(id),))
              rows = cursor.fetchall()
              medal = Medals(rows[0][0], rows[0][1], rows[0][2], rows[0][3])
              print(medal.id)

          if request.method == 'POST' and 'add' in request.form:
              #year = request.form.get('year')
              gold = request.form.get('gold')
              silver = request.form.get('silver')
              bronze = request.form.get('bronze')

              with dbcon.connect(app.config['dsn']) as conn:
                  cursor = conn.cursor()
                  cursor.execute("""UPDATE medals SET GOLD=%s, SILVER=%s, BRONZE=%s WHERE ID=%s""",(gold, silver, bronze,int(id),))
                  conn.commit()

                  return redirect(url_for('medals_page'))
          now = datetime.datetime.now()
          return render_template('Medalsupdate.html', current_time=now.ctime(), medal=medal)

7.2 Medal_Records Update
------------------------

      This is the HTML file of update page of Medal_Records and 'Save' button. It is made by Bootstrap value="{{medal.attribute}}" provide the fill the blanks in form with old values.
      The name of form is 'addreco'.

      .. code-block:: python

            <form method="post">
            <div class="modal-body">
              <div class="form-group">
                <label for="name">Best Score</label>
                <input type="text" class="form-control" id="year" name="bscore" placeholder="bscore" value="{{medalrec.bscore}}">
              </div>
            </div>
            <div class="modal-footer">
              <button type="submit" name="addreco" class="btn btn-primary">Save</button>
            </div>
          </form>


      The function given below uses both POST and GET methods. POST provides to reach the record and GET provides the change on it.
      It is related to 'addreco' form which is mentioned before.

      .. code-block:: python

            @app.route('/updaterec/<int:id>', methods=['POST', 'GET'])
            def updatemedalrec(id):
                with dbcon.connect(app.config['dsn']) as conn:
                    cursor = conn.cursor()
                    cursor.execute("""
                            SELECT * FROM medal_records WHERE id = %s
                            """, (int(id),))
                    rows = cursor.fetchall()
                    medalrec = Medal_Records(rows[0][0], rows[0][1], rows[0][2])
                    print(medalrec.id)
                if request.method == 'POST' and 'addreco' in request.form:
                    bscore = request.form.get('bscore')
                    if not bscore:
                        return redirect(url_for('medals_page'))
                    with dbcon.connect(app.config['dsn']) as conn:
                        cursor = conn.cursor()
                        cursor.execute("""UPDATE medal_records SET bscore=%s WHERE ID=%s""",(float(bscore), int(id),))

                        conn.commit()

                        return redirect(url_for('medals_page'))
                now = datetime.datetime.now()
                return render_template('Medalsbestupdate.html', current_time=now.ctime(), medalrec=medalrec)


7.3 Fr_Medals Update
--------------------

      This is the HTML file of update page of Fr_Medals and 'Save' button. It is made by Bootstrap value="{{medal.attribute}}" provide the fill the blanks in form with old values.
      The name of form is 'addfru'.

      .. code-block:: python

            <form method="post">
            <div class="modal-body">
              <div class="form-group">
                <label for="name">Name</label>
                <input type="text" class="form-control" id="name" name="name" placeholder="name" value="{{fr_medals.frname}}">
              </div>
              <div class="form-group">
                <label for="name">Age</label>
                <input type="text" class="form-control" id="age" name="age" placeholder="age" value="{{fr_medals.age}}">
              </div>
              </div>
               <div class="modal-footer">
                 <button type="submit" name="addfru" class="btn btn-primary">Save</button>
               </div>
            </form>

      The function given below uses both POST and GET methods. POST provides to reach the record and GET provides the change on it.
      It is related to 'addfru' form which is mentioned before.

      .. code-block:: python

            @app.route('/updatemedalfr/<int:id>', methods=['POST', 'GET'])
            def updatemedalfr(id):
                with dbcon.connect(app.config['dsn']) as conn:
                    cursor = conn.cursor()
                    cursor.execute("""
                            SELECT * FROM fr_medals WHERE id = %s
                            """, (int(id),))
                    rows = cursor.fetchall()
                    fr_medals = Fr_Medals(rows[0][0], rows[0][1], rows[0][2],rows[0][3])
                    print(fr_medals.id)
                if request.method == 'POST' and 'addfru' in request.form:
                    name = request.form.get('name')
                    age = request.form.get('age')

                    with dbcon.connect(app.config['dsn']) as conn:
                        cursor = conn.cursor()
                        cursor.execute("""UPDATE fr_medals SET NAME=%s, AGE=%s WHERE ID=%s""",(name, int(age), int(id),))

                        conn.commit()

                        return redirect(url_for('medals_page'))
                now = datetime.datetime.now()
                return render_template('Medalsfrupdate.html', current_time=now.ctime(), fr_medals=fr_medals)

8. Search Function
==================

      This is the search box and the 'Search' button of the page.
      The name of form is 'search'. value="{{kw}}" is the searched word and send to the function.

      .. code-block:: python

            <div class="row">
                     <form method="get">
                        <div class="col-sm-8">
                          <div class="form-group">
                            <input type="text" class="form-control" id="keyword" name="keyword" value="{{kw}}" placeholder="Keyword">
                          </div>
                        </div>
                        <div class="col-sm-4">
                          <button type="submit" name="search" class="btn btn-primary">Search</button>
                        </div>
                     </form>
                  </div>

         The search function uses just GET method and a 'keyword' is requested. 'dict(key='%'+kw+'%')' provides to search not only the full word but also some part of the word.
         Because of Medal_Records just some numbers, there is no need to comparison for Medal_Records table. It returns all the values in the database.
         SQL writes the matched values arrays. The function renders just that arrays, not the arrays which included all the records.

         .. code-block:: python

              if request.method == 'GET' and 'keyword' in request.args:
              kw = request.args.get('keyword')

              with dbcon.connect(app.config['dsn']) as conn:
                  cursor = conn.cursor()
                  cursor.execute("""SELECT * FROM medals WHERE gold ILIKE %(key)s OR silver ILIKE %(key)s OR bronze ILIKE %(key)s""", dict(key='%'+kw+'%'))
                  rows = cursor.fetchall()
                  medals = {}
                  for row in rows:
                      medals[int(row[0])] = Medals(row[0], row[1], row[2], row[3])

                  cursorr = conn.cursor()
                  cursorr.execute("""SELECT * FROM fr_medals WHERE name ILIKE %(key)s""", dict(key='%'+kw+'%'))
                  rows = cursorr.fetchall()
                  fr_medals = {}
                  for row in rows:
                      fr_medals[int(row[0])] = Fr_Medals(row[0], row[1], row[2],row[3])

                  return render_template('Medals.html', current_time=now.ctime(), medals=medals.values(), kw=kw, medal_records=medal_records.values(), fr_medals=fr_medals.values())
