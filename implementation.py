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
					check_eq(a1,b1)
					check_eq(a2,b2)
					check_eq(a3,b3)
				
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

n= int(sys.argv[1])
def check_eq(a,b,k):
	r = a * k + b
	interm = r**2 - 4*n
	res = math.sqrt(interm) 
	if (res.is_integer()):
		print "a = " + str(a) + " b = " + str(b)
		print "result p-q= " + str(res) + " at r = " + str(r)
		p = (r + res)/2
		print "p = " + str(p)
		print "q = " + str(n/p)
		print "k = " + str(k)

def prep_check():

	if (n % 10 == 1):
		if (n % 100 == 1):
			if ((n+1) % 3 == 0):
				print "----------------------------------------"
				a1 = 300
				b1 = 102
				g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
				e1 = (n - b1) / a1
				print "\ng1 = " + str(g1) + " e1 = " + str(e1)
				for k in range(g1 + 1,e1,1):
					check_eq(a1,b1,k)

				print "----------------------------------------"
				a2 = 300
				b2 = 198
				g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
				e2 = (n - b2) / a2
				print "\ng2 = " + str(g2) + " e2 = " + str(e2)
				for k in range(g2 + 1,e2,1):
					check_eq(a2,b2,k)

				print "----------------------------------------"
				a3 = 60
				b3 = 30
				g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
				e3 = (n - b3) / a3
				print "\ng3 = " + str(g3) + " e3 = " + str(e3)
				for k in range(g3 + 1,e3,1):
					check_eq(a3,b3,k)
					#TODO: check the case where n = 504455801
				print "----------------------------------------"
			else:
				print "----------------------------------------"
				a1 = 300
				b1 = 2
				g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
				e1 = (n - b1) / a1
				print "\ng1 = " + str(g1) + " e1 = " + str(e1)
				for k in range(g1 + 1,e1,1):
					check_eq(a1,b1,k)

				print "----------------------------------------"
				a2 = 300
				b2 = 202
				g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
				e2 = (n - b2) / a2
				print "\ng2 = " + str(g2) + " e2 = " + str(e2)
				for k in range(g2 + 1,e2,1):
					check_eq(a2,b2,k)

				print "----------------------------------------"
				a3 = 300
				b3 = 98
				g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
				e3 = (n - b3) / a3
				print "\ng3 = " + str(g3) + " e3 = " + str(e3)
				for k in range(g3 + 1,e3,1):
					check_eq(a3,b3,k)
				
				print "----------------------------------------"
				a4 = 300
				b4 = 298
				g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
				e4 = (n - b4) / a4
				print "\ng4 = " + str(g4) + " e4 = " + str(e4)
				for k in range(g4 + 1,e4,1):
					check_eq(a4,b4,k)

				print "----------------------------------------"
				a5 = 60
				b5 = 10
				g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
				e5 = (n - b5) / a5
				print "\ng5 = " + str(g5) + " e5 = " + str(e5)
				for k in range(g5 + 1,e5,1):
					check_eq(a5,b5,k)

				print "----------------------------------------"
				a6 = 60
				b6 = 50
				g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
				e6 = (n - b6) / a6
				print "\ng6 = " + str(g6) + " e6 = " + str(e6)
				for k in range(g6 + 1,e6,1):
					check_eq(a6,b6,k)
				print "----------------------------------------"


		if (n % 100 == 21):
			if ((n+1) % 3 == 0):
				print "----------------------------------------"
				a1 = 300
				b1 = 222
				g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
				e1 = (n - b1) / a1
				print "\ng1 = " + str(g1) + " e1 = " + str(e1)
				for k in range(g1 + 1,e1,1):
					check_eq(a1,b1,k)

				print "----------------------------------------"
				a2 = 300
				b2 = 78
				g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
				e2 = (n - b2) / a2
				print "\ng2 = " + str(g2) + " e2 = " + str(e2)
				for k in range(g2 + 1,e2,1):
					check_eq(a2,b2,k)

				print "----------------------------------------"
				a3 = 60
				b3 = 30
				g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
				e3 = (n - b3) / a3
				print "\ng3 = " + str(g3) + " e3 = " + str(e3)
				for k in range(g3 + 1,e3,1):
					check_eq(a3,b3,k)
				print "----------------------------------------"
			else:
				print "----------------------------------------"
				a1 = 300
				b1 = 22
				g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
				e1 = (n - b1) / a1
				print "\ng1 = " + str(g1) + " e1 = " + str(e1)
				for k in range(g1 + 1,e1,1):
					check_eq(a1,b1,k)

				print "----------------------------------------"
				a2 = 300
				b2 = 122
				g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
				e2 = (n - b2) / a2
				print "\ng2 = " + str(g2) + " e2 = " + str(e2)
				for k in range(g2 + 1,e2,1):
					check_eq(a2,b2,k)

				print "----------------------------------------"
				a3 = 300
				b3 = 278
				g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
				e3 = (n - b3) / a3
				print "\ng3 = " + str(g3) + " e3 = " + str(e3)
				for k in range(g3 + 1,e3,1):
					check_eq(a3,b3,k)
				print "----------------------------------------"
				
				print "----------------------------------------"
				a4 = 300
				b4 = 178
				g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
				e4 = (n - b4) / a4
				print "\ng4 = " + str(g4) + " e4 = " + str(e4)
				for k in range(g4 + 1,e4,1):
					check_eq(a4,b4,k)

				print "----------------------------------------"
				a5 = 60
				b5 = 10
				g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
				e5 = (n - b5) / a5
				print "\ng5 = " + str(g5) + " e5 = " + str(e5)
				for k in range(g5 + 1,e5,1):
					check_eq(a5,b5,k)

				print "----------------------------------------"
				a6 = 60
				b6 = 50
				g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
				e6 = (n - b6) / a6
				print "\ng6 = " + str(g6) + " e6 = " + str(e6)
				for k in range(g6 + 1,e6,1):
					check_eq(a6,b6,k)
				print "----------------------------------------"
		if (n % 100 == 41):
			if ((n+1) % 3 == 0):
				print "----------------------------------------"
				a1 = 300
				b1 = 42
				g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
				e1 = (n - b1) / a1
				print "\ng1 = " + str(g1) + " e1 = " + str(e1)
				for k in range(g1 + 1,e1,1):
					check_eq(a1,b1,k)

				print "----------------------------------------"
				a2 = 300
				b2 = 258
				g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
				e2 = (n - b2) / a2
				print "\ng2 = " + str(g2) + " e2 = " + str(e2)
				for k in range(g2 + 1,e2,1):
					check_eq(a2,b2,k)

				print "----------------------------------------"
				a3 = 60
				b3 = 30
				g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
				e3 = (n - b3) / a3
				print "\ng3 = " + str(g3) + " e3 = " + str(e3)
				for k in range(g3 + 1,e3,1):
					check_eq(a3,b3,k)
				print "----------------------------------------"
			else:
				print "----------------------------------------"
				a1 = 300
				b1 = 142
				g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
				e1 = (n - b1) / a1
				print "\ng1 = " + str(g1) + " e1 = " + str(e1)
				for k in range(g1 + 1,e1,1):
					check_eq(a1,b1,k)

				print "----------------------------------------"
				a2 = 300
				b2 = 242
				g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
				e2 = (n - b2) / a2
				print "\ng2 = " + str(g2) + " e2 = " + str(e2)
				for k in range(g2 + 1,e2,1):
					check_eq(a2,b2,k)

				print "----------------------------------------"
				a3 = 300
				b3 = 57
				g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
				e3 = (n - b3) / a3
				print "\ng3 = " + str(g3) + " e3 = " + str(e3)
				for k in range(g3 + 1,e3,1):
					check_eq(a3,b3,k)
				print "----------------------------------------"
				
				print "----------------------------------------"
				a4 = 300
				b4 = 158
				g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
				e4 = (n - b4) / a4
				print "\ng4 = " + str(g4) + " e4 = " + str(e4)
				for k in range(g4 + 1,e4,1):
					check_eq(a4,b4,k)

				print "----------------------------------------"
				a5 = 60
				b5 = 10
				g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
				e5 = (n - b5) / a5
				print "\ng5 = " + str(g5) + " e5 = " + str(e5)
				for k in range(g5 + 1,e5,1):
					check_eq(a5,b5,k)

				print "----------------------------------------"
				a6 = 60
				b6 = 50
				g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
				e6 = (n - b6) / a6
				print "\ng6 = " + str(g6) + " e6 = " + str(e6)
				for k in range(g6 + 1,e6,1):
					check_eq(a6,b6,k)
				print "----------------------------------------"
			
		if (n % 100 == 61):
			if ((n+1) % 3 == 0):
				print "----------------------------------------"
				a1 = 300
				b1 = 162
				g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
				e1 = (n - b1) / a1
				print "\ng1 = " + str(g1) + " e1 = " + str(e1)
				for k in range(g1 + 1,e1,1):
					check_eq(a1,b1,k)

				print "----------------------------------------"
				a2 = 300
				b2 = 138
				g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
				e2 = (n - b2) / a2
				print "\ng2 = " + str(g2) + " e2 = " + str(e2)
				for k in range(g2 + 1,e2,1):
					check_eq(a2,b2,k)

				print "----------------------------------------"
				a3 = 60
				b3 = 30
				g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
				e3 = (n - b3) / a3
				print "\ng3 = " + str(g3) + " e3 = " + str(e3)
				for k in range(g3 + 1,e3,1):
					check_eq(a3,b3,k)
				print "----------------------------------------"
			else:
				print "----------------------------------------"
				a1 = 300
				b1 = 62
				g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
				e1 = (n - b1) / a1
				print "\ng1 = " + str(g1) + " e1 = " + str(e1)
				for k in range(g1 + 1,e1,1):
					check_eq(a1,b1,k)

				print "----------------------------------------"
				a2 = 300
				b2 = 262
				g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
				e2 = (n - b2) / a2
				print "\ng2 = " + str(g2) + " e2 = " + str(e2)
				for k in range(g2 + 1,e2,1):
					check_eq(a2,b2,k)

				print "----------------------------------------"
				a3 = 300
				b3 = 38
				g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
				e3 = (n - b3) / a3
				print "\ng3 = " + str(g3) + " e3 = " + str(e3)
				for k in range(g3 + 1,e3,1):
					check_eq(a3,b3,k)
				print "----------------------------------------"
				
				print "----------------------------------------"
				a4 = 300
				b4 = 238
				g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
				e4 = (n - b4) / a4
				print "\ng4 = " + str(g4) + " e4 = " + str(e4)
				for k in range(g4 + 1,e4,1):
					check_eq(a4,b4,k)

				print "----------------------------------------"
				a5 = 60
				b5 = 10
				g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
				e5 = (n - b5) / a5
				print "\ng5 = " + str(g5) + " e5 = " + str(e5)
				for k in range(g5 + 1,e5,1):
					check_eq(a5,b5,k)

				print "----------------------------------------"
				a6 = 60
				b6 = 50
				g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
				e6 = (n - b6) / a6
				print "\ng6 = " + str(g6) + " e6 = " + str(e6)
				for k in range(g6 + 1,e6,1):
					check_eq(a6,b6,k)
				print "----------------------------------------"
				
		if (n % 100 == 81):
			if ((n+1) % 3 == 0):
				print "----------------------------------------"
				a1 = 300
				b1 = 282
				g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
				e1 = (n - b1) / a1
				print "\ng1 = " + str(g1) + " e1 = " + str(e1)
				for k in range(g1 + 1,e1,1):
					check_eq(a1,b1,k)

				print "----------------------------------------"
				a2 = 300
				b2 = 18
				g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
				e2 = (n - b2) / a2
				print "\ng2 = " + str(g2) + " e2 = " + str(e2)
				for k in range(g2 + 1,e2,1):
					check_eq(a2,b2,k)

				print "----------------------------------------"
				a3 = 60
				b3 = 30
				g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
				e3 = (n - b3) / a3
				print "\ng3 = " + str(g3) + " e3 = " + str(e3)
				for k in range(g3 + 1,e3,1):
					check_eq(a3,b3,k)
				print "----------------------------------------"
			else:
				print "----------------------------------------"
				a1 = 300
				b1 = 82
				g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
				e1 = (n - b1) / a1
				print "\ng1 = " + str(g1) + " e1 = " + str(e1)
				for k in range(g1 + 1,e1,1):
					check_eq(a1,b1,k)

				print "----------------------------------------"
				a2 = 300
				b2 = 182
				g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
				e2 = (n - b2) / a2
				print "\ng2 = " + str(g2) + " e2 = " + str(e2)
				for k in range(g2 + 1,e2,1):
					check_eq(a2,b2,k)

				print "----------------------------------------"
				a3 = 300
				b3 = 118
				g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
				e3 = (n - b3) / a3
				print "\ng3 = " + str(g3) + " e3 = " + str(e3)
				for k in range(g3 + 1,e3,1):
					check_eq(a3,b3,k)
				print "----------------------------------------"
				
				print "----------------------------------------"
				a4 = 300
				b4 = 218
				g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
				e4 = (n - b4) / a4
				print "\ng4 = " + str(g4) + " e4 = " + str(e4)
				for k in range(g4 + 1,e4,1):
					check_eq(a4,b4,k)

				print "----------------------------------------"
				a5 = 60
				b5 = 10
				g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
				e5 = (n - b5) / a5
				print "\ng5 = " + str(g5) + " e5 = " + str(e5)
				for k in range(g5 + 1,e5,1):
					check_eq(a5,b5,k)

				print "----------------------------------------"
				a6 = 60
				b6 = 50
				g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
				e6 = (n - b6) / a6
				print "\ng6 = " + str(g6) + " e6 = " + str(e6)
				for k in range(g6 + 1,e6,1):
					check_eq(a6,b6,k)
				print "----------------------------------------"

		if (n % 100 == 11):
			if (int(str(n)[-3]) % 2 != 0):
				if ((n+1) % 3 == 0):
					print "----------------------------------------"
					a1 = 600
					b1 = 312
					g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
					e1 = (n - b1) / a1
					print "\ng1 = " + str(g1) + " e1 = " + str(e1)
					for k in range(g1 + 1,e1,1):
						check_eq(a1,b1,k)
	
					print "----------------------------------------"
					a2 = 600
					b2 = 288
					g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
					e2 = (n - b2) / a2
					print "\ng2 = " + str(g2) + " e2 = " + str(e2)
					for k in range(g2 + 1,e2,1):
						check_eq(a2,b2,k)
	
					print "----------------------------------------"
					a3 = 120
					b3 = 0
					g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
					e3 = (n - b3) / a3
					print "\ng3 = " + str(g3) + " e3 = " + str(e3)
					for k in range(g3 + 1,e3,1):
						check_eq(a3,b3,k)
					print "----------------------------------------"
				else:
					print "----------------------------------------"
					a1 = 600
					b1 = 112
					g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
					e1 = (n - b1) / a1
					print "\ng1 = " + str(g1) + " e1 = " + str(e1)
					for k in range(g1 + 1,e1,1):
						check_eq(a1,b1,k)
	
					print "----------------------------------------"
					a2 = 600
					b2 = 512
					g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
					e2 = (n - b2) / a2
					print "\ng2 = " + str(g2) + " e2 = " + str(e2)
					for k in range(g2 + 1,e2,1):
						check_eq(a2,b2,k)
	
					print "----------------------------------------"
					a3 = 600
					b3 = 88
					g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
					e3 = (n - b3) / a3
					print "\ng3 = " + str(g3) + " e3 = " + str(e3)
					for k in range(g3 + 1,e3,1):
						check_eq(a3,b3,k)
					print "----------------------------------------"
					
					print "----------------------------------------"
					a4 = 600
					b4 = 488
					g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
					e4 = (n - b4) / a4
					print "\ng4 = " + str(g4) + " e4 = " + str(e4)
					for k in range(g4 + 1,e4,1):
						check_eq(a4,b4,k)
	
					print "----------------------------------------"
					a5 = 120
					b5 = 40
					g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
					e5 = (n - b5) / a5
					print "\ng5 = " + str(g5) + " e5 = " + str(e5)
					for k in range(g5 + 1,e5,1):
						check_eq(a5,b5,k)
	
					print "----------------------------------------"
					a6 = 120
					b6 = 80
					g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
					e6 = (n - b6) / a6
					print "\ng6 = " + str(g6) + " e6 = " + str(e6)
					for k in range(g6 + 1,e6,1):
						check_eq(a6,b6,k)
					print "----------------------------------------"
			elif (int(str(n)[-3]) % 2 == 0): 
				if ((n+1) % 3 == 0):
					print "----------------------------------------"
					a1 = 600
					b1 = 12
					g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
					e1 = (n - b1) / a1
					print "\ng1 = " + str(g1) + " e1 = " + str(e1)
					for k in range(g1 + 1,e1,1):
						check_eq(a1,b1,k)
	
					print "----------------------------------------"
					a2 = 600
					b2 = 588
					g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
					e2 = (n - b2) / a2
					print "\ng2 = " + str(g2) + " e2 = " + str(e2)
					for k in range(g2 + 1,e2,1):
						check_eq(a2,b2,k)
	
					print "----------------------------------------"
					a3 = 120
					b3 = 60
					g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
					e3 = (n - b3) / a3
					print "\ng3 = " + str(g3) + " e3 = " + str(e3)
					for k in range(g3 + 1,e3,1):
						check_eq(a3,b3,k)
					print "----------------------------------------"
				else:
					print "----------------------------------------"
					a1 = 600
					b1 = 212
					g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
					e1 = (n - b1) / a1
					print "\ng1 = " + str(g1) + " e1 = " + str(e1)
					for k in range(g1 + 1,e1,1):
						check_eq(a1,b1,k)
	
					print "----------------------------------------"
					a2 = 600
					b2 = 412
					g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
					e2 = (n - b2) / a2
					print "\ng2 = " + str(g2) + " e2 = " + str(e2)
					for k in range(g2 + 1,e2,1):
						check_eq(a2,b2,k)
	
					print "----------------------------------------"
					a3 = 600
					b3 = 188
					g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
					e3 = (n - b3) / a3
					print "\ng3 = " + str(g3) + " e3 = " + str(e3)
					for k in range(g3 + 1,e3,1):
						check_eq(a3,b3,k)
					print "----------------------------------------"
					
					print "----------------------------------------"
					a4 = 600
					b4 = 388
					g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
					e4 = (n - b4) / a4
					print "\ng4 = " + str(g4) + " e4 = " + str(e4)
					for k in range(g4 + 1,e4,1):
						check_eq(a4,b4,k)
	
					print "----------------------------------------"
					a5 = 120
					b5 = 20
					g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
					e5 = (n - b5) / a5
					print "\ng5 = " + str(g5) + " e5 = " + str(e5)
					for k in range(g5 + 1,e5,1):
						check_eq(a5,b5,k)
	
					print "----------------------------------------"
					a6 = 120
					b6 = 100
					g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
					e6 = (n - b6) / a6
					print "\ng6 = " + str(g6) + " e6 = " + str(e6)
					for k in range(g6 + 1,e6,1):
						check_eq(a6,b6,k)
					print "----------------------------------------"
			else:
				print "error"
		if (n % 100 == 31):
			if (int(str(n)[-3]) % 2 != 0):
				if ((n+1) % 3 == 0):
					print "----------------------------------------"
					a1 = 600
					b1 = 132
					g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
					e1 = (n - b1) / a1
					print "\ng1 = " + str(g1) + " e1 = " + str(e1)
					for k in range(g1 + 1,e1,1):
						check_eq(a1,b1,k)
	
					print "----------------------------------------"
					a2 = 600
					b2 = 468
					g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
					e2 = (n - b2) / a2
					print "\ng2 = " + str(g2) + " e2 = " + str(e2)
					for k in range(g2 + 1,e2,1):
						check_eq(a2,b2,k)
	
					print "----------------------------------------"
					a3 = 120
					b3 = 0
					g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
					e3 = (n - b3) / a3
					print "\ng3 = " + str(g3) + " e3 = " + str(e3)
					for k in range(g3 + 1,e3,1):
						check_eq(a3,b3,k)
					print "----------------------------------------"
				else:
					print "----------------------------------------"
					a1 = 600
					b1 = 332
					g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
					e1 = (n - b1) / a1
					print "\ng1 = " + str(g1) + " e1 = " + str(e1)
					for k in range(g1 + 1,e1,1):
						check_eq(a1,b1,k)
	
					print "----------------------------------------"
					a2 = 600
					b2 = 532
					g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
					e2 = (n - b2) / a2
					print "\ng2 = " + str(g2) + " e2 = " + str(e2)
					for k in range(g2 + 1,e2,1):
						check_eq(a2,b2,k)
	
					print "----------------------------------------"
					a3 = 600
					b3 = 68
					g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
					e3 = (n - b3) / a3
					print "\ng3 = " + str(g3) + " e3 = " + str(e3)
					for k in range(g3 + 1,e3,1):
						check_eq(a3,b3,k)
					print "----------------------------------------"
					
					print "----------------------------------------"
					a4 = 600
					b4 = 268
					g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
					e4 = (n - b4) / a4
					print "\ng4 = " + str(g4) + " e4 = " + str(e4)
					for k in range(g4 + 1,e4,1):
						check_eq(a4,b4,k)
	
					print "----------------------------------------"
					a5 = 120
					b5 = 40
					g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
					e5 = (n - b5) / a5
					print "\ng5 = " + str(g5) + " e5 = " + str(e5)
					for k in range(g5 + 1,e5,1):
						check_eq(a5,b5,k)
	
					print "----------------------------------------"
					a6 = 120
					b6 = 80
					g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
					e6 = (n - b6) / a6
					print "\ng6 = " + str(g6) + " e6 = " + str(e6)
					for k in range(g6 + 1,e6,1):
						check_eq(a6,b6,k)
					print "----------------------------------------"
			elif (int(str(n)[-3]) % 2 == 0): 
				if ((n+1) % 3 == 0):
					print "----------------------------------------"
					a1 = 600
					b1 = 432
					g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
					e1 = (n - b1) / a1
					print "\ng1 = " + str(g1) + " e1 = " + str(e1)
					for k in range(g1 + 1,e1,1):
						check_eq(a1,b1,k)
	
					print "----------------------------------------"
					a2 = 600
					b2 = 168
					g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
					e2 = (n - b2) / a2
					print "\ng2 = " + str(g2) + " e2 = " + str(e2)
					for k in range(g2 + 1,e2,1):
						check_eq(a2,b2,k)
	
					print "----------------------------------------"
					a3 = 120
					b3 = 60
					g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
					e3 = (n - b3) / a3
					print "\ng3 = " + str(g3) + " e3 = " + str(e3)
					for k in range(g3 + 1,e3,1):
						check_eq(a3,b3,k)
					print "----------------------------------------"
				else:
					print "----------------------------------------"
					a1 = 600
					b1 = 32
					g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
					e1 = (n - b1) / a1
					print "\ng1 = " + str(g1) + " e1 = " + str(e1)
					for k in range(g1 + 1,e1,1):
						check_eq(a1,b1,k)
	
					print "----------------------------------------"
					a2 = 600
					b2 = 232
					g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
					e2 = (n - b2) / a2
					print "\ng2 = " + str(g2) + " e2 = " + str(e2)
					for k in range(g2 + 1,e2,1):
						check_eq(a2,b2,k)
	
					print "----------------------------------------"
					a3 = 600
					b3 = 368
					g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
					e3 = (n - b3) / a3
					print "\ng3 = " + str(g3) + " e3 = " + str(e3)
					for k in range(g3 + 1,e3,1):
						check_eq(a3,b3,k)
					print "----------------------------------------"
					
					print "----------------------------------------"
					a4 = 600
					b4 = 568
					g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
					e4 = (n - b4) / a4
					print "\ng4 = " + str(g4) + " e4 = " + str(e4)
					for k in range(g4 + 1,e4,1):
						check_eq(a4,b4,k)
	
					print "----------------------------------------"
					a5 = 120
					b5 = 20
					g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
					e5 = (n - b5) / a5
					print "\ng5 = " + str(g5) + " e5 = " + str(e5)
					for k in range(g5 + 1,e5,1):
						check_eq(a5,b5,k)
	
					print "----------------------------------------"
					a6 = 120
					b6 = 100
					g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
					e6 = (n - b6) / a6
					print "\ng6 = " + str(g6) + " e6 = " + str(e6)
					for k in range(g6 + 1,e6,1):
						check_eq(a6,b6,k)
					print "----------------------------------------"
			else:
				print "error"
		if (n % 100 == 51):
			if (int(str(n)[-3]) % 2 != 0):
				if ((n+1) % 3 == 0):
					print "----------------------------------------"
					a1 = 600
					b1 = 552
					g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
					e1 = (n - b1) / a1
					print "\ng1 = " + str(g1) + " e1 = " + str(e1)
					for k in range(g1 + 1,e1,1):
						check_eq(a1,b1,k)
	
					print "----------------------------------------"
					a2 = 600
					b2 = 48
					g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
					e2 = (n - b2) / a2
					print "\ng2 = " + str(g2) + " e2 = " + str(e2)
					for k in range(g2 + 1,e2,1):
						check_eq(a2,b2,k)
	
					print "----------------------------------------"
					a3 = 120
					b3 = 0
					g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
					e3 = (n - b3) / a3
					print "\ng3 = " + str(g3) + " e3 = " + str(e3)
					for k in range(g3 + 1,e3,1):
						check_eq(a3,b3,k)
					print "----------------------------------------"
				else:
					print "----------------------------------------"
					a1 = 600
					b1 = 152
					g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
					e1 = (n - b1) / a1
					print "\ng1 = " + str(g1) + " e1 = " + str(e1)
					for k in range(g1 + 1,e1,1):
						check_eq(a1,b1,k)
	
					print "----------------------------------------"
					a2 = 600
					b2 = 352
					g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
					e2 = (n - b2) / a2
					print "\ng2 = " + str(g2) + " e2 = " + str(e2)
					for k in range(g2 + 1,e2,1):
						check_eq(a2,b2,k)
	
					print "----------------------------------------"
					a3 = 600
					b3 = 248
					g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
					e3 = (n - b3) / a3
					print "\ng3 = " + str(g3) + " e3 = " + str(e3)
					for k in range(g3 + 1,e3,1):
						check_eq(a3,b3,k)
					print "----------------------------------------"
					
					print "----------------------------------------"
					a4 = 600
					b4 = 448
					g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
					e4 = (n - b4) / a4
					print "\ng4 = " + str(g4) + " e4 = " + str(e4)
					for k in range(g4 + 1,e4,1):
						check_eq(a4,b4,k)
	
					print "----------------------------------------"
					a5 = 120
					b5 = 40
					g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
					e5 = (n - b5) / a5
					print "\ng5 = " + str(g5) + " e5 = " + str(e5)
					for k in range(g5 + 1,e5,1):
						check_eq(a5,b5,k)
	
					print "----------------------------------------"
					a6 = 120
					b6 = 80
					g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
					e6 = (n - b6) / a6
					print "\ng6 = " + str(g6) + " e6 = " + str(e6)
					for k in range(g6 + 1,e6,1):
						check_eq(a6,b6,k)
					print "----------------------------------------"
			elif (int(str(n)[-3]) % 2 == 0): 
				if ((n+1) % 3 == 0):
					print "----------------------------------------"
					a1 = 600
					b1 = 252
					g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
					e1 = (n - b1) / a1
					print "\ng1 = " + str(g1) + " e1 = " + str(e1)
					for k in range(g1 + 1,e1,1):
						check_eq(a1,b1,k)
	
					print "----------------------------------------"
					a2 = 600
					b2 = 348
					g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
					e2 = (n - b2) / a2
					print "\ng2 = " + str(g2) + " e2 = " + str(e2)
					for k in range(g2 + 1,e2,1):
						check_eq(a2,b2,k)
	
					print "----------------------------------------"
					a3 = 120
					b3 = 60
					g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
					e3 = (n - b3) / a3
					print "\ng3 = " + str(g3) + " e3 = " + str(e3)
					for k in range(g3 + 1,e3,1):
						check_eq(a3,b3,k)
					print "----------------------------------------"
				else:
					print "----------------------------------------"
					a1 = 600
					b1 = 52
					g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
					e1 = (n - b1) / a1
					print "\ng1 = " + str(g1) + " e1 = " + str(e1)
					for k in range(g1 + 1,e1,1):
						check_eq(a1,b1,k)
	
					print "----------------------------------------"
					a2 = 600
					b2 = 452
					g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
					e2 = (n - b2) / a2
					print "\ng2 = " + str(g2) + " e2 = " + str(e2)
					for k in range(g2 + 1,e2,1):
						check_eq(a2,b2,k)
	
					print "----------------------------------------"
					a3 = 600
					b3 = 148
					g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
					e3 = (n - b3) / a3
					print "\ng3 = " + str(g3) + " e3 = " + str(e3)
					for k in range(g3 + 1,e3,1):
						check_eq(a3,b3,k)
					print "----------------------------------------"
					
					print "----------------------------------------"
					a4 = 600
					b4 = 548
					g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
					e4 = (n - b4) / a4
					print "\ng4 = " + str(g4) + " e4 = " + str(e4)
					for k in range(g4 + 1,e4,1):
						check_eq(a4,b4,k)
	
					print "----------------------------------------"
					a5 = 120
					b5 = 20
					g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
					e5 = (n - b5) / a5
					print "\ng5 = " + str(g5) + " e5 = " + str(e5)
					for k in range(g5 + 1,e5,1):
						check_eq(a5,b5,k)
	
					print "----------------------------------------"
					a6 = 120
					b6 = 100
					g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
					e6 = (n - b6) / a6
					print "\ng6 = " + str(g6) + " e6 = " + str(e6)
					for k in range(g6 + 1,e6,1):
						check_eq(a6,b6,k)
					print "----------------------------------------"
			else:
				print "error"
		if (n % 100 == 71):
			if (int(str(n)[-3]) % 2 != 0):
				if ((n+1) % 3 == 0):
					print "----------------------------------------"
					a1 = 600
					b1 = 372
					g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
					e1 = (n - b1) / a1
					print "\ng1 = " + str(g1) + " e1 = " + str(e1)
					for k in range(g1 + 1,e1,1):
						check_eq(a1,b1,k)
	
					print "----------------------------------------"
					a2 = 600
					b2 = 228
					g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
					e2 = (n - b2) / a2
					print "\ng2 = " + str(g2) + " e2 = " + str(e2)
					for k in range(g2 + 1,e2,1):
						check_eq(a2,b2,k)
	
					print "----------------------------------------"
					a3 = 120
					b3 = 0
					g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
					e3 = (n - b3) / a3
					print "\ng3 = " + str(g3) + " e3 = " + str(e3)
					for k in range(g3 + 1,e3,1):
						check_eq(a3,b3,k)
					print "----------------------------------------"
				else:
					print "----------------------------------------"
					a1 = 600
					b1 = 172
					g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
					e1 = (n - b1) / a1
					print "\ng1 = " + str(g1) + " e1 = " + str(e1)
					for k in range(g1 + 1,e1,1):
						check_eq(a1,b1,k)
	
					print "----------------------------------------"
					a2 = 600
					b2 = 572
					g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
					e2 = (n - b2) / a2
					print "\ng2 = " + str(g2) + " e2 = " + str(e2)
					for k in range(g2 + 1,e2,1):
						check_eq(a2,b2,k)
	
					print "----------------------------------------"
					a3 = 600
					b3 = 428
					g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
					e3 = (n - b3) / a3
					print "\ng3 = " + str(g3) + " e3 = " + str(e3)
					for k in range(g3 + 1,e3,1):
						check_eq(a3,b3,k)
					print "----------------------------------------"
					
					print "----------------------------------------"
					a4 = 600
					b4 = 28
					g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
					e4 = (n - b4) / a4
					print "\ng4 = " + str(g4) + " e4 = " + str(e4)
					for k in range(g4 + 1,e4,1):
						check_eq(a4,b4,k)
	
					print "----------------------------------------"
					a5 = 120
					b5 = 40
					g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
					e5 = (n - b5) / a5
					print "\ng5 = " + str(g5) + " e5 = " + str(e5)
					for k in range(g5 + 1,e5,1):
						check_eq(a5,b5,k)
	
					print "----------------------------------------"
					a6 = 120
					b6 = 80
					g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
					e6 = (n - b6) / a6
					print "\ng6 = " + str(g6) + " e6 = " + str(e6)
					for k in range(g6 + 1,e6,1):
						check_eq(a6,b6,k)
					print "----------------------------------------"
			elif (int(str(n)[-3]) % 2 == 0): 
				if ((n+1) % 3 == 0):
					print "----------------------------------------"
					a1 = 600
					b1 = 72
					g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
					e1 = (n - b1) / a1
					print "\ng1 = " + str(g1) + " e1 = " + str(e1)
					for k in range(g1 + 1,e1,1):
						check_eq(a1,b1,k)
	
					print "----------------------------------------"
					a2 = 600
					b2 = 528
					g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
					e2 = (n - b2) / a2
					print "\ng2 = " + str(g2) + " e2 = " + str(e2)
					for k in range(g2 + 1,e2,1):
						check_eq(a2,b2,k)
	
					print "----------------------------------------"
					a3 = 120
					b3 = 60
					g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
					e3 = (n - b3) / a3
					print "\ng3 = " + str(g3) + " e3 = " + str(e3)
					for k in range(g3 + 1,e3,1):
						check_eq(a3,b3,k)
					print "----------------------------------------"
				else:
					print "----------------------------------------"
					a1 = 600
					b1 = 272
					g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
					e1 = (n - b1) / a1
					print "\ng1 = " + str(g1) + " e1 = " + str(e1)
					for k in range(g1 + 1,e1,1):
						check_eq(a1,b1,k)
	
					print "----------------------------------------"
					a2 = 600
					b2 = 472
					g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
					e2 = (n - b2) / a2
					print "\ng2 = " + str(g2) + " e2 = " + str(e2)
					for k in range(g2 + 1,e2,1):
						check_eq(a2,b2,k)
	
					print "----------------------------------------"
					a3 = 600
					b3 = 128
					g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
					e3 = (n - b3) / a3
					print "\ng3 = " + str(g3) + " e3 = " + str(e3)
					for k in range(g3 + 1,e3,1):
						check_eq(a3,b3,k)
					print "----------------------------------------"
					
					print "----------------------------------------"
					a4 = 600
					b4 = 328
					g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
					e4 = (n - b4) / a4
					print "\ng4 = " + str(g4) + " e4 = " + str(e4)
					for k in range(g4 + 1,e4,1):
						check_eq(a4,b4,k)
	
					print "----------------------------------------"
					a5 = 120
					b5 = 20
					g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
					e5 = (n - b5) / a5
					print "\ng5 = " + str(g5) + " e5 = " + str(e5)
					for k in range(g5 + 1,e5,1):
						check_eq(a5,b5,k)
	
					print "----------------------------------------"
					a6 = 120
					b6 = 100
					g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
					e6 = (n - b6) / a6
					print "\ng6 = " + str(g6) + " e6 = " + str(e6)
					for k in range(g6 + 1,e6,1):
						check_eq(a6,b6,k)
					print "----------------------------------------"
			else:
				print "error"
		if (n % 100 == 91):
			if (int(str(n)[-3]) % 2 != 0):
				if ((n+1) % 3 == 0):
					print "----------------------------------------"
					a1 = 600
					b1 = 192
					g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
					e1 = (n - b1) / a1
					print "\ng1 = " + str(g1) + " e1 = " + str(e1)
					for k in range(g1 + 1,e1,1):
						check_eq(a1,b1,k)
	
					print "----------------------------------------"
					a2 = 600
					b2 = 408
					g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
					e2 = (n - b2) / a2
					print "\ng2 = " + str(g2) + " e2 = " + str(e2)
					for k in range(g2 + 1,e2,1):
						check_eq(a2,b2,k)
	
					print "----------------------------------------"
					a3 = 120
					b3 = 0
					g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
					e3 = (n - b3) / a3
					print "\ng3 = " + str(g3) + " e3 = " + str(e3)
					for k in range(g3 + 1,e3,1):
						check_eq(a3,b3,k)
					print "----------------------------------------"
				else:
					print "----------------------------------------"
					a1 = 600
					b1 = 392
					g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
					e1 = (n - b1) / a1
					print "\ng1 = " + str(g1) + " e1 = " + str(e1)
					for k in range(g1 + 1,e1,1):
						check_eq(a1,b1,k)
	
					print "----------------------------------------"
					a2 = 600
					b2 = 592
					g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
					e2 = (n - b2) / a2
					print "\ng2 = " + str(g2) + " e2 = " + str(e2)
					for k in range(g2 + 1,e2,1):
						check_eq(a2,b2,k)
	
					print "----------------------------------------"
					a3 = 600
					b3 = 8
					g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
					e3 = (n - b3) / a3
					print "\ng3 = " + str(g3) + " e3 = " + str(e3)
					for k in range(g3 + 1,e3,1):
						check_eq(a3,b3,k)
					print "----------------------------------------"
					
					print "----------------------------------------"
					a4 = 600
					b4 = 208
					g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
					e4 = (n - b4) / a4
					print "\ng4 = " + str(g4) + " e4 = " + str(e4)
					for k in range(g4 + 1,e4,1):
						check_eq(a4,b4,k)
	
					print "----------------------------------------"
					a5 = 120
					b5 = 40
					g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
					e5 = (n - b5) / a5
					print "\ng5 = " + str(g5) + " e5 = " + str(e5)
					for k in range(g5 + 1,e5,1):
						check_eq(a5,b5,k)
	
					print "----------------------------------------"
					a6 = 120
					b6 = 80
					g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
					e6 = (n - b6) / a6
					print "\ng6 = " + str(g6) + " e6 = " + str(e6)
					for k in range(g6 + 1,e6,1):
						check_eq(a6,b6,k)
					print "----------------------------------------"
			elif (int(str(n)[-3]) % 2 == 0): 
				if ((n+1) % 3 == 0):
					print "----------------------------------------"
					a1 = 600
					b1 = 492
					g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
					e1 = (n - b1) / a1
					print "\ng1 = " + str(g1) + " e1 = " + str(e1)
					for k in range(g1 + 1,e1,1):
						check_eq(a1,b1,k)
	
					print "----------------------------------------"
					a2 = 600
					b2 = 108
					g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
					e2 = (n - b2) / a2
					print "\ng2 = " + str(g2) + " e2 = " + str(e2)
					for k in range(g2 + 1,e2,1):
						check_eq(a2,b2,k)
	
					print "----------------------------------------"
					a3 = 120
					b3 = 60
					g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
					e3 = (n - b3) / a3
					print "\ng3 = " + str(g3) + " e3 = " + str(e3)
					for k in range(g3 + 1,e3,1):
						check_eq(a3,b3,k)
					print "----------------------------------------"
				else:
					print "----------------------------------------"
					a1 = 600
					b1 = 92
					g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
					e1 = (n - b1) / a1
					print "\ng1 = " + str(g1) + " e1 = " + str(e1)
					for k in range(g1 + 1,e1,1):
						check_eq(a1,b1,k)
	
					print "----------------------------------------"
					a2 = 600
					b2 = 292
					g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
					e2 = (n - b2) / a2
					print "\ng2 = " + str(g2) + " e2 = " + str(e2)
					for k in range(g2 + 1,e2,1):
						check_eq(a2,b2,k)
	
					print "----------------------------------------"
					a3 = 600
					b3 = 308
					g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
					e3 = (n - b3) / a3
					print "\ng3 = " + str(g3) + " e3 = " + str(e3)
					for k in range(g3 + 1,e3,1):
						check_eq(a3,b3,k)
					print "----------------------------------------"
					
					print "----------------------------------------"
					a4 = 600
					b4 = 508
					g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
					e4 = (n - b4) / a4
					print "\ng4 = " + str(g4) + " e4 = " + str(e4)
					for k in range(g4 + 1,e4,1):
						check_eq(a4,b4,k)
	
					print "----------------------------------------"
					a5 = 120
					b5 = 20
					g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
					e5 = (n - b5) / a5
					print "\ng5 = " + str(g5) + " e5 = " + str(e5)
					for k in range(g5 + 1,e5,1):
						check_eq(a5,b5,k)
	
					print "----------------------------------------"
					a6 = 120
					b6 = 100
					g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
					e6 = (n - b6) / a6
					print "\ng6 = " + str(g6) + " e6 = " + str(e6)
					for k in range(g6 + 1,e6,1):
						check_eq(a6,b6,k)
					print "----------------------------------------"
			else:
				print "error"

