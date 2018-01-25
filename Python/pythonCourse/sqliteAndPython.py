import sqlite3

# this establishes a connection or creates table if it doesn't exist
# you can use this >> connection = sqlite3.connect(':memory:') << for temp table
connection = sqlite3.connect("test_database.db")

# instantiates a cursor object. this enables operations on a database
c = connection.cursor()

# creates a table names People with 3 new columns FirstName, LastName, Age
c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")

# insert data into the table
c.execute("INSERT INTO People VALUES('Ron','Obvious',42)")

# commit that data to the table
connection.commit()

c.execute("DROP TABLE IF EXISTS People")
