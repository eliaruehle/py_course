### Teil 3: Kontrollstrukturen

+ Lege dir eine Liste mit mindestens 5 Strings an. Iteriere danach über die Liste und füge an jedes String Element ein "!" an. Lass dir danach die Liste ausgeben. 

+ Erstelle eine Liste von Integer/Float Werten. Berechne den Mittelwert der in der Liste enthaltenen Elemente und gib diesen aus. Caste den Mittelwert zu einem Integer und prüfe ob das resultierende Ergebnis gerade oder ungerade ist. 

+ Benutze das "match"-Statement und schreibe ein Programm, welches prüft ob ein gegebener Integer Wert gerade oder ungerade ist. Je nach Fall soll ein entsprechender String ausgegeben werden.

+ Schreibe ein Programm, was die ersten 100 Primzahlen ausgibt. Du kannst dabei folgende Funktion verwenden: 
```python
def is_prime(n:int) -> bool:
    if n < 2:
        return False
    for i in range(2, int((n ** 0.5))+1):
        if n%i == 0:
            return False
    return True
```

+ Schreibe eine Funktion, welche einen String als Argument bekommt und für diese beurteilt, ob es sich um ein Palindrom handelt. z.B. sollte die Funktion für "Anna" den Wert True und für "Elia" den Wert "False" zurückgeben.

+ Implementiere eine lineare Suche. Bei der linearen Suche wird ein Array mit Werten nach einem bestimmten Wert durchsucht. Wenn der gesucht Wert gefunden wurde gib den Index zurück, an welchem sich der Wert befindet. __Hinweis:__ Die Funktion enumerate() kann helfen, was macht sie?

+ __(Zusatz - schwer):__ Recherchiere, wie die binäre Suche funktioniert. Implementiere eine Funktion, welches die Liste [2,1,5,6,3,8,9,3,2,5,6,1] durchsucht und den Index zurückgibt, an dem das Element 6 auftaucht. Was sind Anforderungen an die Liste vor Beginn der Suche?