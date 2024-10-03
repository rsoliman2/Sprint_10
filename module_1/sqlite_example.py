import sqlite3
import queries as q

connection =sqlite3.connect('rpg_db.sqlite3')

cursor = connection.cursor()

query = 'SELECT character_id, name FROM charactercreator_character;'

results = cursor.execute(q.SELECT_ALL).fetchall()

if __name__=='__main__':
    print(results[:5])