#sudo service postgresql start
import psycopg2
con = psycopg2.connect(database = 'chackobhavan')
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS paintapp")
cur.execute("CREATE TABLE paintapp(id serial, title text, imagedata text)")
con.commit()
con.close()
