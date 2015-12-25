#################################
Parts Implemented by Ege Çetindağ
#################################

Swimming Styles
===============


   In this section, there are 3 tables which are Styless, Men and Women.

Styles table
------------

      Operations for in this table are insert, delete, update and search. Also, in the first page get_styles() function is used 
   
   with GET method to write all rows in the Styless table.

   .. code-block:: python

         query = "SELECT TITLE, METER FROM STYLESS WHERE (ID = %s)"


   .. code-block:: python

      <td class="t1">
      <input type="checkbox" name="styles_to_delete"
         value="{{ key }}" />
      </td>
      <td class="t1">
         <a href="{{ url_for('style_page', key=key) }}">
         {{ Style.title }}</a>
      </td>
      <td class="t1">
         <a href="{{ url_for('style_page', key=key) }}">
         {{ Style.year }} </a>
      </td>
      <td class="t1">
      </td>



Insert
~~~~~~
      To insert a new tuple, add button is clicked in the Styles.html. With this button, style_edit() function is called.

   This function returns to style_edit.html


   .. code-block:: python

                @app.route('/Styles/add')
                def style_edit():
                now = datetime.datetime.now()
                return render_template('style_edit.html', current_time=now.ctime())

   After submitting the text boxes in the style_edit.html, with the post method it calls the styles_page() function and it

   goes to the else part of this function.

   .. code-block:: python

              else:
                  title = request.form['title']
                  year = request.form['year']
                  app.store.add_style(title,year)
                  return redirect(url_for('styles_page'))

  This code takes the title and year strings from request form and send it to the SQL code to insert the table.

  With redirection to styles_page(), GET method is called and Table is shown in the html file.

   .. code-block:: python

             query = "INSERT INTO STYLESS (TITLE, METER) VALUES (%s, %s)"

Delete
~~~~~~

     To Delete a tuple, first tuple is selected by select box and Delete button is clicked. By clicking it, with the POST method

  styles_page() function is called.

   .. code-block:: python

            elif 'delete' in request.form:
               keys = request.form.getlist('styles_to_delete')
               for key in keys:
                  app.store.delete_style(int(key))
               return redirect(url_for('styles_page'))

  With the select box 'styles_to_delete' related keys are sent to the SQL code and deleted from the database

   .. code-block:: python

            query = "DELETE FROM STYLESS WHERE (ID = %s)"

  Since, foreign keys that reference this table are on delete restrict, a tuple cannot be deleted if it has any child. 
  
  If there is an exception this code works:

   .. code-block:: python

      except dbapi2.DatabaseError:
               flash('Cannot be deleted: You can not delete it if it has any child! ')
               connection.rollback()

 In the layout.html there is a code that catches the exceptions and using the text in a pop-up page
   .. code-block:: python

      {% with messages = get_flashed_messages(with_categories=true) %}
      {% if messages %}

       <ul class=flashes>
       {% for category, message in messages %}
            <script>
               var message = {{ message|tojson }};
            alert(message)
         </script>

Update
~~~~~~

      For updating a tuple, related row is selected by select box and submitted by update button in the Style.html.

   With the POST method, styles_page() function is called.

   .. code-block:: python

         elif 'update' in request.form:
            keys = request.form.getlist('styles_to_delete')
               for key in keys:
            return render_template('style_update.html', key=key)

  This function returns key of the tuple that will be updated to style_update.html

  On the html page, textboxes should be filled and by submitting it, page will call the style_update(key) function

   .. code-block:: python

     if request.method== 'POST':
        title = request.form['title']
        year = request.form['year']
        app.store.update_style(int(key),title,year)
    return redirect(url_for('styles_page'))

   Key is sending automatically and title and year should be given in the textboxes.

    .. code-block:: python

       query = "UPDATE STYLESS SET TITLE = %s, METER = %s WHERE (ID = %s)"

   With this query, it is updated in database

Search
~~~~~~

      For search function there is little textbox in the main table and search button. When it is filled and clicked

   style_search() function is called

    .. code-block:: python

       <form action="{{ url_for('style_search') }}" method="post">

    .. code-block:: python

      if request.method == 'POST':
         word =request.form['word']
         Styles=app.store.search_style(word)
         now = datetime.datetime.now()
         return render_template('Styles.html', Styles=Styles, current_time=now.ctime())

   Word that comes from the textbox is sent to the sql code to find some tuples and it returns the all rows that are matched.

   It is okay to search some part of a word and it is not case sensitive.

   .. code-block:: python

        query = "SELECT ID, TITLE, METER FROM STYLESS WHERE (TITLE ILIKE '%%' || %s || '%%')"


   These matched tuples are sent to the main html and shown in the table.

