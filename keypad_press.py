#!/usr/bin/env python
from typing import List
from scipy.special import comb
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='',formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-k','--keys',type=int,default=5)
args=parser.parse_args()

nkeys=args.keys

def find_permutations(remaining : int, current : list) -> List[List[int]]:
	""" finds all permutations of possible keypad presses
	Example:
	>>> # the standard 5 key sipher lock
	>>> find_permutations(5,[])
	"""		
	if remaining == 0:
		return [current]
	all_outcomes=[]
	for i in range(1,remaining+1):
		combo=current+[i]
		all_outcomes+=find_permutations(remaining-i,combo)
	# the case where we don't press any more buttons; do not include the [] case
	if len(current):
		all_outcomes+=[current]
	return all_outcomes

permutations=find_permutations(nkeys,[])
print("Permutations:")
print(permutations)
print('')

total=0
for permutation in permutations:
	outcomes=[]
	remaining_presses=nkeys
	for v in permutation:
		outcomes.append(comb(remaining_presses,v,exact=True))
		remaining_presses-=v
	_prod=np.prod(outcomes)
	total+=_prod
	print("%s: prod(%s)=%d"%(str(permutation).ljust(16),outcomes,_prod))

print(f"\n{total} total combinations")

	
