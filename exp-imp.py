#!/usr/bin/env python
'''
implementsation of the Ahmed et.al. p+q search
psudocode:
	if n mod 10 == 1 then:
		if n mod 100 == 01 then:
			if n+1 mod 3 == 0 then:
				a1 = 300
				b1 = 102
				a2 = 300
				b2 = 198
				a3 = 60
				b3 = 30
				for k:




		if n mod 100 == 21 then:
		if n mod 100 == 41 then:
		if n mod 100 == 61 then:
		if n mod 100 == 81 then:
		if n mod 100 == 11 then:
		if n mod 100 == 31 then:
		if n mod 100 == 51 then:
		if n mod 100 == 71 then:
		if n mod 100 == 91 then:
'''
import sys
import math
import json
n= int(sys.argv[1])
def check_eq(a,b,k):
	r = a * k + b
	interm = r**2 - 4*n
	print interm
	res = math.sqrt(interm)
	print "interm = " + str(interm) + " square? " + str(res.is_integer())
	if (res.is_integer()):
		print "result p-q= " + str(res) + " at r = " + str(r)
		p = (r + res)/2
		q = (n/p)
		print "p = " + str(p)
		print "q = " + str(q)
		print "k = " + str(k)
		if (p.is_integer() & q.is_integer()):
			print "DONE!"
			exit()
