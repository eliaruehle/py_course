# Zusammenspiel mehrerer Klassen 

### Wir wollen eine Klasse "Car" und eine Klasse "Person" modellieren. Diese beiden Klassen sollen jeweils in einer eigenen source code Datei angelegt werden. (z.B. person.py, car.py)
### Folgende Anforderungen sollen erfüllt werden:
### <ins> Klasse Person: </ins>
- ein "Person" Objekt soll als Attribute einen Vornamen, Nachnamen, Alter und die Information, ob sie männlich/weiblich/divers ist, haben
- ruft man die print() Funktion auf einer Person auf sollte der Vorname und Nachname als zusammenhängender String ausgegeben werden
- für das Alter und das Geschlecht einer Person sollte es getter- und setter-Methoden geben; für das Alter bietet sich zusätzlich eine has_birthday() Funktion an
- es sollte eine Funktion register_mail() geben, die einer Person eine Mail-Adresse zuordnet; diese soll als Klassenvariable gespeichert werden; zusätzlich ist eine zugewiesene Mail nur dann gültig, wenn ein @ in ihr vorkommt; es sollte ein getter für die Adresse geben, welcher eine Error-Nachricht ausgibt, wenn noch keine Mail registriert ist
### <ins> Klasse Car: </ins>
- ein "Car" Objekt soll als Attribute einen Modellnamen, ein Herestellungsjahr, die Anzahl an Sitzplätzen, sowie eine PS-Zahl haben, zusätzlich soll gespeichert werden können, wer in dem Auto sitzt
- wird die print() Funktion auf ein Car Objelt aufgerufen, so sollte der Name, das Herstellungsjahr sowie die PS Anzahl in einem "sinnvollen" Satz ausgeben werden
- es sollte Fuktionen add_passenger() und delte_passenger() geben, welche Personen in Autos setzen und sie entfernen kann (achtet hier auf Rahmenbedingungen z.B. Sitzplätze)
- erweitere nun die Funktionalität, sodass mehrer Personen gleichzeitig hinzugefügt und entfernt werden können z.B. mit add_multiple_pessengers()
- Es sollte eine Funktion getPassengers() geben, welche die Namen aller Mitfahrer auflistet
- ist ein "Car" voll besetzt soll es eine Funktion startRide() geben, welche ausgibt, dass die Fahrt beginnt und wer alles an Board ist; ist das "Car" nicht voll besetzt soll eine entsprechende Fehlermeldung kommen
### <ins> Main: </ins>
- legt eine neue Datei main.py in eurem working-directory an 
- importiert die Klassen "Person" und "Car" aus den jeweiligen Datein
- erstellt nun einige Car und Person Objekte und weist Persons einem Car zu
- testet ebenfalls die von euch geschriebenen Methoden der einzelnen Klassen, entweder über passende print-outs oder über den __assert()__ Befehl