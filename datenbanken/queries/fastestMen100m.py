import sys
import psycopg2

# Verbindung zur Datenbank herstellen
username = "student"
password = "pgadmin"

def get_top_5_male_sprinters():
    try:
        myConnection = psycopg2.connect(
            host='localhost',
            port=5432,
            database='student',
            user=username,
            password=password
        )
        
        with myConnection.cursor() as myCursor:
            try:
                # Abfrage für die 5 schnellsten männlichen Läufer über 100m
                query = """
                SELECT name, result FROM public.results
                WHERE gender = 'M' AND event = '400M Men'
                ORDER BY result ASC
                LIMIT 5;
                """
                myCursor.execute(query)
                results = myCursor.fetchall()
                
                print("Top 5 männliche Läufer auf 100m:")
                for rank, (name, result) in enumerate(results, start=1):
                    print(f"{rank}. {name} - {result} Sekunden")
            
            except psycopg2.Error as error:
                print("Fehler bei der Abfrage mit SELECT: \n" + str(error))
            
    except psycopg2.Error as error:
        print("Fehler beim Verbinden mit der Datenbank: \n" + str(error))
    finally:
        if myConnection:
            myConnection.close()

# Funktion aufrufen
get_top_5_male_sprinters()