def prep_check():
	fp = open('eq.json', 'w')
	d = {}
	print "----------------------------------------"
	a1 = 300
	b1 = 102
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1) + " e1 = " + str(e1)
	a2 = 300
	b2 = 198
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2) + " e2 = " + str(e2)
	a3 = 60
	b3 = 30
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	#
	#
	#TODO:
	d.update({'3|01' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 }})
	a1 = 300
	b1 = 2
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 300
	b2 = 202
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 300
	b3 = 98
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	a4 = 300
	b4 = 298
	g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
	e4 = (n - b4) / a4
	print "\ng4 = " + str(g4+1) + " e4 = " + str(e4)
	a5 = 60
	b5 = 10
	g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
	e5 = (n - b5) / a5
	print "\ng5 = " + str(g5+1) + " e5 = " + str(e5)
	a6 = 60
	b6 = 50
	g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
	e6 = (n - b6) / a6
	print "\ng6 = " + str(g6+1) + " e6 = " + str(e6)
	d.update({ '3!|01' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 , 'a4': a4 , 'a5': a5 , 'a6' : a6 , 'b4': b4 , 'b5': b5 , 'b6' : b6  }})
	a1 = 300
	b1 = 222
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 300
	b2 = 78
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 60
	b3 = 30
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	d.update({ '3|21' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 }})
	a1 = 300
	b1 = 22
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 300
	b2 = 122
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 300
	b3 = 278
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	a4 = 300
	b4 = 178
	g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
	e4 = (n - b4) / a4
	print "\ng4 = " + str(g4+1) + " e4 = " + str(e4)
	a5 = 60
	b5 = 10
	g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
	e5 = (n - b5) / a5
	print "\ng5 = " + str(g5+1) + " e5 = " + str(e5)
	a6 = 60
	b6 = 50
	g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
	e6 = (n - b6) / a6
	print "\ng6 = " + str(g6+1) + " e6 = " + str(e6)
	d.update({ '3!|21' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 , 'a4': a4 , 'a5': a5 , 'a6' : a6 , 'b4': b4 , 'b5': b5 , 'b6' : b6  }})
	a1 = 300
	b1 = 42
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 300
	b2 = 258
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 60
	b3 = 30
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	d.update({ '3|41' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 }})
	a1 = 300
	b1 = 142
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 300
	b2 = 242
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 300
	b3 = 58
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	a4 = 300
	b4 = 158
	g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
	e4 = (n - b4) / a4
	print "\ng4 = " + str(g4+1) + " e4 = " + str(e4)
	a5 = 60
	b5 = 10
	g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
	e5 = (n - b5) / a5
	print "\ng5 = " + str(g5+1) + " e5 = " + str(e5)
	a6 = 60
	b6 = 50
	g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
	e6 = (n - b6) / a6
	print "\ng6 = " + str(g6+1) + " e6 = " + str(e6)
	d.update({ '3!|41' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 , 'a4': a4 , 'a5': a5 , 'a6' : a6 , 'b4': b4 , 'b5': b5 , 'b6' : b6  }})
	a1 = 300
	b1 = 162
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 300
	b2 = 138
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 60
	b3 = 30
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	d.update({ '3|61' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 }})
	a1 = 300
	b1 = 62
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 300
	b2 = 262
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 300
	b3 = 38
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	a4 = 300
	b4 = 238
	g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
	e4 = (n - b4) / a4
	print "\ng4 = " + str(g4+1) + " e4 = " + str(e4)
	a5 = 60
	b5 = 10
	g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
	e5 = (n - b5) / a5
	print "\ng5 = " + str(g5+1) + " e5 = " + str(e5)
	a6 = 60
	b6 = 50
	g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
	e6 = (n - b6) / a6
	print "\ng6 = " + str(g6+1) + " e6 = " + str(e6)
	d.update({ '3!|61' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 , 'a4': a4 , 'a5': a5 , 'a6' : a6 , 'b4': b4 , 'b5': b5 , 'b6' : b6  }})
	a1 = 300
	b1 = 282
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 300
	b2 = 18
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 60
	b3 = 30
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	d.update({ '3|81' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 }})
	a1 = 300
	b1 = 82
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 300
	b2 = 182
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 300
	b3 = 118
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	a4 = 300
	b4 = 218
	g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
	e4 = (n - b4) / a4
	print "\ng4 = " + str(g4+1) + " e4 = " + str(e4)
	a5 = 60
	b5 = 10
	g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
	e5 = (n - b5) / a5
	print "\ng5 = " + str(g5+1) + " e5 = " + str(e5)
	a6 = 60
	b6 = 50
	g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
	e6 = (n - b6) / a6
	print "\ng6 = " + str(g6+1) + " e6 = " + str(e6)
	d.update({ '3!|81' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 , 'a4': a4 , 'a5': a5 , 'a6' : a6 , 'b4': b4 , 'b5': b5 , 'b6' : b6  }})
	a1 = 600
	b1 = 312
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	print "r = " + str(a1) + "k + " + str(b1)
	a2 = 600
	b2 = 288
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	print "r = " + str(a2) + "k + " + str(b2)
	a3 = 120
	b3 = 0
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	print "r = " + str(a3) + "k + " + str(b3)
	d.update({ '3,4|11' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 }})
	a1 = 600
	b1 = 112
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 600
	b2 = 512
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 600
	b3 = 88
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	a4 = 600
	b4 = 488
	g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
	e4 = (n - b4) / a4
	print "\ng4 = " + str(g4+1) + " e4 = " + str(e4)
	a5 = 120
	b5 = 40
	g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
	e5 = (n - b5) / a5
	print "\ng5 = " + str(g5+1) + " e5 = " + str(e5)
	a6 = 120
	b6 = 80
	g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
	e6 = (n - b6) / a6
	print "\ng6 = " + str(g6+1) + " e6 = " + str(e6)
	d.update({ '3!,4|11' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 , 'a4': a4 , 'a5': a5 , 'a6' : a6 , 'b4': b4 , 'b5': b5 , 'b6' : b6  }})
	a1 = 600
	b1 = 12
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 600
	b2 = 588
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 120
	b3 = 60
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	d.update({ '3,4!|11' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 }})
	print "in"
	a1 = 600
	b1 = 212
	g1 = (int(2 * math.ceil(math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 600
	b2 = 412
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 600
	b3 = 188
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	a4 = 600
	b4 = 388
	g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
	e4 = (n - b4) / a4
	print "\ng4 = " + str(g4+1) + " e4 = " + str(e4)
	a5 = 120
	b5 = 20
	g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
	e5 = (n - b5) / a5
	print "\ng5 = " + str(g5+1) + " e5 = " + str(e5)
	a6 = 120
	b6 = 100
	g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
	e6 = (n - b6) / a6
	print "\ng6 = " + str(g6+1) + " e6 = " + str(e6)
	d.update({ '3!,4!|11' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 , 'a4': a4 , 'a5': a5 , 'a6' : a6 , 'b4': b4 , 'b5': b5 , 'b6' : b6  }})
	a1 = 600
	b1 = 132
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 600
	b2 = 468
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 120
	b3 = 0
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	d.update({ '3,4|31' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 }})
	a1 = 600
	b1 = 332
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 600
	b2 = 532
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 600
	b3 = 68
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	a4 = 600
	b4 = 268
	g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
	e4 = (n - b4) / a4
	print "\ng4 = " + str(g4+1) + " e4 = " + str(e4)
	a5 = 120
	b5 = 40
	g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
	e5 = (n - b5) / a5
	print "\ng5 = " + str(g5+1) + " e5 = " + str(e5)
	a6 = 120
	b6 = 80
	g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
	e6 = (n - b6) / a6
	print "\ng6 = " + str(g6+1) + " e6 = " + str(e6)
	d.update({ '3!,4|31' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 , 'a4': a4 , 'a5': a5 , 'a6' : a6 , 'b4': b4 , 'b5': b5 , 'b6' : b6  }})
	a1 = 600
	b1 = 432
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 600
	b2 = 168
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 120
	b3 = 60
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	d.update({ '3,4!|31' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 }})
	a1 = 600
	b1 = 32
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 600
	b2 = 232
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 600
	b3 = 368
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	a4 = 600
	b4 = 568
	g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
	e4 = (n - b4) / a4
	print "\ng4 = " + str(g4+1) + " e4 = " + str(e4)
	a5 = 120
	b5 = 20
	g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
	e5 = (n - b5) / a5
	print "\ng5 = " + str(g5+1) + " e5 = " + str(e5)
	a6 = 120
	b6 = 100
	g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
	e6 = (n - b6) / a6
	print "\ng6 = " + str(g6+1) + " e6 = " + str(e6)
	d.update({ '3!,4!|31' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 , 'a4': a4 , 'a5': a5 , 'a6' : a6 , 'b4': b4 , 'b5': b5 , 'b6' : b6  }})
	a1 = 600
	b1 = 552
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 600
	b2 = 48
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 120
	b3 = 0
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	d.update({ '3,4|51' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 }})
	a1 = 600
	b1 = 152
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 600
	b2 = 352
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 600
	b3 = 248
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	a4 = 600
	b4 = 448
	g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
	e4 = (n - b4) / a4
	print "\ng4 = " + str(g4+1) + " e4 = " + str(e4)
	a5 = 120
	b5 = 40
	g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
	e5 = (n - b5) / a5
	print "\ng5 = " + str(g5+1) + " e5 = " + str(e5)
	a6 = 120
	b6 = 80
	g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
	e6 = (n - b6) / a6
	print "\ng6 = " + str(g6+1) + " e6 = " + str(e6)
	d.update({ '3!,4|51' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 , 'a4': a4 , 'a5': a5 , 'a6' : a6 , 'b4': b4 , 'b5': b5 , 'b6' : b6  }})
	a1 = 600
	b1 = 252
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 600
	b2 = 348
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 120
	b3 = 60
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	d.update({ '3,4!|51' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 }})
	a1 = 600
	b1 = 52
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 600
	b2 = 452
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 600
	b3 = 148
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	a4 = 600
	b4 = 548
	g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
	e4 = (n - b4) / a4
	print "\ng4 = " + str(g4+1) + " e4 = " + str(e4)
	a5 = 120
	b5 = 20
	g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
	e5 = (n - b5) / a5
	print "\ng5 = " + str(g5+1) + " e5 = " + str(e5)
	a6 = 120
	b6 = 100
	g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
	e6 = (n - b6) / a6
	print "\ng6 = " + str(g6+1) + " e6 = " + str(e6)
	d.update({ '3!,4!|51' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 , 'a4': a4 , 'a5': a5 , 'a6' : a6 , 'b4': b4 , 'b5': b5 , 'b6' : b6  }})
	a1 = 600
	b1 = 372
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 600
	b2 = 228
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 120
	b3 = 0
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	d.update({ '3,4|71' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 }})
	a1 = 600
	b1 = 172
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 600
	b2 = 572
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 600
	b3 = 428
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	a4 = 600
	b4 = 28
	g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
	e4 = (n - b4) / a4
	print "\ng4 = " + str(g4+1) + " e4 = " + str(e4)
	a5 = 120
	b5 = 40
	g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
	e5 = (n - b5) / a5
	print "\ng5 = " + str(g5+1) + " e5 = " + str(e5)
	a6 = 120
	b6 = 80
	g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
	e6 = (n - b6) / a6
	print "\ng6 = " + str(g6+1) + " e6 = " + str(e6)
	d.update({ '3!,4|71' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 , 'a4': a4 , 'a5': a5 , 'a6' : a6 , 'b4': b4 , 'b5': b5 , 'b6' : b6  }})
	a1 = 600
	b1 = 72
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 600
	b2 = 528
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 120
	b3 = 60
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	d.update({ '3,4!|71' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 }})
	a1 = 600
	b1 = 272
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 600
	b2 = 472
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 600
	b3 = 128
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	a4 = 600
	b4 = 328
	g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
	e4 = (n - b4) / a4
	print "\ng4 = " + str(g4+1) + " e4 = " + str(e4)
	a5 = 120
	b5 = 20
	g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
	e5 = (n - b5) / a5
	print "\ng5 = " + str(g5+1) + " e5 = " + str(e5)
	a6 = 120
	b6 = 100
	g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
	e6 = (n - b6) / a6
	print "\ng6 = " + str(g6+1) + " e6 = " + str(e6)
	d.update({ '3!,4!|71' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 , 'a4': a4 , 'a5': a5 , 'a6' : a6 , 'b4': b4 , 'b5': b5 , 'b6' : b6  }})
	a1 = 600
	b1 = 192
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 600
	b2 = 408
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 120
	b3 = 0
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	d.update({ '3,4|91' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 }})
	a1 = 600
	b1 = 392
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 600
	b2 = 592
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 600
	b3 = 8
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	a4 = 600
	b4 = 208
	g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
	e4 = (n - b4) / a4
	print "\ng4 = " + str(g4+1) + " e4 = " + str(e4)
	a5 = 120
	b5 = 40
	g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
	e5 = (n - b5) / a5
	print "\ng5 = " + str(g5+1) + " e5 = " + str(e5)
	a6 = 120
	b6 = 80
	g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
	e6 = (n - b6) / a6
	print "\ng6 = " + str(g6+1) + " e6 = " + str(e6)
	d.update({ '3!,4|91' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 , 'a4': a4 , 'a5': a5 , 'a6' : a6 , 'b4': b4 , 'b5': b5 , 'b6' : b6  }})
	a1 = 600
	b1 = 492
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 600
	b2 = 108
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 120
	b3 = 60
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	d.update({ '3,4!|91' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 }})
	a1 = 600
	b1 = 92
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 600
	b2 = 292
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 600
	b3 = 308
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	a4 = 600
	b4 = 508
	g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
	e4 = (n - b4) / a4
	print "\ng4 = " + str(g4+1) + " e4 = " + str(e4)
	a5 = 120
	b5 = 20
	g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
	e5 = (n - b5) / a5
	print "\ng5 = " + str(g5+1) + " e5 = " + str(e5)
	a6 = 120
	b6 = 100
	g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
	e6 = (n - b6) / a6
	print "\ng6 = " + str(g6+1) + " e6 = " + str(e6)
	d.update({ '3!,4!|91' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 , 'a4': a4 , 'a5': a5 , 'a6' : a6 , 'b4': b4 , 'b5': b5 , 'b6' : b6  }})
