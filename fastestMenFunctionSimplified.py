
import sys
import psycopg2

# Verbindung zur Datenbank herstellen
username = "student"
password = "pgadmin"

try: 
    # Etablieren einer Verbindung zur Datenbank
    myConnection = psycopg2.connect(
        host='localhost',
        port=5432,
        database='student',
        user=username,
        password=password
    )
except psycopg2.Error as error:
    print("Fehler beim Verbinden mit der Datenbank: \n" + str(error))
    sys.exit()



with myConnection.cursor() as myCursor:
    myCursor.execute("PREPARE fastest_runner AS "
                    "SELECT name FROM public.results "
                    "WHERE gender = 'M' AND event = $1 "
                    "ORDER BY result ASC LIMIT 1;")

def get_fastest_male_runner(events):
    with myConnection.cursor() as myCursor:
        for event in events:
            myCursor.execute("EXECUTE fastest_runner (%s);", (event,))
            result = myCursor.fetchone()
            print(f"{event}: {result[0]}")

get_fastest_male_runner(['100M Men', '200M Men', '400M Men'])
