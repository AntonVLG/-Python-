# Функция подсчета кол-ва самых часто употребляемых слов в тексте

import re
from collections import Counter

def count_words(path):
	with open(path) as file:
		all_words = re.findall(r"[0-9a-zA-Z-']+", file.read())
		all_words = [word.upper() for word in all_words]
		print('\nTotalWords:', len(all_words))

	word_counts = Counter()
	for word in all_words:
		word_counts[word] +=1

	print('\nСамые частые 20 Слов:')
	for word in word_counts.most_common(20):
		print(word[0], '\t',word[1])


count_words('text.txt')			