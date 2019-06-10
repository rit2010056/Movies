import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sql_path = os.path.join(BASE_DIR, 'db.sqlite3')
file_path = os.path.join(BASE_DIR, 'scripts/imdb.json')

print(BASE_DIR)
print(file_path)
print(sql_path)