# First lesson

## Bevor es losgeht

### Einleitung

- Wer sind wir?:
  - Name, Studiengang,...
- Was wollen wir hier machen?
  - basic-Konzepte der Programmierung, speziell für Python
    - menti: Programmiererfahrung, Motivation
  - Lerneinheit:
    - A: wir erklären und zeigen
    - B: Aufgaben zum selbst bearbeiten
  - menti: Wünsche für Themen?

## Lesson 1: Basics

### Python

- Scriptsprache:
  - Vergleich Programmiersprache (JAVA, C++, ...)
  - Interpreter:
    - Zeile für Zeile
    - nicht optimiert -> langsamer
  - dynamische Typisierung
    - Interpreter schließt selbst auf Typ
      - *SHOW*
    - im Verlauf änderbar
      - *SHOW*
    - casting möglich = von uns empfohlen
      - Übersicht
      - Sicherer
- reduzierte Syntax
  - nah dem Englischen
  - intuitives Schreiben
- Warum also Python
  - *ZEN OF PYTHON*
    - direkt, unkompliziert
    - Prototyping
  - einfach aber mächtig
    - A: Einsteiger
      - erste Kontakte (Programmierung, Programmierparadigmen,...)
    - B: Fortgeschrittene
      - Webentwicklung, Data Science, Machine Learning/ Deep Learning, Computerspiele

### Installation

- see installation.md

### Arbeit mit Python

- wie also Code schreiben und ausführen?
- interactive Mode
  - direkt mit Interpreter agierend
  Code direkt in Kommandozeile schreiben
  - betreten mittels:

```zsh
$ python3
```

  - REPL
    - Read Evaluate Print Loop
    - E + V + A
  - Enter = Ausführen
  - Shift + Enter = Zeilenumbruch
  - verlassen: "exit()"
  - *show*
  - perfekt geeignet um kleine Code-Snippets zu testen 
    - nicht wiederverwendbar
- größere Projekte, persistenter Code
  - schreiben Code in Editor/ IDE 
  - Speicherung als .py Datei
  - Ausführung mittels 

```zsh
$ python3 *datei_name.py* 
```
  - python3 steuert Interpreter an
  - datei_name.py auszuführende Datei

- Syntax
  - einfach, nah natürlicher Sprache
  - Kontrollfluss weitgehend ohne Semikolons, Klammerung
    - Einrückung
    - Grad der Einrückung definiert Blöcke oder Scopes
      - Gültigkeit von Variablen
      - Zugehörigkeit von Statements,...
    - in bspw C++ Einrückung nur Übersicht
  - Kommentare
    - #...
    - ''' ... '''
    - von Interpreter überlesen
      - beispiel dyn. Typisierung bereits gesehen
- Variablen
  - repräsentieren Wert im Speicher
    - Zugriff über Name
  - Name
    - eindeutige Identifikation
    - A-Z, a-z, 0-9, _
    - case sensitiv
      - MY_VAR ≠ my_var
    - sollten repräsentativ für den Wert benannt werden
    - camelCase, PascalCase, snake_case
      - Stil, Lesbarkeit, sollte einheitlich sein
  - müssen nicht deklariert sondern werden bei Wertzuweisung definiert
  - Typ
    - dynamisch
    - änderbar bei neuzuweisung

### Einfache Datentypen & -strukturen

---

[detailed bullets](https://docs.google.com/document/d/1ajODE2xZRfZ0tcr0La8fF50Lt_4n9iv19isfEGMoNlY/edit)
[presentation](https://www.mentimeter.com/app/dashboard)


### Augaben

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

+ Erstelle zwei Tuple und addiere sie mit "+". Welche Dimensionierung hat das entstehende Tuple? Wie kann man diese ausgeben? Kann man Tupel auch mit verschiedenen Datentypen angeben, wenn ja testet dies aus!

#### Dictionarys

+ Erstelle zunächst ein leeres Dictionary (Welche 2 Methoden kann man dafür anwenden? Gibt es eine, die "schöner" ist?). Füge dann 5 Vorlesungen sowie den Professor hinzu der diese hält. Gib für 2 Vorlesungen aus, von welchem Professor sie gehalten werden. 

+ Eine Lehrveranstaltung kann ab sofort von mehreren Professoren gehalten werden. Ändere das Dictionary entsprechend ab, welche Datenstruktur eignet sich zum Ablegen mehrerer Vorlesungen?

+ (Zusatz:) Finde raus wie man sich alle keys und alle values eines vorhanden Dictionarys ausgeben lassen kann und teste es an deinem eigenen Beispiel.
