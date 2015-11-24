import psycopg2 as dbapi2

from Records import Record
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
            query = "UPDATE RECO SET NAME = ?, REC = ? WHERE (ID = ?)"
            cursor.execute(query, (name, rec, key))
            connection.commit()
    def get_record(self, key):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "SELECT NAME, REC FROM RECO WHERE (ID = ?)"
            cursor.execute(query, (key))
            name, surname, record = cursor.fetchone()
            return Record(name, surname, record)
    def get_records(self):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "SELECT ID, NAME, REC FROM RECO ORDER BY ID"
            cursor.execute(query)
            Records = [(key, Record(name, rec))
                      for key, name, rec in cursor]
            return Records
        
