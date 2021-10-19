#include<stdio.h>


int main (){


	float nkwh = 0.0f, total;
	float LowR, HighR, Ex;
	LowR = 50.00;
	HighR = 95.00;

	printf("Input the kw/w:\t");
	scanf("%5f", &nkwh);

	if(nkwh < 25){
	
		total = nkwh*0.085;
		total = total * LowR;
		printf("The total is: %.2f\n", total);
		printf("The excess is: none\n");
		printf("The input is: %.2f\n", nkwh);
	
	}else{
		total = nkwh * 0.085;
		total = total * HighR;
		Ex = nkwh - 25;
		printf("The total is: %.2f\n", total);
		printf("The excess is: %.2f\n", Ex);
		printf("The input is: %.2f\n", nkwh);
	}

	return 0;
}

