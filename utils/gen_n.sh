#!/bin/bash

n=$1 # Number of bits
p=$(openssl prime -generate -bits $n)
q=$(openssl prime -generate -bits $n)
n=$(echo "$p * $q" | bc)
np1_mod3=$(echo "( $n + 1 ) %  3" | bc)
np1_mod7=$(echo "( $n + 1 ) %  7" | bc)
echo "$p * $q  =  $n ,	$np1_mod3,	$np1_mod7"
