#!/usr/bin/env python
# Download word dictionary from http://www.slovio.com/1/0.slovio/d-main.zip

import codecs
import os
import random
import sys
import zipfile
try:
    from urllib.request import urlopen
except ImportError:
    from urllib import urlopen

from collections import defaultdict


DICTIONARY_URL = 'http://www.slovio.com/1/0.slovio/d-main.zip'


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
                elif word in [e.replace('-', '') for e in value_words_list]:
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
    def read_csv_file(path):
        with codecs.open(path, encoding='Windows-1252') as dict_file:
            raw_lines = [line.split(';') for line in dict_file]
        return raw_lines

    def unzip_file(zip_file_path, csv_file_path):
        import zipfile

        zf = zipfile.PyZipFile(zip_file_path)

        with open(csv_file_path, 'wb') as f:
            f.write(zf.read(zf.infolist()[0].filename))

    def download_dictionary(url, zip_file_path):
        with open(zip_file_path, 'wb') as f:
            f.write(urlopen(url).read())

    current_folder = os.path.abspath(os.path.dirname(__file__))
    zip_file_path = os.path.join(current_folder, 'd-main.zip')
    csv_file_path = os.path.join(current_folder, 'd-main.csv')

    if os.path.isfile(csv_file_path):
        raw_lines = read_csv_file(csv_file_path)

    elif os.path.isfile(zip_file_path):
        unzip_file(zip_file_path, csv_file_path)
        raw_lines = read_csv_file(csv_file_path)

    else:
        print(
            "No dictionary file found in either {} or {}. Downloading from {}"
            .format(csv_file_path, zip_file_path, DICTIONARY_URL)
        )
        download_dictionary(DICTIONARY_URL, zip_file_path)
        unzip_file(zip_file_path, csv_file_path)
        raw_lines = read_csv_file(csv_file_path)

    slovio_dict = defaultdict(list)

    for raw_line in raw_lines:
        try:
            slovio_dict[raw_line[0].lower()].append(raw_line[2])
        except IndexError:
            pass
    return slovio_dict


if __name__ == '__main__':
    main()
