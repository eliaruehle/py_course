## Teil 4: Sortierung, List Comprehension, Lambda-Funktionen

### Sortierung
+ Lege dir eine Liste von Strings an. Schreibe nun Funktionen um folgende (aufsteigende) Sortierungen auf Listen durchzuführen: 
  + sortiere die Liste nach der Länge der Strings
  + sortiere die Strings nach der alphabetischen Reihenfolge ihrer letzten Buchstaben 
  + sortiere die Strings nach der alphabetischen Reihenfolge des mittleren Buchstabens
  + sortiere die Strings nach der Reihenfolge ihrer Hashwerte, nutzte dabei die hash(s:str) -> int Funktion um den Hash zu berechnen

+ Lege eine Liste von Paaren an, wobei jedes Paar aus zwei Zahlenwerten bestehen soll. Sortiere die Liste absteigend nach den Zahlenwerten des zweiten Tupeleintrags. 

### Lambda-Funktionen
+ Lege dir eine Liste von Integern an und definiere folgende Funktionen als Lambda-Funktion um sie mit map() auf deiner Liste anzuwenden:
  + berechne die Quadratwurzel jeder einzelnen Zahl
  + berechne die Dreierpotenz jeder Zahl 
  + inkrementiere die Zahl um ihr Doppeltes
  + subtrahiere von der Zahl ihre Quersumme

+ Schreibe eine Liste von beliebigen Zahlen (float & int) und berechne die Summe über alle Zahlen indem du die reduce() Funktion aus dem functools package nutzt. 

+ Erzeuge eine Liste mit zufälligen Integern (importiere dazu das modul random und nutze value = random.randint(upper, lower) um einen randomisierten Integer im Intervall [upper, lower] zu erhalten) und filtere diese Liste nach Elementen, welche gerade sind. Probiere das gleiche auch für das Filtern nach ungeraden Einträgen. 