import psycopg2 as dbapi2
from Olympics_d import Olympic
from Pools_d import Pool
from Sponsors_d import Sponsor
from Openwater import Openw
from Openwater import Openwall
from Openwater import Swimmer
from Openwater import Competition
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
            query = "SELECT ID, TITLE, METER FROM STYLESS WHERE (TITLE ILIKE '%%' || %s || '%%')"
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
            query = "SELECT ID, NAME, TIME, STYLEID FROM MEN WHERE (NAME ILIKE '%%' || %s || '%%') AND (STYLEID= %s)"
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
            query = "SELECT ID, NAME, TIME, STYLEID FROM WOMEN WHERE (NAME ILIKE '%%' || %s || '%%') AND (STYLEID= %s)"
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
    
    def get_openw(self, key):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "SELECT COMPID, WINNERID, YEAR FROM OPENWATER WHERE (ID = %s)"
            cursor.execute(query, (key,))
            compid,winnerid,year= cursor.fetchone()
            return Openw(compid,winnerid,year)
        
    def get_openws(self):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "SELECT ID, COMPID, WINNERID, YEAR FROM OPENWATER ORDER BY YEAR"
            cursor.execute(query)
            Openwater = [(key, Openw(compid,winnerid,year))
                        for key, compid,winnerid,year in cursor]
            return Openwater
    def add_openw(self, o1):
        try:
            with dbapi2.connect(self.dsn) as connection:
                cursor = connection.cursor()
                query = "INSERT INTO OPENWATER (COMPID, WINNERID,  YEAR) VALUES (%s, %s, %s)"
                cursor.execute(query, (o1.compid, o1.winnerid, o1.year))
                connection.commit()
                self.last_key = cursor.lastrowid
        except dbapi2.DatabaseError:
            flash('There is no data has this id. Check winner id or competition id! ')
            connection.rollback()
        finally:
            connection.close()
            
    def delete_openw(self, key):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM OPENWATER WHERE (ID = %s) "
            cursor.execute(query, (key,))
            connection.commit()
    def update_openw(self, key, compid, winnerid, year):
        try:
            with dbapi2.connect(self.dsn) as connection:
                cursor = connection.cursor()
                query = "UPDATE OPENWATER SET COMPID = %s, WINNERID = %s, YEAR = %s WHERE (ID = %s)"
                cursor.execute(query, (compid,winnerid, year, key))
                connection.commit()
        except dbapi2.DatabaseError:
            flash('You entered the wrong data or there is also a data with this id !')
            connection.rollback()
        finally:
            connection.close()

    def search_openw(self, tosearch):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "SELECT ID, COMPID, WINNERID, YEAR FROM OPENWATER WHERE (ID = %s)"
            cursor.execute(query,(tosearch,))
            Openwater = [(key, Openw(compid,winnerid,year))
                      for key, compid, winnerid, year in cursor]
            return Openwater
    
    def get_swimmer(self, key):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "SELECT NAME, SURNAME, NATIONALITY FROM SWIMMERS WHERE (ID = %s)"
            cursor.execute(query, (key,))
            name,surname,nationality= cursor.fetchone()
            return Swimmer(name,surname,nationality)
        
    def get_swimmers(self):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "SELECT ID, NAME, SURNAME, NATIONALITY FROM SWIMMERS ORDER BY ID"
            cursor.execute(query)
            Openwater = [(key, Swimmer(name,surname,nationality))
                        for key, name,surname,nationality in cursor]
            return Openwater   

    def add_swimmer(self, s1):
        try:
            with dbapi2.connect(self.dsn) as connection:
                cursor = connection.cursor()
                query = "INSERT INTO SWIMMERS (NAME, SURNAME, NATIONALITY) VALUES (%s, %s, %s)"
                cursor.execute(query, (s1.name, s1.surname, s1.nationality))
                connection.commit()
                self.last_key = cursor.lastrowid
        except dbapi2.DatabaseError:
            flash('You entered the wrong data or there is also a data with this id !')
            connection.rollback()
        finally:
            connection.close()   
            
    def delete_swimmer(self, key):
        try:
            with dbapi2.connect(self.dsn) as connection:
                cursor = connection.cursor()
                query = "DELETE FROM SWIMMERS WHERE (ID = %s)"
                cursor.execute(query, (key,))
                connection.commit()
        except dbapi2.DatabaseError:
            flash('Cannot be deleted: this data is used in another table!')
            connection.rollback()
        finally:
            connection.close()
    def update_swimmer(self, key, name, surname, nationality):
        try:
            with dbapi2.connect(self.dsn) as connection:
                cursor = connection.cursor()
                query = "UPDATE SWIMMERS SET NAME = %s, SURNAME = %s, NATIONALITY = %s WHERE (ID = %s)"
                cursor.execute(query, (name,surname, nationality, key))
                connection.commit()
        except dbapi2.DatabaseError:
            flash('You entered the wrong data or there is also a data with this id !')
            connection.rollback()
        finally:
            connection.close()

    def search_swimmer(self, tosearch):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "SELECT ID, NAME,SURNAME, NATIONALITY FROM SWIMMERS WHERE (NAME LIKE %s)"
            cursor.execute(query,(tosearch,))
            Openwater = [(key, Swimmer(name,surname,nationality))
                      for key, name, surname, nationality in cursor]
            return Openwater
    def get_comp(self, key):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "SELECT ID, COMPNAME, NUMBER_OF_SWIMMERS,LOCATION, PRIZE FROM COMPETITION WHERE (ID = %s)"
            cursor.execute(query, (key,))
            compname,snumber,location,prize= cursor.fetchone()
            return Competition(compname,snumber,location,prize)
        
    def get_comps(self):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "SELECT ID,COMPNAME,NUMBER_OF_SWIMMERS, LOCATION, PRIZE FROM COMPETITION ORDER BY ID"
            cursor.execute(query)
            Openwater = [(key, Competition(compname,snumber,location,prize))
                        for key, compname,snumber,location,prize in cursor]
            return Openwater  
    def add_comp(self, c1):
        try:
            with dbapi2.connect(self.dsn) as connection:
                cursor = connection.cursor()
                query = "INSERT INTO COMPETITION (COMPNAME,NUMBER_OF_SWIMMERS, LOCATION,PRIZE) VALUES (%s, %s, %s,%s)"
                cursor.execute(query, (c1.compname,c1.snumber, c1.location,c1.prize))
                connection.commit()
                self.last_key = cursor.lastrowid
        except dbapi2.DatabaseError:
            flash('You entered the wrong data or there is also a data with this id !')
            connection.rollback()
        finally:
            connection.close()   
            
    def delete_comp(self, key):
        try:
            with dbapi2.connect(self.dsn) as connection:
                cursor = connection.cursor()
                query = "DELETE FROM COMPETITION WHERE (ID = %s)"
                cursor.execute(query, (key,))
                connection.commit()
        except dbapi2.DatabaseError:
            flash('Cannot be deleted: this data is used in another table!')
            connection.rollback()
        finally:
            connection.close()      
    def update_comp(self, key,compname, snumber, location, prize):
        try:
            with dbapi2.connect(self.dsn) as connection:
                cursor = connection.cursor()
                query = "UPDATE COMPETITION SET COMPNAME= %s, NUMBER_OF_SWIMMERS = %s, LOCATION=%s, PRIZE = %s WHERE (ID = %s)"
                cursor.execute(query, (compname,snumber,location, prize, key))
                connection.commit()
        except dbapi2.DatabaseError:
            flash('You entered the wrong data or there is also a data with this id !')
            connection.rollback()
        finally:
            connection.close()
            
    def search_comp(self, tosearch):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "SELECT ID, COMPNAME,NUMBER_OF_SWIMMERS,LOCATION, PRIZE FROM COMPETITION WHERE (COMPNAME LIKE %s)"
            cursor.execute(query,(tosearch,))
            Openwater = [(key, Competition(compname,snumber,location,prize))
                      for key, compname,snumber, location,prize in cursor]
            return Openwater
    def get_openwall(self):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "SELECT COMPETITION.ID, COMPETITION.COMPNAME, COMPETITION.LOCATION, OPENWATER.YEAR, COMPETITION.NUMBER_OF_SWIMMERS, COMPETITION.PRIZE, SWIMMERS.NAME, SWIMMERS.SURNAME FROM  OPENWATER LEFT JOIN COMPETITION ON COMPETITION.ID = OPENWATER.COMPID LEFT JOIN SWIMMERS ON SWIMMERS.ID = OPENWATER.WINNERID ORDER BY OPENWATER.YEAR"
            cursor.execute(query)
            Openwater = [(key, Openwall(comp,location, year,swimmers,prize,winnername,winnersurname))
                      for key, comp,location, year,swimmers,prize,winnername,winnersurname in cursor]
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
        try:
            with dbapi2.connect(self.dsn) as connection:
                cursor = connection.cursor()
                query = "INSERT INTO OLYMPICS (FULLNAME, SPONSORID, YEAR, POOLID ) VALUES ( %s, %s, %s, %s)"
                cursor.execute(query, (Olymp.Fullname, Olymp.SwimmerId,Olymp.Year, Olymp.Poolid))
                connection.commit()
                self.last_key = cursor.lastrowid
        except dbapi2.DatabaseError:
            flash('Unable to add. Please be sure that Pool and Sponsor with such ids exist')
            connection.rollback()
        finally:
            connection.close()

    def delete_olympic(self, key):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM OLYMPICS WHERE (LISTNO = %s)"
            cursor.execute(query, (key,))
            connection.commit()

    def update_olympic(self, key, Fullname,SwimmerId,Year,Poolid):
        try:
            with dbapi2.connect(self.dsn) as connection:
                cursor = connection.cursor()
                query = "UPDATE OLYMPICS SET FULLNAME = %s, SPONSORID = %s, YEAR = %s, POOLID = %s WHERE (LISTNO = %s)"
                cursor.execute(query, (Fullname,SwimmerId,Year,Poolid, key))
                connection.commit()
        except dbapi2.DatabaseError:
            flash('Unable to Update. Please be sure that new Sponsor and Pool ids exist.')
            connection.rollback()
        finally:
            connection.close()
    def olympics_search(self, word):
            with dbapi2.connect(self.dsn) as connection:
                cursor = connection.cursor()
                query = "SELECT LISTNO,FULLNAME,SPONSORID,YEAR,POOLID FROM OLYMPICS WHERE (FULLNAME LIKE %s)"
                cursor.execute(query,(word,))
                Olympics = [(key, Olympic(Fullname,SwimmerId,Year,Poolid))
                          for key,Fullname,SwimmerId,Year,Poolid in cursor]
                return Olympics

    def get_pool(self, key):
            with dbapi2.connect(self.dsn) as connection:
                cursor = connection.cursor()
                query = "SELECT ID,POOLNAME,CITY,AREA FROM POOLS WHERE (LISTNO = %s)"
                cursor.execute(query, (key,))
                Id,Poolname,City,Area = cursor.fetchone()
                return Pool(Id,Poolname,City,Area)

    def get_pools(self):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "SELECT LISTNO,ID,POOLNAME,CITY,AREA FROM POOLS ORDER BY LISTNO"
            cursor.execute(query)
            Pools = [(key, Pool(Id,Poolname,City,Area))
                      for key,Id,Poolname,City,Area in cursor]
            return Pools

    def add_pool(self, Newpool):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO POOLS (ID,POOLNAME,CITY,AREA ) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (Newpool.Id, Newpool.Poolname,Newpool.City, Newpool.Area))
            connection.commit()
            self.last_key = cursor.lastrowid

    def delete_pool(self, key):
        try:
            with dbapi2.connect(self.dsn) as connection:
                cursor = connection.cursor()
                query = "DELETE FROM POOLS WHERE (LISTNO = %s)"
                cursor.execute(query, (key,))
                connection.commit()
        except dbapi2.DatabaseError:
            flash('Due this PoolId is being used in Olympics table currently,Row cannot be deleted.')
            connection.rollback()
        finally:
            connection.close()

    def update_pool(self, key,Id,Poolname,City,Area):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "UPDATE POOLS SET ID = %s, POOLNAME = %s, CITY = %s, AREA = %s WHERE (LISTNO = %s)"
            cursor.execute(query, (Id,Poolname,City,Area,key))
            connection.commit()

    def pools_search(self, word):
            with dbapi2.connect(self.dsn) as connection:
                cursor = connection.cursor()
                query = "SELECT LISTNO,ID,POOLNAME,CITY,AREA FROM POOLS WHERE (POOLNAME LIKE %s)"
                cursor.execute(query,(word,))
                Pools = [(key, Pool(Id,Poolname,City,Area))
                          for key,Id,Poolname,City,Area in cursor]
                return Pools


    def get_sponsor(self, key):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "SELECT SPONSORID, SWIMMERNAME, BIRTHYEAR FROM SPONSORS WHERE (LISTNO = %s)"
            cursor.execute(query, (key,))
            Sponsorid,Swimmername,Birthyear = cursor.fetchone()
            return Sponsor(Sponsorid,Swimmername,Birthyear)

    def get_sponsors(self):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "SELECT LISTNO, SPONSORID, SWIMMERNAME, BIRTHYEAR FROM SPONSORS ORDER BY LISTNO"
            cursor.execute(query)
            Sponsors = [(key, Sponsor(Sponsorid,Swimmername,Birthyear))
                      for key, Sponsorid,Swimmername,Birthyear in cursor]
            return Sponsors

    def add_sponsor(self, Olymp):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO SPONSORS (SPONSORID, SWIMMERNAME, BIRTHYEAR ) VALUES ( %s, %s, %s)"
            cursor.execute(query, (Olymp.Sponsorid, Olymp.Swimmername,Olymp.Birthyear))
            connection.commit()
            self.last_key = cursor.lastrowid
    def delete_sponsor(self, key):
        try:
            with dbapi2.connect(self.dsn) as connection:
                cursor = connection.cursor()
                query = "DELETE FROM SPONSORS WHERE (LISTNO = %s)"
                cursor.execute(query, (key,))
                connection.commit()
        except dbapi2.DatabaseError:
            flash('Due this Sponsorid is being used in Olympics table currently,Row cannot be deleted.')
            connection.rollback()
        finally:
            connection.close()

    def update_sponsor(self, key,Sponsorid,Swimmername,Birthyear):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "UPDATE SPONSORS SET SPONSORID = %s, SWIMMERNAME = %s, BIRTHYEAR = %s WHERE (LISTNO = %s)"
            cursor.execute(query, (Sponsorid,Swimmername,Birthyear, key))
            connection.commit()

    def sponsors_search(self, word):
            with dbapi2.connect(self.dsn) as connection:
                cursor = connection.cursor()
                query = "SELECT LISTNO, SPONSORID, SWIMMERNAME, BIRTHYEAR FROM SPONSORS WHERE (SWIMMERNAME LIKE %s)"
                cursor.execute(query,(word,))
                Sponsors = [(key, Sponsor(Sponsorid,Swimmername,Birthyear))
                          for key,Sponsorid,Swimmername,Birthyear in cursor]
                return Sponsors
