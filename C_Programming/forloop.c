#include <stdio.h>

int main()
{	
	int a;
	printf("Enter the table of multiplication :\n");
	scanf("%d", &a);

	int i;
	for(i=1; i<=10; i++)
	{
		printf("%d X %d = %d\n", a, i, a*i);

	}

	return 0;
}