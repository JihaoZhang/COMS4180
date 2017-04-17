#!/usr/bin/python

import sys 
from pprint import pprint
import operator
import time
def main():
	if len(sys.argv) != 5:
		print "Usage: the program take exactly 4 inputs: an integer n that is the length of the ngrams, an integer s that is the length of the slide, the name of the file to analyze, the name of the output file"
		return
	
	f1 = open(sys.argv[3], 'rb')
	f2 = open(sys.argv[4], 'wb')
	
	n = int(sys.argv[1])
	s = int(sys.argv[2])
	
	count = {}

	time1 = time.clock()

	while True:
		currentNgram = f1.read(n)
		if len(currentNgram) != n:
			break
		currentNgram = ngramToHex(currentNgram)
		if count.has_key(currentNgram):
			count[currentNgram] += 1
		else:
			count[currentNgram] = 1
		f1.seek(s-n, 1)

	sortedByCount = sorted(count.items(), key=operator.itemgetter(0))
	sortedByCount = sorted(sortedByCount, key=operator.itemgetter(1), reverse=True)
	pprint(sortedByCount[0:20])
	f2.write(str(sortedByCount))
	f1.close()
	f2.close()
	time2 = time.clock()
	print time2 - time1

def ngramToHex(currentNgram):
	# print currentNgram
	# print currentNgram[0]
	# print currentNgram[1]
	# print currentNgram[2]
	if len(currentNgram) == 1:
		return hex(ord(currentNgram))
	elif len(currentNgram) == 2:
		return hex((ord(currentNgram[0]) << 8) + ord(currentNgram[1]))
	elif len(currentNgram) == 3:
		return hex((((ord(currentNgram[0]) << 8) + ord(currentNgram[1])) << 8) + ord(currentNgram[2]))
	return ""

if __name__ == '__main__':
	main()