####################################################################################################


	if (n % 10 == 9):
		if (n % 100 == 9):
			if ((n+1) % 3 == 0):
				print "----------------------------------------"
				a1 = 300
				b1 = 6
				g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
				e1 = (n - b1) / a1
				print "\ng1 = " + str(g1) + " e1 = " + str(e1)
				for k in range(g1 + 1,e1,1):
					check_eq(a1,b1,k)

				print "----------------------------------------"
				a2 = 300
				b2 = 294
				g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
				e2 = (n - b2) / a2
				print "\ng2 = " + str(g2) + " e2 = " + str(e2)
				for k in range(g2 + 1,e2,1):
					check_eq(a2,b2,k)

				print "----------------------------------------"
				a3 = 60
				b3 = 30
				g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
				e3 = (n - b3) / a3
				print "\ng3 = " + str(g3) + " e3 = " + str(e3)
				for k in range(g3 + 1,e3,1):
					check_eq(a3,b3,k)
				print "----------------------------------------"
			else:
				print "----------------------------------------"
				a1 = 300
				b1 = 106
				g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
				e1 = (n - b1) / a1
				print "\ng1 = " + str(g1) + " e1 = " + str(e1)
				for k in range(g1 + 1,e1,1):
					check_eq(a1,b1,k)

				print "----------------------------------------"
				a2 = 300
				b2 = 206
				g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
				e2 = (n - b2) / a2
				print "\ng2 = " + str(g2) + " e2 = " + str(e2)
				for k in range(g2 + 1,e2,1):
					check_eq(a2,b2,k)

				print "----------------------------------------"
				a3 = 300
				b3 = 94
				g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
				e3 = (n - b3) / a3
				print "\ng3 = " + str(g3) + " e3 = " + str(e3)
				for k in range(g3 + 1,e3,1):
					check_eq(a3,b3,k)
				
				print "----------------------------------------"
				a4 = 300
				b4 = 194
				g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
				e4 = (n - b4) / a4
				print "\ng4 = " + str(g4) + " e4 = " + str(e4)
				for k in range(g4 + 1,e4,1):
					check_eq(a4,b4,k)

				print "----------------------------------------"
				a5 = 60
				b5 = 10
				g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
				e5 = (n - b5) / a5
				print "\ng5 = " + str(g5) + " e5 = " + str(e5)
				for k in range(g5 + 1,e5,1):
					check_eq(a5,b5,k)

				print "----------------------------------------"
				a6 = 60
				b6 = 50
				g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
				e6 = (n - b6) / a6
				print "\ng6 = " + str(g6) + " e6 = " + str(e6)
				for k in range(g6 + 1,e6,1):
					check_eq(a6,b6,k)
				print "----------------------------------------"


		if (n % 100 == 29):
			if ((n+1) % 3 == 0):
				print "----------------------------------------"
				a1 = 300
				b1 = 246
				g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
				e1 = (n - b1) / a1
				print "\ng1 = " + str(g1) + " e1 = " + str(e1)
				for k in range(g1 + 1,e1,1):
					check_eq(a1,b1,k)

				print "----------------------------------------"
				a2 = 300
				b2 = 54
				g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
				e2 = (n - b2) / a2
				print "\ng2 = " + str(g2) + " e2 = " + str(e2)
				for k in range(g2 + 1,e2,1):
					check_eq(a2,b2,k)

				print "----------------------------------------"
				a3 = 60
				b3 = 30
				g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
				e3 = (n - b3) / a3
				print "\ng3 = " + str(g3) + " e3 = " + str(e3)
				for k in range(g3 + 1,e3,1):
					check_eq(a3,b3,k)
				print "----------------------------------------"
			else:
				print "----------------------------------------"
				a1 = 300
				b1 = 46
				g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
				e1 = (n - b1) / a1
				print "\ng1 = " + str(g1) + " e1 = " + str(e1)
				for k in range(g1 + 1,e1,1):
					check_eq(a1,b1,k)

				print "----------------------------------------"
				a2 = 300
				b2 = 146
				g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
				e2 = (n - b2) / a2
				print "\ng2 = " + str(g2) + " e2 = " + str(e2)
				for k in range(g2 + 1,e2,1):
					check_eq(a2,b2,k)

				print "----------------------------------------"
				a3 = 300
				b3 = 154
				g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
				e3 = (n - b3) / a3
				print "\ng3 = " + str(g3) + " e3 = " + str(e3)
				for k in range(g3 + 1,e3,1):
					check_eq(a3,b3,k)
				print "----------------------------------------"
				
				print "----------------------------------------"
				a4 = 300
				b4 = 254
				g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
				e4 = (n - b4) / a4
				print "\ng4 = " + str(g4) + " e4 = " + str(e4)
				for k in range(g4 + 1,e4,1):
					check_eq(a4,b4,k)

				print "----------------------------------------"
				a5 = 60
				b5 = 10
				g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
				e5 = (n - b5) / a5
				print "\ng5 = " + str(g5) + " e5 = " + str(e5)
				for k in range(g5 + 1,e5,1):
					check_eq(a5,b5,k)

				print "----------------------------------------"
				a6 = 60
				b6 = 50
				g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
				e6 = (n - b6) / a6
				print "\ng6 = " + str(g6) + " e6 = " + str(e6)
				for k in range(g6 + 1,e6,1):
					check_eq(a6,b6,k)
				print "----------------------------------------"
		if (n % 100 == 49):
			if ((n+1) % 3 == 0):
				print "----------------------------------------"
				a1 = 300
				b1 = 186
				g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
				e1 = (n - b1) / a1
				print "\ng1 = " + str(g1) + " e1 = " + str(e1)
				for k in range(g1 + 1,e1,1):
					check_eq(a1,b1,k)

				print "----------------------------------------"
				a2 = 300
				b2 = 114
				g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
				e2 = (n - b2) / a2
				print "\ng2 = " + str(g2) + " e2 = " + str(e2)
				for k in range(g2 + 1,e2,1):
					check_eq(a2,b2,k)

				print "----------------------------------------"
				a3 = 60
				b3 = 30
				g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
				e3 = (n - b3) / a3
				print "\ng3 = " + str(g3) + " e3 = " + str(e3)
				for k in range(g3 + 1,e3,1):
					check_eq(a3,b3,k)
				print "----------------------------------------"
			else:
				print "----------------------------------------"
				a1 = 300
				b1 = 86
				g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
				e1 = (n - b1) / a1
				print "\ng1 = " + str(g1) + " e1 = " + str(e1)
				for k in range(g1 + 1,e1,1):
					check_eq(a1,b1,k)

				print "----------------------------------------"
				a2 = 300
				b2 = 286
				g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
				e2 = (n - b2) / a2
				print "\ng2 = " + str(g2) + " e2 = " + str(e2)
				for k in range(g2 + 1,e2,1):
					check_eq(a2,b2,k)

				print "----------------------------------------"
				a3 = 300
				b3 = 14
				g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
				e3 = (n - b3) / a3
				print "\ng3 = " + str(g3) + " e3 = " + str(e3)
				for k in range(g3 + 1,e3,1):
					check_eq(a3,b3,k)
				print "----------------------------------------"
				
				print "----------------------------------------"
				a4 = 300
				b4 = 214
				g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
				e4 = (n - b4) / a4
				print "\ng4 = " + str(g4) + " e4 = " + str(e4)
				for k in range(g4 + 1,e4,1):
					check_eq(a4,b4,k)

				print "----------------------------------------"
				a5 = 60
				b5 = 10
				g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
				e5 = (n - b5) / a5
				print "\ng5 = " + str(g5) + " e5 = " + str(e5)
				for k in range(g5 + 1,e5,1):
					check_eq(a5,b5,k)

				print "----------------------------------------"
				a6 = 60
				b6 = 50
				g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
				e6 = (n - b6) / a6
				print "\ng6 = " + str(g6) + " e6 = " + str(e6)
				for k in range(g6 + 1,e6,1):
					check_eq(a6,b6,k)
				print "----------------------------------------"
			
		if (n % 100 == 69):
			if ((n+1) % 3 == 0):
				print "----------------------------------------"
				a1 = 300
				b1 = 126
				g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
				e1 = (n - b1) / a1
				print "\ng1 = " + str(g1) + " e1 = " + str(e1)
				for k in range(g1 + 1,e1,1):
					check_eq(a1,b1,k)

				print "----------------------------------------"
				a2 = 300
				b2 = 174
				g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
				e2 = (n - b2) / a2
				print "\ng2 = " + str(g2) + " e2 = " + str(e2)
				for k in range(g2 + 1,e2,1):
					check_eq(a2,b2,k)

				print "----------------------------------------"
				a3 = 60
				b3 = 30
				g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
				e3 = (n - b3) / a3
				print "\ng3 = " + str(g3) + " e3 = " + str(e3)
				for k in range(g3 + 1,e3,1):
					check_eq(a3,b3,k)
				print "----------------------------------------"
			else:
				print "----------------------------------------"
				a1 = 300
				b1 = 26
				g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
				e1 = (n - b1) / a1
				print "\ng1 = " + str(g1) + " e1 = " + str(e1)
				for k in range(g1 + 1,e1,1):
					check_eq(a1,b1,k)

				print "----------------------------------------"
				a2 = 300
				b2 = 226
				g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
				e2 = (n - b2) / a2
				print "\ng2 = " + str(g2) + " e2 = " + str(e2)
				for k in range(g2 + 1,e2,1):
					check_eq(a2,b2,k)

				print "----------------------------------------"
				a3 = 300
				b3 = 74
				g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
				e3 = (n - b3) / a3
				print "\ng3 = " + str(g3) + " e3 = " + str(e3)
				for k in range(g3 + 1,e3,1):
					check_eq(a3,b3,k)
				print "----------------------------------------"
				
				print "----------------------------------------"
				a4 = 300
				b4 = 274
				g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
				e4 = (n - b4) / a4
				print "\ng4 = " + str(g4) + " e4 = " + str(e4)
				for k in range(g4 + 1,e4,1):
					check_eq(a4,b4,k)

				print "----------------------------------------"
				a5 = 60
				b5 = 10
				g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
				e5 = (n - b5) / a5
				print "\ng5 = " + str(g5) + " e5 = " + str(e5)
				for k in range(g5 + 1,e5,1):
					check_eq(a5,b5,k)

				print "----------------------------------------"
				a6 = 60
				b6 = 50
				g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
				e6 = (n - b6) / a6
				print "\ng6 = " + str(g6) + " e6 = " + str(e6)
				for k in range(g6 + 1,e6,1):
					check_eq(a6,b6,k)
				print "----------------------------------------"
				
		if (n % 100 == 89):
			if ((n+1) % 3 == 0):
				print "----------------------------------------"
				a1 = 300
				b1 = 66
				g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
				e1 = (n - b1) / a1
				print "\ng1 = " + str(g1) + " e1 = " + str(e1)
				for k in range(g1 + 1,e1,1):
					check_eq(a1,b1,k)

				print "----------------------------------------"
				a2 = 300
				b2 = 234
				g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
				e2 = (n - b2) / a2
				print "\ng2 = " + str(g2) + " e2 = " + str(e2)
				for k in range(g2 + 1,e2,1):
					check_eq(a2,b2,k)

				print "----------------------------------------"
				a3 = 60
				b3 = 30
				g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
				e3 = (n - b3) / a3
				print "\ng3 = " + str(g3) + " e3 = " + str(e3)
				for k in range(g3 + 1,e3,1):
					check_eq(a3,b3,k)
				print "----------------------------------------"
			else:
				print "----------------------------------------"
				a1 = 300
				b1 = 166
				g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
				e1 = (n - b1) / a1
				print "\ng1 = " + str(g1) + " e1 = " + str(e1)
				for k in range(g1 + 1,e1,1):
					check_eq(a1,b1,k)

				print "----------------------------------------"
				a2 = 300
				b2 = 266
				g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
				e2 = (n - b2) / a2
				print "\ng2 = " + str(g2) + " e2 = " + str(e2)
				for k in range(g2 + 1,e2,1):
					check_eq(a2,b2,k)

				print "----------------------------------------"
				a3 = 300
				b3 = 34
				g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
				e3 = (n - b3) / a3
				print "\ng3 = " + str(g3) + " e3 = " + str(e3)
				for k in range(g3 + 1,e3,1):
					check_eq(a3,b3,k)
				print "----------------------------------------"
				
				print "----------------------------------------"
				a4 = 300
				b4 = 134
				g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
				e4 = (n - b4) / a4
				print "\ng4 = " + str(g4) + " e4 = " + str(e4)
				for k in range(g4 + 1,e4,1):
					check_eq(a4,b4,k)

				print "----------------------------------------"
				a5 = 60
				b5 = 10
				g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
				e5 = (n - b5) / a5
				print "\ng5 = " + str(g5) + " e5 = " + str(e5)
				for k in range(g5 + 1,e5,1):
					check_eq(a5,b5,k)

				print "----------------------------------------"
				a6 = 60
				b6 = 50
				g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
				e6 = (n - b6) / a6
				print "\ng6 = " + str(g6) + " e6 = " + str(e6)
				for k in range(g6 + 1,e6,1):
					check_eq(a6,b6,k)
				print "----------------------------------------"

		if (n % 100 == 19):
			if (int(str(n)[-3]) % 2 != 0):
				if ((n+1) % 3 == 0):
					print "----------------------------------------"
					a1 = 600
					b1 = 576
					g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
					e1 = (n - b1) / a1
					print "\ng1 = " + str(g1) + " e1 = " + str(e1)
					for k in range(g1 + 1,e1,1):
						check_eq(a1,b1,k)
	
					print "----------------------------------------"
					a2 = 600
					b2 = 24
					g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
					e2 = (n - b2) / a2
					print "\ng2 = " + str(g2) + " e2 = " + str(e2)
					for k in range(g2 + 1,e2,1):
						check_eq(a2,b2,k)
	
					print "----------------------------------------"
					a3 = 120
					b3 = 0
					g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
					e3 = (n - b3) / a3
					print "\ng3 = " + str(g3) + " e3 = " + str(e3)
					for k in range(g3 + 1,e3,1):
						check_eq(a3,b3,k)
					print "----------------------------------------"
				else:
					print "----------------------------------------"
					a1 = 600
					b1 = 176
					g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
					e1 = (n - b1) / a1
					print "\ng1 = " + str(g1) + " e1 = " + str(e1)
					for k in range(g1 + 1,e1,1):
						check_eq(a1,b1,k)
	
					print "----------------------------------------"
					a2 = 600
					b2 = 376
					g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
					e2 = (n - b2) / a2
					print "\ng2 = " + str(g2) + " e2 = " + str(e2)
					for k in range(g2 + 1,e2,1):
						check_eq(a2,b2,k)
	
					print "----------------------------------------"
					a3 = 600
					b3 = 224
					g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
					e3 = (n - b3) / a3
					print "\ng3 = " + str(g3) + " e3 = " + str(e3)
					for k in range(g3 + 1,e3,1):
						check_eq(a3,b3,k)
					print "----------------------------------------"
					
					print "----------------------------------------"
					a4 = 600
					b4 = 424
					g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
					e4 = (n - b4) / a4
					print "\ng4 = " + str(g4) + " e4 = " + str(e4)
					for k in range(g4 + 1,e4,1):
						check_eq(a4,b4,k)
	
					print "----------------------------------------"
					a5 = 120
					b5 = 40
					g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
					e5 = (n - b5) / a5
					print "\ng5 = " + str(g5) + " e5 = " + str(e5)
					for k in range(g5 + 1,e5,1):
						check_eq(a5,b5,k)
	
					print "----------------------------------------"
					a6 = 120
					b6 = 80
					g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
					e6 = (n - b6) / a6
					print "\ng6 = " + str(g6) + " e6 = " + str(e6)
					for k in range(g6 + 1,e6,1):
						check_eq(a6,b6,k)
					print "----------------------------------------"
			elif (int(str(n)[-3]) % 2 == 0): 
				if ((n+1) % 3 == 0):
					print "----------------------------------------"
					a1 = 600
					b1 = 276
					g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
					e1 = (n - b1) / a1
					print "\ng1 = " + str(g1) + " e1 = " + str(e1)
					for k in range(g1 + 1,e1,1):
						check_eq(a1,b1,k)
	
					print "----------------------------------------"
					a2 = 600
					b2 = 324
					g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
					e2 = (n - b2) / a2
					print "\ng2 = " + str(g2) + " e2 = " + str(e2)
					for k in range(g2 + 1,e2,1):
						check_eq(a2,b2,k)
	
					print "----------------------------------------"
					a3 = 120
					b3 = 60
					g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
					e3 = (n - b3) / a3
					print "\ng3 = " + str(g3) + " e3 = " + str(e3)
					for k in range(g3 + 1,e3,1):
						check_eq(a3,b3,k)
					print "----------------------------------------"
				else:
					print "----------------------------------------"
					a1 = 600
					b1 = 76
					g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
					e1 = (n - b1) / a1
					print "\ng1 = " + str(g1) + " e1 = " + str(e1)
					for k in range(g1 + 1,e1,1):
						check_eq(a1,b1,k)
	
					print "----------------------------------------"
					a2 = 600
					b2 = 476
					g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
					e2 = (n - b2) / a2
					print "\ng2 = " + str(g2) + " e2 = " + str(e2)
					for k in range(g2 + 1,e2,1):
						check_eq(a2,b2,k)
	
					print "----------------------------------------"
					a3 = 600
					b3 = 124
					g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
					e3 = (n - b3) / a3
					print "\ng3 = " + str(g3) + " e3 = " + str(e3)
					for k in range(g3 + 1,e3,1):
						check_eq(a3,b3,k)
					print "----------------------------------------"
					
					print "----------------------------------------"
					a4 = 600
					b4 = 524
					g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
					e4 = (n - b4) / a4
					print "\ng4 = " + str(g4) + " e4 = " + str(e4)
					for k in range(g4 + 1,e4,1):
						check_eq(a4,b4,k)
	
					print "----------------------------------------"
					a5 = 120
					b5 = 20
					g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
					e5 = (n - b5) / a5
					print "\ng5 = " + str(g5) + " e5 = " + str(e5)
					for k in range(g5 + 1,e5,1):
						check_eq(a5,b5,k)
	
					print "----------------------------------------"
					a6 = 120
					b6 = 100
					g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
					e6 = (n - b6) / a6
					print "\ng6 = " + str(g6) + " e6 = " + str(e6)
					for k in range(g6 + 1,e6,1):
						check_eq(a6,b6,k)
					print "----------------------------------------"
			else:
				print "error"
		if (n % 100 == 39):
			if (int(str(n)[-3]) % 2 != 0):
				if ((n+1) % 3 == 0):
					print "----------------------------------------"
					a1 = 600
					b1 = 516
					g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
					e1 = (n - b1) / a1
					print "\ng1 = " + str(g1) + " e1 = " + str(e1)
					for k in range(g1 + 1,e1,1):
						check_eq(a1,b1,k)
	
					print "----------------------------------------"
					a2 = 600
					b2 = 84
					g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
					e2 = (n - b2) / a2
					print "\ng2 = " + str(g2) + " e2 = " + str(e2)
					for k in range(g2 + 1,e2,1):
						check_eq(a2,b2,k)
	
					print "----------------------------------------"
					a3 = 120
					b3 = 60
					g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
					e3 = (n - b3) / a3
					print "\ng3 = " + str(g3) + " e3 = " + str(e3)
					for k in range(g3 + 1,e3,1):
						check_eq(a3,b3,k)
					print "----------------------------------------"
				else:
					print "----------------------------------------"
					a1 = 600
					b1 = 116
					g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
					e1 = (n - b1) / a1
					print "\ng1 = " + str(g1) + " e1 = " + str(e1)
					for k in range(g1 + 1,e1,1):
						check_eq(a1,b1,k)
	
					print "----------------------------------------"
					a2 = 600
					b2 = 316
					g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
					e2 = (n - b2) / a2
					print "\ng2 = " + str(g2) + " e2 = " + str(e2)
					for k in range(g2 + 1,e2,1):
						check_eq(a2,b2,k)
	
					print "----------------------------------------"
					a3 = 600
					b3 = 284
					g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
					e3 = (n - b3) / a3
					print "\ng3 = " + str(g3) + " e3 = " + str(e3)
					for k in range(g3 + 1,e3,1):
						check_eq(a3,b3,k)
					print "----------------------------------------"
					
					print "----------------------------------------"
					a4 = 600
					b4 = 484
					g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
					e4 = (n - b4) / a4
					print "\ng4 = " + str(g4) + " e4 = " + str(e4)
					for k in range(g4 + 1,e4,1):
						check_eq(a4,b4,k)
	
					print "----------------------------------------"
					a5 = 120
					b5 = 20
					g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
					e5 = (n - b5) / a5
					print "\ng5 = " + str(g5) + " e5 = " + str(e5)
					for k in range(g5 + 1,e5,1):
						check_eq(a5,b5,k)
	
					print "----------------------------------------"
					a6 = 120
					b6 = 100
					g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
					e6 = (n - b6) / a6
					print "\ng6 = " + str(g6) + " e6 = " + str(e6)
					for k in range(g6 + 1,e6,1):
						check_eq(a6,b6,k)
					print "----------------------------------------"
			elif (int(str(n)[-3]) % 2 == 0): 
				if ((n+1) % 3 == 0):
					print "----------------------------------------"
					a1 = 600
					b1 = 216
					g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
					e1 = (n - b1) / a1
					print "\ng1 = " + str(g1) + " e1 = " + str(e1)
					for k in range(g1 + 1,e1,1):
						check_eq(a1,b1,k)
	
					print "----------------------------------------"
					a2 = 600
					b2 = 384
					g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
					e2 = (n - b2) / a2
					print "\ng2 = " + str(g2) + " e2 = " + str(e2)
					for k in range(g2 + 1,e2,1):
						check_eq(a2,b2,k)
	
					print "----------------------------------------"
					a3 = 120
					b3 = 0
					g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
					e3 = (n - b3) / a3
					print "\ng3 = " + str(g3) + " e3 = " + str(e3)
					for k in range(g3 + 1,e3,1):
						check_eq(a3,b3,k)
					print "----------------------------------------"
				else:
					print "----------------------------------------"
					a1 = 600
					b1 = 16
					g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
					e1 = (n - b1) / a1
					print "\ng1 = " + str(g1) + " e1 = " + str(e1)
					for k in range(g1 + 1,e1,1):
						check_eq(a1,b1,k)
	
					print "----------------------------------------"
					a2 = 600
					b2 = 416
					g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
					e2 = (n - b2) / a2
					print "\ng2 = " + str(g2) + " e2 = " + str(e2)
					for k in range(g2 + 1,e2,1):
						check_eq(a2,b2,k)
	
					print "----------------------------------------"
					a3 = 600
					b3 = 84
					g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
					e3 = (n - b3) / a3
					print "\ng3 = " + str(g3) + " e3 = " + str(e3)
					for k in range(g3 + 1,e3,1):
						check_eq(a3,b3,k)
					print "----------------------------------------"
					
					print "----------------------------------------"
					a4 = 600
					b4 = 584
					g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
					e4 = (n - b4) / a4
					print "\ng4 = " + str(g4) + " e4 = " + str(e4)
					for k in range(g4 + 1,e4,1):
						check_eq(a4,b4,k)
	
					print "----------------------------------------"
					a5 = 120
					b5 = 40
					g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
					e5 = (n - b5) / a5
					print "\ng5 = " + str(g5) + " e5 = " + str(e5)
					for k in range(g5 + 1,e5,1):
						check_eq(a5,b5,k)
	
					print "----------------------------------------"
					a6 = 120
					b6 = 80
					g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
					e6 = (n - b6) / a6
					print "\ng6 = " + str(g6) + " e6 = " + str(e6)
					for k in range(g6 + 1,e6,1):
						check_eq(a6,b6,k)
					print "----------------------------------------"
			else:
				print "error"
		if (n % 100 == 59):
			if (int(str(n)[-3]) % 2 != 0):
				if ((n+1) % 3 == 0):
					print "----------------------------------------"
					a1 = 600
					b1 = 456
					g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
					e1 = (n - b1) / a1
					print "\ng1 = " + str(g1) + " e1 = " + str(e1)
					for k in range(g1 + 1,e1,1):
						check_eq(a1,b1,k)
	
					print "----------------------------------------"
					a2 = 600
					b2 = 144
					g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
					e2 = (n - b2) / a2
					print "\ng2 = " + str(g2) + " e2 = " + str(e2)
					for k in range(g2 + 1,e2,1):
						check_eq(a2,b2,k)
	
					print "----------------------------------------"
					a3 = 120
					b3 = 0
					g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
					e3 = (n - b3) / a3
					print "\ng3 = " + str(g3) + " e3 = " + str(e3)
					for k in range(g3 + 1,e3,1):
						check_eq(a3,b3,k)
					print "----------------------------------------"
				else:
					print "----------------------------------------"
					a1 = 600
					b1 = 56
					g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
					e1 = (n - b1) / a1
					print "\ng1 = " + str(g1) + " e1 = " + str(e1)
					for k in range(g1 + 1,e1,1):
						check_eq(a1,b1,k)
	
					print "----------------------------------------"
					a2 = 600
					b2 = 256
					g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
					e2 = (n - b2) / a2
					print "\ng2 = " + str(g2) + " e2 = " + str(e2)
					for k in range(g2 + 1,e2,1):
						check_eq(a2,b2,k)
	
					print "----------------------------------------"
					a3 = 600
					b3 = 344
					g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
					e3 = (n - b3) / a3
					print "\ng3 = " + str(g3) + " e3 = " + str(e3)
					for k in range(g3 + 1,e3,1):
						check_eq(a3,b3,k)
					print "----------------------------------------"
					
					print "----------------------------------------"
					a4 = 600
					b4 = 544
					g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
					e4 = (n - b4) / a4
					print "\ng4 = " + str(g4) + " e4 = " + str(e4)
					for k in range(g4 + 1,e4,1):
						check_eq(a4,b4,k)
	
					print "----------------------------------------"
					a5 = 120
					b5 = 40
					g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
					e5 = (n - b5) / a5
					print "\ng5 = " + str(g5) + " e5 = " + str(e5)
					for k in range(g5 + 1,e5,1):
						check_eq(a5,b5,k)
	
					print "----------------------------------------"
					a6 = 120
					b6 = 80
					g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
					e6 = (n - b6) / a6
					print "\ng6 = " + str(g6) + " e6 = " + str(e6)
					for k in range(g6 + 1,e6,1):
						check_eq(a6,b6,k)
					print "----------------------------------------"
			elif (int(str(n)[-3]) % 2 == 0): 
				if ((n+1) % 3 == 0):
					print "----------------------------------------"
					a1 = 600
					b1 = 156
					g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
					e1 = (n - b1) / a1
					print "\ng1 = " + str(g1) + " e1 = " + str(e1)
					for k in range(g1 + 1,e1,1):
						check_eq(a1,b1,k)
	
					print "----------------------------------------"
					a2 = 600
					b2 = 444
					g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
					e2 = (n - b2) / a2
					print "\ng2 = " + str(g2) + " e2 = " + str(e2)
					for k in range(g2 + 1,e2,1):
						check_eq(a2,b2,k)
	
					print "----------------------------------------"
					a3 = 120
					b3 = 60
					g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
					e3 = (n - b3) / a3
					print "\ng3 = " + str(g3) + " e3 = " + str(e3)
					for k in range(g3 + 1,e3,1):
						check_eq(a3,b3,k)
					print "----------------------------------------"
				else:
					print "----------------------------------------"
					a1 = 600
					b1 = 356
					g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
					e1 = (n - b1) / a1
					print "\ng1 = " + str(g1) + " e1 = " + str(e1)
					for k in range(g1 + 1,e1,1):
						check_eq(a1,b1,k)
	
					print "----------------------------------------"
					a2 = 600
					b2 = 556
					g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
					e2 = (n - b2) / a2
					print "\ng2 = " + str(g2) + " e2 = " + str(e2)
					for k in range(g2 + 1,e2,1):
						check_eq(a2,b2,k)
	
					print "----------------------------------------"
					a3 = 600
					b3 = 44
					g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
					e3 = (n - b3) / a3
					print "\ng3 = " + str(g3) + " e3 = " + str(e3)
					for k in range(g3 + 1,e3,1):
						check_eq(a3,b3,k)
					print "----------------------------------------"
					
					print "----------------------------------------"
					a4 = 600
					b4 = 244
					g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
					e4 = (n - b4) / a4
					print "\ng4 = " + str(g4) + " e4 = " + str(e4)
					for k in range(g4 + 1,e4,1):
						check_eq(a4,b4,k)
	
					print "----------------------------------------"
					a5 = 120
					b5 = 20
					g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
					e5 = (n - b5) / a5
					print "\ng5 = " + str(g5) + " e5 = " + str(e5)
					for k in range(g5 + 1,e5,1):
						check_eq(a5,b5,k)
	
					print "----------------------------------------"
					a6 = 120
					b6 = 100
					g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
					e6 = (n - b6) / a6
					print "\ng6 = " + str(g6) + " e6 = " + str(e6)
					for k in range(g6 + 1,e6,1):
						check_eq(a6,b6,k)
					print "----------------------------------------"
			else:
				print "error"
		if (n % 100 == 79):
			if (int(str(n)[-3]) % 2 != 0):
				if ((n+1) % 3 == 0):
					print "----------------------------------------"
					a1 = 600
					b1 = 396
					g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
					e1 = (n - b1) / a1
					print "\ng1 = " + str(g1) + " e1 = " + str(e1)
					for k in range(g1 + 1,e1,1):
						check_eq(a1,b1,k)
	
					print "----------------------------------------"
					a2 = 600
					b2 = 204
					g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
					e2 = (n - b2) / a2
					print "\ng2 = " + str(g2) + " e2 = " + str(e2)
					for k in range(g2 + 1,e2,1):
						check_eq(a2,b2,k)
	
					print "----------------------------------------"
					a3 = 120
					b3 = 60
					g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
					e3 = (n - b3) / a3
					print "\ng3 = " + str(g3) + " e3 = " + str(e3)
					for k in range(g3 + 1,e3,1):
						check_eq(a3,b3,k)
					print "----------------------------------------"
				else:
					print "----------------------------------------"
					a1 = 600
					b1 = 196
					g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
					e1 = (n - b1) / a1
					print "\ng1 = " + str(g1) + " e1 = " + str(e1)
					for k in range(g1 + 1,e1,1):
						check_eq(a1,b1,k)
	
					print "----------------------------------------"
					a2 = 600
					b2 = 596
					g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
					e2 = (n - b2) / a2
					print "\ng2 = " + str(g2) + " e2 = " + str(e2)
					for k in range(g2 + 1,e2,1):
						check_eq(a2,b2,k)
	
					print "----------------------------------------"
					a3 = 600
					b3 = 4
					g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
					e3 = (n - b3) / a3
					print "\ng3 = " + str(g3) + " e3 = " + str(e3)
					for k in range(g3 + 1,e3,1):
						check_eq(a3,b3,k)
					print "----------------------------------------"
					
					print "----------------------------------------"
					a4 = 600
					b4 = 404
					g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
					e4 = (n - b4) / a4
					print "\ng4 = " + str(g4) + " e4 = " + str(e4)
					for k in range(g4 + 1,e4,1):
						check_eq(a4,b4,k)
	
					print "----------------------------------------"
					a5 = 120
					b5 = 20
					g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
					e5 = (n - b5) / a5
					print "\ng5 = " + str(g5) + " e5 = " + str(e5)
					for k in range(g5 + 1,e5,1):
						check_eq(a5,b5,k)
	
					print "----------------------------------------"
					a6 = 120
					b6 = 100
					g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
					e6 = (n - b6) / a6
					print "\ng6 = " + str(g6) + " e6 = " + str(e6)
					for k in range(g6 + 1,e6,1):
						check_eq(a6,b6,k)
					print "----------------------------------------"
			elif (int(str(n)[-3]) % 2 == 0): 
				if ((n+1) % 3 == 0):
					print "----------------------------------------"
					a1 = 600
					b1 = 96
					g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
					e1 = (n - b1) / a1
					print "\ng1 = " + str(g1) + " e1 = " + str(e1)
					for k in range(g1 + 1,e1,1):
						check_eq(a1,b1,k)
	
					print "----------------------------------------"
					a2 = 600
					b2 = 504
					g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
					e2 = (n - b2) / a2
					print "\ng2 = " + str(g2) + " e2 = " + str(e2)
					for k in range(g2 + 1,e2,1):
						check_eq(a2,b2,k)
	
					print "----------------------------------------"
					a3 = 120
					b3 = 0
					g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
					e3 = (n - b3) / a3
					print "\ng3 = " + str(g3) + " e3 = " + str(e3)
					for k in range(g3 + 1,e3,1):
						check_eq(a3,b3,k)
					print "----------------------------------------"
				else:
					print "----------------------------------------"
					a1 = 600
					b1 = 296
					g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
					e1 = (n - b1) / a1
					print "\ng1 = " + str(g1) + " e1 = " + str(e1)
					for k in range(g1 + 1,e1,1):
						check_eq(a1,b1,k)
	
					print "----------------------------------------"
					a2 = 600
					b2 = 496
					g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
					e2 = (n - b2) / a2
					print "\ng2 = " + str(g2) + " e2 = " + str(e2)
					for k in range(g2 + 1,e2,1):
						check_eq(a2,b2,k)
	
					print "----------------------------------------"
					a3 = 600
					b3 = 104
					g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
					e3 = (n - b3) / a3
					print "\ng3 = " + str(g3) + " e3 = " + str(e3)
					for k in range(g3 + 1,e3,1):
						check_eq(a3,b3,k)
					print "----------------------------------------"
					
					print "----------------------------------------"
					a4 = 600
					b4 = 304
					g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
					e4 = (n - b4) / a4
					print "\ng4 = " + str(g4) + " e4 = " + str(e4)
					for k in range(g4 + 1,e4,1):
						check_eq(a4,b4,k)
	
					print "----------------------------------------"
					a5 = 120
					b5 = 40
					g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
					e5 = (n - b5) / a5
					print "\ng5 = " + str(g5) + " e5 = " + str(e5)
					for k in range(g5 + 1,e5,1):
						check_eq(a5,b5,k)
	
					print "----------------------------------------"
					a6 = 120
					b6 = 80
					g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
					e6 = (n - b6) / a6
					print "\ng6 = " + str(g6) + " e6 = " + str(e6)
					for k in range(g6 + 1,e6,1):
						check_eq(a6,b6,k)
					print "----------------------------------------"
			else:
				print "error"
		if (n % 100 == 99):
			if (int(str(n)[-3]) % 2 != 0):
				if ((n+1) % 3 == 0):
					print "----------------------------------------"
					a1 = 600
					b1 = 336
					g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
					e1 = (n - b1) / a1
					print "\ng1 = " + str(g1) + " e1 = " + str(e1)
					for k in range(g1 + 1,e1,1):
						check_eq(a1,b1,k)
	
					print "----------------------------------------"
					a2 = 600
					b2 = 264
					g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
					e2 = (n - b2) / a2
					print "\ng2 = " + str(g2) + " e2 = " + str(e2)
					for k in range(g2 + 1,e2,1):
						check_eq(a2,b2,k)
	
					print "----------------------------------------"
					a3 = 120
					b3 = 0
					g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
					e3 = (n - b3) / a3
					print "\ng3 = " + str(g3) + " e3 = " + str(e3)
					for k in range(g3 + 1,e3,1):
						check_eq(a3,b3,k)
					print "----------------------------------------"
				else:
					print "----------------------------------------"
					a1 = 600
					b1 = 136
					g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
					e1 = (n - b1) / a1
					print "\ng1 = " + str(g1) + " e1 = " + str(e1)
					for k in range(g1 + 1,e1,1):
						check_eq(a1,b1,k)
	
					print "----------------------------------------"
					a2 = 600
					b2 = 536
					g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
					e2 = (n - b2) / a2
					print "\ng2 = " + str(g2) + " e2 = " + str(e2)
					for k in range(g2 + 1,e2,1):
						check_eq(a2,b2,k)
	
					print "----------------------------------------"
					a3 = 600
					b3 = 64
					g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
					e3 = (n - b3) / a3
					print "\ng3 = " + str(g3) + " e3 = " + str(e3)
					for k in range(g3 + 1,e3,1):
						check_eq(a3,b3,k)
					print "----------------------------------------"
					
					print "----------------------------------------"
					a4 = 600
					b4 = 464
					g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
					e4 = (n - b4) / a4
					print "\ng4 = " + str(g4) + " e4 = " + str(e4)
					for k in range(g4 + 1,e4,1):
						check_eq(a4,b4,k)
	
					print "----------------------------------------"
					a5 = 120
					b5 = 40
					g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
					e5 = (n - b5) / a5
					print "\ng5 = " + str(g5) + " e5 = " + str(e5)
					for k in range(g5 + 1,e5,1):
						check_eq(a5,b5,k)
	
					print "----------------------------------------"
					a6 = 120
					b6 = 80
					g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
					e6 = (n - b6) / a6
					print "\ng6 = " + str(g6) + " e6 = " + str(e6)
					for k in range(g6 + 1,e6,1):
						check_eq(a6,b6,k)
					print "----------------------------------------"
			elif (int(str(n)[-3]) % 2 == 0): 
				if ((n+1) % 3 == 0):
					print "----------------------------------------"
					a1 = 600
					b1 = 36
					g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
					e1 = (n - b1) / a1
					print "\ng1 = " + str(g1) + " e1 = " + str(e1)
					for k in range(g1 + 1,e1,1):
						check_eq(a1,b1,k)
	
					print "----------------------------------------"
					a2 = 600
					b2 = 564
					g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
					e2 = (n - b2) / a2
					print "\ng2 = " + str(g2) + " e2 = " + str(e2)
					for k in range(g2 + 1,e2,1):
						check_eq(a2,b2,k)
	
					print "----------------------------------------"
					a3 = 120
					b3 = 60
					g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
					e3 = (n - b3) / a3
					print "\ng3 = " + str(g3) + " e3 = " + str(e3)
					for k in range(g3 + 1,e3,1):
						check_eq(a3,b3,k)
					print "----------------------------------------"
				else:
					print "----------------------------------------"
					a1 = 600
					b1 = 364
					g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
					e1 = (n - b1) / a1
					print "\ng1 = " + str(g1) + " e1 = " + str(e1)
					for k in range(g1 + 1,e1,1):
						check_eq(a1,b1,k)
	
					print "----------------------------------------"
					a2 = 600
					b2 = 236
					g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
					e2 = (n - b2) / a2
					print "\ng2 = " + str(g2) + " e2 = " + str(e2)
					for k in range(g2 + 1,e2,1):
						check_eq(a2,b2,k)
	
					print "----------------------------------------"
					a3 = 600
					b3 = 436
					g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
					e3 = (n - b3) / a3
					print "\ng3 = " + str(g3) + " e3 = " + str(e3)
					for k in range(g3 + 1,e3,1):
						check_eq(a3,b3,k)
					print "----------------------------------------"
					
					print "----------------------------------------"
					a4 = 600
					b4 = 164
					g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
					e4 = (n - b4) / a4
					print "\ng4 = " + str(g4) + " e4 = " + str(e4)
					for k in range(g4 + 1,e4,1):
						check_eq(a4,b4,k)
	
					print "----------------------------------------"
					a5 = 120
					b5 = 20
					g5 = (int(math.ceil(2 * math.sqrt(n))) - b5)/a5
					e5 = (n - b5) / a5
					print "\ng5 = " + str(g5) + " e5 = " + str(e5)
					for k in range(g5 + 1,e5,1):
						check_eq(a5,b5,k)
	
					print "----------------------------------------"
					a6 = 120
					b6 = 100
					g6 = (int(math.ceil(2 * math.sqrt(n))) - b6)/a6
					e6 = (n - b6) / a6
					print "\ng6 = " + str(g6) + " e6 = " + str(e6)
					for k in range(g6 + 1,e6,1):
						check_eq(a6,b6,k)
					print "----------------------------------------"
			else:
				print "error"

