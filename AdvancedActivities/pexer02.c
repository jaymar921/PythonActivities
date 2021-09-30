#include <stdio.h>

int main(){

   int price, tendered;
   double p,t,change, decimal;
   printf("Input the price of an Item: ");
   scanf("%4d", &price);
   printf("Tendered Amount: ");
   scanf("%4d", &tendered);
   
   p = price/100.0F;
   t = tendered/100.0F;
   printf("\nPrice of the item is %.2f", p);
   printf("\nTendered amount %.2f", t);
   
   change = (t - p);
   printf("\nChange: %.2f \n", change);
   change*=100;
   printf("\n10 Pesos: %d", (int)(change/1000));
   printf("\n 5 Pesos: %d", ((int)change)%1000/500);
   printf("\n 1 Pesos: %d", ((int)change)%1000%500/100);
   printf("\n25 Cents: %d", ((int)change)%1000%500%100/25);
   printf("\n10 Cents: %d", ((int)change)%1000%500%100%25/10);
   printf("\n 5 Cents: %d", ((int)change)%1000%500%100%25%10/5);
   return 0;
}

/*
Filename: PEXER02

Create a flowchart and C program that will accept the price of an item and tendered amount of the customer. Display the change and the coin denomination. 

	Example:
		Input the price of an item: 1315
		Tendered amount: 2000

		Price of the item is 13.15
		Tendered amount 20.00
		
		Change: 6.85

		Coin Denomination
		
		10 pesos → 0
		5 pesos → 1
		1 pesos → 1
		.25 cents → 2
		.10 cents -->3
		.05 cents -->1
 
Note: Assume that the user will input up-to 4 digits.
*/


