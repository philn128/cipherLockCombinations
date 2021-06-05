#!/usr/bin/env python

import numpy as np

#C(n), D(n), D(n,k): see combos_count.md

#D(n,k) for n,k in {1,...,m}
def combos_array(m):
    d = np.empty((m, m), dtype=np.int64)
    for n in range(1,m+1):
        d[n-1,0] = 1
        for k in range(2,m+1):
            if n < k:
                d[n-1,k-1] = 0
            else:
                d[n-1,k-1] = k * (d[n-2,k-1] + d[n-2,k-2])
    return d

#D(n) for n in {1,...,m}
def full_combos(m): #D(n)
    d = combos_array(m)
    return np.sum(d, axis=1)

#C(n) for n in {1,...,m}
def combos(m): 
    return 2*full_combos(m) - 1

print(combos(8)) #fifth element should be 1081
