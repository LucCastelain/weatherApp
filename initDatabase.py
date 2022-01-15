import sqlite3

connection = sqlite3.connect("database.db")

with open("createDatabase.sql") as file:
    connection.executescript(file.read())

cursor = connection.cursor()
cursor.execute("INSERT INTO sensors (country, city) VALUES (?, ?)", ("France", "Brest"))

connection.commit()
connection.close()