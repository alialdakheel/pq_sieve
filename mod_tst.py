#!/usr/bin/env python

import json
from pprint import pprint

#fp = open("mod_p.json", "w")


mod_p = dict()
for p in [7,11,13]:
    mod_p[p]= dict()
    for i in range(0,p):
        for j in range(0,p):
            if ((i+j) % p) in mod_p.get(p,{-1:-1}).get((i*j+1) % p,[-1,-1]):
                continue
            mod_p[p].setdefault((i*j+1) % p,[]).append((i+j) % p)

#	for i in range(0,11):
#	    for j in range(0,11):
#	        if ((i+j) % 11) in mod_11.get((i*j+1) % 11,[-1,-1]):
#	            continue
#	        mod_11.setdefault((i*j+1) % 11,[]).append((i+j) % 11)

#mod_p = {7:mod_7, 11:mod_11}
#json.dump(mod_p,fp)
pprint(mod_p)
