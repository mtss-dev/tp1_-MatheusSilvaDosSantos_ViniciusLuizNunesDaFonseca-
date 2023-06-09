import psycopg2
import subprocess

#If you are using WSL2, replace host='localhost' with host=ip_address in line 11, because WSL2 uses one IP for it!
#ip_address = subprocess.check_output("ip addr show eth0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}'", shell=True).decode().strip()

def drop_db():
    conn = None
    try:
        # connect to the PostgreSQL server without specifying the database name
        conn = psycopg2.connect(dbname='postgres', user='postgres', password='postgres', host='localhost')
        conn.autocommit = True  

        # create a cursor object to execute commands
        cur = conn.cursor()

        cur.execute("DROP DATABASE amazon")

        # close cursor and connection
        cur.close()
        conn.close()

        print("'amazon' database successfully deleted!")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()        