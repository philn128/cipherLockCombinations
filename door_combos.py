#!/usr/bin/env python
from itertools import chain, combinations, permutations
from scipy.special import comb
import argparse

parser = argparse.ArgumentParser(description='',formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-k','--keys',type=int,default=5)
args=parser.parse_args()

def accel_asc(n):
	a = [0 for i in range(n + 1)]
	k = 1
	y = n - 1
	while k != 0:
		x = a[k - 1] + 1
		k -= 1
		while 2 * x <= y:
			a[k] = x
			y -= x
			k += 1
		l = k + 1
		while x <= y:
			a[k] = x
			a[l] = y
			yield a[:k + 2]
			x += 1
			y -= 1
		a[k] = x + y
		y = x + y - 1
		yield a[:k + 1]

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return set(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))

def num_combos(num_keypad_buttons : int, press_sequence : tuple):
	"""For a given number of buttons on the keypad, and a press sequence, calculates the number of
	codes. A press sequence of (1,2,1) means that you have a single press, then a double press, then
	another single press for your code."""
	ret = 1
	num_buttons_available = num_keypad_buttons
	for i in press_sequence:
		ret *= int(comb(num_buttons_available, i))
		num_buttons_available -= i
	return ret

# Number of buttons on the keypad
NUM_BUTTONS = args.keys

partitions = list(accel_asc(NUM_BUTTONS))  # Convert to list, just so we can view it

partitions_powersets = [powerset(i) for i in partitions]

# Discard empty sets
for i in partitions_powersets:
	i.discard(())

possible_press_combinations = set()

for partition_powerset in partitions_powersets:
	for subset in partition_powerset:
		possible_press_combinations.add(subset)

possible_press_permutations = list()
for i in possible_press_combinations:
	possible_press_permutations.append(list(permutations(i, len(i))))

# flatten the list of lists of tuples to be a list of tuples
possible_press_permutations = [item for sublist in possible_press_permutations for item in sublist]
# convert to set of tuples. This removes duplicates
possible_press_permutations = set(possible_press_permutations)

num_possible_codes_per_subset = []
for i in possible_press_permutations:
	num_possible_codes_per_subset.append(num_combos(NUM_BUTTONS, i))

num_possible_codes = sum(num_possible_codes_per_subset)

print(f"Number of possible codes: {num_possible_codes}")
