import psycopg2 as dbapi2
from Pools import Pool
from flask import render_template
import datetime
from flask import redirect
from flask import url_for


    def get_pool(self, key):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "SELECT ID,POOLNAME,CITY,AREA FROM POOLS WHERE (ID = %s)"
            cursor.execute(query, (key))
            Id,Poolname,City,Area = cursor.fetchone()
            return Pool(Id,Poolname,City,Area)
    def get_pools(self):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM POOLS ORDER BY ID"
            cursor.execute(query)
            Pools = [Pool(Id,Poolname,City,Area ))
                      for Id,Poolname,City,Area in cursor]
            return Pools
	
    def add_pool(self, Newpool):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO POOLS (ID,POOLNAME,CITY,AREA ) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (Newpool.Id, Newpool.Poolname,Newpool.City, Newpool.Area))
            connection.commit()
            self.last_key = cursor.lastrowid
    def delete_pool(self, key):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM POOLS WHERE (ID = %s)"
            cursor.execute(query, (key))
            connection.commit()

    def update_pool(self, Updateto, Newpool):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "UPDATE POOLS SET ID = %s, POOLNAME = %s, CITY = %s, AREA = %s WHERE (ID = %s)"
            cursor.execute(query, (Newpool.Id, Newpool.Poolname,Newpool.City, Newpool.Area, Updateto))
            connection.commit()

  def pool_search(self,tosearch)
	with dbapi2.connect(self.dsn) as connection:
		cursor = connection.cursor()
		query = "SELECT ID,POOLNAME,CITY,AREA FROM POOLS WHERE (POOLNAME LIKE %s)"
		cursor.execute(query,tosearch)
		Id,Poolname,City,Area = cursor.fetchone()
 		return Pool(Id,Poolname,City,Area)