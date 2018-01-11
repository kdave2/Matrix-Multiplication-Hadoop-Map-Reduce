#!/usr/bin/env python
import sys
a={}
b={}
for input_line in sys.stdin:
	input_line = input_line.strip()
	
	this_key,value = input_line.split("\t",1)
	v = value.split(",")
	if this_key=='a':
		a[(int(v[1]),int(v[2]))]=int(v[3])
	elif this_key=='b':
		b[(int(v[1]),int(v[2]))]=int(v[3])
	
#and fill the blanks  
#for i in range(0,5):  
#	for j in range(0,5):  
#		if (i,j) not in a.keys():
#			a[(i,j)]=0
#		if (j,i) not in b.keys():
#			b[(j,i)]=0 
result=0
#compute the multiplication A*Bij = SUM(Aik * Bkj) for k in 0..4  
for i in range(0,4):  
	for j in range(0,5):  
		for k in range(0,3):  
			result = result + a[(i,k)]*b[(k,j)]  
		print("({0},{1})\t{2}".format(i,j,result))
		result =0  
     
