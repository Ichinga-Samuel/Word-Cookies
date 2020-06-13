import itertools as it
import pprint as pp


def word_cookies(cookie):
	with open('Common English Words.txt', 'r') as fh:
		fh = fh.readlines()
		valid_words = {i.strip() for i in fh}  # a set containing all the words
		cookies = {}
		for i in range(3, len(cookie)+1):
			# permutation produces invalid words, an intersection with the set of valid words will return
			# the valid words produced by the permutation operation
			words = {''.join(i) for i in it.permutations(cookie, i)} & valid_words
			# there might be no valid words and permutation will return an empty set.
			# no need to add them to the dictionary of cookies
			if words != set():
				cookies[f'{i} Letter Words'] = words

		pp.pprint(cookies, indent=2)


word_cookies('Excellent')
