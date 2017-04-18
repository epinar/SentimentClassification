from decimal import Decimal
from collections import Counter
import glob, os
import re
import math

dicts = [{}, {}] # Dictionaries for each class
nOfDocs = [0, 0] # Number of documents in each class
nOfTerms = [0, 0] # Number of terms in each class
condprob = {} # Conditional probabilites of words

# Returns the alphanumerical words of a text as a list.
def words(text): return re.findall(r'\w+', text)

# Reads the files in a directory.
def reader(directory, dic):
	os.chdir(directory)
	for file in glob.glob("*.txt"):
		corpus = Counter(words(open(file).read()))
		addToDict(corpus, dic)
		nOfDocs[dic] += 1

# Constructs the dictionaries of classes.
def addToDict(corpus, dic):
	for w in corpus:
		nOfTerms[dic] += 1
		if w in dicts[dic]:
			dicts[dic][w] += 1 
		else:
			dicts[dic][w] = 1

# Calculates the conditional probabilities of each word in dictionary. Takes the Laplace smooting coefficient alpha as input.
def calcLikeli(alpha):
	global condprob
	condprob = {}
	for d, dic in enumerate(dicts):
		for k, v in dic.items():
			if k not in condprob:
				condprob[k] = {0: 0, 1: 0}
				if alpha is not 0:
					condprob[k][1-d] = math.log(Decimal(alpha)) - math.log(nOfTerms[d]+alpha*len(dicts[d]))
			condprob[k][d] = math.log(Decimal(v+alpha)) - math.log(nOfTerms[d]+alpha*len(dicts[d]))

# Starts the training phase.
def doTrain(alpha):
	cwd = os.getcwd()
	reader("data/train/pos/", 1) #positives
	os.chdir(cwd)
	reader("data/train/neg/", 0) #negatives
	os.chdir(cwd)
	calcLikeli(alpha)
	