Men and Women Tables
--------------------

      To reach Men and Women tables, any tuple can be selected from the Styless tables. When it is clicked, style_page(key)

   function is called. Here, key is the ID of the selected tuple and it is used to get men and women lists with their Styleid's

   equal to ID of the selected row. Basically, by clicking every tuple, you can see the men and women lists pointed to tuple

   by their foreign key.

   .. code-block:: python

      @app.route('/Styles/<int:key>')
      def style_page(key):
          Allmen= app.store.get_men(key)
          Allwomen=app.store.get_women(key)
          now = datetime.datetime.now()
          return render_template('person.html', Allmen=Allmen, Allwomen=Allwomen, key=key, current_time=now.ctime())

   .. code-block:: python

       query = "SELECT ID, NAME, TIME, STYLEID FROM MEN WHERE (STYLEID = %s)"

PS: Since Men and Women tables are similar to each other, functions for two tables will be explained by using Men table.

Insert
~~~~~~
      To insert a new tuple, add button is clicked in the Person.html. With this button, men_edit(key)

   function is called. This function returns to men_edit.html


   .. code-block:: python

                @app.route('/Styles/add')
                def men_edit(key):
               now = datetime.datetime.now()
               return render_template('men_edit.html',key=key, current_time=now.ctime())

   Key is sent to every function for these tables because the functions are for not all of the Men or Women tables but only

   called tuples where foreign key matches ID of Styless Table.

   .. code-block:: python
   
       else:
         name = request.form['name']
         time = request.form['time']
         styleid=key
         man1=Men(name,time,styleid)
         app.store.add_women(man1)
         return redirect(url_for('style_page',key=key))

   To add to the sql table this query is called:

   .. code-block:: python

             query = "INSERT INTO MEN (NAME, TIME, STYLEID) VALUES (%s, %s, %s)"


Delete
~~~~~~

     In order to delete a tuple from Men table, tuple is selected by select box and Delete button is clicked.

  This button calls men_page(key) function with the POST method.

   .. code-block:: python

        elif 'delete' in request.form:
          keys = request.form.getlist('person_to_delete')
          for key in keys:
            app.store.delete_men(int(key))
            return redirect(url_for('style_page',key=ids))

   Here, ids is the foreign key, key is the ID of the tuple. At the end ids is sent to the html file as key.

   In delete_men(int) function, tuple with related id is deleted.

   .. code-block:: python

      query = "DELETE FROM MEN WHERE (ID = %s)"

Update
~~~~~~

     For updating a tuple, related row is selected by select box and submitted by update button in the Person.html.

   With the POST method, men_page(key) function is called.

   .. code-block:: python

         elif 'update' in request.form:
        keys = request.form.getlist('person_to_delete')
        for key in keys:
            return render_template('men_update.html',key=key, ids=ids)

  This function returns id of the related tuple and foreign key of the related tuple and it opens men_update.html to

  get neccesary data from request form in this html file.

   .. code-block:: python

    def person_update(key,ids):
    if request.method == 'POST':
        name = request.form['name']
        time = request.form['time']
        styleid=ids
        app.store.update_men(key,name,time,styleid)
    return redirect(url_for('style_page',key=ids))

   Key and foreign key(styleid) is sent automatically and name, time should be given in the textboxes.

Search
~~~~~~

      By filling the textbox and clicking search button men_search(key) function is called.

   .. code-block:: python

          if request.method == 'POST':
            word =request.form['word']
            Allmen= app.store.search_men(word,key)
            now = datetime.datetime.now()
            return render_template('person.html',key=key, Allmen=Allmen, current_time=now.ctime())

   With this code, word and foreign key is sent to the query.

   .. code-block:: python

        query = "SELECT ID, NAME, TIME, STYLEID FROM MEN WHERE (NAME ILIKE '%%' || %s || '%%') AND (STYLEID= %s)"


   When searched word can be found in Name and foreign key is also matched, results return to person.html.













