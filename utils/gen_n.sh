#!/bin/bash

N=$1 # Number of bits
N_2=$(echo "$N / 2" | bc)
p=$(openssl prime -generate -bits $N)
q=$(openssl prime -generate -bits $N)
p2=$(openssl prime -generate -bits $[ N - N_2 ])
q2=$(openssl prime -generate -bits $[ N + N_2 ])
n=$(echo "$p * $q" | bc)
ppq=$(echo "$p + $q" | bc)
pmq=$(echo "$p - $q" | bc)
ppq2=$(echo "$p2 + $q2" | bc)
pmq2=$(echo "$p2 - $q2" | bc)
np1_mod3=$(echo "( $n ) %  3" | bc)
np1_mod7=$(echo "( $n ) %  7" | bc)
echo "n = p*q = $p '*' $q  =  $n ,	nmod3= $np1_mod3, nmod7= $np1_mod7, p+q= $ppq, p-q= ${pmq#-}"
echo "n = p2*q2 = $p2 '*' $q2  =  $n,  p+q= $ppq2, p-q= ${pmq2#-}"
