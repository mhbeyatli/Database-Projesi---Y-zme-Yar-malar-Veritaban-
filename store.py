import psycopg2 as dbapi2
from Olympics_d import Olympic
from Openwater import Openw
from Records import Record
from Styles import Men
from Styles import Women
from Records import Recor
from Records import RecorLow
from Styles import Style
from flask import render_template
from flask import flash
import datetime
from flask import redirect

from flask import url_for

class Store:
    def __init__(self, dsn):
        self.dsn = dsn
        self.last_key = None

    def add_style(self, title,year):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO STYLESS (TITLE, METER) VALUES (%s, %s)"
            cursor.execute(query, (title, year))
            connection.commit()
            self.last_key = cursor.lastrowid
    def delete_style(self, key):
        try:
            with dbapi2.connect(self.dsn) as connection:
                cursor = connection.cursor()
                query = "DELETE FROM STYLESS WHERE (ID = %s)"
                cursor.execute(query, (key,))
                connection.commit()
        except dbapi2.DatabaseError:
            flash('Cannot be deleted: You cant delete it if it has any child! ')
            connection.rollback()
        finally:
            connection.close()
    def update_style(self, key, title, year):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "UPDATE STYLESS SET TITLE = %s, METER = %s WHERE (ID = %s)"
            cursor.execute(query, (title, year,key))
            connection.commit()

    def get_style(self, key):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "SELECT TITLE, METER FROM STYLESS WHERE (ID = %s)"
            cursor.execute(query, (key,))
            title, year = cursor.fetchone()
        return Style(title, year)
    def get_styles(self):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "SELECT ID, TITLE, METER FROM STYLESS ORDER BY ID"
            cursor.execute(query)
            Styles = [(key, Style( title, year))
                      for key, title, year in cursor]
        return Styles

    def search_style(self, tosearch):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "SELECT ID, TITLE, METER FROM STYLESS WHERE (TITLE LIKE %s)"
            cursor.execute(query,(tosearch,))
            Styles = [(key, Style(title, year))
                      for key, title, year in cursor]
            return Styles
    def add_men(self, person1):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO MEN (NAME, TIME, STYLEID) VALUES (%s, %s, %s)"
            cursor.execute(query, (person1.name, person1.time,person1.styleid))
            connection.commit()
            self.last_key = cursor.lastrowid
    def delete_men(self, key):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM MEN WHERE (ID = %s)"
            cursor.execute(query, (key,))
            connection.commit()

    def get_men(self,key):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "SELECT ID, NAME, TIME, STYLEID FROM MEN WHERE (STYLEID = %s)"
            cursor.execute(query,(key,))
            Allmen = [(key, Men(name,time, styleid))
                      for key, name, time, styleid in cursor]
            return Allmen

    def search_men(self, tosearch, ids):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "SELECT ID, NAME, TIME, STYLEID FROM MEN WHERE (NAME LIKE %s) AND (STYLEID= %s)"
            cursor.execute(query,(tosearch,ids))
            Allmen = [(key, Men(name, time, styleid))
                      for key, name, time, styleid in cursor]
            return Allmen


    def update_men(self, key, name, time, styleid):
        try:
            with dbapi2.connect(self.dsn) as connection:
                cursor = connection.cursor()
                query = "UPDATE MEN SET NAME = %s, TIME = %s,STYLEID = %s WHERE (ID = %s)"
                cursor.execute(query, (name, time,styleid,key))
                connection.commit()
        except dbapi2.DatabaseError:
            flash('Cannot be update ')
            connection.rollback()
        finally:
            connection.close()


    def get_women(self,key):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "SELECT ID, NAME, TIME, STYLEID FROM WOMEN WHERE (STYLEID = %s)"
            cursor.execute(query,(key,))
            Allwomen = [(key, Women(name,time, styleid))
                      for key, name, time, styleid in cursor]
            return Allwomen
    def add_women(self, person1):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO WOMEN (NAME, TIME, STYLEID) VALUES (%s, %s, %s)"
            cursor.execute(query, (person1.name, person1.time,person1.styleid))
            connection.commit()
            self.last_key = cursor.lastrowid
    def delete_women(self, key):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM WOMEN WHERE (ID = %s)"
            cursor.execute(query, (key,))
            connection.commit()
    def update_women(self, key, name, time, styleid):
        try:
            with dbapi2.connect(self.dsn) as connection:
                cursor = connection.cursor()
                query = "UPDATE WOMEN SET NAME = %s, TIME = %s,STYLEID = %s WHERE (ID = %s)"
                cursor.execute(query, (name, time,styleid,key))
                connection.commit()
        except dbapi2.DatabaseError:
            flash('Cannot be update ')
            connection.rollback()
        finally:
            connection.close()
    def search_women(self, tosearch, ids):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "SELECT ID, NAME, TIME, STYLEID FROM WOMEN WHERE (NAME LIKE %s) AND (STYLEID= %s)"
            cursor.execute(query,(tosearch,ids))
            Allwomen = [(key, Women(name, time, styleid))
                      for key, name, time, styleid in cursor]
            return Allwomen

    def add_record(self, record1):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO RECO (NAME, REC) VALUES (%s, %s)"
            cursor.execute(query, (record1.name, record1.rec))
            connection.commit()

    def add_recor(self, recor1):
        try:
            with dbapi2.connect(self.dsn) as connection:
                cursor = connection.cursor()
                query = "INSERT INTO RECOC (NAME, RECOR) VALUES (%s, %s)"
                cursor.execute(query, (recor1.name, recor1.recor))
                connection.commit()
                self.last_key = cursor.lastrowid
        except dbapi2.DatabaseError:
            flash('Cannot be add, cause Record list has no record that you entered. ')
            connection.rollback()
        finally:
            connection.close()

    def add_lowrecor(self, lowrecor1):
        try:
            with dbapi2.connect(self.dsn) as connection:
                cursor = connection.cursor()
                query = "INSERT INTO RECOL (NAME, LOWRECOR) VALUES (%s, %s)"
                cursor.execute(query, (lowrecor1.name, lowrecor1.lowrecor))
                connection.commit()
                self.last_key = cursor.lastrowid
        except dbapi2.DatabaseError:
            flash('Cannot be add, cause Record list has no record that you entered. ')
            connection.rollback()
        finally:
            connection.close()


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

    def delete_recor(self, key):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM RECOC WHERE (ID = %s)"
            cursor.execute(query, (key,))
            connection.commit()

    def delete_lowrecor(self, key):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM RECOL WHERE (ID = %s)"
            cursor.execute(query, (key,))
            connection.commit()

    def update_lowrecor(self, key, name, lowrecor):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "UPDATE RECOL SET NAME = %s, LOWRECOR = %s WHERE (ID = %s)"
            cursor.execute(query, (name, lowrecor, key))
            connection.commit()
    def update_record(self, key, name, rec):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "UPDATE RECO SET NAME = %s, REC = %s WHERE (ID = %s)"
            cursor.execute(query, (name, rec, key))
            connection.commit()

    def update_recor(self, key, name, recor):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "UPDATE RECOC SET NAME = %s, RECOR = %s WHERE (ID = %s)"
            cursor.execute(query, (name, recor, key))
            connection.commit()

    def get_lowrecor(self):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "SELECT ID, NAME, LOWRECOR FROM RECOL ORDER BY ID"
            cursor.execute(query)
            LowRecors = [(key, RecorLow(name, lowrecor))
                      for key, name, lowrecor in cursor]
        return LowRecors

    def get_lowrecors(self):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "SELECT ID, NAME, LOWRECOR FROM RECOL ORDER BY ID"
            cursor.execute(query)
            LowRecors = [(key, RecorLow(name, lowrecor))
                      for key, name, lowrecor in cursor]
            return LowRecors

    def get_record(self, key):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "SELECT NAME, REC FROM RECO WHERE (ID = %s)"
            cursor.execute(query, (key,))
            name, rec = cursor.fetchone()
            return Record(name, rec)


    def get_recor(self):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "SELECT ID, NAME, RECOR FROM RECOC ORDER BY ID"
            cursor.execute(query)
            Recors = [(key, Recor(name, recor))
                      for key, name, recor in cursor]
        return Recors



    def get_records(self):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "SELECT ID, NAME, REC FROM RECO ORDER BY ID"
            cursor.execute(query)
            Records = [(key, Record(name, rec))
                      for key, name, rec in cursor]
            return Records

    def get_recors(self):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "SELECT ID, NAME, RECOR FROM RECOC ORDER BY ID"
            cursor.execute(query)
            Recors = [(key, Recor(name, recor))
                      for key, name, recor in cursor]
            return Recors

    def record_search(self, tosearch):
            with dbapi2.connect(self.dsn) as connection:
                cursor = connection.cursor()
                query = "SELECT ID, NAME, REC FROM RECO WHERE (NAME LIKE %s)"
                cursor.execute(query,(tosearch,))
                Records = [(key, Record(name, rec))
                          for key, name, rec in cursor]
                return Records

    def recor_search(self, tosearch):
            with dbapi2.connect(self.dsn) as connection:
                cursor = connection.cursor()
                query = "SELECT ID, NAME, RECOR FROM RECOC WHERE (NAME LIKE %s)"
                cursor.execute(query,(tosearch,))
                Recors = [(key, Recor(name, recor))
                          for key, name, recor in cursor]
                return Recors

    def lowrecor_search(self, tosearch):
            with dbapi2.connect(self.dsn) as connection:
                cursor = connection.cursor()
                query = "SELECT ID, NAME, LOWRECOR FROM RECOL WHERE (NAME LIKE %s)"
                cursor.execute(query,(tosearch,))
                LowRecors = [(key, RecorLow(name, lowrecor))
                          for key, name, lowrecor in cursor]
                return LowRecors
    def get_openw(self):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "SELECT ID, COMPETITION, WINNERID, YEAR FROM OPENWATER ORDER BY YEAR"
            cursor.execute(query)
            Openwater = [(key, Openw(competition,winnerid,year))
                        for key, competition,winnerid,year in cursor]
            return Openwater
    def add_openw(self, o1):
        try:
            with dbapi2.connect(self.dsn) as connection:
                cursor = connection.cursor()
                query = "INSERT INTO OPENWATER (COMPETITION, WINNERID,  YEAR) VALUES (%s, %s, %s)"
                cursor.execute(query, (o1.comp, o1.winnerid, o1.year))
                connection.commit()
                self.last_key = cursor.lastrowid
        except dbapi2.DatabaseError:
            connection.rollback()
        finally:
            connection.close()
    def delete_openw(self, key):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM OPENWATER WHERE (ID = %s)"
            cursor.execute(query, (key,))
            connection.commit()
    def update_openw(self, key, comp, winnerid, year):
        try:
            with dbapi2.connect(self.dsn) as connection:
                cursor = connection.cursor()
                query = "UPDATE OPENWATER SET COMPETITION = %s, WINNERID = %s, YEAR = %s WHERE (ID = %s)"
                cursor.execute(query, (comp,winnerid, year, key))
                connection.commit()
        except dbapi2.DatabaseError:
            connection.rollback()
        finally:
            connection.close()

    def search_openw(self, tosearch):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "SELECT ID, COMPETITION,WINNERID, YEAR FROM OPENWATER WHERE (COMPETITION LIKE %s)"
            cursor.execute(query,(tosearch,))
            Openwater = [(key, Openw(comp,winnerid,year))
                      for key, comp, winnerid, year in cursor]
            return Openwater

    def get_olympic(self, key):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "SELECT FULLNAME, SPONSORID,YEAR,POOLID FROM OLYMPICS WHERE (LISTNO = %s)"
            cursor.execute(query, (key,))
            Fullname,SwimmerId,Year,Poolid = cursor.fetchone()
            return Olympic(Fullname,SwimmerId,Year,Poolid)

    def get_olympics(self):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "SELECT LISTNO, FULLNAME, SPONSORID, YEAR, POOLID FROM OLYMPICS ORDER BY LISTNO"
            cursor.execute(query)
            Olympics = [(key, Olympic(Fullname, SwimmerId, Year, Poolid))
                      for key, Fullname, SwimmerId, Year, Poolid in cursor]
            return Olympics

    def add_olympic(self, Olymp):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO OLYMPICS (FULLNAME, SPONSORID, YEAR, POOLID ) VALUES ( %s, %s, %s, %s)"
            cursor.execute(query, (Olymp.Fullname, Olymp.SwimmerId,Olymp.Year, Olymp.Poolid))
            connection.commit()
            self.last_key = cursor.lastrowid
    def delete_olympic(self, key):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM OLYMPICS WHERE (LISTNO = %s)"
            cursor.execute(query, (key,))
            connection.commit()

    def update_olympic(self, key, Fullname,SwimmerId,Year,Poolid):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "UPDATE OLYMPICS SET FULLNAME = %s, SPONSORID = %s, YEAR = %s, POOLID = %s WHERE (LISTNO = %s)"
            cursor.execute(query, (Fullname,SwimmerId,Year,Poolid, key))
            connection.commit()

    def olympics_search(self, word):
            with dbapi2.connect(self.dsn) as connection:
                cursor = connection.cursor()
                query = "SELECT LISTNO,FULLNAME,SPONSORID,YEAR,POOLID FROM OLYMPICS WHERE (FULLNAME LIKE %s)"
                cursor.execute(query,(word,))
                Olympics = [(key, Olympic(Fullname,SwimmerId,Year,Poolid))
                          for key,Fullname,SwimmerId,Year,Poolid in cursor]
                return Olympics
