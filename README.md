#Word Cookies

Cheat for popular Android game Word Cookies.  
Use the permutations function from the itertools library and a set of common English words to get the answers.
---
```python
from itertools import permutations
from pprint import pprint


def word_cookies(cookie: str, lower: int = 3):
	cookie = cookie.lower()
	upper = len(cookie) + 1
	with open('Common English Words.txt', 'r') as words:
		# a set containing all the words
		words = {i.strip().lower() for i in words.readlines() if lower <= len(i) <= upper}
        
		# Get correct words by intersecting the set of valid words and the permutations of the given cookie
		# Arrange valid words in a dictionary using length of words as keys starting from the value of the lower range
		return {f"{i} Letter Words": {''.join(word) for word in permutations(cookie, i)} & words for i in range(lower, upper)}
        
    
cookies = word_cookies("Excellent")
pprint(cookies) 

# { '3 Letter Words': { 'cee',
#                       'cen',
#                       'cle',
#                       'cte',
#                       'ctn',
#                       'eel',
#                       'een',
#                       'ele',
#                       'ell',
#                       'elt',
#                       'enc',
#                       'ene',
#                       'enl',
#                       'ent',
#                       'etc',
#                       'exc',
#                       'ext',
#                       'lee',
#                       'len',
#                       'let',
#                       'lex',
#                       'nee',
#                       'nel',
#                       'net',
#                       'tec',
#                       'tee',
#                       'tel',
#                       'ten',
#                       'tex',
#                       'tln',
#                       'xcl'},
#   '4 Letter Words': { 'cele',
#                       'cell',
#                       'celt',
#                       'cene',
#                       'cent',
#                       'cete',
#                       'clee',
#                       'elec',
#                       'elle',
#                       'elne',
#                       'ence',
#                       'encl',
#                       'eten',
#                       'excl',
#                       'exec',
#                       'lect',
#                       'leet',
#                       'lene',
#                       'lent',
#                       'lete',
#                       'neel',
#                       'neet',
#                       'nell',
#                       'nete',
#                       'next',
#                       'teel',
#                       'teen',
#                       'tele',
#                       'tell',
#                       'xctl'},
#   '5 Letter Words': { 'celle',
#                       'clete',
#                       'ctene',
#                       'eeten',
#                       'elect',
#                       'eleen',
#                       'elene',
#                       'ellen',
#                       'excel',
#                       'exect',
#                       'lenee',
#                       'neele',
#                       'nelle',
#                       'teece',
#                       'telex'},
#   '6 Letter Words': { 'celene',
#                       'cetene',
#                       'ectene',
#                       'ellene',
#                       'encell',
#                       'leetle',
#                       'tellee',
#                       'tellen'},
#   '7 Letter Words': set(),
#   '8 Letter Words': set(),
#   '9 Letter Words': {'excellent'}}
```
