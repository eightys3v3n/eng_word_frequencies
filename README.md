# English word frequencies
This repo contains a Python script that reads source text files and counts the number of occurrences of each word. It then saves the word in a specified format for use in other projects. There are some pre-generated files for quick use. There is also a data structure for easy manipulation and use of the generated word lists.

## main.py
### Desc: The program used to count word occurrences in the source texts.

### Usage:
* Place a variety of text files in source_texts/.
* Run the program `python word_frequencies.py`.
* The created word_frequencies.json file contains the words and their frequencies in the source texts.

## word_frequencies.py
A class containing the required functions to use and modify a stored word frequency list. See file for functions and documentation.

## list1.json
A word frequencies list generated from a random set of fiction and non-fiction texts downloaded from [textfiles.com](http://textfiles.com/etext/).

## word_frequencies.json
* Line 1: A json encoded list of unique words.
* Line 2: A dictionary of the occurrence count of each unique word.