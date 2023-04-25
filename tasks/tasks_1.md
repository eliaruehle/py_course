## Augaben
### Teil 1 & 2: Simple und forgeschrittene Datenstrukturen

#### Zahlen

+ Schreibe ein Programm, dass zwei Zahlen addiert und ausgibt. Versuche auch die Datentypen int und float zu mischen, von welchem Datentyp ist das Ergebnis?

+ Schreibe ein Programm, dass zwei Gleitkommazahlen addiert und das Ergebnis als Ganzzahl ausgibt. Probiere ob du es gezielt schaffst die Zahl einmal abgerundet und einmal aufgerundet auszugeben. Recherchiere nach den passenden Funktionen.

#### Strings

+ Schreibe ein Programm, dass zwei Strings konkateniert und ausgibt. Was passiert wenn man string1 += string2 berechnet und ausgeben lässt?

+ Definiere dir einen String und probiere aus, was die Funktionen count(), find(), split(), upper(), lower() tun!

count(“…“)
find(“…“)
split(“…“)
upper( )
lower( )

#### Listen

+ Schreibe eine Liste und füge alle Module hinzu, die du in diesem Semester belegst. Gib danach das letze Modul aus, welches du der Liste hinzugefügt hast. Gib auch die Anzahl aller Listenelemente aus.

+ Erstelle eine Liste aus mindestens 4 verschieden Datentypen. Gib für 2 Listenelemente den Typ aus. Wie kannst du auf Listenelemente zugreifen?

#### Sets
+ Versuche aus einer von dir neu angelegten oder bereits vorhanden Liste ein Set zu extrahieren. Worin besteht der Unterschied zu einer List?

+ Gebe dir die Anzahl an Einträgen des Sets aus, füge dann ein Element hinzu, welches schon vorhanden ist (recherchiere, wie das geht) und gib erneut die Länge aus, was passiert?
Füge nun ein neues Element hinzu, was beobachtest du jetzt?

#### Tupel
+ Erstelle ein Tupel mit 3 Einträgen und versuche einen Eintrag zu verändern. Ist dies möglich? Was gibt der Interpreter aus? Erstelle nun ein Tupel ohne es mit Werten zu initialisieren, wie kann man das realisiren?

#### Dictionarys

+ Erstelle zunächst ein leeres Dictionary (Welche 2 Methoden kann man dafür anwenden? Gibt es eine, die "schöner" ist?). Füge dann 5 Vorlesungen sowie den Professor hinzu der diese hält. Gib für 2 Vorlesungen aus, von welchem Professor sie gehalten werden. 

+ Eine Lehrveranstaltung kann ab sofort von mehreren Professoren gehalten werden. Ändere das Dictionary entsprechend ab, welche Datenstruktur eignet sich zum Ablegen mehrerer Vorlesungen?

+ (Zusatz:) Finde raus wie man sich alle keys und alle values eines vorhanden Dictionarys ausgeben lassen kann und teste es an deinem eigenen Beispiel.

### Teil 3: Kontrollstrukturen

+ Lege dir eine Liste mit mindestens 5 Strings an. Iteriere danach über die Liste und füge an jedes String Element ein "!" an. Lass dir danach die Liste ausgeben. 

+ Erstelle eine Liste von Integer/Float Werten. Berechne den Mittelwert der in der Liste enthaltenen Elemente und gib diesen aus. Caste den Mittelwert zu einem Integer und prüfe ob das resultierende Ergebnis gerade oder ungerade ist. 

+ Benutze das "match"-Statement und schreibe ein Programm, welches prüft ob ein gegebener Integer Wert gerade oder ungerade ist. Je nach Fall soll ein entsprechender String ausgegeben werden.

+ Schreibe ein Programm, was die ersten 100 Primzahlen ausgibt. Du kannst dabei folgende Funktion verwenden: 
```python
def is_prime(n:int) -> bool:
    if n < 2:
        return False
    for i in range(1, (n ** 0.5)+1):
        if n%i == 0:
            return False
        else:
            return True
```

+ Schreibe eine Funktion, welche einen String als Argument bekommt und für diese beurteilt, ob es sich um ein Palindrom handelt. z.B. sollte die Funktion für "Anna" den Wert True und für "Elia" den Wert "False" zurückgeben.

+ Implementiere eine lineare Suche. Bei der linearen Suche wird ein Array mit Werten nach einem bestimmten Wert durchsucht. Wenn der gesucht Wert gefunden wurde gib den Index zurück, an welchem sich der Wert befindet. __Hinweis:__ Die Funktion enumerate() kann helfen, was macht sie?

+ __(Zusatz - schwer):__ Recherchiere, wie die binäre Suche funktioniert. Implementiere eine Funktion, welches die Liste [2,1,5,6,3,8,9,3,2,5,6,1] durchsucht und den Index zurückgibt, an dem das Element 6 auftaucht. Was sind Anforderungen an die Liste vor Beginn der Suche?