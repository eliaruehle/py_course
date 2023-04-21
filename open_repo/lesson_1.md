# Python

## Über Python

+ Scriptsprache
  + Interpreter 
    + Zeile für Zeile übersetzung des Script in Binärcode
    + langsamer
  + dynamische Typisierung
    + Interpreter schließt selbst auf Typ einer Variable
    + Typ im Verlauf des Programmes änderbar
+ reduzierte Syntax
  + nah an englischer Sprache
  + leicht zu lernen 
    + einsteigergeeignet - erste Kontakte mit Programmierung, Programmierparadigmen
+ direkt, unkompliziert, einfach aber mächtig
  + perfekt für schnelles Prototyping
  + verwendung in Webentwicklung, Data Science, Machine Learning, ...


## Arbeit mit Python

### 1. Interaktiver Modus
  - direkte Interaktion mit Interpreter in Kommandozeile
  - REPL = Read Evaluate Print Loop
  - testen kleiner Codestücke
  - nicht persistent (keine Wiederverwendung möglich)

  1. starten: Kommandozeilenbefehl: 
  ```zsh
  $ python3
  ```
  2. arbeiten: Code direkt im Terminal schreiben (Zeilenumbruch = SHift + Enter)
  3. beenden : "exit()" + Enter


### 2. Ausführen von Dateien
  - Trennung von Bearbeitung und Ausführung
  - persistent
  1. Code in IDE oder Editor schreiben
  2. Speicherung als .py Datei (zB.: hello_world.py)
  3. Ausführung:
    - Navigation in korrektes Verzeichnis
    - Kommandozeilenbefehl:
  ```zsh
  $ python3 *datei_name.py* 
  ```

## Syntax

+ Kontrollfluss durch Einrückung strukturiert
  + weitgehend ohne Semikolons, Klammerung
  + Grad der Einrückung definiert Blöcke/ Scopes
+ Kommentare
  + einzeilig: ***#*** Kommentar
  + mehrzeilig: ***'''*** ... ***'''*** oder ***"""*** ... ***"""***

## Variablen

+ repräsentieren Werte im Speicher
+ Name:
  + eindeutig
  + ermöglicht Zugriff
  + A-Z, a-z, _
    + PascalCase: SomeUselessVariableName
    + camelCase: someUselessVariableName
    + snake_case: some_useless_variable_name
+ Typ:
  + dynamisch, änderbar
  + mit ***type(*** _varName_ ***)*** bekommt man den Typ der entsprechenden Variable


## Datentypen & -strukturen

1. Numerische Typen

    |   | Ganzzahlen - Integer | Gleitkommazahlen - Float | Komplexe Zahlen |
    | ------------------- | ------------------- | ---------------- | --------------|
    | | ```a = 20``` | ```b = 3.6``` | ```c = 5 + 2j```|
    | kann zu ... konvertiert werden | float, complex | int, complex | |

    *Hinweis: Konvertierung mittels int(b), complex(a),...*

2. Texte- Strings

  + ```string_a = "Hello"```
  + eigentlich Liste von Buchstaben
  + Konkatenation:
    + string_a **+** string_b
    + nicht mit Zahlenwerten möglich!
  + Formatierung
    + nur Momentaufnahme, keine dauerhafte Änderung des Strings
    + Placeholder {} für Zahlenwert
      + string_c = "I am {} years old"
    + string_c.format(a)
  + viele Funktionen für Strings:
  ```
  string_a.count("a")
  string_a.upper()
  ...
  ```

3. BOOLE'sche Werte

  + *True*  
    + 1 bzw ≠0
    + alle nicht leeren Strukturen
  + *False*
    + 0
    + leere Strukturen (Listen, Sets, Tupel,...)

*Hinweis ***bool(*** variable ***)*** gibt BOOLE'schen Wert einer Variable zurück*

4. Listen

```
list = [ ]
```
  + änderbar, geordnet, mit Duplikaten
  + Zugriff:
    + ```list[ index ] ```
  + Hinzufügen
    + am Ende: ```list.append(item)```
    + an bestimmter Stelle: ```list.insert(index, item)```
  + Entfernen
    + bestimmtes Element: ```list.remove(item)```
    + an bestimmter Stelle: ```list.pop(index)```ODER ```del list[index]```
  + Bearbeiten
    + ```list[index]= item ```
  + viele weitere Funktionen:
    + clear(), sort(), reverse(),...

```
list = [1,2,3,4]
first = list[0]
last = list[3]
list.append(6)
list[4] = 5
```

5. Tupel

```
tupel = ()
``` 
  + geordnet, nicht änderbar, mit Duplikaten
  + Zugriff: 
    + ```tupel[index]```
    + Entpacken:
```
tupel = (1,2,3) 
(a,b,c) = tupel  
(x,y*) = tupel
```
*a ist erstes Tupelelement, b zweites,...* 
*y ist Liste der restlichen Elemente*

  + Bearbeiten:
    + nicht änderbar, daher Work-Around: Umwandlung in Liste
```
tupel_list = list(tupel)
   #bearbeiten
tupel = tupel (tupel_list)
```

6. Sets
```
set = {}
```
  + ungeordnet, Elemente nicht änderbar, keine Duplikate
  + Hinzufügen:
    + ```set.add(item)```
  + Entfernen:
    + ```set.remove(item)``` nur, wenn Element in Set
    + ```set.discard(item)``` egal, ob Element vorhanden oder nicht

7. Dictionary
```
dict = { a : b}
```
  + Speicherung von Key-Value - Paaren
  + geordnet, änderbar, keine Duplikate
  + Zugriff:
    + ```dict[key]```
    + ```dict.get(key)``` 
  + Hinzufügen oder Bearbeiten:
    + je nachdem, ob der key bereits vorhanden ist oder nicht
    + ```dict[key] = value```
    + ```dict.update({ key : value })```
  + Entfernen
    + ```del dict[key]```
    + ```dict.pop(key)```
  + weitere Funktionen:
    + keys(), values(), ...
    

### Überblick zu Datenstrukturen

| | Liste | Tupel | Set | Dictionary |
|---|---|---|---|---|
| Initialisierung | list = [] | tupel = () | set = {} | dict = {} |
| Ordnung | ja | ja | nein | ja |
| Änderbarkeit | ja | nein | nein | ja |
| Duplikate | ja | ja | nein | nein | 

*Hinweis: geordnet/ ungeordnet bezieht sich auf eine feste Reihenfolge der Elemente innerhalb der Struktur, nicht auf eine Sortierung*

*Hinweis: änderbar/ nicht änderbar bezieht sich auf die Bearbeitung der Elemente, nicht der Datenstruktur selbst. Sets gelten als nicht änderbar, können aber bspw. um Elemente erweitert werden.*