#####################################################################################################

	if (n % 10 == 3):
		if (int(str(n)[-2]) % 2 != 0):
			if ((n+1) % 3 == 0):
				print "----------------------------------------"
				a1 = 60
				b1 = 54
				g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
				e1 = (n - b1) / a1
				print "\ng1 = " + str(g1) + " e1 = " + str(e1)
				for k in range(g1 + 1,e1,1):
					check_eq(a1,b1,k)
	
				print "----------------------------------------"
				a2 = 60
				b2 = 6
				g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
				e2 = (n - b2) / a2
				print "\ng2 = " + str(g2) + " e2 = " + str(e2)
				for k in range(g2 + 1,e2,1):
					check_eq(a2,b2,k)
	
				print "----------------------------------------"
			else:
				print "----------------------------------------"
				a1 = 60
				b1 = 14
				g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
				e1 = (n - b1) / a1
				print "\ng1 = " + str(g1) + " e1 = " + str(e1)
				for k in range(g1 + 1,e1,1):
					check_eq(a1,b1,k)
	
				print "----------------------------------------"
				a2 = 60
				b2 = 34
				g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
				e2 = (n - b2) / a2
				print "\ng2 = " + str(g2) + " e2 = " + str(e2)
				for k in range(g2 + 1,e2,1):
					check_eq(a2,b2,k)
	
				print "----------------------------------------"
				a3 = 60
				b3 = 26
				g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
				e3 = (n - b3) / a3
				print "\ng3 = " + str(g3) + " e3 = " + str(e3)
				for k in range(g3 + 1,e3,1):
					check_eq(a3,b3,k)
				print "----------------------------------------"
				
				print "----------------------------------------"
				a4 = 60
				b4 = 46
				g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
				e4 = (n - b4) / a4
				print "\ng4 = " + str(g4) + " e4 = " + str(e4)
				for k in range(g4 + 1,e4,1):
					check_eq(a4,b4,k)
	
				print "----------------------------------------"
		elif (int(str(n)[-2]) % 2 == 0): 
			if ((n+1) % 3 == 0):
				print "----------------------------------------"
				a1 = 60
				b1 = 24
				g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
				e1 = (n - b1) / a1
				print "\ng1 = " + str(g1) + " e1 = " + str(e1)
				for k in range(g1 + 1,e1,1):
					check_eq(a1,b1,k)
	
				print "----------------------------------------"
				a2 = 60
				b2 = 36
				g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
				e2 = (n - b2) / a2
				print "\ng2 = " + str(g2) + " e2 = " + str(e2)
				for k in range(g2 + 1,e2,1):
					check_eq(a2,b2,k)
	
				print "----------------------------------------"
			else:
				print "----------------------------------------"
				a1 = 60
				b1 = 4
				g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
				e1 = (n - b1) / a1
				print "\ng1 = " + str(g1) + " e1 = " + str(e1)
				for k in range(g1 + 1,e1,1):
					check_eq(a1,b1,k)
	
				print "----------------------------------------"
				a2 = 60
				b2 = 44
				g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
				e2 = (n - b2) / a2
				print "\ng2 = " + str(g2) + " e2 = " + str(e2)
				for k in range(g2 + 1,e2,1):
					check_eq(a2,b2,k)
	
				print "----------------------------------------"
				a3 = 60
				b3 = 16
				g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
				e3 = (n - b3) / a3
				print "\ng3 = " + str(g3) + " e3 = " + str(e3)
				for k in range(g3 + 1,e3,1):
					check_eq(a3,b3,k)
				print "----------------------------------------"
				
				print "----------------------------------------"
				a4 = 60
				b4 = 56
				g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
				e4 = (n - b4) / a4
				print "\ng4 = " + str(g4) + " e4 = " + str(e4)
				for k in range(g4 + 1,e4,1):
					check_eq(a4,b4,k)
	
				print "----------------------------------------"
		else:
			print "error"
	if (n % 10 == 7):
		if (int(str(n)[-2]) % 2 != 0):
			if ((n+1) % 3 == 0):
				print "----------------------------------------"
				a1 = 60
				b1 = 18
				g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
				e1 = (n - b1) / a1
				print "\ng1 = " + str(g1) + " e1 = " + str(e1)
				for k in range(g1 + 1,e1,1):
					check_eq(a1,b1,k)
	
				print "----------------------------------------"
				a2 = 60
				b2 = 42
				g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
				e2 = (n - b2) / a2
				print "\ng2 = " + str(g2) + " e2 = " + str(e2)
				for k in range(g2 + 1,e2,1):
					check_eq(a2,b2,k)
	
				print "----------------------------------------"
			else:
				print "----------------------------------------"
				a1 = 60
				b1 = 38
				g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
				e1 = (n - b1) / a1
				print "\ng1 = " + str(g1) + " e1 = " + str(e1)
				for k in range(g1 + 1,e1,1):
					check_eq(a1,b1,k)
	
				print "----------------------------------------"
				a2 = 60
				b2 = 58
				g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
				e2 = (n - b2) / a2
				print "\ng2 = " + str(g2) + " e2 = " + str(e2)
				for k in range(g2 + 1,e2,1):
					check_eq(a2,b2,k)
	
				print "----------------------------------------"
				a3 = 60
				b3 = 2
				g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
				e3 = (n - b3) / a3
				print "\ng3 = " + str(g3) + " e3 = " + str(e3)
				for k in range(g3 + 1,e3,1):
					check_eq(a3,b3,k)
				print "----------------------------------------"
				
				print "----------------------------------------"
				a4 = 60
				b4 = 22
				g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
				e4 = (n - b4) / a4
				print "\ng4 = " + str(g4) + " e4 = " + str(e4)
				for k in range(g4 + 1,e4,1):
					check_eq(a4,b4,k)
	
				print "----------------------------------------"
		elif (int(str(n)[-2]) % 2 == 0): 
			if ((n+1) % 3 == 0):
				print "----------------------------------------"
				a1 = 60
				b1 = 48
				g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
				e1 = (n - b1) / a1
				print "\ng1 = " + str(g1) + " e1 = " + str(e1)
				for k in range(g1 + 1,e1,1):
					check_eq(a1,b1,k)
	
				print "----------------------------------------"
				a2 = 60
				b2 = 12
				g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
				e2 = (n - b2) / a2
				print "\ng2 = " + str(g2) + " e2 = " + str(e2)
				for k in range(g2 + 1,e2,1):
					check_eq(a2,b2,k)
	
				print "----------------------------------------"
			else:
				print "----------------------------------------"
				a1 = 60
				b1 = 8
				g1 = (int(math.ceil(2 * math.sqrt(n))) - b1)/a1
				e1 = (n - b1) / a1
				print "\ng1 = " + str(g1) + " e1 = " + str(e1)
				for k in range(g1 + 1,e1,1):
					check_eq(a1,b1,k)
	
				print "----------------------------------------"
				a2 = 60
				b2 = 28
				g2 = (int(math.ceil(2 * math.sqrt(n))) - b2)/a2
				e2 = (n - b2) / a2
				print "\ng2 = " + str(g2) + " e2 = " + str(e2)
				for k in range(g2 + 1,e2,1):
					check_eq(a2,b2,k)
	
				print "----------------------------------------"
				a3 = 60
				b3 = 32
				g3 = (int(math.ceil(2 * math.sqrt(n))) - b3)/a3
				e3 = (n - b3) / a3
				print "\ng3 = " + str(g3) + " e3 = " + str(e3)
				for k in range(g3 + 1,e3,1):
					check_eq(a3,b3,k)
				print "----------------------------------------"
				
				print "----------------------------------------"
				a4 = 60
				b4 = 52
				g4 = (int(math.ceil(2 * math.sqrt(n))) - b4)/a4
				e4 = (n - b4) / a4
				print "\ng4 = " + str(g4) + " e4 = " + str(e4)
				for k in range(g4 + 1,e4,1):
					check_eq(a4,b4,k)
	
				print "----------------------------------------"
		else:
			print "error"


def main():
	prep_check()

main()
