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

- Elias stuff follows

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

+ Schreibe ein Programm, dass zwei Zahlen addiert und ausgibt.

+ Schreibe ein Programm, dass zwei Gleitkommazahlen addiert und das Ergebnis als Ganzzahl ausgibt.

#### Strings

+ Schreibe ein Programm, dass zwei Strings konkateniert und ausgibt.

+ Definiere dir einen String und probiere aus, was die Funktionen count(), find(), split(), upper(), lower() tun!

count(“…“)
find(“…“)
split(“…“)
upper( )
lower( )

#### Listen

+ Schreibe eine Liste und füge alle Module hinzu, die du in diesem Semester belegst.

+ Schreibe eine Liste mit

#### After all

+ Schreibe ein Programm, dass zwei Gleitkommazahlen addiert und das Ergebnis als korrekt gerundete Ganzzahl ausgibt.

+ 
