#include <stdio.h>

int main() {

 
	int rate;
	float DistanceCovered;
	int totalpay = 0;
	rate = 2;
	
	
	printf("\n==============================\n");
	printf("Input the distance covered the trip took: ");
	scanf("%5f", &DistanceCovered);
	printf("\n==============================\n");
	printf("Total distance is %.2f meters\n", DistanceCovered);
	
	if (DistanceCovered < 300) {
	
		printf("Your payment if 20 Php\n");	   
		
	}else{
	totalpay = 20;
	DistanceCovered = DistanceCovered - 300;
	DistanceCovered = DistanceCovered / 200; 
	totalpay = totalpay + (DistanceCovered * rate);
	
	printf("\n==============================\n");
	printf("The total payment is %d Php\n", totalpay);

	}
	
		
	
	return 0;
}

