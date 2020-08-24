#include <stdio.h>

int add(int a, int b){
	// a = 10;
	// b = 5;

	return a + b;
}



int main(){

	int c, x, y;
	printf("Enter the first value \n");
	scanf("%d", &x);

	printf("Enter the second value \n");
	scanf("%d", &y);

	c = add(x, y);
	printf("The sum is %d\n", c);
	return 0;
}