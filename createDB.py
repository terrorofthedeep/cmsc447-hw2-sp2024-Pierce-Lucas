import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

#Wipes any existing database and makes a new one
cursor.execute("DROP TABLE IF EXISTS people")
cursor.execute("CREATE TABLE people (name text, id integer, points integer)")

#Table creates successfully, but I can't seem to load starting_database in correctly?


#Format: (Name, ID, Points)
starting_database = [
    ("Steve Smith", 211, 80),
    ("Jian Wong", 122, 92),
    ("Chris Peterson", 213, 91),
    ("Sai Patel", 524, 94),
    ("Andrew Whitehead", 425, 99),
    ("Lynn Roberts", 626, 90),
    ("Robert Sanders ", 287, 75)
]

#Add starting_database to database.db
cursor.executemany("insert into people values (?, ?, ?)", starting_database)
connection.commit()

#Debug print statement
for row in cursor.execute("select * from people"):
    print(row)


connection.close()