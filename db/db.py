import psycopg2
from author import Author

con = psycopg2.connect(
    database="name_db",
    user="postgres",
    password="password",
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


class DB(object):
    limit = 2

    @staticmethod
    def get_authors(current_page: int):
        offset = limit * current_page
        con = DB.create_connector_db()
        cur = con.cursor()
        cur.execute("SELECT * FROM authors ORDER BY last_name ASC  LIMIT " + str(DB.limit) + " OFFSET " + str(offset))
        rows_authors = cur.fetchall()
        DB.close_connector_db(con)
        rows_author_class = []
        for row in rows_authors:
            rows_author_class.append(Author(row[0], row[1], row[2]))
        return rows_author_class

    @staticmethod
    def get_count_page(table_name: str):
        con = DB.create_connector_db()
        cur = con.cursor()
        cur.execute("SELECT count(*) FROM " + str(table_name))
        count_page = round(int(cur.fetchall()[0][0]) / limit)
        DB.close_connector_db(con)
        return count_page

    @staticmethod
    def create_connector_db():
        con = psycopg2.connect(
            database="name_db",
            user="postgres",
            password="password",
            host="127.0.0.1",
            port="5432"
        )

        print("Database opened successfully")

        return con

    @staticmethod
    def close_connector_db(con):
        print("Operation done successfully")
        con.close()