####################################################################################################
	a1 = 300
	b1 = 6
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 300
	b2 = 294
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 60
	b3 = 30
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	d.update({ '3|09' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 }})
	a1 = 300
	b1 = 106
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 300
	b2 = 206
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 300
	b3 = 94
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	a4 = 300
	b4 = 194
	g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
	e4 = (n - b4) / a4
	print "\ng4 = " + str(g4+1) + " e4 = " + str(e4)
	a5 = 60
	b5 = 10
	g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
	e5 = (n - b5) / a5
	print "\ng5 = " + str(g5+1) + " e5 = " + str(e5)
	a6 = 60
	b6 = 50
	g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
	e6 = (n - b6) / a6
	print "\ng6 = " + str(g6+1) + " e6 = " + str(e6)
	d.update({ '3!|09' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 , 'a4': a4 , 'a5': a5 , 'a6' : a6 , 'b4': b4 , 'b5': b5 , 'b6' : b6  }})
	a1 = 300
	b1 = 246
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 300
	b2 = 54
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 60
	b3 = 30
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	d.update({ '3|29' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 }})
	a1 = 300
	b1 = 46
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 300
	b2 = 146
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 300
	b3 = 154
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	a4 = 300
	b4 = 254
	g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
	e4 = (n - b4) / a4
	print "\ng4 = " + str(g4+1) + " e4 = " + str(e4)
	a5 = 60
	b5 = 10
	g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
	e5 = (n - b5) / a5
	print "\ng5 = " + str(g5+1) + " e5 = " + str(e5)
	a6 = 60
	b6 = 50
	g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
	e6 = (n - b6) / a6
	print "\ng6 = " + str(g6+1) + " e6 = " + str(e6)
	d.update({ '3!|29' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 , 'a4': a4 , 'a5': a5 , 'a6' : a6 , 'b4': b4 , 'b5': b5 , 'b6' : b6  }})
	a1 = 300
	b1 = 186
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 300
	b2 = 114
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 60
	b3 = 30
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	d.update({ '3|49' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 }})
	a1 = 300
	b1 = 86
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 300
	b2 = 286
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 300
	b3 = 14
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	a4 = 300
	b4 = 214
	g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
	e4 = (n - b4) / a4
	print "\ng4 = " + str(g4+1) + " e4 = " + str(e4)
	a5 = 60
	b5 = 10
	g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
	e5 = (n - b5) / a5
	print "\ng5 = " + str(g5+1) + " e5 = " + str(e5)
	a6 = 60
	b6 = 50
	g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
	e6 = (n - b6) / a6
	print "\ng6 = " + str(g6+1) + " e6 = " + str(e6)
	d.update({ '3!|49' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 , 'a4': a4 , 'a5': a5 , 'a6' : a6 , 'b4': b4 , 'b5': b5 , 'b6' : b6  }})
	a1 = 300
	b1 = 126
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 300
	b2 = 174
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 60
	b3 = 30
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	d.update({ '3|69' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 }})
	a1 = 300
	b1 = 26
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 300
	b2 = 226
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 300
	b3 = 74
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	a4 = 300
	b4 = 274
	g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
	e4 = (n - b4) / a4
	print "\ng4 = " + str(g4+1) + " e4 = " + str(e4)
	a5 = 60
	b5 = 10
	g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
	e5 = (n - b5) / a5
	print "\ng5 = " + str(g5+1) + " e5 = " + str(e5)
	a6 = 60
	b6 = 50
	g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
	e6 = (n - b6) / a6
	print "\ng6 = " + str(g6+1) + " e6 = " + str(e6)
	d.update({ '3!|69' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 , 'a4': a4 , 'a5': a5 , 'a6' : a6 , 'b4': b4 , 'b5': b5 , 'b6' : b6  }})
	a1 = 300
	b1 = 66
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 300
	b2 = 234
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 60
	b3 = 30
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	d.update({ '3|89' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 }})
	a1 = 300
	b1 = 166
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 300
	b2 = 266
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 300
	b3 = 34
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	a4 = 300
	b4 = 134
	g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
	e4 = (n - b4) / a4
	print "\ng4 = " + str(g4+1) + " e4 = " + str(e4)
	a5 = 60
	b5 = 10
	g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
	e5 = (n - b5) / a5
	print "\ng5 = " + str(g5+1) + " e5 = " + str(e5)
	a6 = 60
	b6 = 50
	g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
	e6 = (n - b6) / a6
	print "\ng6 = " + str(g6+1) + " e6 = " + str(e6)
	d.update({ '3!|89' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 , 'a4': a4 , 'a5': a5 , 'a6' : a6 , 'b4': b4 , 'b5': b5 , 'b6' : b6  }})
	a1 = 600
	b1 = 576
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 600
	b2 = 24
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 120
	b3 = 0
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	d.update({ '3,4|19' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 }})
	a1 = 600
	b1 = 176
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 600
	b2 = 376
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 600
	b3 = 224
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	a4 = 600
	b4 = 424
	g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
	e4 = (n - b4) / a4
	print "\ng4 = " + str(g4+1) + " e4 = " + str(e4)
	a5 = 120
	b5 = 40
	g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
	e5 = (n - b5) / a5
	print "\ng5 = " + str(g5+1) + " e5 = " + str(e5)
	a6 = 120
	b6 = 80
	g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
	e6 = (n - b6) / a6
	print "\ng6 = " + str(g6+1) + " e6 = " + str(e6)
	d.update({ '3!,4|19' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 , 'a4': a4 , 'a5': a5 , 'a6' : a6 , 'b4': b4 , 'b5': b5 , 'b6' : b6  }})
	a1 = 600
	b1 = 276
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 600
	b2 = 324
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 120
	b3 = 60
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	d.update({ '3,4!|19' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 }})
	a1 = 600
	b1 = 76
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 600
	b2 = 476
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 600
	b3 = 124
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	a4 = 600
	b4 = 524
	g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
	e4 = (n - b4) / a4
	print "\ng4 = " + str(g4+1) + " e4 = " + str(e4)
	a5 = 120
	b5 = 20
	g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
	e5 = (n - b5) / a5
	print "\ng5 = " + str(g5+1) + " e5 = " + str(e5)
	a6 = 120
	b6 = 100
	g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
	e6 = (n - b6) / a6
	print "\ng6 = " + str(g6+1) + " e6 = " + str(e6)
	d.update({ '3!,4!|19' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 , 'a4': a4 , 'a5': a5 , 'a6' : a6 , 'b4': b4 , 'b5': b5 , 'b6' : b6  }})
	a1 = 600
	b1 = 516
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 600
	b2 = 84
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 120
	b3 = 60
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	d.update({ '3,4|39' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 }})
	a1 = 600
	b1 = 116
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 600
	b2 = 316
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 600
	b3 = 284
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	a4 = 600
	b4 = 484
	g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
	e4 = (n - b4) / a4
	print "\ng4 = " + str(g4+1) + " e4 = " + str(e4)
	a5 = 120
	b5 = 20
	g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
	e5 = (n - b5) / a5
	print "\ng5 = " + str(g5+1) + " e5 = " + str(e5)
	a6 = 120
	b6 = 100
	g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
	e6 = (n - b6) / a6
	print "\ng6 = " + str(g6+1) + " e6 = " + str(e6)
	d.update({ '3!,4|39' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 , 'a4': a4 , 'a5': a5 , 'a6' : a6 , 'b4': b4 , 'b5': b5 , 'b6' : b6  }})
	a1 = 600
	b1 = 216
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 600
	b2 = 384
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 120
	b3 = 0
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	d.update({ '3,4!|39' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 }})
	a1 = 600
	b1 = 16
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 600
	b2 = 416
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 600
	b3 = 84
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	a4 = 600
	b4 = 584
	g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
	e4 = (n - b4) / a4
	print "\ng4 = " + str(g4+1) + " e4 = " + str(e4)
	a5 = 120
	b5 = 40
	g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
	e5 = (n - b5) / a5
	print "\ng5 = " + str(g5+1) + " e5 = " + str(e5)
	a6 = 120
	b6 = 80
	g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
	e6 = (n - b6) / a6
	print "\ng6 = " + str(g6+1) + " e6 = " + str(e6)
	d.update({ '3!,4!|39' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 , 'a4': a4 , 'a5': a5 , 'a6' : a6 , 'b4': b4 , 'b5': b5 , 'b6' : b6  }})
	a1 = 600
	b1 = 456
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 600
	b2 = 144
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 120
	b3 = 0
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	d.update({ '3,4|59' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 }})
	a1 = 600
	b1 = 56
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 600
	b2 = 256
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 600
	b3 = 344
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	a4 = 600
	b4 = 544
	g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
	e4 = (n - b4) / a4
	print "\ng4 = " + str(g4+1) + " e4 = " + str(e4)
	a5 = 120
	b5 = 40
	g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
	e5 = (n - b5) / a5
	print "\ng5 = " + str(g5+1) + " e5 = " + str(e5)
	a6 = 120
	b6 = 80
	g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
	e6 = (n - b6) / a6
	print "\ng6 = " + str(g6+1) + " e6 = " + str(e6)
	d.update({ '3!,4|59' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 , 'a4': a4 , 'a5': a5 , 'a6' : a6 , 'b4': b4 , 'b5': b5 , 'b6' : b6  }})
	a1 = 600
	b1 = 156
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 600
	b2 = 444
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 120
	b3 = 60
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	d.update({ '3,4!|59' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 }})
	a1 = 600
	b1 = 356
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 600
	b2 = 556
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 600
	b3 = 44
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	a4 = 600
	b4 = 244
	g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
	e4 = (n - b4) / a4
	print "\ng4 = " + str(g4+1) + " e4 = " + str(e4)
	a5 = 120
	b5 = 20
	g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
	e5 = (n - b5) / a5
	print "\ng5 = " + str(g5+1) + " e5 = " + str(e5)
	a6 = 120
	b6 = 100
	g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
	e6 = (n - b6) / a6
	print "\ng6 = " + str(g6+1) + " e6 = " + str(e6)
	d.update({ '3!,4!|59' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 , 'a4': a4 , 'a5': a5 , 'a6' : a6 , 'b4': b4 , 'b5': b5 , 'b6' : b6  }})
	a1 = 600
	b1 = 396
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 600
	b2 = 204
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 120
	b3 = 60
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	d.update({ '3,4|79' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 }})
	a1 = 600
	b1 = 196
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 600
	b2 = 596
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 600
	b3 = 4
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	a4 = 600
	b4 = 404
	g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
	e4 = (n - b4) / a4
	print "\ng4 = " + str(g4+1) + " e4 = " + str(e4)
	a5 = 120
	b5 = 20
	g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
	e5 = (n - b5) / a5
	print "\ng5 = " + str(g5+1) + " e5 = " + str(e5)
	a6 = 120
	b6 = 100
	g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
	e6 = (n - b6) / a6
	print "\ng6 = " + str(g6+1) + " e6 = " + str(e6)
	d.update({ '3!,4|79' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 , 'a4': a4 , 'a5': a5 , 'a6' : a6 , 'b4': b4 , 'b5': b5 , 'b6' : b6  }})
	a1 = 600
	b1 = 96
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 600
	b2 = 504
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 120
	b3 = 0
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	d.update({ '3,4!|79' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 }})
	a1 = 600
	b1 = 296
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 600
	b2 = 496
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 600
	b3 = 104
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	a4 = 600
	b4 = 304
	g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
	e4 = (n - b4) / a4
	print "\ng4 = " + str(g4+1) + " e4 = " + str(e4)
	a5 = 120
	b5 = 40
	g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
	e5 = (n - b5) / a5
	print "\ng5 = " + str(g5+1) + " e5 = " + str(e5)
	a6 = 120
	b6 = 80
	g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
	e6 = (n - b6) / a6
	print "\ng6 = " + str(g6+1) + " e6 = " + str(e6)
	d.update({ '3!,4!|79' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 , 'a4': a4 , 'a5': a5 , 'a6' : a6 , 'b4': b4 , 'b5': b5 , 'b6' : b6  }})
	a1 = 600
	b1 = 336
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 600
	b2 = 264
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 120
	b3 = 0
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	d.update({ '3,4|99' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 }})
	a1 = 600
	b1 = 136
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 600
	b2 = 536
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 600
	b3 = 64
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	a4 = 600
	b4 = 464
	g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
	e4 = (n - b4) / a4
	print "\ng4 = " + str(g4+1) + " e4 = " + str(e4)
	a5 = 120
	b5 = 40
	g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
	e5 = (n - b5) / a5
	print "\ng5 = " + str(g5+1) + " e5 = " + str(e5)
	a6 = 120
	b6 = 80
	g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
	e6 = (n - b6) / a6
	print "\ng6 = " + str(g6+1) + " e6 = " + str(e6)
	d.update({ '3!,4|99' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 , 'a4': a4 , 'a5': a5 , 'a6' : a6 , 'b4': b4 , 'b5': b5 , 'b6' : b6  }})
	a1 = 600
	b1 = 36
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 600
	b2 = 564
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 120
	b3 = 60
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	d.update({ '3,4!|99' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 }})
	a1 = 600
	b1 = 364
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 600
	b2 = 236
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 600
	b3 = 436
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	a4 = 600
	b4 = 164
	g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
	e4 = (n - b4) / a4
	print "\ng4 = " + str(g4+1) + " e4 = " + str(e4)
	a5 = 120
	b5 = 20
	g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
	e5 = (n - b5) / a5
	print "\ng5 = " + str(g5+1) + " e5 = " + str(e5)
	a6 = 120
	b6 = 100
	g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
	e6 = (n - b6) / a6
	print "\ng6 = " + str(g6+1) + " e6 = " + str(e6)
	d.update({ '3!,4!|99' : { 'a1': a1 , 'a2': a2 , 'a3' : a3 , 'b1': b1 , 'b2': b2 , 'b3' : b3 , 'a4': a4 , 'a5': a5 , 'a6' : a6 , 'b4': b4 , 'b5': b5 , 'b6' : b6  }})
