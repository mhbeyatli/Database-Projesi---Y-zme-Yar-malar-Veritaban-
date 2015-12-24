Developer Guide
===============

Database Design
---------------

   Our project's database design is implemented seperately. Each team member has designed his/her own database.

   So, our project's database design and E/R diagrams is going to be explained seperately.

   However connection of our database and project is same for all group members.

   The database is created in the website https://api.elephantsql.com with the create table commmands in SQL.

   The website and database can be accessable on the https://hub.jazz.net/.

   The developer has to log in to hub jazz after that he/she can access to database.

   Connection code is going to be given in codes section of developer guide

1. Group Member
^^^^^^^^^^^^^^^

2. Anıl AĞCAS's database part and E/R diagram
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

2.1. Database Design
""""""""""""""""""""

Pools table structurally has five attributes. Additional to pool name, pool id, area, city also listno is an attribute of pools table which is not being shown to end-user in any case. Listno is being used only for ordering the pools by the time they are entered. Pools table has created by following SQL code;

        .. code-block:: sql
        
               CREATE TABLE POOLS ( 
               LISTNO SERIAL,
               ID INTEGER PRIMARY KEY,
               POOLNAME VARCHAR(100) UNIQUE NOT NULL, 
               CITY VARCHAR(30) NOT NULL,
               AREA INTEGER ) 
               
               
Olympics table has five attributes. Four of them are being seen by user and two foreign keys which references ‘Pools’ and ‘Sponsors’ tables. And the attribute named LISTNO that not being seen by user is being used for ordering rows. Code for creating table at SQL can be seen below.



    .. code-block:: sql
      
            CREATE TABLE OLYMPICS( 
            LISTNO SERIAL PRIMARY KEY,
            FULLNAME VARCHAR(20), 
            SPONSORID INTEGER 
            REFERENCES SPONSORS(SPONSORID)
            ON DELETE RESTRICT ON UPDATE, 
            YEAR INTEGER,
            POOLID INTEGER REFERENCES POOLS(ID)
            ON DELETE RESTRICT ON UPDATE CASCADE )
           
Sponsors table has four attributes structurally which are ListNo, Sponsorid,SponsorName, Year. ListNo is being used only for ordering the rows and not being shown to user in any case. Primary key of the table Is ID and being referenced by Olympics table in order to get additional information with a sponsor having that id without using any additional rows at Olympics table.Sponsors table has been created by following SQL code;


      .. code-block:: sql

            CREATE TABLE SPONSORS( 
            LISTNO SERIAL,
            SPONSORID INTEGER PRIMARY KEY,
            SPONSORNAME VARCHAR(30),
            YEAR INTEGER )
             
2.2. E/R Diagram
""""""""""""""""

   E/R diagram for my Tables :

   .. figure:: anldiagram.png
      :scale: 50 %
      :alt: 

      *Entity/Relation diagram of Olympics,Pools,Sponsors*


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
   Anil Agca
   Mustafa Tıkır
   member4
   member5
