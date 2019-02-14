import os
import nltk
import matplotlib.pyplot as plt
import json
import warnings
warnings.filterwarnings("ignore", message="numpy.dtype size changed")


def main():
	train_revs = parse_files('yelp/train')
	test_revs = parse_files('yelp/test')

	#Performs tokenization, normalization, stemming, and stopword removal on 'Content' and adds the result to a new key called 'clean' in the same data structure
	preprocess(train_revs)
	preprocess(test_revs)

	print(train_revs[0])

	#stores the processed reviews for convenience so I don't have to do it every time I run the program
	write_files('trainfile', train_revs, 'testfile', test_revs)

	train_revs = parse_files('trainfile')
	test_revs = parse_files('testfile')


def zipfs_law(train, test):
	freqs = 

def preprocess(reviews):
	punctuation = '. , < > / ? ; : \' " ] [ } { - _ = + ) ( \\ | ! @ # $ % ^ & * ` ~'.split()
	stopwords = get_stopwords()

	tokenizer = nltk.tokenize.treebank.TreebankWordTokenizer()
	stemmer = nltk.stem.snowball.EnglishStemmer()

	for rev in reviews:
		tokens = tokenizer.tokenize(rev['Content'])
		clean = []

		for word in tokens:
			#elims puncuation
			if word in punctuation:
				continue
			#changes to lower case
			word = word.lower()

			#if it can be converted to float it is either float or integer
			try:
				test = float(word)
			except ValueError:
				pass
			else:
				clean.append('NUM')
				continue

			#stems
			word = stemmer.stem(word)
			#removes stopwords
			if word in stopwords:
				continue
			#if it's made it this far, we want this version of the word in our cleaned tokens list
			clean.append(word)

		rev['clean'] = clean




def parse_files(filepath):
	reviews = []
	if os.path.isdir(filepath):
		for file in os.listdir(filepath):
			with open(os.path.join(filepath,file), 'r') as file:
				data = json.loads(file.read())
			for review in data['Reviews']:
				reviews.append(review)
	else:
		with open(filepath, 'r') as file:
			data = json.loads(file.read())
		for review in data:
			reviews.append(review)
	return reviews

def get_stopwords():
	stopwords = []
	with open('stopwords', 'r') as stop:
		for line in stop:
			if line == "\n":
				continue
			else:
				stopwords.append(line.strip())
	return stopwords

def write_files(trainpath, train, testpath, test):
	with open(trainpath, 'w') as trainfile:
		trainfile.write(json.dumps(train))
	with open(testpath, 'w') as testfile:
		testfile.write(json.dumps(test))

if __name__ == '__main__':
	main()