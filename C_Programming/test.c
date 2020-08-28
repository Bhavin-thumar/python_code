#include <stdio.h>

// int main()
// {
// 	int a;
// 	int c;
// 	float b;
// 	a = 60; 
// 	b = 8;
// 	c = 10;

// 	printf("The value of a * b : %f\n", a*b); // %f if resultant is type float
// 	printf("The value of a / b : %f\n", a/b);
// 	printf("The value of a + b : %f\n", a+b);
// 	printf("The value of a + c : %d\n", a+c); // %d if resultant is type int
// 	printf("The value of a / c : %d\n", a/c);
	

// 	return 0;
// }


int main(){

	char reply;
	printf("press y to continue else quit:\n");
	scanf("%c", &reply);
	printf("The size of int is %ld\n",sizeof(int));
	printf("The value of reply is %c", reply);

	return 0;
}