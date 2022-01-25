import sqlite3

db = sqlite3.connect('rests_base.db', check_same_thread=False)
sql = db.cursor()

# sql.execute('drop table statistic')
# db.commit()

sql.execute('''CREATE TABLE IF NOT EXISTS restorans (
    id integer PRIMARY KEY AUTOINCREMENT,
    category TEXT,
    title TEXT,
    address TEXT,
    rating REAL,
    latitude real,
    longitude real
)''')

a = []


def add(category, title, address, rating, latitude, longitude):
    sql.execute(f"INSERT INTO restorans (category, title, address, rating, latitude, longitude) VALUES (?, ?, ?, ?, ?, ?)", (category, title, address, rating, latitude, longitude))
    db.commit()

def dell(cat):
    sql.execute(f"DELETE FROM restorans WHERE category = '{cat}'")
    db.commit()

for value in sql.execute("SELECT * FROM restorans"):
    print(value)
