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

int main() {

  int array[2][2] = {{1,2},
                      {3,4}};
 int *p = array;
 printf("%d\n", *(p + 3));   // accessing elements of array using pointer arithmetic (pointer variable)
 printf("%d\n", *array[1]);  // accessing elements of array using array subscripting
 printf("%d\n", **(array + 1));   // accessing elements of array using array arithmetic
 // printf("%d\n",sizeof(array));
  return 0;
}
