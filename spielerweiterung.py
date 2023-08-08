import sys, urllib.request

# Verbindung zu einer URL
try:
    u = urllib.request.urlopen \
    ("http://localhost/Programmbeispiele/url_lesen.htm")
except:
    print("Fehler")
    sys.exit(0)

# Alle Zeilen in eine Liste lesen
li = u.readlines()

# Schließt die Verbindung
u.close()

# Ausgabe der Liste
for element in li:
    print(element)
    