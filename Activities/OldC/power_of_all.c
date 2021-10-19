#include<stdio.h>

int main(){

	int nums[100];
	int counter = 0;
	int input = -1;
	int i = 0;
	int output= 1;
	
	while(input != 0){
		printf("Enter a number: ");
		scanf("%d", &input);
		nums[counter] = input;
		counter++;
	}
	
	printf("Product of ");
	for(; i < counter-1; i++){
		printf("%d ",nums[i]);
		output *= (int)nums[i];
	}
	printf(" is %d", output);

	return 0;
}

