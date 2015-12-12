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
            cursor.execute(query, (Olymp.Fullname, Olymp.SwimmerId,Olymp.Year, Olymp.Poolid))
            connection.commit()
            self.last_key = cursor.lastrowid
    def delete_sponsor(self, key):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM SPONSORS WHERE (LISTNO = %s)"
            cursor.execute(query, (key,))
            connection.commit()

    def update_sponsor(self, key,Sponsorid,Swimmername,Birthyear):
        with dbapi2.connect(self.dsn) as connection:
            cursor = connection.cursor()
            query = "UPDATE SPONSORS SET SPONSORID = %s, SWIMMERNAME = %s, BIRTHYEAR = %s WHERE (LISTNO = %s)"
            cursor.execute(query, (Sponsorid,Swimmername,Birthyear, key))
            connection.commit()

    def sponsors_search(self, word):
            with dbapi2.connect(self.dsn) as connection:
                cursor = connection.cursor()
                query = "SELECT SPONSORID, SWIMMERNAME, BIRTHYEAR FROM SPONSORS WHERE (FULLNAME LIKE %s)"
                cursor.execute(query,(word,))
                Sponsors = [(key, Sponsor(Sponsorid,Swimmername,Birthyear))
                          for key,Sponsorid,Swimmername,Birthyear in cursor]
                return Sponsors
