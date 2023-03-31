import math

'''
Zunächst betrachten wir die einfachste aller Suchen, die lineare Suche.
Bei der linearen Suche wird eine gegebene Liste solange elementweise durchsucht, bis das zu suchende Element gefunden wurde.
Es wird immer das _erste_ gefundene Element zurückgegeben.
'''
def linear_search(list, element):
    for index in range(len(list)):
        # insert your code here
        pass
    raise ValueError(f"The list does not contain the element '{element}'.")

'''
Als nächstes wollen wir linear nach dem n-ten Vorkommen eines Elementes in einer Liste suchen.
Dabei wollen wir eine counter-Variable einführen, die immer hochgezählt wird, wenn ein Vorkommen gefunden wurde.
Es soll stets der Index der Liste zurückgegeben werden, an der das n-te Element steht.
Achtet auch hier auf eine Fehlerbehandlung für Elemente, die nicht in der Liste enthalten sind.
'''
def search_for_nth(list, element, n):
    # insert your code here, the template "return" can be removed
    return 0


'''
Als nächstes betrachten wir die binäre Suche. Die Idee ist hier, dass eine _vorsortierte_ Liste vorliegt, in welcher wiefolgt gesucht wird:
1) Greife auf das mittelste Objekt in der Liste zu.
2) Prüfe das Element an dieser Stelle wiefolgt:
    - ist es dem gesuchte, so gib es zurück
    - ist es kleiner, so suche in der rechten Teilliste
    - ist es größer, so suche in der linken Teilliste
Die Suche in den Teillisten kann über einen rekursiven Aufruf realisiert werden. 
Denkt an die Fehlerbehandlung!
'''
def binary_search(list, element):
    list.sort()         # übernimmt die Vorsortierung der Liste, sie Dokumentation für mehr Information
    # Hinweis: nutze math.floor() um einen Wert auf den nächsten Integer abzurunden 

'''
Der folgende Code prüft ob ihr die Funktionen richtig implementiert habt.
Bitte verändert diesen nicht, oder nur, wenn ihr sicher seid, was ihr tut ;)
'''
import unittest

class SearchTests(unittest.TestCase):

    list = [1,2,2,4,2,5,7,8,10,12]

    def test_linear_search(self):
        self.assertEqual(linear_search(self.list, 7), 7)
        self.assertEqual(linear_search(self.list, 2), 2)
    
    def test_error_message(self):
        self.assertRaises(ValueError, linear_search(self.list, 15))
        self.assertRaises(ValueError, binary_search(self.list, 15))
        self.assertRaises(ValueError, search_for_nth(self.list, 2, 4))
        self.assertRaises(ValueError, search_for_nth(self.list, 15, 1))
    
    def test_binary_search(self):
        self.assertEqual(binary_search(self.list, 7), 7)
        self.assertEqual(binary_search(self.list, 2), 2)
    
    def test_nth_search(self):
        self.assertEqual(search_for_nth(self.list, 2, 3), 4)
        self.assertEqual(search_for_nth(self.list, 2, 2), 2)

if __name__ == '__main__':
    unittest.main(exit=False)
