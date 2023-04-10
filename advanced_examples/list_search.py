import math

'''
Zunächst betrachten wir die einfachste aller Suchen, die lineare Suche.
Bei der linearen Suche wird eine gegebene Liste solange elementweise durchsucht, bis das zu suchende Element gefunden wurde.
'''
def linear_search(list, element):
    for index in range(len(list)):
        if list[index] == element:
            return element
    raise ValueError(f"The list does not contain the searched element '{element}'")

# Variante der lineare Suche mit Typing, das kann man machen um mehr Typsicherheit in Programme zu bekommen.
def linear_search2(list : list[int], element : int) -> int:
    for index in range(len(list)):
        if list[index] == element:
            return element
    raise ValueError(f"The list does not contain the searched element '{element}'")

'''
Als nächstes wollen wir linear nach dem n-ten Vorkommen eines Elementes in einer Liste suchen.
Dabei wollen wir eine counter-Variable einführen, die immer hochgezählt wird, wenn ein Vorkommen gefunden wurde.
'''
def search_for_nth(list, element, n):
    counter = 0
    for index in range(len(list)):
        if list[index] == element:
            counter += 1
            if counter == n:
                return index
    raise ValueError(f"The List does not contain n appearances of the element '{element}'")


'''
Als nächstes betrachten wir die binäre Suche. Die Idee ist hier, dass eine _vorsortierte_ Liste vorliegt, in welcher wiefolgt gesucht wird:
1) Greife auf das mittelste Objekt in der Liste zu.
2) Prüfe das Element an dieser Stelle wiefolgt:
    - ist es dem gesuchte, so gib es zurück
    - ist es kleiner, so suche in der rechten Teilliste
    - ist es größer, so suche in der linken Teilliste
'''
def binary_search(list : list, element):
    list.sort()
    n = math.floor(len(list)/2)
    if list[n] == element:
        return element
    elif list[n] < element:
        return binary_search(list[n+1:], element)
    elif list[n] > element:
        return binary_search(list[:n], element)
    raise ValueError(f"The list does not contain the searched element '{element}'")

import unittest
    
class SearchTests(unittest.TestCase):

    list = [1,2,2,4,2,5,7,8,10,12]

    def test_linear_search(self):
        self.assertEqual(linear_search(self.list, 7), 7)
        self.assertEqual(linear_search2(self.list, 2), 2)
    
    def test_error_message(self):
        with self.assertRaises(ValueError):
            linear_search(self.list, 15)
            binary_search(self.list, 15)
            search_for_nth(self.list, 2, 4)
            search_for_nth(self.list, 15, 1)
        '''
        self.assertRaises(Exception, binary_search(self.list, 15))
        self.assertRaises(Exception, search_for_nth(self.list, 2, 4))
        self.assertRaises(Exception, search_for_nth(self.list, 15, 1))
        '''
    
    def test_binary_search(self):
        self.assertEqual(binary_search(self.list.copy(), 7), 7)
        self.assertEqual(binary_search(self.list.copy(), 2), 2)
    
    def test_nth_search(self):
        self.assertEqual(search_for_nth(self.list, 2, 3), 4)
        self.assertEqual(search_for_nth(self.list, 2, 2), 2)

if __name__ == '__main__':
    unittest.main(exit=False)
    