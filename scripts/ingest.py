import json
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("BASE DIR", BASE_DIR)
sql_path = os.path.join(BASE_DIR, 'db.sqlite3')

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Exception as e:
        print(e)

    return None


def insert_genre_list():
    genre_list = [
        u'Sci-Fi', u'Crime', u'Romance', u'Animation', u'Music', u'Adult', u'Comedy',
        u'War', u'Horror', u'Film-Noir', u'Western', u'News', u'Reality-TV',
        u'Thriller', u'Adventure', u'Mystery',
        u'Short', u'Talk-Show', u'Drama', u'Action',
        u'Documentary', u'Musical', u'History', u'Family', u'Fantasy',
        u'Game-Show', u'Sport', u'Biography']

    conn = create_connection(sql_path)
    cur = conn.cursor()

    for i in genre_list:
        sql = "INSERT INTO genre(name) VALUES('{}') ".format(i)
        print(sql)
        cur.execute(sql)
        conn.commit()


def get_all_genre():
    dictionary = {}

    conn = create_connection(sql_path)
    cur = conn.cursor()

    sql = "SELECT id,name from genre"

    cur.execute(sql)
    rows = cur.fetchall()
    genre_dict = dict(rows)

    return genre_dict

#Insering all distinct genre
insert_genre_list()

file_path = os.path.join(BASE_DIR, 'scripts/imdb.json')

with open(file_path) as f:
    genre = []
    json = json.load(f)
    f.close()


genre_dict = get_all_genre()
print(genre_dict)

conn = create_connection(sql_path)
cursor = conn.cursor()

for d in json:
    popularity = d['99popularity']
    director = d['director']
    imdb_score = d['imdb_score']
    name = d['name']
    genres = list(map(lambda x: x.strip(), d['genre']))

    sql = "INSERT INTO movie (popularity,director,imdb_score,name) VALUES (?,?,?,?) "

    print("insert movies ", sql)

    cursor.execute(sql, (popularity, director, imdb_score, name))
    movie_id = cursor.lastrowid
    conn.commit()

    for genre in genres:

        for id, name in genre_dict.items():
            if name == genre:
                genre_id= id

        # genre_id = genre_dict.keys()[genre_dict.values().index(genre)]

        query = "INSERT INTO movie_genre (movie_id, genre_id) values(?, ?)"
        cursor.execute(query, (movie_id, genre_id))
        conn.commit()



