#include <stdio.h>

int main(){
	
	float tax=0.0825;
	
	float tv = 400;
	float vcr =220;
	float rc = 35.2f;
	float cd = 300;
	float tr = 120;
	
	
	float subtotal, taxes,grandtotal;
	
	int q1,q2,q3,q4,q5;
	
	printf("How many TV are sold? ");
	scanf("%d",&q1);
	printf("How many VCRs are sold? ");
	scanf("%d",&q2);
	printf("How many Remote Control are sold? ");
	scanf("%d",&q3);
	printf("How many CD are sold? ");
	scanf("%d",&q4);
	printf("How many Tape Recorder are sold? ");
	scanf("%d",&q5);
	
	
	printf("Quantities \t Description \t Unit Prices \t TotalPrices\n");
	printf("  %d \t\t\tTV    \t %.2f \t %.2f\n", q1,tv,q1*tv);
	printf("  %d \t\t\tVCR    \t %.2f \t %.2f\n", q2,vcr,q2*vcr);
	printf("  %d \t\t\tRC    \t %.2f \t\t %.2f\n", q3,rc,q3*rc);
	printf("  %d \t\t\tCD    \t %.2f \t %.2f\n", q4,cd,q4*cd);
	printf("  %d \t\t\tTR    \t %.2f \t %.2f\n", q5,tr,q5*tr);
	
	subtotal = (q1*tv)+(q2*vcr)+(q3*rc)+(q4*cd)+(q5*tr);
	taxes = subtotal*tax;
	grandtotal = subtotal+taxes;
	printf("\t\t\t\t\t          TOTAL\n");
	printf("\t\t\t\t  SUB TOTAL  : %.2f\n",subtotal);
	printf("\t\t\t\t  VAT        : %.2f\n",taxes);
	printf("\t\t\t\t  GRAND TOTAL: %.2f\n",grandtotal);
	
	return 0;
}

