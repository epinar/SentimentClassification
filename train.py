from decimal import Decimal
from collections import Counter
import glob, os
import re
import math

dicts = [{}, {}]
nOfDocs = [0, 0]
nOfTerms = [0, 0]
condprob = {}

def words(text): return re.findall(r'\w+', text)

def reader(directory, dic):
	os.chdir(directory)
	for file in glob.glob("*.txt"):
		corpus = Counter(words(open(file).read()))
		addToDict(corpus, dic)
		nOfDocs[dic] += 1

def addToDict(corpus, dic):
	for w in corpus:
		nOfTerms[dic] += 1
		if w in dicts[dic]:
			dicts[dic][w] += 1 
		else:
			dicts[dic][w] = 1

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

def doTrain(alpha):
	cwd = os.getcwd()
	reader("data/train/pos/", 1) #positives
	os.chdir(cwd)
	reader("data/train/neg/", 0) #negatives
	os.chdir(cwd)
	calcLikeli(alpha)
	