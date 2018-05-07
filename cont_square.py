#!/usr/bin/env python

'''
@params
	square: the previous square
	C_pre: previous C
	a: equation parameter
	b: equation parameter 2
	k: the search integer
@return
	next square
'''
def cont_sq(square, C_pre , a_2_2):
	if C_pre == 0 :
		#C_pre = calc_c(a, b, k)	
		print Error 
		exit(1)
	C0 =  C_pre + a_2_2
	return (square + C_pre),C0


'''
@params
	a: equation parameter
	b: equation parameter 2
	k: the search integer
@return
	C_pre
'''
def calc_c(a, b, k):
	return ((2*k - 1) * a**2 + 2*a*b)
