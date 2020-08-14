#include <stdio.h>

int main()
{
	int a;
	int i = 1;

	printf("Enter value of multiplication :\n");
	scanf("%d", &a);

	while(i<=10)
	{
		printf("%d X %d = %d\n", a, i, a*i);
		i += 1;
	}


	return 0;
}