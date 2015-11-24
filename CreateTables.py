try:
    connection = dbapi2.connect(dsn)
    cursor = connection.cursor()
    statement = """CREATE TABLE OLYMPICS(
	LISTNO SERIAL INTEGER(4) PRIMARY KEY,
	FULLNAME VARCHAR(20),
	SWIMMERID INTEGER(5) REFERENCES TO SWIMMERS(SID),
	YEAR INTEGER(5),
	POOLID INTEGER(5),
	FOREIGN KEY POOLID REFERENCES TO POOLS(ID)
	ON DELETE RESTRICT
	ON UPDATE CASCADE
)
    cursor.execute(statement)
    connection.commit()
    cursor.close()
except dbapi2.DatabaseError:
    connection.rollback()
finally:
    connection.close()


with dbapi2.connect(dsn) as connection:
    cursor = connection.cursor()
    statement = """CREATE TABLE POOLS (
	ID INTEGER(3) PRIMARY KEY,
	POOLNAME VARCHAR(100) UNIQUE NOT NULL,
	CITY VARCHAR(30) NOT NULL,
	AREA INTEGER(10)
	)"""
    cursor.execute(statement)
    cursor.close()
