from collections import defaultdict
import shutil, os, json

__author__ = "Terrence Plunkett"


class WordFrequencies:
	""" Stores a list of words and the number of times the words have been added to the object.
	"""
	def __init__(self):
		self.words = set()
		self.counts = defaultdict(lambda:0)

	def add(self, word):
		""" Add a word if it isn't already in the list or increment the count for that word by 1.
			Makes everything lowercase, only adds words containing [a-z].
		"""
		if word.isalpha():
			word = word.lower()
			self.words.add(word)
			self.counts[word] += 1

	def get(self, word):
		""" Return the number of occurrences of the specified word.
		"""
		return self.counts[word]

	def update(self, words):
		""" Perform add() on an iterable of words.
		"""
		for w in words:
			self.add(w)

	def num_words_counted(self):
		""" Return the number of words that have been counted.
		"""
		return sum(self.counts.values())

	def num_unique_words(self):
		""" Return how many unique words have been counted.
		"""
		return len(self.words)

	def save(self, path):
		""" Export this object to a file in the form of:
			line 1: json string for a list of unique words
			line 2: json dictionary where key is unique word and value is number of occurrences.
		"""
		with open(path, 'w') as f:
			words = json.dumps(list(self.words))
			counts = json.dumps(self.counts)
			r = f.write(words)
			r = f.write('\n')
			r = f.write(counts)

	def load(self, path):
		""" Import a file based on the same form as the save() method and add it to this object.
		"""
		words, counts = open(path, 'r').read().split('\n')
		words = set(json.loads(words))
		counts = json.loads(counts)
		self.words = words
		self.counts.update(counts)


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

	files_path = "D:\\Downloads" # folder to load source texts from.
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


if __name__ == '__main__':
	main()