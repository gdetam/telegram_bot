import psycopg2
from author import Author

con = psycopg2.connect(
    database="telegram_bot_audiobooks",
    user="postgres",
    password="fallen365",
    host="127.0.0.1",
    port="5432"
)

print("Database opened successfully")

cur = con.cursor()
offset = 0
limit = 2

cur.execute("SELECT count(*) FROM authors")
counter_pagination_authors = round(int(cur.fetchall()[0][0]) / limit)

cur.execute("SELECT * FROM authors ORDER BY last_name ASC  LIMIT " + str(limit) + " OFFSET " + str(offset))
rows_authors = cur.fetchall()
rows_author_class = []
for row in rows_authors:
    rows_author_class.append(Author(row[0], row[1], row[2]))

cur.execute("SELECT * FROM genres")
rows_genres = cur.fetchall()

print("Operation done successfully")
con.close()
