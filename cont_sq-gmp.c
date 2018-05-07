#include <time.h>
#include <stdio.h>
#include <gmp.h>

void cont_sq(mpz_t square, mpz_t C_1, mpz_t a_2_2){

	mpz_add(square, square, C_1);
	mpz_add(C_1, C_1, a_2_2);
}

int main(){
	mpz_t a;
	mpz_t b;
	mpz_t a_2;
	mpz_t a_2_2;
	mpz_t ab_2;
	mpz_t k;
	mpz_t r;
	mpz_t r_2;
	mpz_t C_1;
	unsigned int n = 100000;
	mpz_inits(a, b, a_2, a_2_2, ab_2, k, r, r_2, C_1, NULL);
	mpz_set_ui(a, 600);
	mpz_set_ui(b, 222);
	mpz_mul(a_2, a, a);
	mpz_mul_ui(a_2_2, a_2, 2);
	mpz_mul(ab_2, a, b);
	mpz_mul_ui(ab_2, ab_2, 2);
	mpz_set_ui(k, 1);
	mpz_mul(r, k, a);
	mpz_add(r, r, b);
	mpz_mul(r_2, r, r);
	mpz_add(C_1, a_2, ab_2);
	mpz_add(C_1, C_1, a_2_2);


	clock_t start, diff, end, start1, diff1 = 0 , end1;	
	start1 = clock();
	for (unsigned int i = 0; i<n; i++){
		start = clock();
		cont_sq(r_2, C_1, a_2_2);
		end = clock();
		gmp_printf("result: %Zd \n", r_2);
		diff = end - start;
		diff1 += diff;
		printf("diff time %d \n",diff);
	}

	end1 = clock();
	//diff1 = end1 - start1;
	gmp_printf("time taken %d seconds, result = %Zd \n", diff1, r_2);
	mpz_clears(a, b, a_2, a_2_2, ab_2, k, r, r_2, C_1, NULL);
	
	return 0;
}
