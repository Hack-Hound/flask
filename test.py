import psycopg2

conn = psycopg2.connect("postgresql://aryamann123_gmail_co:hyWMtGe9y8OsAgaODVkJLQ@cuddly-rugrat-4055.6xw.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full")

cur = conn.cursor()

cur.execute("select * from test")