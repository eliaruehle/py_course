## __Objektorientierung Teil 2 - Vererbung und abstrakte Klassen__

### Wir wollen Vererbung und Objektorientiertung anhand von Autos nachvollziehen:
- es soll die Klassen Car, ElectricCar und HybridCar geben 
- die Klassen ElectricCar und HybridCar sollen von Car erben
- ein Car definiert sich über den ModelName, ReleaseYear, PS und Company 
- neben Funktionen zum übersichtlichen print-out sollten __mindestens__ folgende Funktionen gegeben sein:
  - start() - startet ein Auto, dies sollte auch gespeichert werden
  - stop() - stellt ein Auto wieder aus, dies sollte ebenfalls festegehalten werden und ausgebeben werden
  - es sollte eine abstrakte Funktion fuel() geben, welche später implementiert wird 
  - eine Funktion addUser soll es ermöglichen einem Car maximal 3 eingetragene Nutzer zuzuordnen
- die Klassen ElectricCar and HybridCar erben von Car, dabei soll folgendes beachtet werden:
  - ElectricCar sollte ein zusätzliches Attribut "capacity" besitzen, welches die Tankkapazität beschreibt; auch ein Attribut "status" für den aktuellen Füllstand ist sinnvoll
  - HybridCar sollte sowohl einen normalen Tank mit dem Attribut "capacity_organic" als auch ein "capacity_elec" Attribut haben; auch hier ist "status" angebracht
  - fuel() muss in beiden Klassen implementiert werden
- es sollte eine Funktion "drive()" geben, welche als Attribut den Kraftstoff bekommt, den die Fahrt verbraucht; es sollte nur gefahren werden dürfen, wenn das Auto gestartet wurde und genügend Energie/Kraftstoff zur Verfügung steht 
- legt am Ende in einer main() Funktion Objekte an und testet eure Funktionalität