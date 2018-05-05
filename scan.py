import nltk
import argparse
import nltk.corpus
import operator
from string import punctuation
from collections import defaultdict


def frequency(textTokens, rejectExtremeValues=True):
	
	freqDict = defaultdict(float)
	
	for line in textTokens:
		for w in line:
			if w not in set(nltk.corpus.stopwords.words('english')+list(punctuation)):
				freqDict[w]+=1

	if rejectExtremeValues:
		maximum = float(max(freqDict.values()))
		
		for (w, v) in freqDict.items():
			freqDict[w] = v / maximum
			if freqDict[w] >= 0.85 or freqDict[w] <= 0.15:
				freqDict[w] = v - 1 

	return freqDict


def calculateProb(fDict, textTokens, num, ):
	
	sentenceRank = defaultdict(float)
	
	for sentence in textTokens:
		s = " ".join(sentence)
		for word in sentence:
			if word in fDict:
				sentenceRank[s] += fDict[word]

	summaryLines=[]

	for i in range(0, num):
		if len(sentenceRank)!=0:
			s = max( sentenceRank.items(), key = operator.itemgetter(1))[0]
			
			summaryLines.append(s)
			del sentenceRank[s]

	return summaryLines


def summary(text, num):
	"""takes input as text and n in which summary of text
	 should be represented"""
	
	sentenceTokens = nltk.sent_tokenize(text)
	
	textTokens=[]
	for tok in sentenceTokens:
		textTokens.append(nltk.word_tokenize(tok.lower())) 

	fDict = frequency(textTokens, False)

	summary = calculateProb(fDict, textTokens, num)

	return summary	


if __name__=="__main__":
	
	parser = argparse.ArgumentParser(description='TextScan: Scan Text, one file at a time')

	parser.add_argument("filename", help='Enter the filename')
	parser.add_argument("-s", "--summarize", help="Summarize the text", action="store_true")
	parser.add_argument("-n", "--number", help="Number of lines", type = int, required=True)

	args = parser.parse_args()

	if args.summarize:
		
		f = open(args.filename, 'r')
		text = f.read()

		text = text.replace('\n', "")
		summ = summary(text, args.number)

		print(summ)