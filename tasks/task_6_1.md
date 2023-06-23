# Zusammenspiel mehrerer Klassen 

### Wir wollen eine Klasse "Car" und eine Klasse "Person" modellieren. Diese beiden Klassen sollen jeweils in einer eigenen source code Datei angelegt werden. (z.B. person.py, car.py)
### Folgende Anforderungen sollen erfüllt werden:
### <ins> Klasse Person: </ins>
- ein "Person" Objekt soll als Attribute einen Vornamen, Nachnamen, Alter und die Information, ob sie männlich/weiblich/divers ist, haben
- ruft man die print() Funktion auf einer Person auf sollte der Vorname und Nachname als zusammenhängender String ausgegeben werden
- für das Alter und das Geschlecht einer Person sollte es getter- und setter-Methoden geben 
- es sollte eine Funktion registerMail() geben, die einer Person eine Mail-Adresse zuordnet; diese soll als Klassenvariable gespeichert werden; zusätzlich ist eine zugewiesene Mail nur dann gültig, wenn ein @ in ihr vorkommt  
### <ins> Klasse Car: </ins>
- ein "Car" Objekt soll als Attribute einen Modellnamen, ein Herestellungsjahr, die Anzahl an Sitzplätzen, sowie eine PS-Zahl haben, zusätzlich soll gespeichert werden können, wer in dem Auto sitzt
- wird die print() Funktion auf ein Car Objelt aufgerufen, so sollte der Name, das Herstellungsjahr sowie die PS Anzahl in einem "sinnvollen" Satz ausgeben werden
- es sollte Fuktionen addPassenger() und deltePassenger() geben, welche Personen in Autos setzen und sie entfernen kann (achtet hier auf Rahmenbedingungen z.B. Sitzplätze)
- Es sollte eine Funktion getPassengers() geben, welche die Namen aller Mitfahrer auflistet
- ist ein "Car" voll besetzt soll es eine Funktion startRide() geben, welche ausgibt, dass die Fahrt beginnt und wer alles an Board ist; ist das "Car" nicht voll besetzt soll eine entsprechende Fehlermeldung kommen
### <ins> Main: </ins>
- legt eine neue Datei main.py in eurem working-directory an 
- importiert die Klassen "Person" und "Car" aus den jeweiligen Datein
- erstellt nun einige Car und Person Objekte und weist Persons einem Car zu
- testet ebenfalls die von euch geschriebenen Methoden der einzelnen Klassen, entweder über passende print-outs oder über den __assert()__ Befehl