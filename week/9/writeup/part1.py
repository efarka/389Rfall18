#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing a useful library -- feel free to add any others you find necessary
import hashlib
import string

# this will work if you place this script in your writeup folder
wordlist = open("../probable-v2-top1575.txt", 'r')
hashes= open("../hashes", 'r')

wordlist=wordlist.readlines()
wordlist=[word.strip() for word in wordlist]
hashes=hashes.readlines()
# a string equal to 'abcdefghijklmnopqrstuvwxyz'.
salts = string.ascii_lowercase

for word in wordlist:
	for salt in salts:
    		curr=salt+word
		currhash=hashlib.sha512(curr).hexdigest()
	
		for h in hashes:
			h=h.splitlines()[0]
			if currhash==h:
				print('password is: ' + curr)

