#!/usr/bin/env python
import sys
for line in sys.stdin:
	line = line.strip()
	entry = line.split(",")
	key = entry[0]
	value= line
	if key=='a':
		print('{0}\t{1}'.format(key,value))
	elif key=='b':
		print('{0}\t{1}'.format(key,value))
		
