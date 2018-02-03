#!/usr/bin/env python
# Download word dictionary from http://www.slovio.com/1/0.slovio/d-main.zip

import codecs
from collections import defaultdict
import random
import sys


def main():
	word_list = sys.argv[1:]
	reverse = False

	if '-r' in word_list:
		word_list.remove('-r')
		reverse = True

	slovio_dict = read_slovio_dict()

	if reverse:
		for word in word_list:
			reverse_words = []
			for key_word, value_words_list in slovio_dict.items():
				if word in value_words_list:
					reverse_words.append(key_word)

			print_translation(word, word_list=reverse_words)

	elif word_list:
		for word in word_list:
			print_translation(word, slovio_dict)
	else:
		random_key = random.choice(tuple(slovio_dict))
		print_translation(random_key, slovio_dict)


def print_translation(word, word_dict=None, word_list=None):
	if word_list:
		print("slovio reverse: {}: {}".format(word, ', '.join(word_list)))
	elif word in word_dict:
		print("slovio: {}: {}".format(word, ', '.join(word_dict[word])))
	else:
		print("slovio: no entry found for {}".format(word))


def read_slovio_dict():
	with codecs.open("/path/to/csv/file.csv", encoding='Windows-1252') as dict_file:
		raw_lines = [line.split(';') for line in dict_file]

	slovio_dict = defaultdict(list)

	for raw_line in raw_lines:
		try:
			slovio_dict[raw_line[0].lower()].append(raw_line[2])
		except IndexError:
			pass
	return slovio_dict


if __name__ == '__main__':
	main()

