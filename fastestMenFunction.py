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
    try:
        # Prepared Statement für die Abfrage
        myCursor.execute("PREPARE fastest_runner AS "
                        "SELECT name FROM public.results "
                        "WHERE gender = 'M' AND event = $1 "
                        "ORDER BY result ASC LIMIT 1;")
    except psycopg2.Error as error:
        print("Fehler bei der Query Preparation: \n" + str(error))

def get_fastest_male_runner(events):
    try:
        with myConnection.cursor() as myCursor:
            for event in events:
                try:
                    # Ausführung des Prepared Statements
                    myCursor.execute("EXECUTE fastest_runner (%s);", (event,))
                    result = myCursor.fetchone()
                    if result:
                        print(f"Schnellster Mann {event}: {result[0]}")
                    else:
                        print(f"Keine Ergebnisse für {event}")

                except psycopg2.Error as error:
                    print("Fehler bei der Abfrage mit SELECT: \n" + str(error))
            
    except psycopg2.Error as error:
        print("Fehler beim Zugriff auf die Datenbank: \n" + str(error))

# Funktion dreimal ausführen
get_fastest_male_runner(['100M Men', '200M Men', '400M Men'])
#get_fastest_male_runner('100M Men')
#get_fastest_male_runner('200M Men')
#get_fastest_male_runner('400M Men')
