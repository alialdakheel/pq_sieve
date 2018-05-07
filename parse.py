#!/usr/bin/env python

import json
from pprint import pprint

fp = open('eq.json', 'r')

eq = json.load(fp)

pprint(eq)
