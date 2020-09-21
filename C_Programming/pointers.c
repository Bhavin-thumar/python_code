#include<stdio.h>

int main(){

/*    int a = 5;
    int *ptr;
    ptr = &a;
    int **ptr1;
    ptr1 = &ptr;

    printf("Value of a is : %d\n", a);
    printf("Value of a is : %d\n", *&a);
    printf("address of a is : %u\n", &a);

    printf("address of ptr is : %u\n", &ptr);
    printf("Value stored in ptr is : %u\n", ptr);
    printf("Value of pointer point to a is : %d\n", *ptr);

    printf("address of ptrl is : %u\n", &ptr1);
    printf("Value stored in ptr1 is : %u\n", ptr1);
    printf("Value of pointer point by ptr1 is : %d\n", **ptr1);

    printf("Value is : %u\n", *ptr1);

    */
    int a = 10;
    int *ptr;
    ptr = &a;

    printf("address of a is %p\n", &a);
    printf("address to pointer is %p\n", ptr);
    printf("Value of pointer is %d", *ptr);

    return 0;

}
