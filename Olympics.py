import psycopg2 as dbapi2
from Olympics import Olympic
from flask import render_template
import datetime
from flask import redirect
from flask import url_for


    def get_olympic(self, key):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "SELECT LISTNO,FULLNAME,SWIMMERID,YEAR,POOLID FROM OLYMPICS WHERE (LISTNO = %s)"
            cursor.execute(query, (key))
            Listno,Fullname,SwimmerId,Year,Poolid = cursor.fetchone()
            return Olympic(Listno,Fullname,SwimmerId,Year,Poolid)
    def get_olympics(self):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM OLYMPICS ORDER BY LISTNO"
            cursor.execute(query)
            Olympics = [Olympic(Listno,Fullname,SwimmerId,Year,Poolid))
                      for Listno,Fullname,SwimmerId,Year,Poolid in cursor]
            return Olympics
	
    def add_olympic(self, Olymp):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO OLYMPICS (LISTNO, FULLNAME, SWIMMERID, YEAR, POOLID ) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (Olymp.Listno, Olymp.Fullname, Olymp.SwimmerId,Olymp.Year, Olymp.Poolid))
            connection.commit()
            self.last_key = cursor.lastrowid
    def delete_olympic(self, key):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM OLYMPICS WHERE (LISTID = %s)"
            cursor.execute(query, (key,))
            connection.commit()

    def update_olympic(self, Updateto, Olymp):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "UPDATE OLYMPICS SET LISTNO = %s, FULLNAME = %s, SWIMMERID = %s, YEAR, POOLID WHERE (LISTNO = %s)"
            cursor.execute(query, (Olymp.Listno, Olymp.Fullname, Olymp.SwimmerId,Olymp.Year, Olymp.Poolid, Updateto))
            connection.commit()

  def olympic_search(self,tosearch)
	with dbapi2.connect(self.dsn) as connection:
		cursor = connection.cursor()
		query = "SELECT LISTNO,FULLNAME,SWIMMERID,YEAR,POOLID FROM OLYMPICS WHERE (FULLNAME LIKE %s)"
		cursor.execute(query,tosearch)
		Listno,Fullname,SwimmerId,Year,Poolid = cursor.fetchone()
 		return Olympic(Listno,Fullname,SwimmerId,Year,Poolid)