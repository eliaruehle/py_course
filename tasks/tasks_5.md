## Teil 5: Objektorientierung

+ Definiere eine Klasse "Bankkonto". Diese Klasse soll folgende Funktionalitäten erfüllen:
  + bei der Initialisierung eines Accounts soll jeweils Vorname, Nachname und initiales Vermögen eines Anlegers spezifiziert werden können 
  + es soll Funktionen geben, welche den Namen des Kontoinhabers sowie den aktuellen Kontostand zurückgeben
  + es soll Funktionen für mögliche Transaktionen (Ein- und Auszahlung) geben, dabei sollte stets geprüft und zurückgegeben werden, ob eine Transaktion gültig ist:
    + ein negativer Kontostand darf nie entstehen
    + ab Einzahlungen von mehr als 15000 Geldeinheiten erhebt die Bank einen Bearbeitungszins von 1%, dieser soll vom Transaktionsbetrag abgezogen werden
    + nichtpositive Einzahlungen sollen einen Error werfen
  + das Konto soll auf Wunsch aktiviert und deaktiviert werden können
  + wenn man einen print() auf ein Bankkonto-Objekt aufruft soll folgende Ausgabe erscheinen: "Das ist das Bankkonto von {Vorname} {Nachname}."