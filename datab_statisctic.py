import sqlite3

db = sqlite3.connect('statistic_base.db', check_same_thread=False)
sql = db.cursor()

sql.execute('''CREATE TABLE IF NOT EXISTS statistic (
    categ TEXT,
    name TEXT,
    region TEXT
)''')

def add(category, name, reg):
    sql.execute(f"INSERT INTO statistic (categ, name, region) VALUES (?, ?, ?)", (category, name, reg))
    db.commit()

# for value in sql.execute("SELECT * FROM statistic").fetchall():
#     print(value)

