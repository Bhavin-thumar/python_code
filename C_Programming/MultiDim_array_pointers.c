#include<stdio.h>

int main(){

    int a[2][3] = {
                    {10, 20, 30},
                    {40, 50, 60}
                    };

    for(int i = 0; i < 2; i++){
        for(int j = 0; j < 3; j++){
            printf("The address of a[%d][%d] is %u\n", i, j, &a[i][j]);
        }

    }
    printf("\n");

    printf("The address of a is :%u\n", a);
    printf("The address of a +1 is :%u\n", a + 1);

    printf("\n");
    printf("The address of *a is :%u\n", *a);
    printf("The address of *a +1 is :%u\n", *(a + 1));

    printf("\n");
    printf("The address of **a is :%u\n", **a);
    printf("The address of *(*a +1) is :%u\n", *(*(a + 1)));

    int *p = a;
    //p = &a;

    printf("\n");
    printf("The address of *p is :%u\n", *p);
    printf("The address of *p + 1 is :%u\n", *(p + 1));

    int (*ptr)[2] = a;


    printf("\n");
    printf("The address of *ptr is :%u\n", *ptr);
    printf("The address of *ptr + 1 is :%u\n", *(ptr + 1));

    //printf("The address of *p + 2 is :%d\n", *(p + 2));
    //printf("The address of *p + 3 is :%d\n", *(p + 3));
    //printf("The address of *p + 4 is :%d\n", *(p + 4));
    //printf("The value of **p is :%d\n", **p);
}
