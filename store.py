import psycopg2 as dbapi2

from Openwater import Openw
from Records import Record
from Styles import Person
from Styles import Style
from flask import render_template
import datetime
from flask import redirect

from flask import url_for

class Store:
    def __init__(self, dsn):
        self.dsn = dsn
        self.last_key = None
        
    def add_style(self, style1):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO STYLESS (TITLE, YR) VALUES (%s, %s)"
            cursor.execute(query, (style1.title, style1.year))
            connection.commit()
            self.last_key = cursor.lastrowid
    def delete_style(self, key):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM STYLESS WHERE (ID = %s)"
            cursor.execute(query, (key,))
            connection.commit()

    def update_style(self, key, title, year):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "UPDATE STYLESS SET TITLE = %s, YR = %s WHERE (ID = %s)"
            cursor.execute(query, (title, year, key))
            connection.commit()

    def get_style(self, key):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "SELECT TITLE, YR FROM STYLESS WHERE (ID = %s)"
            cursor.execute(query, (key,))
            title, year = cursor.fetchone()
        return Style(title, year)
    def get_styles(self):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "SELECT ID, TITLE, YR FROM STYLESS ORDER BY ID"
            cursor.execute(query)
            Styles = [(key, Style(title, year))
                      for key, title, year in cursor]
        return Styles
    
    def search_style(self, tosearch):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "SELECT ID, TITLE, YR FROM STYLESS WHERE (TITLE LIKE %s)"
            cursor.execute(query,(tosearch,))
            Styles = [(key, Style(title, year))
                      for key, title, year in cursor]
            return Styles
    
    def add_record(self, record1):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO RECO (NAME, REC) VALUES (%s, %s)"
            cursor.execute(query, (record1.name, record1.rec))
            connection.commit()
            self.last_key = cursor.lastrowid
    def delete_record(self, key):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM RECO WHERE (ID = %s)"
            cursor.execute(query, (key,))
            connection.commit()

    def update_record(self, key, name, rec):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "UPDATE RECO SET NAME = %s, REC = %s WHERE (ID = %s)"
            cursor.execute(query, (name, rec, key))
            connection.commit()
    
    def get_record(self, key):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "SELECT NAME, REC FROM RECO WHERE (ID = %s)"
            cursor.execute(query, (key,))
            name, rec = cursor.fetchone()
            return Record(name, rec)
    def get_records(self):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "SELECT ID, NAME, REC FROM RECO ORDER BY ID"
            cursor.execute(query)
            Records = [(key, Record(name, rec))
                      for key, name, rec in cursor]
            return Records
        
    def record_search(self, tosearch):
            with dbapi2.connect(self.dsn) as connection:
                cursor = connection.cursor()
                query = "SELECT ID, NAME, REC FROM RECO WHERE (NAME LIKE %s)"
                cursor.execute(query,(tosearch,))
                Records = [(key, Record(name, rec))
                          for key, name, rec in cursor]
                return Records
    def get_openw(self):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "SELECT ID, COMPETITION, WINNER, YEAR FROM OPENWATER ORDER BY YEAR"
            cursor.execute(query)
            Openwater = [(key, Openw(competition,winner,year))
                        for key, competition,winner,year in cursor]
            return Openwater
        
    def add_openw(self, o1):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO OPENWATER (COMPETITION, WINNER,  YEAR) VALUES (%s, %s, %s)"
            cursor.execute(query, (o1.comp, o1.winner, o1.year))
            connection.commit()
            self.last_key = cursor.lastrowid
    def delete_openw(self, key):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM OPENWATER WHERE (ID = %s)"
            cursor.execute(query, (key,))
            connection.commit()
    def update_openw(self, key, comp, winner, year):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "UPDATE OPENWATER SET COMPATITION = %s, WINNER = %s, YEAR = %s WHERE (ID = %s)"
            cursor.execute(query, (comp,winner, year, key))
            connection.commit()
            
    def add_person(self, person1):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO PERSON (CNTRY, TIME) VALUES (%s, %s)"
            cursor.execute(query, (person1.cntry, person1.time))
            connection.commit()
            self.last_key = cursor.lastrowid
    def delete_person(self, key):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM PERSON WHERE (ID = %s)"
            cursor.execute(query, (key,))
            connection.commit()
    def get_person(self):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "SELECT ID, CNTRY, TIME FROM PERSON ORDER BY ID"
            cursor.execute(query)
            Persons = [(key, Person(cntry, time))
                      for key, cntry, time in cursor]
        return Persons
     def update_person(self, key, cntry, time):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "UPDATE PERSON SET CNTRY = %s, TIME = %s WHERE (ID = %s)"
            cursor.execute(query, (cntry, time,key))
            connection.commit()
            
  

                
