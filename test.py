from collections import Counter
import glob, os
import re
import train 
import math
from decimal import Decimal

res = [[0, 0],[0, 0]] #results, 

def words(text): return re.findall(r'\w+', text)

def reader(directory, dic):
	os.chdir(directory)
	for f in glob.glob("*.txt"):
		corpus = Counter(words(open(f).read()))
		c = classify(corpus)
		res[dic][c] += 1

# 1 is class positive, 0 is class negative
def classify(corpus):
	p1 = math.log(Decimal(train.nOfDocs[0])) - math.log(train.nOfDocs[0]+train.nOfDocs[1])
	p2 = math.log(Decimal(train.nOfDocs[1])) - math.log(train.nOfDocs[0]+train.nOfDocs[1])
	p = Decimal(p1 - p2)
	for w in corpus:
		if w in train.condprob:
			c0 = Decimal(train.condprob[w][0])
			c1 = Decimal(train.condprob[w][1])
			p = p + c0 - c1
	return (0 if p>0 else 1)

def doTest():
	global res
	res = [[0,0], [0,0]]
	cwd = os.getcwd()
	reader("data/test/neg/", 0) #negatives
	os.chdir(cwd)
	reader("data/test/pos/", 1) #positives
	os.chdir(cwd)