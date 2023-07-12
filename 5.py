import psycopg2

conn = psycopg2.connect(database = 'netologydb', user = 'postgres', password = '1234') 

with conn.cursor() as cur:
    cur.execute('CREATE TABLE test (id SERIAL PRIMARY KEY);')
    conn.commit()
    
conn.close()
