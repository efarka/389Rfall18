#!/usr/bin/env python2

import sys
import struct
from datetime import datetime

# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0xdeadbeef
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python2 stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version = struct.unpack("<LL", data[0:8])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))


i = 8
timestamp=struct.unpack("<L", data[i:i+4]); i+=4
try:
	timestamp=datetime.fromtimestamp(timestamp[0])
except:
	bork("invalid time")
print("TIMESTAMP= " + str(timestamp))


author=data[i:i+8]; i+=8
if not(all(ord(char) < 128 for char in author)):
	bork("invalid author")
print("AUTHOR= " + str(author))


sec=struct.unpack("<L", data[i:i+4]); i+=4;
sec=sec[0]
if sec <1:
	bork("invalid section count")
print("SECTION COUNT= " + str(sec))

# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

print("-------  BODY  -------")
for a in range(0, sec+2):
	type, len=struct.unpack("<LL", data[i:i+8]); i+=8
	print("section number" + str(a+1))
	
	if type==1:
		print("png")
		secdata=data[i:i+len]; i+=len
		file=open("389rpic.png", "w")
		file.write("\x89\x50\x4e\x47\x0d\x0a\x1a\x0a")
		file.write(secdata)
		
	elif type==2:
		print("dwords")
		numwords=len/8
		arr=[]
		for i in range(0, numwords):
			curr=struct.unpack("<Q", data[i:i+8]); i+=8;
			arr.append(curr)
		for word in arr:
			print(str(word[0]))	
	elif type==3:
		print("utf8")
		secdata=data[i:i+len]; i+=len
		print(secdata)

	elif type==4:
		print("doubles")
		numwords=len/8
		arr=[]
		for i in range(0, numwords):
			curr=struct.unpack("<d", data[i:i+8]); i+=8;
			arr.append(curr)
		for word in arr:
			print(str(word[0]))
	elif type==5:
		print("words")
		#secdata=data[i:i+len]; i+=len;
		numwords=len/4
		tmp=i
		arr=[]
		for i in range(0, numwords):
			curr=struct.unpack("<L", data[i:i+4]); i+=4;
			arr.append(curr)
		for word in arr:
			print(str(word[0]))

		i=tmp+len
	elif type==6:
		print("cords")
		if(len !=16):
			bork("invalid coordinates")
		lat, lon= struct.unpack("dd", data[i:i+16]); i+=len
		print(str(lat) + ", " +  str(lon))

	elif type==7:
		print("reference")
		if(len!=4):
			bork("invalid reference")
		ref=struct.unpack("<L", data[i:i+4]); i+=len
		ref=ref[0]
		if ref<0 or ref>(a+1):
			bork("bad ref number")
		print("ref to " + str(ref))

	elif type==9:
		print("ascii")
		secdata=data[i:i+len]; i+=len;
		print(secdata)

	else:
		bork("invalid type")
	print(" ")
	
