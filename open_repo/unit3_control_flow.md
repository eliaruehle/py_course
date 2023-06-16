# Kontrollfluss - Statements

## 1. IF-Statement

+ bedingte Codeausführung

```py
if  condition1  :   
  statementA           #nur ausgeführt, wenn condition1 == True 
elif condition2 :    
  statementB           #wenn condition1 == False and condition2 == True
else :      
  statementC           #wenn condition1 == False und condition2 == False
```

*auch ohne **elif** oder **else**-Zweig*


## 2. WHILE-Statement

+ wiederholte Codeausführung
+ geknüpft an Bedingung

```py
while condition :
    statement       #ausgeführt, solange condition == True
    break
```

****break*** bricht gesamtes while-Statement ab,*  
****continue*** bricht momentanen Schleifendurchlauf ab*


## 3. For-Statement

+ wiederholte Codeausführung
+ iterierend über Datenstruktur

```py
for x in interable:
    statement       #für jedes x in Interable ausgeführt
    continue
```

****break*** bricht gesamtes while-Statement ab,*  
****continue*** bricht momentanen Schleifendurchlauf ab*

## 4. Match-Statement

+ selektive Codeausführung
+ Fallunterscheidung nach wert einer Variablen

```python3
match variable:
    case case1:
        statement1
    case case2:
        statement2
    ...
```

same as:

```py
if variable == case1 :
    statement1
elif variable == case2 :
    statement2
elif ...
```

## Funktionen

### Was sind Funktionen

+ Auslagerung von Code gleicher Funktionalität
+ Code, der nur nur ausgeführt wird, wenn er aufgerufen wird
+ Vergleich: Funktion in der Mathematik:
  + statt jedes mal den Term zur Berechnung eines Argumentes anzugeben sagen wir "f(x) = y"
  + ebenso in der Programmierung:
    + statt jedes mal einzeln zu berechnen, rufen wir die Funktion mit den entsprechenden Parametern auf und bekommen gegebenenfalls einen Wert zurück

### Wie definieren wir Funktionen

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


### Wie arbeiten wir mit Funktionen

+ Aufruf:
  + funktionsname(...)
  + in Klammern die Argumente übergeben
    + genau so viele wie in Definition
    + wenn *parameter oder **parameter : egal
+ 

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
