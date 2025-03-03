// Klassen des JDBC-API direkt als Namen verfügbar machen
import java.sql.*;

// Einfaches Java-Programm als Beispiel für den Zugriff auf die Datenbank
// mit Hilfe von API-Calls aus JDBC. 
//
// Zur Ausführung zunächst die Klasse erzeugen:
// javac sehrEinfachesAPIProgramm.java
// Dann die eigentliche Ausführung starten:
// java -cp ../java_libs/postgresql-42.6.0.jar:. sehrEinfachesAPIProgramm

public class sehrEinfachesAPIProgramm {
    public static void main (String args[]) {
        try {
            // Lade den DB Client library)
            Class.forName("org.postgresql.Driver");
        } catch (Exception ex) {
            System.out.println("JDBC Client konnte nicht geladen werden: \n" + ex);
        }

        // Der Connection String besteht aus:
        // protocol:DB client:hostname:port/database
        String connectionString = "jdbc:postgresql://localhost:5432/student";

        String username = "student";
        String password = "pgadmin";

        Connection con;
        Statement stmt;

        try {
            // Etablieren einer Verbindung zur Datenbank
            con = DriverManager.getConnection(connectionString, username, password);

            // Hole Statement zur Interaktion mit der DB
            stmt = con.createStatement();


        } catch (SQLException ex) {
            System.out.println("Fehler beim Etablieren der DB-Vebindung! \n" + ex);  
            return;          
        }


        try {
            // Schicke SELECT-Anfrage an Datenbank
            ResultSet rs = stmt.executeQuery("SELECT VERSION() AS VERSION_LABEL");
            
            // Positioniere Cursor auf ersten Datensatz
            rs.next();

            // Hole Wert des ersten Attributs (wir wissen, dass das ein String ist)
            String versionString = rs.getString(1);

            // Ausgabe des Attributwertes
            System.out.println("Ergebenis der Query: \n" + versionString);

        } catch (SQLException ex) {
            System.out.println("Fehler beim der Abfrage mit SELECT: \n" + ex);  
            return;          
        }

        int result;
        try {
            // Beispiel für eine DDL-Statement mit executeUpdate!
            result  = stmt.executeUpdate(
                "DROP TABLE IF EXISTS testtable"
                );

            // Beispiel für eine DDL-Statement mit executeUpdate!
            result  = stmt.executeUpdate(
                "CREATE TABLE testtable (" + 
                    "id INTEGER NOT NULL, " + 
                    "name TEXT)"
                );

        } catch (SQLException ex) {
            System.out.println("Exception beim DDL-Statement: \n" + ex);
            return;
        }


    }


}
