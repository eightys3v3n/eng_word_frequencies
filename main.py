from collections import defaultdict
from word_frequencies import WordFrequencies
import shutil, os, json


__author__ = "Terrence Plunkett"


def source_whole_file(words, file):
	""" Read an entire file into memory, separate it into words, add all the words to the global words object.
	"""
	try:
		raw = open(file, 'r').read()
	except Exception as e:
		continue
	raw = raw.split()
	print("{} contains {} alpha words.".format(file, len(raw)))
	words.update(raw)

global words

words = WordFrequencies()
def main():
	""" Source all the files in the files_path directory and read them into the global words object.
	"""
	global words

	files_path = "source_texts" # folder to load source texts from.
	paths = os.listdir(files_path)
	files = []
	for p in paths:
		p = os.path.join(files_path, p)
		if os.path.isfile(p):
			files.append(p)
	for f in files:
		ext = f[f.rfind(os.path.extsep)+1:]
		if ext != 'txt':
			files.remove(f)
	print("Found {} txt files in {}".format(len(files), files_path))
	for file in files:
		source_whole_file(words, file)

	print("Counted {} words, {} of which are unique.".format(words.num_words_counted(), words.num_unique_words()))
	words.save("word_frequencies.json")


if __name__ == '__main__':
	main()