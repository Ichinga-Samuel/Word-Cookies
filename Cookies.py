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


cookies = word_cookies('Excellent')
pprint(cookies, indent=2)
