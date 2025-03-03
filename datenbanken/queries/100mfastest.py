
# Einfaches Python-Programm als Beispiel für den Zugriff auf die Datenbank
# mit Hilfe von API-Calls aus JDBC. Der Treiber ist im Paket psycopg2 enthalten 

import sys
import psycopg2

# Der Connection String besteht aus:
# protocol:DB client:hostname:port/database
# connectionString = "jdbc:postgresql://localhost:5432/student"

username = "student"
password = "pgadmin"

try: 
    # Etablieren einer Verbindung zur Datenbank
    myConnection =  psycopg2.connect(
        host = 'localhost',
        port = 5432,
        database = 'student',
        user = username,
        password = password
    )
except psycopg2.Error as error:
    print("Fehler beim Verbinden mit der Datenbank: \n" + error); 
    sys.exit()

    # Hole ein Cursor-Objekt zur Interaktion mit der DB
with myConnection.cursor() as myCursor: 
    try: 
        # Schicke SELECT-Anfrage an Datenbank
        myCursor.execute("SELECT VERSION() AS VERSION_LABEL")
        
        # Positioniere Cursor auf ersten Datensatz
        row = myCursor.fetchone()

        # Hole Wert des ersten Attributs (wir wissen, dass das ein String ist)
        versionString = row[0]

        #Ausgabe des Attributwertes
        print("Ergebenis der Query: \n" + versionString);
    except psycopg2.Error as error:
        print("Fehler beim der Abfrage mit SELECT: \n" + error); 
        sys.exit()
    
    try:
        # Abfrage für die 5 schnellsten männlichen Läufer über 100m
        query = """
        SELECT name, time FROM public.results
        WHERE gender = 'male' AND distance = 100
        ORDER BY time ASC
        LIMIT 5;
        """
        myCursor.execute(query)
        results = myCursor.fetchall()
                
        print("Top 5 männliche Läufer auf 100m:")
        for rank, (name, time) in enumerate(results, start=1):
            print(f"{rank}. {name} - {time} Sekunden")
            
    except psycopg2.Error as error:
        print("Fehler bei der Abfrage mit SELECT: \n" + str(error))