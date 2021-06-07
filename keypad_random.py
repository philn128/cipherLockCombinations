#!/usr/bin/env python
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='',formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-n','--attempts', help='number of random attempts to try',type=float,default=10000)
parser.add_argument('-k','--keys',type=int,default=5)
args=parser.parse_args()

keys=args.keys

attempts=set()

for i in range(int(args.attempts)):
	v=list(range(1,keys+1))
	np.random.shuffle(v)
	v=v[:np.random.randint(1,len(v)+1)]
	string=''
	while len(v) > 0:
		simultaneous_press=np.random.randint(1,len(v)+1)
		string+=str(tuple(sorted(v[:simultaneous_press])))
		v=v[simultaneous_press:]
	string=string.replace(' ','')
	string=string.replace(',','')
	assert len(string)!=0
	attempts.add(string)

print('\n'.join(attempts))
print("\n")	
print("%d solutions found"%len(attempts))