#####################################################################################################
	a1 = 60
	b1 = 54
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 60
	b2 = 6
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	d.update({ '3,4|03' : { 'a1': a1 , 'a2': a2 , 'b1': b1 , 'b2': b2 }})
	a1 = 60
	b1 = 14
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 60
	b2 = 34
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 60
	b3 = 26
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	a4 = 60
	b4 = 46
	g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
	e4 = (n - b4) / a4
	print "\ng4 = " + str(g4+1) + " e4 = " + str(e4)
	d.update({ '3!,4|03' : { 'a1': a1 , 'a2': a2 , 'a3': a3 , 'a4': a4 , 'b1': b1 , 'b2': b2 , 'b3': b3 , 'b4': b4 }})
	a1 = 60
	b1 = 24
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 60
	b2 = 36
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	d.update({ '3,4!|03' : { 'a1': a1 , 'a2': a2 , 'b1': b1 , 'b2': b2 }})
	a1 = 60
	b1 = 4
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 60
	b2 = 44
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 60
	b3 = 16
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	a4 = 60
	b4 = 56
	g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
	e4 = (n - b4) / a4
	print "\ng4 = " + str(g4+1) + " e4 = " + str(e4)
	d.update({ '3!,4!|03' : { 'a1': a1 , 'a2': a2 , 'a3': a3 , 'a4': a4 , 'b1': b1 , 'b2': b2 , 'b3': b3 , 'b4': b4 }})
	a1 = 60
	b1 = 18
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 60
	b2 = 42
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	d.update({ '3,4|07' : { 'a1': a1 , 'a2': a2 , 'b1': b1 , 'b2': b2}})
	a1 = 60
	b1 = 38
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 60
	b2 = 58
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 60
	b3 = 2
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	a4 = 60
	b4 = 22
	g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
	e4 = (n - b4) / a4
	print "\ng4 = " + str(g4+1) + " e4 = " + str(e4)
	d.update({ '3!,4|07' : { 'a1': a1 , 'a2': a2 , 'a3': a3 , 'a4': a4 , 'b1': b1 , 'b2': b2 , 'b3': b3 , 'b4': b4 }})
	a1 = 60
	b1 = 48
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 60
	b2 = 12
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	d.update({ '3,4!|07' : { 'a1': a1 , 'a2': a2 , 'b1': b1 , 'b2': b2}})
	a1 = 60
	b1 = 8
	g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
	e1 = (n - b1) / a1
	print "\ng1 = " + str(g1+1) + " e1 = " + str(e1)
	a2 = 60
	b2 = 28
	g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
	e2 = (n - b2) / a2
	print "\ng2 = " + str(g2+1) + " e2 = " + str(e2)
	a3 = 60
	b3 = 32
	g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
	e3 = (n - b3) / a3
	print "\ng3 = " + str(g3+1) + " e3 = " + str(e3)
	a4 = 60
	b4 = 52
	g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
	e4 = (n - b4) / a4
	print "\ng4 = " + str(g4+1) + " e4 = " + str(e4)
	d.update({ '3!,4!|07' : { 'a1': a1 , 'a2': a2 , 'a3': a3 , 'a4': a4 , 'b1': b1 , 'b2': b2 , 'b3': b3 , 'b4': b4 }})
	print "----------------------------------------"
	json.dump(d,fp)
def main():
	prep_check()
main()
