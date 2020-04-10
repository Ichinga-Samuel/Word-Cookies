import itertools as it
import functools as ft
import os
import pprint as pp


print(os.getcwd())

@ft.lru_cache(maxsize=128)
def word(a):
	with open('words.txt', 'r') as f, open('word.txt', 'r') as ff, open(f'{a}.txt','w') as ah:
		fh = f.readlines()
		ffh = ff.readlines()
		s = set(i.strip() for i in it.chain(fh, ffh))
		l3 = sorted({''.join(i) for i in it.permutations(a, 3)} & s)
		l4 = sorted({''.join(i) for i in it.permutations(a, 4)} & s)
		l5 = sorted({''.join(i) for i in it.permutations(a, 5)} & s)
		l6 = sorted({''.join(i) for i in it.permutations(a, 6)} & s)
		l7 = sorted({''.join(i) for i in it.permutations(a, 7)} & s)
		out = l3 + l4 + l5 + l6 + l7
		for i in out:
			ah.write(i+'\n')

		os.startfile(f'{a}.txt')

word('')
