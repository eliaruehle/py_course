# Funktionen

## Was sind Funktionen

+ Auslagerung von Code gleicher Funktionalität
+ Code, der nur nur ausgeführt wird, wenn er aufgerufen wird
+ Vergleich: Funktion in der Mathematik:
  + statt jedes mal den Term zur Berechnung eines Argumentes anzugeben sagen wir "f(x) = y"
  + ebenso in der Programmierung:
    + statt jedes mal einzeln zu berechnen, rufen wir die Funktion mit den entsprechenden Parametern auf und bekommen gegebenenfalls einen Wert zurück

## Wie definieren wir Funktionen

+ Keyword ***def*** 
+ identifier *name_der_funktion*
+ in den Klammern: zu übergebende Parameter
  + beliebig viele
  + durch Klammern getrennt:
    + dentifikation bei Argumentübergabe dann über Reihenfolge
    + Anzahl nicht bekannt: *arguments
      + Parameter als Tupel der beim Aufruf übergebenen Argumente
      + Zugriff mit Index
  + key-value:
    + Identifikation bei Argumentübergabe über den Namen
    + Anzahl nicht bekannt: **arguments
      + Parameter als dictionary der beim Aufruf übergebenen Argumente
      + Zugriff mit key
  + default- Wert
    + def functon_name(parametername = default_value)
+ code follows
+ ***return*** Statement
  + springt zurück an die aufrufende Stelle im Kontrollfluss
  + Wert hinter ***return*** wird zurückgegeben
+ pass: springt ohne return zurück in Programmcode

```py
def function(parameters):
    ...
    return 
```


## Wie arbeiten wir mit Funktionen

+ Aufruf:
  + funktionsname(...)
  + in Klammern die Argumente übergeben
    + genau so viele wie in Definition
    + wenn *parameter oder **parameter : egal
+ 
