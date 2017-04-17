#!/usr/bin/python

import sys 
from pprint import pprint
from scapy.all import *

listOfString = ['ColumbiaXX', 'HarvardXXX', 'YaleXXXXXX', 'PrincetonX', 'BrownXXXXX']

def main():
	if len(sys.argv) != 3:
		print 'Please enter the source and destination port numbers.'
		return

	srcPort = int(sys.argv[1])
	dstPort = int(sys.argv[2])
	for i in xrange(0, 21):
		iplayer = IP(dst='127.0.0.1')
		transportlayer=TCP(sport=srcPort,dport=(3000+i))
		packet=iplayer/transportlayer
		packet.show()
		send(packet)

	for s in listOfString:
		payload = Raw(load=s)
		iplayer = IP(dst='127.0.0.1')
		transportlayer=TCP(sport=srcPort,dport=dstPort)
		packet=iplayer/transportlayer/payload
		packet.show()
		send(packet)



if __name__ == '__main__':
	main()