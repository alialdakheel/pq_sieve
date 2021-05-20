#include <time.h>
#include <stdio.h>

void cont_sq(unsigned int *square, unsigned int *C_1, unsigned int a_2_2){

	*square = *square + *C_1;
	*C_1 = *C_1 + a_2_2;
}

int main(){
	unsigned int a = 600;
	unsigned int b = 222;
	unsigned int a_2 = a * a;
	unsigned int a_2_2 = 2 * a_2;
	unsigned int ab_2 = 2 * a * b;
	unsigned int k = 1;
	unsigned int r = a * k + b;
	unsigned int r_2 = r * r;
	unsigned int C_1 = a_2_2 + a_2 + ab_2;
	unsigned int n = 1000;
	
	clock_t start, diff, end, start1, diff1 = 0 , end1;	
	start1 = clock();
	for (int i = 0; i<n; i++){
		start = clock();
		cont_sq(&r_2, &C_1, a_2_2);
		end = clock();
		printf("result: %u \n", r_2);
		diff = end - start;
		diff1 += diff;
		printf("diff time %d \n",diff);
	}

	end1 = clock();
	//diff1 = end1 - start1;
	printf("time taken %d seconds, result = %u \n", diff1, r_2);
	
	return 0;
}
