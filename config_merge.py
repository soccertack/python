#!/usr/bin/env python

DEST = "./config_dest"
SRC = "./config_src"

def findline(src_line, fdest):
	ret = False
	fdest.seek(0)
	while True:
		line = fdest.readline()	
		if not line:
			break;
		if src_line == line:
			#print line
			ret = True
	return ret

def main():
	fin = open(SRC)
	fdest = open (DEST)
	while True:
		line = fin.readline()
		if not line:
			break;
		ret = findline(line, fdest)
		if not ret:
			print "Not Found: "+line.strip()
	fin.close()
	fdest.close()

if __name__ == "__main__":
	main()
