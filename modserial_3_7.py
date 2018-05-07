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
import json
from math import ceil
from math import sqrt
from gmpy2 import mpz
from gmpy2 import is_square
from gmpy2 import isqrt

def check_eq(a,b,k,n,fplot,index):
	r = a * k + b
	interm = r**2 - 4*n
	#res = math.sqrt(interm)
	is_res = is_square(mpz(interm))
	#print interm
	if (is_res):
		#run(gnuplot -p -e "set terminal wx; plot
		res_f = open("div_8.list", "a+")
		print "\n----------------------------------------------"
		print 'n = ' + str(n) + '	4n = ' + str(4*n)
		print '- interm = ' + str(interm)
		res = isqrt(interm)
		print "result p-q= " + str(res) + " at r = " + str(r)
		p = (r + res)/2
		q = n / p
                res_f.write("n+1 = " + str(n+1) + '     ' + "r = " + str(r) + '     ' + "8|n+1 : " + str((n+1) % 8 == 0) + '      ' + "8|r = " + str(r % 8 == 0) + '      ' + "p = " + str(p) + '      '  + "q = " + str(q) + '\n')
		#res_f.write(str(n) + " " + str(index) + " " + str(k) + " " + str(res) + " " + str(r) + " " + str(interm) + " " + str(p) + " " + str(q) + "\n")
		print "p = " + str(p)
		print "q = " + str(q)
		print "k = " + str(k)
		if (p * q == n):
			print "DONE!"
			exit()

def prep_check(s1,s2,s3,n):
	fp = open('eq.json', 'r')
	eq = json.load(fp)
	l = len(eq[s1 + s2 + '|' + s3]) / 2
	a = []; b = []; g = []; e = []; fplot = []

	print n
	for i in range(1,l+1):
		fplot.append(open('plot' + str(i), 'w'))
		a.append(mpz(eq[s1 + s2 + '|' + s3]['a'+ str(i)]))
		b.append(mpz(eq[s1 + s2 + '|' + s3]['b'+ str(i)]))
		g.append(int(ceil((2 * ceil(sqrt(n)) - b[i-1]) / a[i-1])))
		e.append(int(ceil((sqrt(n**2 + 4*n - 1) - b[i-1]) / a[i-1])))
#		print 'a' + str(i) + ' = ' + str(a[i-1])
#		print 'b' + str(i) + ' = ' + str(b[i-1])
#		print 'g' + str(i) + ' = ' + str(g[i-1])
#		print 'e' + str(i) + ' = ' + str(e[i-1])

	fp.close()
	gs = sorted(enumerate(g) , key = lambda i:i[1])
	print gs
	print e
	n = mpz(n)
#	for i in range(0,len(g)-1):
#			#print "it happend!"
#		for k in range(gs[i][1] , gs[i+1][1]):
#			for v in range(0,i+1):
#				check_eq(a[gs[v][0]],b[gs[v][0]],k,n,fplot[gs[v][0]])
#				print 'check: g' + str(gs[v][0]) + ' = ' + str(gs[v][1]) + '	k' + str(i) + ' = ' + str(k)


	m_e = min(e)
	m_g = min(g)
	while (m_g <= m_e):
		#print "\rk = " + str(k),
		i = 0
		while (i < l):
			#print 'for index ' + str(i) + ' at k = ' + str(g[i])
			check_eq(a[i],b[i],g[i],n,fplot[i],i)
			g[i] += 1
			if (g[i] >= m_e):
				ind_e = e.index(m_e)
				del e[ind_e]
				del g[ind_e]
				del a[ind_e]
				del b[ind_e]
				l = len(a)
				print " deleting ind " + str(ind_e) + " e now : ",
				print e
				if (l == 0):
					print "Ending..."
					exit()
				m_e = min(e)
			i += 1


def start(n):
	n_100 = int(str(n)[-3])
	n_10 = int(str(n)[-2])
	n_1 = int(str(n)[-1])

	if ((n+1) % 3 == 0):
		s1 = '3'
	elif ((n+1) % 3 != 0):
		s1 = '3!'
	else:
		print "Error"
		exit(1)

	if (n_1 == 3 or n_1 == 7):
		s3 = '0' + str(n_1)
		if (n_10 % 2 != 0):
			s2 = ',4'
		elif (n_10 % 2 == 0):
			s2 = ',4!'
		else:
			print "Error"
			exit(1)

	elif (n_1 == 1 or n_1 == 9):
		s3 = str(n_10) + str(n_1)
		if (n_10 % 2 != 0):
			if (n_100 % 2 != 0):
				s2 = ',4'
			elif (n_100 % 2 == 0):
				s2 = ',4!'
			else:
				print "Error"
				exit(1)
		elif (n_10 % 2 == 0):
			s2 = ''
		else:
			print "Error"
			exit(1)
	else:
		print "Error"
		exit(1)
	prep_check(s1,s2,s3,n)


def main():
	n = int(sys.argv[1])
	start(n)

main()
