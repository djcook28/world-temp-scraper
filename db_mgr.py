import sqlite3

connection = sqlite3.connect("temperatures.db")
cursor = connection.cursor()

def save(date, temp):
    cursor.execute("INSERT INTO temperatures VALUES (?, ?)", (date, temp))
    connection.commit()

def load():
    data = cursor.execute("SELECT * FROM temperatures")
    return data.fetchall()