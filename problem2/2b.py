#!/usr/bin/python

import sys 
from pprint import pprint
from scapy.all import *

def main():
	f = open('inpartb.txt')
	src = f.readline().rstrip()
	dst = f.readline().rstrip()
	print src
	print dst
	srcPort = f.readline()
	dstPort = f.readline()
	iplayer = IP(src=src, dst=dst)
	transportlayer=TCP(sport=int(srcPort),dport=int(dstPort))
	httpHeader = f.read()

	http = Raw(load=httpHeader)

	packet=iplayer/transportlayer/http
	print str(packet)
	packet.show()
	send(packet)
	f.close()

if __name__ == '__main__':
	main()