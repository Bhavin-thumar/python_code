#include <stdio.h>

int main(){

	int a;
	int i = 1;

	printf("Enter the table of multiplication :\n");
	scanf("%d", &a);

	do
	{

	printf("%d X %d = %d\n", a, i, a*i);
	i = i + 1;

	}while(i<11);


	return 0;
}