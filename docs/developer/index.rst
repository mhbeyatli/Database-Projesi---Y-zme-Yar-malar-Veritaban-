Developer Guide
===============

Database Design
---------------

**explain the database design of your project**


**include the E/R diagram(s)**


   Our project's database design is implemented seperately. Each team member has designed his/her own database.

   So, our project's database design and E/R diagrams is going to be explained seperately.

   However connection of our database and project is same for all group members.

   The database is created in the website https://api.elephantsql.com with the create table commmands in SQL.

   The website and database can be accessable on the https://hub.jazz.net/.

   The developer has to log in to hub jazz after that he/she can access to database.

   Connection code is going to be given in codes section of developer guide

1. Group Member
^^^^^^^^^^^^^^^

2. Anil Agca
^^^^^^^^^^^^
   E/R diagram for my Tables :

   .. figure:: anldiagram.png
      :scale: 50 %
      :alt: 

      *Entity/Relation diagram of Olympics,Pools,Sponsors*

All data included at Anil Agca section.

3. Mustafa Tıkır's database part and E/R diagram
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
3.1. Database Design
""""""""""""""""""""

   Topic of this part of the project is records of swimmers.

   Databases are created related to this topic.

   In this part, there are 3 tables that holds the swimmer records.

   First one is general records table and it is created with the SQL code in elephantSQL:

   .. code-block:: python

      CREATE TABLE RECO(
      ID SERIAL PRIMARY KEY,
      NAME VARCHAR(40),
      REC INTEGER UNIQUE
      )

   Second one is High scores list for records. It has an foreing key from first table.

   Also, in RECOR attribute there are restriction on delete and cascade on update.

   .. code-block:: python

      CREATE TABLE RECOC(
      ID SERIAL PRIMARY KEY,
      NAME VARCHAR(40),
      RECOR INTEGER REFERENCES RECO(REC)
      ON DELETE RESTRICT
      ON UPDATE CASCADE
      )

   Third one and the last one is Lowest scores list for records. It also has an foreign key from first table.

   Also, in LOWRECOR attribute there are restriction on delete and cascade on update.

   .. code-block:: python

      CREATE TABLE RECOL(
      ID SERIAL PRIMARY KEY,
      NAME VARCHAR(40),
      LOWRECOR INTEGER REFERENCES RECO(REC)
      ON DELETE RESTRICT
      ON UPDATE CASCADE
      )

3.2. E/R Diagram
""""""""""""""""

   E/R diagram of this part :

   .. figure:: TIKIR/ERdiagram.png
      :scale: 50 %
      :alt: ER diagram

      *Entity/Relation diagram*

4. Group Member
^^^^^^^^^^^^^^^

5. Group Member
^^^^^^^^^^^^^^^


Code
----

**explain the technical structure of your code**

**to include a code listing, use the following example**::

   .. code-block:: python

      class Foo:

         def __init__(self, x):
            self.x = x

:

   Connection with the database and our project is done in the server.py file which is main file for the python codes.

   These given python codes(functions) connects the database with the project.

   .. code-block:: python

      def get_elephantsql_dsn(vcap_services):
          """Returns the data source name for ElephantSQL."""
          parsed = json.loads(vcap_services)
          uri = parsed["elephantsql"][0]["credentials"]["uri"]
          match = re.match('postgres://(.*?):(.*?)@(.*?)(:(\d+))?/(.*)', uri)
          user, password, host, _, port, dbname = match.groups()
          dsn = """user='{}' password='{}' host='{}' port={}
              dbname='{}'""".format(user, password, host, port, dbname)
          return dsn

   .. code-block:: python

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

.. toctree::

   member1
   member2
   Mustafa Tıkır
   member4
   member5
